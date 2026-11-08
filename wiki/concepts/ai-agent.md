---
title: "AI Agent"
type: concept
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - ai-agent
  - agentic
  - tools
  - architecture
sources:
  - hermes-agent-9router
  - hermes-agent-kerja
  - openclaw-vps
  - jev-ai
  - otak-bisnis
confidence: high
---

# AI Agent

> Sistem yang memakai model bahasa sebagai pengambil keputusan, tetapi dilengkapi memori, tool, saluran komunikasi, dan prosedur yang membuatnya bisa mengerjakan tugas multi-langkah secara mandiri.

## Apa itu

Dalam korpus ini, "AI agent" bukan chatbot yang menjawab pertanyaan. Ia adalah perangkat lunak yang berjalan terus (biasanya di VPS), menerima perintah dari Telegram/WhatsApp atau dashboard, membaca konteks dan memori, memilih tool, mengeksekusi beberapa langkah, lalu melaporkan hasil. [[hermes-agent|Hermes Agent]] dan [[openclaw|OpenClaw]] adalah dua implementasi yang dibahas.

Anatomi yang berulang di sumber:

| Lapisan | Fungsi | Contoh |
|---|---|---|
| Model | Otak yang menalar dan memilih langkah | GLM 5.3, GPT-6 Astra, Claude Fable |
| Gateway/runtime | Menjalankan agent, sesi, cron, tool | Hermes gateway, OpenClaw gateway |
| Router model | Menyebar permintaan dan fallback | [[9router|9Router]], combo model |
| Memori | Fakta tentang pengguna, pekerjaan, aturan | `user.md`, `memory.md`, wiki |
| Skills | SOP dan prosedur yang bisa dipanggil | [[agent-skills|Agent Skills]] |
| Tool | Browser, shell, file, email, coding | MCP, CLI, API |
| Kanal | Cara manusia memberi perintah | Telegram, dashboard, CLI |
| Akses privat | Mengamankan dashboard | [[self-hosting-agents|Tailscale]] |

## Mengapa penting

Model bahasa saja tidak cukup untuk pekerjaan berulang. Ia lupa konteks antar-sesi, tidak punya akses ke file, dan tidak bisa bertindak. Agent menambahkan tiga hal yang mengubah kegunaannya:

1. **Persistensi.** Agent hidup di server dan bisa dihubungi kapan saja, tidak bergantung pada laptop yang menyala.
2. **Konteks yang dimiliki.** Memori, dokumen, dan wiki membuat jawaban spesifik untuk pengguna, bukan generik.
3. **Eksekusi.** Tool dan skill membuat agent bisa menulis file, membuat presentasi, mendeploy website, atau menyortir email.

Namun agent juga memperbesar kesalahan. Jika konteksnya buruk, ia akan salah dengan percaya diri. Karena itu sumber menekankan supervisi, aturan keras, dan audit.

## Tiga pola yang muncul

### 1. Agent sebagai operator pengetahuan

[[business-brain|Business Brain]] memakai agent untuk meng-ingest dokumen ke wiki, menjawab pertanyaan dari wiki, dan menyimpan jawaban sebagai memori. Di sini agent adalah pustakawan, bukan penulis utama.

### 2. Agent sebagai pekerja

[[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]] memakai agent untuk membuat presentasi, script konten, dan prototipe website. Kualitasnya bergantung pada design system, persona, tool, dan brief.

### 3. Agent sebagai orkestrator model

Agent utama tidak harus mengerjakan semua hal. Ia bisa memanggil [[decision-model|decision model]] seperti [[jev-typesafe|JEV]] untuk klasifikasi massal, atau meneruskan tugas berat ke model frontier. Ini adalah pola "model utama + spesialis" yang dijelaskan di [[model-routing|Model Routing]].

## Yang membedakan agent bagus dan buruk

- **Konteks, bukan model.** Sumber berulang kali menemukan bahwa konfigurasi dan briefing lebih menentukan daripada merek model.
- **Tool yang lengkap.** Presentasi butuh skill PowerPoint dan preview; coding butuh akses repo dan shell.
- **Memori yang terawat.** Memori yang tidak pernah di-review menjadi beban dan sumber halusinasi.
- **Batas kewenangan.** Aturan seperti "jangan kirim email tanpa persetujuan" harus eksplisit.
- **Umpan balik manusia.** Agent yang tidak memberi progres atau asumsi sulit dikoreksi.

## Kutipan

> "Hermes Agent ini adalah framework AI Agent open source. License-nya dari MIT, buatan Nous Research." — [[hermes-agent-9router|Hermes Agent + 9Router]], 7:46

> "AI itu cuma eksekutor. Otaknya ada di kalian." — [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]], 27:43

## Koneksi

- [[agent-memory|Agent Memory]] — lapisan yang membuat agent mengenal pengguna.
- [[agent-skills|Agent Skills]] — prosedur yang membuat agent konsisten.
- [[self-hosting-agents|Self-Hosting Agents]] — cara menjalankannya 24/7.
- [[model-routing|Model Routing]] — cara memilih dan mengganti model.
- [[business-brain|Business Brain]] — aplikasi agent untuk pengetahuan bisnis.
- [[decision-model|Decision Model]] — spesialis untuk keputusan massal.

## Perbedaan dan pertanyaan terbuka

- Apakah agent persisten lebih berguna daripada asisten chat biasa untuk pekerjaan yang tidak berulang? Biaya operasionalnya lebih tinggi.
- Berapa banyak otonomi yang aman diberikan? Sumber menyarankan aturan keras, tetapi tidak ada standar audit.
- Apakah memori jangka panjang lebih baik disimpan sebagai file Markdown, database vektor, atau wiki terstruktur? Korpus ini condong ke Markdown yang bisa dibaca manusia.
- Bagaimana mengukur ROI agent di luar anekdot?

## Sumber

- [[hermes-agent-9router|Hermes Agent + 9Router]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[openclaw-vps|OpenClaw di VPS]]
- [[jev-ai|JEV AI untuk Pemula]]
- [[otak-bisnis|Otak Bisnis AI]]
