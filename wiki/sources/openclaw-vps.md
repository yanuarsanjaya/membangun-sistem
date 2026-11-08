---
title: "OpenClaw di VPS (2026)"
type: source
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - openclaw
  - vps
  - tailscale
  - memory
  - review
source_path: "raw/TUTORIAL PASANG OPENCLAW DI KOMPUTER KALIAN SENDIRI.md"
source_url: https://www.youtube.com/watch?v=obQSPdSUkqI
author: David Alfa Sunarna
published: 2026-10-09
ingested: 2026-11-08
confidence: high
---

# OpenClaw di VPS (2026)

> Review dan tutorial OpenClaw pada akhir 2026: pemasangan di VPS, koneksi ChatGPT dan model murah, Tailscale, migrasi workspace lama, serta penilaian jujur tentang relevansinya setelah Claude membatasi akses.

## Sitasi

- **Penulis:** David Alfa Sunarna
- **Terbit:** 2026-10-09
- **URL:** <https://www.youtube.com/watch?v=obQSPdSUkqI>
- **Salinan lokal:** `raw/TUTORIAL PASANG OPENCLAW DI KOMPUTER KALIAN SENDIRI.md`

## Ringkasan

OpenClaw dirilis 24 November 2025 oleh Peter Steinberger dan menjadi salah satu proyek yang mempopulerkan personal AI agent. Penulis mengklaim alat ini membantu meningkatkan penghasilan dan mengefisienkan pekerjaan coding serta konten. Namun Anthropic menutup akses OAuth Claude ke OpenClaw, dan proyek ini kemudian diakuisisi OpenAI. Video menguji apakah OpenClaw masih relevan di kuartal terakhir 2026.

## Poin kunci

- **Nilai utama OpenClaw adalah memori dan persona.** Workspace menyimpan `user.md`, `memory.md`, `soul.md`, `agents.md`, `identity.md`, dan `dreams.md`, sehingga agent tahu siapa pengguna dan bagaimana cara bekerja.
- **Konteks konten membuat script konsisten.** Arsip script viral dijadikan referensi; agent mempelajari hook, tengah, ending, dan CTA.
- **VPS memberi kendali penuh.** Managed setup lebih mudah tetapi tanpa root dan hanya untuk satu aplikasi; VPS cocok untuk eksperimen dan aplikasi tambahan.
- **Tailscale menyelesaikan masalah akses.** Port forwarding tidak skalabel dan berisiko; Tailscale memberi jaringan privat untuk dashboard.
- **Model alternatif bermasalah.** GLM 5.3 bisa dipakai untuk script, tetapi sering stuck atau kehabisan konteks saat coding; GPT-6 Astra lebih lancar, meski mahal.
- **OpenClaw lebih condong ke ekosistem OpenAI.** Penulis mengalami error autentikasi pada sub-agent dan konfigurasi multi-agent yang tidak konsisten.
- **Untuk kerja agentic sehari-hari, penulis beralih ke Hermes.** OpenClaw tetap relevan untuk pekerjaan sederhana yang butuh konteks dan file.

## Perbandingan VPS vs managed setup

| Aspek | VPS | Managed setup Hostinger |
|---|---|---|
| Kontrol | Root penuh | Tidak ada root |
| Instalasi | Manual (one-liner/Docker) | Otomatis |
| Update dan keamanan | Tanggung jawab pengguna | Ditangani penyedia |
| Fleksibilitas | Bisa banyak aplikasi | Hanya OpenClaw |
| Cocok untuk | Pengguna teknis, eksperimen | Pengguna nonteknis yang ingin langsung pakai |

## Struktur workspace

| File | Fungsi menurut video |
|---|---|
| `agents.md` | Aturan operasional: apa yang harus dibaca dan dilakukan agent |
| `soul.md` | Persona dan gaya bicara agent |
| `identity.md` | Identitas dan avatar |
| `user.md` | Siapa pengguna, lokasi, bisnis, minat |
| `memory.md` | Catatan pekerjaan dan aturan keras (mis. tidak mengirim email tanpa persetujuan) |
| `dreams.md` | Diari aktivitas saat idle untuk audit |
| `memory/` | Backup memori |

## Klaim dan bukti

| Klaim | Bukti atau lokasi | Keyakinan |
|---|---|---|
| OpenClaw dirilis 24 November 2025 oleh Peter Steinberger. | 0:04 | Tinggi |
| OpenClaw diakuisisi OpenAI dan dikelola foundation independen. | 2:04–2:17 | Medium (klaim penulis; perlu verifikasi) |
| Anthropic menutup akses OAuth Claude ke OpenClaw. | 1:31 | Tinggi (berdasarkan pengalaman penulis) |
| Memori dan arsip konten membuat script konsisten. | 0:55–1:04 | Medium (pengalaman penulis) |
| GLM 5.3 lancar untuk script tetapi bermasalah untuk coding. | 51:21–53:22 | Medium (satu percobaan) |
| GPT-6 Astra lebih lancar tetapi mahal. | 54:21–56:04 | Medium (satu percobaan) |
| Hermes lebih mudah dikonfigurasi untuk multi-model. | 51:49–52:16 | Medium (opini penulis) |

## Kutipan

> "OpenClaw adalah salah satu tool yang buat gua jadi kaya raya di era AI ini." — 0:00

> "Model itu enggak ngaruh-ngaruh amat. Yang ngaruh itu konfigurasi kita." — 46:21

> "Bukan berarti kalian pakai model paling canggih hasilnya paling bagus." — 49:06

## Koneksi

- [[openclaw|OpenClaw]] — entitas.
- [[self-hosting-agents|Self-Hosting Agents]] — pola VPS, gateway, Tailscale.
- [[agent-memory|Agent Memory]] — konsep yang terlihat dari struktur workspace.
- [[hermes-vs-openclaw|Hermes Agent vs OpenClaw]] — perbandingan terfokus.
- [[model-routing|Model Routing]] — fallback dan pemilihan model.
- [[ai-slop|AI Slop]] — kritik terhadap output AI yang tidak diperiksa.

## Perbedaan dan pertanyaan terbuka

- Klaim akuisisi OpenAI dan status foundation perlu diverifikasi ke sumber primer.
- Uji coding memakai satu prompt dan satu proyek; kegagalan GLM bisa disebabkan konfigurasi, bukan model.
- Apakah `dreams.md` benar-benar audit yang berguna, atau sekadar log aktivitas?
- Risiko keamanan: `user.md` berisi data pribadi; `memory.md` bisa memuat kredensial jika tidak disiplin.

## Sumber

- [[hermes-agent-9router|Hermes Agent + 9Router]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
