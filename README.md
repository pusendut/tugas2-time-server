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

## ⚙️ Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/pusendut/tugas2-time-server.git
cd tugas2-time-server
