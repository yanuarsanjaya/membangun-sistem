---
title: "Self-Hosting Agents"
type: concept
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - vps
  - hosting
  - tailscale
  - security
sources:
  - hermes-agent-9router
  - hermes-agent-kerja
  - openclaw-vps
confidence: high
---

# Self-Hosting Agents

> Menjalankan AI agent di server milik sendiri (VPS atau mesin rumahan) agar hidup 24/7, bisa diakses dari mana saja, dan tidak bergantung pada laptop yang menyala.

## Apa itu

Self-hosting berarti agent, gateway, router model, dan tool-nya berjalan di mesin yang dikendalikan pengguna. Biasanya berupa VPS Linux (Ubuntu) dengan akses root, atau mini PC/Mac Mini di rumah. [[hermes-agent-9router|Hermes Agent + 9Router]], [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]], dan [[openclaw-vps|OpenClaw di VPS]] memakai pola yang sama: VPS Hostinger, instalasi satu baris, gateway sebagai background service, lalu akses lewat Telegram dan Tailscale.

## Mengapa VPS

- **Selalu hidup.** Laptop yang ditutup mematikan agent.
- **Akses dari mana saja.** Telegram, browser, atau SSH.
- **Kendali penuh.** Bisa memasang tool lain, menjalankan aplikasi, dan mengatur port.
- **Biaya terkendali.** VPS murah ratusan ribu rupiah per bulan; lebih murah daripada membeli mini PC.
- **Skalabilitas sederhana.** Upgrade RAM/CPU tanpa mengganti mesin.

Kekurangannya: keamanan, update, dan maintenance menjadi tanggung jawab pengguna.

## Spesifikasi

| Kebutuhan | RAM/CPU | Contoh |
|---|---|---|
| Agent ringan, satu model, tugas teks | 1 vCPU / 4 GB | KVM1 |
| Agent + router + beberapa tool | 2 vCPU / 8 GB | KVM2 |
| Banyak agent, video, Blender, model lokal | 4+ vCPU / 16–32 GB | KVM4+ |

[[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]] menyebut tugas berat seperti konversi video ke teks dan render 3D membutuhkan lebih banyak resource; tugas kantor biasa cukup dengan 4 GB.

## Pola akses

1. **Telegram/WhatsApp.** Bot sebagai antarmuka utama; tidak perlu membuka port.
2. **Dashboard.** Web UI untuk melihat sesi, model, log, skill, dan cron.
3. **Tailscale.** Jaringan privat yang menghubungkan VPS, laptop, dan HP tanpa mengekspos port ke publik.
4. **SSH.** Untuk administrasi; sebaiknya lewat Tailscale atau kunci SSH.
5. **Port forwarding.** Alternatif cepat, tetapi tidak skalabel dan berisiko.

## Keamanan

- Ganti password default (9Router memakai `123456`).
- Jangan mengekspos dashboard ke internet tanpa autentikasi.
- Simpan API key di environment atau secret manager, bukan di file yang dibaca agent.
- Batasi kewenangan agent: jangan beri akses email, media sosial, atau deploy tanpa persetujuan.
- Audit aktivitas: Hermes punya log; OpenClaw punya `dreams.md`.
- Backup workspace dan memori secara berkala.

## Biaya

| Komponen | Kisaran |
|---|---|
| VPS | Rp100.000–200.000/bulan |
| Model murah | $10–40/bulan |
| Model frontier | $100–200/bulan |
| Tailscale | Gratis untuk penggunaan pribadi |
| Total minimal | ±Rp300.000–400.000/bulan |

Angka ini berasal dari sumber dan berubah cepat. Biaya total harus mencakup waktu konfigurasi dan pemeliharaan.

## Hubungan dengan konsep lain

- [[ai-agent|AI Agent]] — yang dijalankan.
- [[model-routing|Model Routing]] — router yang berjalan di server.
- [[hermes-agent|Hermes Agent]] dan [[openclaw|OpenClaw]] — runtime yang di-hosting.
- [[agent-memory|Agent Memory]] — data yang perlu dibackup.
- [[business-brain|Business Brain]] — bisa berjalan di mesin yang sama.

## Perbedaan dan pertanyaan terbuka

- Apakah VPS lebih baik daripada mini PC rumahan? VPS lebih andal dan mudah diakses; mini PC lebih privat dan tanpa biaya bulanan.
- Berapa lama waktu yang wajar untuk maintenance? Sumber tidak mengukur.
- Apakah Tailscale cukup untuk kepatuhan data? Tergantung data dan yurisdiksi.
- Bagaimana mencegah agent menghabiskan kuota model karena loop?

## Sumber

- [[hermes-agent-9router|Hermes Agent + 9Router]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[openclaw-vps|OpenClaw di VPS]]
