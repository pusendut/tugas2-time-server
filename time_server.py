import socket
import threading
from datetime import datetime

# Fungsi untuk menangani koneksi dari klien
def handle_client(conn, addr):
    print(f"[+] Koneksi diterima dari {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            message = data.decode('utf-8').strip()
            print(f"[{addr}] Diterima: {message}")

            if message == "TIME":
                now = datetime.now()
                waktu = now.strftime("%d %m %Y %H:%M:%S")
                conn.sendall(("JAM " + waktu + "\r\n").encode('utf-8'))
            elif message == "QUIT":
                print(f"[-] Koneksi dari {addr} ditutup oleh klien")
                break
            else:
                conn.sendall(b"Perintah tidak dikenali\r\n")
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        conn.close()

# Membuat socket TCP
HOST = '0.0.0.0'
PORT = 45000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"[+] Server berjalan di {HOST}:{PORT}")

try:
    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
except KeyboardInterrupt:
    print("\n[!] Server dimatikan.")
finally:
    server_socket.close()
