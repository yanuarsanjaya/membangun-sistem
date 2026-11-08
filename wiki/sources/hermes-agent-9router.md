---
title: "Hermes Agent + 9Router (Murah Meriah)"
type: source
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - hermes-agent
  - 9router
  - vps
  - free-tier
  - tutorial
source_path: "raw/TUTORIAL PASANG AI AGENT MURAH MERIAH (HERMES AGENT + 9ROUTER).md"
source_url: https://www.youtube.com/watch?v=HVGQULc853Y
author: David Alfa Sunarna
published: 2026-09-18
ingested: 2026-11-08
confidence: high
---

# Hermes Agent + 9Router (Murah Meriah)

> Tutorial memasang Hermes Agent di VPS murah dan menghubungkannya ke 9Router tier gratis, lalu membandingkannya dengan Claude Code pada tugas coding sederhana.

## Sitasi

- **Penulis:** David Alfa Sunarna
- **Terbit:** 2026-09-18
- **URL:** <https://www.youtube.com/watch?v=HVGQULc853Y>
- **Salinan lokal:** `raw/TUTORIAL PASANG AI AGENT MURAH MERIAH (HERMES AGENT + 9ROUTER).md`

## Ringkasan

Video ini menjawab kritik bahwa tutorial AI agent sebelumnya terlalu mahal karena memakai Claude Code $100–200/bulan. Resepnya: VPS Hostinger KVM2 (2 vCPU, 8 GB RAM), Hermes Agent (framework open source MIT dari Nous Research), dan 9Router (proxy lokal open source MIT) pada tier gratis. Hasilnya agent 24/7 yang bisa diperintah lewat Telegram, dengan biaya hampir hanya VPS.

## Poin kunci

- **Hermes Agent** dirilis Februari 2026, open source MIT, punya memori persisten, klaim bisa membuat skill dari pengalaman, dan lebih fleksibel soal model dibanding OpenClaw.
- **9Router** menyebar permintaan ke banyak penyedia. Tiga tier: langganan (Claude Code, Codex, Gemini, Copilot), model China berbayar murah (GLM, MiniMax, Kimi), dan gratis (iFlow, Qwen, Kiro, OpenCode Unlimited).
- **VPS lebih cocok daripada laptop** untuk agent 24/7: laptop mati berarti agent mati. KVM1 4 GB cukup untuk tugas ringan; KVM2 8 GB untuk penggunaan berat.
- **Setup mencakup** instalasi satu baris, quick setup, bot Telegram, gateway sebagai background service, 9Router via npm, web UI, penggantian password default, dan combo model.
- **Combo** menentukan strategi rotasi: fallback (urut), round-robin, atau fusion.
- **Tier gratis cukup untuk belajar, tidak untuk kerja profesional.** Respons lambat, sering stuck, dan tidak memberi umpan balik.
- **Claude Code tetap unggul** untuk iterasi cepat, meskipun hasil akhir tugas invoice generator tidak jauh berbeda.

## Biaya dan spesifikasi

| Komponen | Pilihan | Catatan |
|---|---|---|
| VPS | Hostinger KVM2, 2 vCPU / 8 GB | Sekitar Rp140.000/bulan; KVM1 1 vCPU / 4 GB cukup untuk tugas ringan |
| Hermes Agent | Open source MIT | Gratis |
| 9Router | Open source MIT | Gratis; biaya hanya ke penyedia model |
| Telegram | BotFather | Gratis |
| Model | Tier 3 gratis | Terbatas, lebih lambat, kualitas lebih rendah |

## Klaim dan bukti

| Klaim | Bukti atau lokasi | Keyakinan |
|---|---|---|
| Hermes Agent open source MIT buatan Nous Research, rilis Februari 2026. | 7:46–8:01 | Tinggi (deskripsi produk) |
| 9Router tidak menagih pengguna; biaya ada di penyedia model. | 14:13–14:27 | Tinggi |
| 9Router punya tiga tier: langganan, model murah, gratis. | 14:27–15:36 | Tinggi |
| Tier gratis cukup untuk belajar tetapi lambat dan sering stuck. | 26:48–27:38 | Tinggi (demo) |
| Claude Code menyelesaikan invoice generator dalam 6 menit. | 29:49 | Tinggi (demo) |
| Hasil Hermes + tier gratis setara atau lebih lengkap, tetapi prosesnya jauh lebih lambat. | 31:05–31:47 | Medium (satu tugas) |
| Untuk profesional, tier 2 atau langganan lebih tepat. | 33:11 | Medium (rekomendasi penulis) |

## Kutipan

> "Yang mahal itu bukan servernya, tapi model AI-nya." — 0:28 (mengutip komentar penonton)

> "Kalau kalian cuman invest 9 router yang free, kalian akan habis waktu di config free tier-nya." — 27:15

> "Untuk profesional, saran saya bagusnya ya pakai Hermes Agent ditambah dengan Nine Router tapi yang tier 2." — 33:11

## Koneksi

- [[hermes-agent|Hermes Agent]] — entitas framework.
- [[9router|9Router]] — entitas proxy.
- [[self-hosting-agents|Self-Hosting Agents]] — pola VPS + gateway + router.
- [[model-routing|Model Routing]] — strategi combo dan fallback.
- [[claude-code|Claude Code]] — pembanding.
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]] — lanjutan dengan model berbayar murah.

## Perbedaan dan pertanyaan terbuka

- Biaya VPS di transcript ambigu ("Rp140.000 untuk 24 bulan" vs total ±Rp2,1 juta per tahun). Halaman ini memakai kisaran bulanan yang disebut di video lain, sekitar Rp140.000–190.000.
- Uji banding hanya satu tugas coding sederhana; tidak mengukur kualitas pada tugas panjang, refactor, atau debugging.
- Apakah tier gratis 9Router masih tersedia dan stabil? Ketersediaan penyedia gratis berubah cepat.
- Keamanan: password default 9Router (`123456`) harus diganti; port dan API key perlu dikunci.

## Sumber

- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[openclaw-vps|OpenClaw di VPS]]
