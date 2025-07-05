# Time Server (Tugas 2 Pemrograman Jaringan)

Program ini merupakan implementasi dari **Time Server TCP multithreading** sesuai ketentuan tugas. Server akan melayani klien yang mengirimkan perintah `TIME` dan `QUIT`, dan merespon sesuai protokol yang telah ditentukan.

## 📌 Spesifikasi

- Transport Protocol: **TCP**
- Port: **45000**
- Bahasa: **Python 3**
- Arsitektur: **Multithreading** (untuk melayani banyak klien secara bersamaan)
- Encoding: **UTF-8**
- Format respon: Diawali dengan string `"JAM"`, contoh: `JAM 05 07 2025 15:00:10`

---

### Clone Repository
```bash
git clone https://github.com/pusendut/tugas2-time-server.git
cd tugas2-time-server
```
## ⚙️ Cara Menjalankan
### Menjalankan Server
```bash
python time_server.py
```
### Menjalankan Client (untuk testing)
```bash
python time_client.py
```
### Format Request dari Client
Perintah TIME → untuk meminta waktu saat ini
→ Dikirim sebagai string: TIME\r\n

Perintah QUIT → untuk mengakhiri koneksi
→ Dikirim sebagai string: QUIT\r\n

![image](https://github.com/user-attachments/assets/71aa038c-aac6-4221-a9d1-fcec43228f7c)

![image](https://github.com/user-attachments/assets/95c761ff-bffd-4ad5-a1fb-b322a1724dc2)

