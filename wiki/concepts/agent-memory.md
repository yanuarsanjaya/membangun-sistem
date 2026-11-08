---
title: "Agent Memory"
type: concept
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - memory
  - context
  - personalization
  - audit
sources:
  - openclaw-vps
  - hermes-agent-kerja
  - otak-bisnis
confidence: high
---

# Agent Memory

> Lapisan penyimpanan yang membuat agent mengingat siapa pengguna, apa yang pernah dikerjakan, dan aturan apa yang harus dipatuhi, sehingga konteks tidak hilang antar-sesi.

## Apa itu

Agent memory adalah kumpulan file atau database yang dibaca agent sebelum bertindak. Di [[openclaw|OpenClaw]], memory berbentuk file di workspace:

| File | Isi |
|---|---|
| `user.md` | Siapa pengguna, lokasi, bisnis, minat |
| `memory.md` | Catatan pekerjaan dan aturan keras |
| `soul.md` / `agents.md` | Persona dan aturan operasional |
| `dreams.md` | Diari aktivitas saat idle |
| `memory/` | Backup memori |

[[hermes-agent|Hermes Agent]] menyimpan memori, sesi, skill, dan konfigurasi serupa, serta bisa mengimpor workspace lama. [[business-brain|Business Brain]] menyimpan memori pengetahuan di wiki Markdown.

## Tiga jenis memori

1. **Memori identitas.** Siapa pengguna, preferensi, gaya bahasa, konteks bisnis.
2. **Memori kerja.** Apa yang sudah dikerjakan, keputusan, deadline, status proyek.
3. **Memori prosedural.** Cara mengerjakan sesuatu — skill, SOP, aturan.

Ketiganya sering bercampur dalam satu file, tetapi sebaiknya dipisahkan agar mudah dirawat dan diaudit.

## Mengapa penting

- **Personalisasi.** Tanpa memori, agent memberi jawaban generik.
- **Konsistensi.** Gaya dan keputusan tidak berubah setiap sesi.
- **Efisiensi.** Tidak perlu menjelaskan ulang konteks.
- **Audit.** Catatan aktivitas memungkinkan manusia memeriksa apa yang dilakukan agent.

## Risiko

- **Memori basi.** Fakta lama tetap dipakai setelah berubah.
- **Memori salah.** Agent mencatat interpretasi sebagai fakta.
- **Kebocoran data.** Profil dan memori bisa memuat informasi sensitif.
- **Konteks berlebihan.** Terlalu banyak memori memperlambat dan mengaburkan prioritas.
- **Ketergantungan.** Pengguna lupa memverifikasi karena agent "sudah tahu".

## Praktik yang baik

- Tulis aturan keras secara eksplisit, misalnya "jangan kirim email tanpa persetujuan".
- Tinjau memori berkala; hapus yang sudah tidak berlaku.
- Pisahkan fakta dari preferensi dan dari spekulasi.
- Backup sebelum migrasi atau upgrade.
- Audit log aktivitas, terutama untuk agent yang punya akses eksternal.
- Jangan menyimpan kredensial di file yang dibaca model.

## Hubungan dengan konsep lain

- [[ai-agent|AI Agent]] — yang memiliki memori.
- [[knowledge-management|Knowledge Management]] — disiplin yang lebih luas.
- [[business-brain|Business Brain]] — memori pengetahuan yang terstruktur.
- [[agent-skills|Agent Skills]] — memori prosedural.
- [[self-hosting-agents|Self-Hosting Agents]] — tempat memori disimpan dan dibackup.

## Perbedaan dan pertanyaan terbuka

- Apakah memori file Markdown cukup untuk jangka panjang, atau perlu database?
- Bagaimana mencegah agent mencatat hal yang salah sebagai fakta?
- Siapa yang memiliki data memori ketika agent dijalankan di VPS pihak ketiga?
- Apakah `dreams.md` berguna untuk audit, atau hanya narasi yang tidak dapat diverifikasi?

## Sumber

- [[openclaw-vps|OpenClaw di VPS]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[otak-bisnis|Otak Bisnis AI]]
