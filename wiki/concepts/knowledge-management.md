---
title: "Knowledge Management"
type: concept
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - knowledge-management
  - sop
  - documentation
  - second-brain
sources:
  - 14-skill-ai
  - otak-bisnis
  - hermes-agent-kerja
  - openclaw-vps
confidence: high
---

# Knowledge Management

> Disiplin menyimpan pengetahuan, konteks, dan prosedur dalam bentuk yang bisa dipakai ulang oleh manusia dan AI — bukan hanya diarsipkan.

## Apa itu

Knowledge management adalah cara menyimpan apa yang diketahui bisnis agar tidak hilang dan bisa dipakai lagi: profil pengguna, SOP, catatan proyek, analisis, design system, arsip konten, dan keputusan. Dalam korpus ini, bentuk yang paling sering muncul adalah folder Markdown, wiki, dan file memori agent.

[[14-skill-ai|14 Skill AI]] menyebutnya skill Builder yang paling *underrated* karena "kedengarannya boring padahal penting banget" (6:20). Alasannya: semua level di atasnya — chatbot, automasi, agent — membutuhkan dokumentasi.

## Mengapa penting

- **Chatbot yang bagus adalah bukti knowledge base yang bagus.** Chatbot tidak otomatis pintar; ia hanya sebaik pengetahuan yang diberikan.
- **Agent butuh konteks.** [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]] menunjukkan bahwa mengimpor 101 file konfigurasi membuat agent tahu persona, gaya, dan cara kerja pengguna.
- **Kualitas pengetahuan menentukan kualitas output.** [[openclaw-vps|OpenClaw di VPS]] menemukan bahwa script bagus lahir dari arsip script viral dan formula yang tersimpan, bukan dari model yang lebih mahal.
- **Pengetahuan adalah aset yang tidak kedaluwarsa saat tool berganti.** Model dan framework berubah; dokumen tetap bisa dipindahkan.

## Bentuk konkret

| Bentuk | Isi | Dipakai untuk |
|---|---|---|
| Profil pengguna | Siapa, bisnis, pelanggan, preferensi | Personalisasi jawaban |
| SOP | Langkah, aturan, quality bar | Menjalankan proses berulang |
| Design system | Warna, font, layout, contoh | Konsistensi visual |
| Arsip konten | Script, hook, performa | Meniru pola yang terbukti |
| Wiki | Konsep, entitas, keputusan | Menjawab pertanyaan |
| Memori agent | Fakta operasional dan aturan keras | Konteks antar-sesi |

## Prinsip yang berulang

1. **Simpan sambil bekerja, bukan setelah selesai.** Ingest saat sumber ditemukan; catat keputusan saat dibuat.
2. **Tulis untuk dibaca mesin dan manusia.** Markdown dengan struktur dan frontmatter lebih berguna daripada catatan acak.
3. **Pisahkan sumber mentah dari interpretasi.** Raw immutable; wiki boleh berubah.
4. **Beri aturan eksplisit.** "Jangan kirim email tanpa persetujuan" harus tertulis, bukan diasumsikan.
5. **Review dan buang.** Pengetahuan basi lebih berbahaya daripada tidak ada pengetahuan.

## Risiko

- **Garbage in, gospel out.** Sumber buruk akan dikutip dengan percaya diri.
- **Dokumentasi sebagai proyek sampingan.** Jika menulis dokumentasi terasa seperti beban, tidak akan dilakukan.
- **Konteks yang terlalu besar.** Memasukkan semua hal membuat agent lambat dan tidak fokus.
- **Data sensitif.** Profil dan memori bisa memuat informasi pribadi; perlu aturan penyimpanan.

## Hubungan dengan konsep lain

- [[business-brain|Business Brain]] — aplikasi untuk bisnis.
- [[agent-skills|Agent Skills]] — prosedur yang diformat untuk agent.
- [[agent-memory|Agent Memory]] — memori operasional.
- [[ai-leverage-levels|AI Leverage Levels]] — posisi skill ini.
- [[prompting|Prompting]] — konteks adalah bahan bakar prompt.

## Perbedaan dan pertanyaan terbuka

- Apakah wiki terstruktur selalu lebih baik daripada pencarian semantik atas dokumen mentah? Untuk skala kecil, mungkin tidak.
- Berapa banyak konteks yang optimal sebelum model justru terganggu?
- Siapa yang bertanggung jawab menjaga pengetahuan tetap akurat di tim kecil?

## Sumber

- [[14-skill-ai|14 Skill AI (Last Minute Creator)]]
- [[otak-bisnis|Otak Bisnis AI (Last Minute Creator)]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[openclaw-vps|OpenClaw di VPS]]
