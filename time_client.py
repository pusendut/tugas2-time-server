import socket

HOST = '127.0.0.1'
PORT = 45000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        cmd = input("").strip()
        if cmd not in ["TIME", "QUIT"]:
            print("")
            continue

        s.sendall((cmd + "\r\n").encode('utf-8'))

        if cmd == "QUIT":
            print("")
            break

        data = s.recv(1024)
        print("Respon dari server:", data.decode('utf-8').strip())
