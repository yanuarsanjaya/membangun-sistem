---
title: "Berapa Budget untuk AI Agent 24/7?"
type: question
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - budget
  - self-hosting
  - cost
  - agent
sources:
  - hermes-agent-9router
  - hermes-agent-kerja
  - openclaw-vps
  - model-comparison-2026-11
confidence: medium
---

# Berapa Budget untuk AI Agent 24/7?

## Pertanyaan

Berapa biaya minimal untuk punya AI agent yang menyala 24/7, bisa diperintah dari Telegram, dan cukup kuat untuk kerja nyata?

## Jawaban singkat

Ada tiga tingkat budget:

| Tingkat | Komponen | Kisaran per bulan | Cocok untuk |
|---|---|---|---|
| Belajar | VPS 4 GB + Hermes + 9Router tier gratis | Rp100.000–200.000 | Eksperimen, belajar, tugas ringan |
| Kerja hemat | VPS 8 GB + Hermes + OpenCode Go/GLM | Rp300.000–400.000 | Script, presentasi, website sederhana, otomasi |
| Profesional | VPS 8 GB+ + langganan frontier (Claude/GPT) | Rp1.500.000–3.500.000+ | Coding berat, visual detail, pekerjaan klien |

Angka ini berasal dari [[hermes-agent-9router|Hermes Agent + 9Router]], [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]], dan [[openclaw-vps|OpenClaw di VPS]], dengan asumsi kurs Rp18.000/USD dan harga 2026.

## Rincian

### 1. VPS

| Spesifikasi | Harga indikatif | Catatan |
|---|---|---|
| 1 vCPU / 4 GB | Rp100.000–190.000/bulan | Cukup untuk agent teks dan satu model |
| 2 vCPU / 8 GB | Rp140.000–200.000/bulan | Nyaman untuk agent + router + tool |
| 4+ vCPU / 16–32 GB | Rp300.000+/bulan | Video, Blender, model lokal |

VPS lebih murah daripada Mac Mini/mini PC untuk kebutuhan selalu hidup, tetapi maintenance menjadi tanggung jawab pengguna.

### 2. Model

| Pilihan | Biaya | Catatan |
|---|---|---|
| 9Router tier gratis | Rp0 | Lambat, terbatas, sering stuck |
| OpenCode Go | $10/bulan (±Rp180.000) | Model China; limit bisa habis |
| OpenCode Go Plus | $40/bulan (±Rp720.000) | Limit lebih besar |
| Google AI Pro | Rp300.000/bulan | Gemini 4 Argon + 5 TB |
| Claude Max | $100–200/bulan | Kualitas tertinggi, biaya tertinggi |

### 3. Biaya tersembunyi

- **Waktu konfigurasi.** Sumber melaporkan berjam-jam untuk mengatur combo, fallback, dan Tailscale.
- **Iterasi.** Output murah sering butuh banyak revisi.
- **Listrik dan perangkat.** Jika memakai mesin sendiri.
- **Kegagalan.** Kuota habis di tengah pekerjaan atau API key bocor.
- **Maintenance.** Update, backup, dan audit keamanan.

## Analisis

Budget minimal yang masih berguna untuk kerja nyata adalah sekitar **Rp300.000–400.000/bulan**: VPS 8 GB, Hermes Agent, dan model murah berbayar. Konfigurasi ini cukup untuk presentasi, script, dan prototipe website, seperti yang didemonstrasikan [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]].

Namun "murah" bukan hanya soal uang. Tier gratis memakan waktu dan kesabaran; [[hermes-agent-9router|Hermes Agent + 9Router]] menyimpulkan bahwa tier gratis cocok untuk belajar, bukan untuk profesional. Jika pekerjaan menghasilkan uang, selisih Rp200.000/bulan untuk model berbayar biasanya sepadan dengan waktu yang dihemat.

Untuk pekerjaan yang menuntut kualitas tertinggi, [[model-comparison-2026-11|perbandingan Terra/Argon/Fable]] menunjukkan bahwa model frontier bisa memakan biaya $21–25 per tugas berat. Pada volume tinggi, langganan lebih ekonomis daripada API.

## Caveat

- Harga berubah cepat; angka ini adalah snapshot 2026.
- Biaya per tugas tidak sama dengan biaya per bulan.
- Tidak semua pekerjaan membutuhkan agent 24/7; untuk tugas sesekali, chatbot biasa lebih murah.
- Faktor kurs dan pajak tidak dihitung.
- Sponsor dan afiliasi dalam sumber dapat memengaruhi rekomendasi.

## Tindak lanjut

- Hitung biaya per tugas untuk pekerjaan yang benar-benar dilakukan, bukan per token.
- Mulai dari VPS 4 GB dan tier murah; naikkan hanya jika perlu.
- Siapkan fallback model agar tidak berhenti saat limit habis.
- Audit pengeluaran bulanan setelah 30 hari.

## Koneksi

- [[self-hosting-agents|Self-Hosting Agents]] — arsitektur dan keamanan.
- [[model-routing|Model Routing]] — cara menekan biaya dengan fallback.
- [[model-tiers|Model Tiers]] — kerangka harga.
- [[hermes-vs-openclaw|Hermes Agent vs OpenClaw]] — pilihan runtime.

## Sumber

- [[hermes-agent-9router|Hermes Agent + 9Router]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[openclaw-vps|OpenClaw di VPS]]
- [[model-comparison-2026-11|GPT-6.1 Terra vs Gemini 4 Argon vs Claude Fable 5.1]]
