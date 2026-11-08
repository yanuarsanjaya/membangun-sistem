---
title: "OpenCode"
type: entity
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - product
  - coding-agent
  - model-provider
  - opencode-go
sources:
  - otak-bisnis
  - hermes-agent-kerja
  - openclaw-vps
  - 14-skill-ai
confidence: medium
---

# OpenCode

> Agen coding dan penyedia akses model yang dipakai untuk membangun wiki, menjalankan agent, dan memberi model murah lewat paket OpenCode Go.

## Apa itu

OpenCode adalah tool agen coding berbasis terminal/desktop yang bisa membuka folder proyek, membaca file, menulis kode, dan menjalankan perintah. Ia juga menyediakan akses model, termasuk model gratis (OpenCode Zen) dan paket berbayar murah (OpenCode Go).

## Peran dalam korpus

- [[otak-bisnis|Otak Bisnis AI]] memakai OpenCode untuk menyiapkan vault LLM Wiki dan meng-ingest dokumen.
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]] memakai OpenCode Go sebagai penyedia model untuk [[hermes-agent|Hermes Agent]]: GLM 5.3 utama, Qwen 3.8 Max cadangan.
- [[14-skill-ai|14 Skill AI]] menyebut OpenCode untuk pekerjaan coding yang lebih serius, dan Open Design untuk desain.
- [[openclaw-vps|OpenClaw di VPS]] memakai OpenCode Go untuk mengakses GLM 5.3.

## Paket dan harga

| Paket | Harga | Catatan |
|---|---|---|
| OpenCode Zen | Gratis | Model terbatas; cocok untuk belajar |
| OpenCode Go | $10/bulan | Berbagai model China; limit bisa habis |
| OpenCode Go Plus | $40/bulan | Limit lebih besar; dipakai untuk pengujian intensif |

Harga dan kuota berubah; angka ini berasal dari sumber 2026.

## Koneksi

- [[ai-agent|AI Agent]] — kategori tool.
- [[hermes-agent|Hermes Agent]] — agent yang memakai OpenCode Go sebagai penyedia.
- [[model-routing|Model Routing]] — OpenCode Go adalah salah satu sumber model.
- [[self-hosting-agents|Self-Hosting Agents]] — OpenCode bisa berjalan di VPS.
- [[business-brain|Business Brain]] — OpenCode dipakai untuk membangun wiki.

## Pertanyaan terbuka

- Apakah OpenCode Go membatasi model tertentu setelah kuota habis?
- Bagaimana kualitas model GLM 5.3 dibanding model frontier untuk coding jangka panjang?
- Apakah paket $10 cukup untuk penggunaan harian, atau hanya untuk eksperimen?

## Sumber

- [[otak-bisnis|Otak Bisnis AI (Last Minute Creator)]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[openclaw-vps|OpenClaw di VPS]]
- [[14-skill-ai|14 Skill AI (Last Minute Creator)]]
