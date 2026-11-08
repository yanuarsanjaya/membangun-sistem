---
title: "Hermes Agent untuk Kerja Nyata"
type: source
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - hermes-agent
  - opencode
  - tailscale
  - workflow
  - presentation
source_path: "raw/TUTORIAL SETUP HERMES AGENT SAMPAI BISA DIPAKAI KERJA BENERAN.md"
source_url: https://www.youtube.com/watch?v=hYufkXGHA6o
author: David Alfa Sunarna
published: 2026-10-23
ingested: 2026-11-08
confidence: high
---

# Hermes Agent untuk Kerja Nyata

> Lanjutan tutorial Hermes Agent: naik ke model berbayar murah (OpenCode Go + GLM 5.3), memasang dashboard dan Tailscale, mengimpor konfigurasi lama, lalu menguji agent pada presentasi, script konten, dan prototipe website.

## Sitasi

- **Penulis:** David Alfa Sunarna
- **Terbit:** 2026-10-23
- **URL:** <https://www.youtube.com/watch?v=hYufkXGHA6o>
- **Salinan lokal:** `raw/TUTORIAL SETUP HERMES AGENT SAMPAI BISA DIPAKAI KERJA BENERAN.md`

## Ringkasan

Video sebelumnya memakai 9Router tier gratis dan hasilnya lambat. Video ini menggantinya dengan tier 2: OpenCode Go $10–40/bulan dengan GLM 5.3 sebagai model utama dan Qwen 3.8 Max sebagai cadangan. Hermes dipasangi dashboard, diakses lewat Tailscale, dan diberi konteks kerja lama (persona, skill script konten, design system Web Ekspor). Tiga pengujian: presentasi PDF, script konten docx, dan prototipe website.

## Poin kunci

- **Model murah yang tepat cukup untuk kerja.** GLM 5.3 medium menyelesaikan setup Tailscale dalam 6 menit dan memakai sekitar 2% dari limit $40.
- **Konteks adalah pembeda.** Impor 101 file konfigurasi lama menghasilkan persona, skill "David content script", memori, dan pemahaman bisnis.
- **Design system harus eksplisit.** Presentasi bagus karena agent diberi palet, font, dan aturan desain, bukan karena modelnya kebetulan pintar.
- **Siapkan tool sebelum menilai hasil.** Agent diminta memasang skill PowerPoint dan menyiapkan preview sebelum membuat slide.
- **Tailscale memberi akses privat.** Dashboard Hermes dan 9Router bisa dibuka dari HP/laptop tanpa mengekspos port ke publik.
- **Iterasi adalah bagian dari kerja.** Script konten pertama berbahasa Indonesia buruk; agent diminta memasang LanguageTool dan mempelajari PUEBI, lalu hasilnya membaik.
- **Agent adalah eksekutor.** Kualitas keluaran ditentukan oleh konteks, tool, dan supervisi manusia.

## Biaya dan konfigurasi

| Komponen | Pilihan | Catatan |
|---|---|---|
| VPS | KVM1 atau KVM2 | Rp100.000–200.000/bulan |
| Model | OpenCode Go $10/bulan | $40 plan dipakai 22% untuk seluruh pengujian |
| Model utama | GLM 5.3 (medium) | Murah, cukup cepat |
| Cadangan | Qwen 3.8 Max | Fallback |
| Akses | Telegram + Tailscale | Telegram untuk chat; Tailscale untuk dashboard |
| Total | ±Rp300.000–400.000/bulan | Klaim penulis |

## Pengujian

| Tugas | Hasil | Catatan |
|---|---|---|
| Presentasi 2 slide (PDF) | Berhasil, desain konsisten | Butuh design system dan skill PowerPoint |
| Script konten (docx) | Berhasil setelah revisi | Bahasa Indonesia awalnya buruk; LanguageTool + PUEBI membantu |
| Prototipe website kafe | Berhasil dalam ±10 menit | Brief jelas, design system dipakai; gambar buatan AI masih lemah |

## Klaim dan bukti

| Klaim | Bukti atau lokasi | Keyakinan |
|---|---|---|
| GLM 5.3 medium memasang Tailscale dalam 6 menit dengan 2% limit. | 19:00–19:13 | Tinggi (demo) |
| Impor 101 file konfigurasi memberi agent persona dan skill. | 23:12–23:47 | Tinggi (demo) |
| Presentasi dengan design system menghasilkan output layak pakai. | 29:32–31:23 | Tinggi (demo) |
| Script konten membaik setelah LanguageTool dan PUEBI. | 34:28–35:41 | Tinggi (demo) |
| Biaya total ±Rp300.000–400.000/bulan. | 2:42–3:03; 40:55 | Medium (perkiraan penulis) |
| Agent bisa menjadi "second brain" yang mengingat konteks kerja. | 40:55 | Medium (klaim kualitatif) |

## Kutipan

> "AI itu cuma eksekutor. Otaknya ada di kalian." — 27:43

> "Kalau malas ya, lu enggak ada bedanya sama AI slop." — 27:35

> "Masalahnya orang yang mengendalikan model tersebut bisa atau enggak." — 36:15

## Koneksi

- [[hermes-agent|Hermes Agent]] — entitas.
- [[opencode|OpenCode]] — penyedia model OpenCode Go.
- [[self-hosting-agents|Self-Hosting Agents]] — pola hosting dan akses privat.
- [[prompting|Prompting]] — pentingnya konteks, design system, dan iterasi.
- [[ai-slop|AI Slop]] — kualitas output sebagai tanggung jawab manusia.
- [[business-brain|Business Brain]] — impor konteks kerja sebagai memori.

## Perbedaan dan pertanyaan terbuka

- Harga OpenCode Go berubah selama video ($10 ke $40). Angka biaya bersifat sementara.
- Uji presentasi dan website hanya satu kali; belum ada perbandingan buta dengan hasil Claude.
- Apakah Tailscale cukup aman untuk data bisnis sensitif? Video menekankan akses privat, tetapi tidak membahas audit dan enkripsi.
- Berapa lama konteks hasil impor bertahan sebelum perlu diperbarui?

## Sumber

- [[hermes-agent-9router|Hermes Agent + 9Router]]
- [[openclaw-vps|OpenClaw di VPS]]
