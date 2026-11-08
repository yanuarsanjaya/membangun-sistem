---
title: "Model Routing"
type: concept
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - model-routing
  - 9router
  - fallback
  - cost
sources:
  - hermes-agent-9router
  - hermes-agent-kerja
  - openclaw-vps
  - jev-ai
confidence: high
---

# Model Routing

> Lapisan perangkat lunak yang memilih, merotasi, dan menggagalkan permintaan ke beberapa penyedia model, sehingga satu agent bisa memakai model murah, model cadangan, dan model spesialis secara bersamaan.

## Apa itu

Model routing memisahkan agent dari satu penyedia. Daripada mengunci agent ke Claude atau GPT, router menyimpan beberapa koneksi (API key atau langganan) dan meneruskan permintaan berdasarkan strategi. [[9router|9Router]] adalah implementasi yang dibahas di [[hermes-agent-9router|Hermes Agent + 9Router]].

Tiga strategi yang muncul:

| Strategi | Cara kerja | Kapan dipakai |
|---|---|---|
| Fallback | Coba model pertama; jika limit/error, pindah ke berikutnya | Produksi sederhana; prioritas model utama |
| Round-robin | Giliran antar-model | Membagi beban; menghindari limit satu penyedia |
| Fusion | Gabungkan atau bandingkan beberapa model | Eksperimen; tugas yang butuh penilaian |

## Tiga tier penyedia

[[hermes-agent-9router|Hermes Agent + 9Router]] membagi sumber model menjadi tiga:

1. **Tier 1 — langganan.** Claude Code, Codex, Gemini, Copilot. Kualitas tinggi, limit jelas, biaya bulanan.
2. **Tier 2 — model murah berbayar.** GLM, MiniMax, Kimi, Qwen. Biaya rendah, kualitas cukup untuk banyak tugas, cocok untuk kerja profesional hemat.
3. **Tier 3 — gratis.** iFlow, Qwen free, Kiro, OpenCode Unlimited. Untuk belajar dan eksperimen; lambat dan terbatas.

## Mengapa penting

- **Biaya.** Satu tugas tidak perlu model termahal. Router memungkinkan model murah untuk tugas rutin dan model frontier untuk tugas sulit.
- **Ketahanan.** Jika satu penyedia limit atau down, agent tetap jalan.
- **Spesialisasi.** Model berbeda unggul di tugas berbeda; router memungkinkan pemilihan per tugas.
- **Eksperimen.** Pengguna bisa membandingkan model tanpa mengubah agent.

## Pola yang muncul di sumber

- **Model utama + fallback.** [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]] memakai GLM 5.3 sebagai utama dan Qwen 3.8 Max sebagai cadangan.
- **Model utama + decision model.** [[jev-ai|JEV AI untuk Pemula]] memakai GLM 5.3 untuk percakapan dan [[jev-typesafe|JEV]] untuk klasifikasi massal. Ini menghemat limit dan waktu.
- **Model murah untuk teks, model frontier untuk visual.** [[openclaw-vps|OpenClaw di VPS]] menemukan GLM lebih baik untuk script bahasa Indonesia, sementara GPT-6 Astra lebih baik untuk hook dan tugas visual tertentu.

## Biaya dan batas

Routing tidak menghilangkan biaya; ia memindahkannya. Yang perlu dihitung:

- Harga per token input, output, dan cache.
- Biaya langganan bulanan.
- Biaya waktu manusia untuk mengonfigurasi dan menunggu.
- Biaya kegagalan: output buruk yang harus diulang.

[[model-comparison-2026-11|Perbandingan Terra/Argon/Fable]] menunjukkan bahwa biaya per token bisa menyesatkan: model termurah menghasilkan output yang butuh banyak iterasi, sedangkan model mahal menyelesaikan lebih sedikit iterasi.

## Risiko

- **Kompleksitas konfigurasi.** Sumber berulang kali melaporkan waktu habis untuk mengatur combo dan fallback.
- **Ketergantungan pada penyedia gratis.** Kuota dan kualitas berubah tanpa pemberitahuan.
- **Kualitas tidak merata.** Model cadangan mungkin jauh lebih lemah; agent bisa diam-diam menurunkan kualitas.
- **Keamanan API key.** Router menyimpan banyak kredensial; akses harus dibatasi.
- **Debugging lebih sulit.** Jika hasil buruk, sulit tahu model mana yang menjawab.

## Hubungan dengan konsep lain

- [[model-tiers|Model Tiers]] — kerangka harga dan kemampuan.
- [[decision-model|Decision Model]] — spesialis yang dipanggil lewat routing.
- [[self-hosting-agents|Self-Hosting Agents]] — tempat router berjalan.
- [[ai-agent|AI Agent]] — konsumen routing.
- [[hermes-agent|Hermes Agent]] — agent yang mendukung custom provider.

## Perbedaan dan pertanyaan terbuka

- Apakah round-robin benar-benar meningkatkan kualitas, atau hanya menyamarkan perbedaan model?
- Berapa banyak model yang masih bisa dikelola sebelum konfigurasi menjadi beban?
- Apakah fusion menghasilkan jawaban lebih baik, atau hanya lebih mahal?
- Bagaimana audit biaya per tugas tanpa mencatat setiap panggilan?

## Sumber

- [[hermes-agent-9router|Hermes Agent + 9Router]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[openclaw-vps|OpenClaw di VPS]]
- [[jev-ai|JEV AI untuk Pemula]]
