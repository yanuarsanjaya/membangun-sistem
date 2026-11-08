# Panduan Menjalankan Sandbox AI Agent di Mac Mini

Dokumen ini berisi panduan operasional untuk menjalankan **Hermes Agent** dan **9Router** di dalam lingkungan terisolasi (*sandbox*) menggunakan **Docker** di Mac Mini Anda, sehingga sistem utama Mac Anda tetap aman.

---

## 1. Prasyarat di Mac Mini
1. **Docker Desktop for Mac** sudah terinstal dan menyala (pastikan ikon Docker di *menu bar* atas berwarna hijau/running).
2. Folder *sandbox* khusus sudah dibuat di komputer Anda (otomatis dibuat oleh skrip, atau buat manual: `mkdir -p ~/ai-workspace`).

---

## 2. Cara Menjalankan Sistem

1. Buka **Terminal** di Mac Mini Anda.
2. Masuk ke direktori tempat file `docker-compose.yml` ini disimpan (misalnya di root folder atau folder proyek Anda).
3. Buat file `.env` untuk menyimpan token rahasia Telegram Anda dengan aman:
   ```bash
   echo "TELEGRAM_BOT_TOKEN=masukkan_token_botfather_anda_disini" > .env
   ```
4. Jalankan kontainer dalam mode latar belakang (*background*):
   ```bash
   docker compose up -d
   ```

---

## 3. Verifikasi Keamanan & Isolasi (Sandbox)

- **Isolasi File (Volume Mounting):** Agent hanya dapat melihat dan memodifikasi file yang ada di dalam folder `~/ai-workspace/` di Mac Anda. File sistem macOS, dokumen pribadi di luar folder tersebut, dan aplikasi lain tertutup rapat dan aman dari jangkauan kontainer.
- **Isolasi Jaringan:** Kedua layanan berkomunikasi melalui *Docker Network* privat (`agent-net`). 9Router mengekspos port `3000` ke localhost untuk Anda akses via browser (`http://localhost:3000`).

---

## 4. Perintah Operasional Sehari-hari

- **Melihat status agent:**
  ```bash
  docker compose ps
  ```
- **Melihat log/aktivitas agent:**
  ```bash
  docker compose logs -f
  ```
- **Mematikan sistem sementara:**
  ```bash
  docker compose down
  ```
- **Membersihkan dan mereset sandbox:**
  ```bash
  docker compose down --volumes
  ```
