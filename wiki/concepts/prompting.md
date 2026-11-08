---
title: "Prompting"
type: concept
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - prompting
  - context
  - iteration
  - briefing
sources:
  - 14-skill-ai
  - hermes-agent-kerja
  - higgsfield-poster-umkm
  - otak-bisnis
confidence: high
---

# Prompting

> Seni memberi AI konteks, tujuan, batasan, dan standar hasil yang cukup jelas sehingga keluaran bisa dinilai dan diperbaiki, bukan sekadar dihasilkan.

## Apa itu

Prompting bukan kumpulan kata ajaib. Dalam korpus ini, prompting yang baik selalu mengandung empat hal:

1. **Konteks.** Siapa pengguna, apa bisnisnya, apa yang sudah diketahui.
2. **Tujuan.** Apa yang ingin dicapai, bukan hanya apa yang ingin dibuat.
3. **Batasan.** Apa yang boleh, apa yang dilarang, format apa yang dipakai.
4. **Standar.** Seperti apa hasil yang dianggap selesai.

[[14-skill-ai|14 Skill AI]] merumuskannya: "yang paling penting dalam prompt engineering itu sebenarnya adalah konteks dan outcome yang jelas" (5:20).

## Mengapa penting

Model yang sama bisa menghasilkan output biasa atau luar biasa tergantung prompt dan konteks. [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]] menunjukkan bahwa presentasi bagus lahir dari design system, persona, dan brief, bukan dari model yang kebetulan lebih mahal. [[higgsfield-poster-umkm|Poster UMKM Tanpa AI Slop]] menunjukkan hal yang sama untuk visual: prompt yang menyebut "keep this exact bowl", "do not add any topping", dan "late afternoon sunlight" menghasilkan gambar yang jauh lebih baik daripada "buatkan poster bakso".

## Pola yang muncul

- **Satu tugas, satu prompt.** Jangan mencampur banyak tujuan dalam satu instruksi.
- **Sebutkan referensi.** Foto, dokumen, contoh, atau halaman wiki.
- **Larangan eksplisit.** "Jangan tambah topping", "jangan pakai em-dash", "jangan kirim email tanpa persetujuan".
- **Format output.** PDF, docx, HTML satu file, tiga baris teks.
- **Minta AI bertanya balik.** Jika konteks belum lengkap, minta klarifikasi sebelum eksekusi.
- **Iterasi.** Prompt pertama adalah draft; revisi berdasarkan hasil.
- **Supervisi.** Prompt tidak menghilangkan tanggung jawab manusia.

## Prompt untuk agent vs prompt untuk chat

| Aspek | Chat | Agent |
|---|---|---|
| Konteks | Ditempel di prompt | Dibaca dari memori dan file |
| Panjang | Bisa panjang | Sebaiknya singkat; detail ada di skill |
| Tool | Tidak ada | Harus disebut atau tersedia |
| Verifikasi | Jawaban langsung | Perlu progres, asumsi, dan hasil uji |
| Risiko | Jawaban salah | Tindakan salah (file, email, deploy) |

Pada agent, prompting bergeser menjadi **briefing**: menjelaskan tujuan, batasan, dan bukti yang dibutuhkan, lalu membiarkan agent memilih langkah. [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]] menekankan bahwa agent harus diberi tool dan konteks sebelum dinilai.

## Kesalahan umum

- **Prompt satu baris untuk tugas kompleks.** Menghasilkan output generik.
- **Terlalu banyak instruksi sekaligus.** Agent kehilangan prioritas.
- **Tidak menyebut format.** Hasil sulit dipakai.
- **Tidak meminta bukti.** Agent mengklaim selesai tanpa verifikasi.
- **Pindah model saat hasil buruk.** Sering kali masalahnya konteks, bukan model.
- **Prompt yang memuja.** Model cenderung setuju; minta kritik eksplisit.

## Hubungan dengan konsep lain

- [[ai-slop|AI Slop]] — hasil dari prompting yang malas.
- [[knowledge-management|Knowledge Management]] — konteks yang baik berasal dari pengetahuan yang tersimpan.
- [[agent-skills|Agent Skills]] — memindahkan prompt panjang menjadi prosedur.
- [[ai-leverage-levels|AI Leverage Levels]] — prompting adalah level dasar, bukan tujuan akhir.
- [[business-brain|Business Brain]] — wiki mengurangi kebutuhan prompt panjang.

## Perbedaan dan pertanyaan terbuka

- Apakah prompting masih keterampilan penting ketika agent membaca konteks sendiri? Ya, tetapi bentuknya berubah menjadi kurasi konteks dan briefing.
- Berapa panjang prompt yang optimal? Tidak ada angka; bergantung pada model dan tugas.
- Apakah teknik prompting tertentu (chain-of-thought, few-shot) masih relevan untuk model 2026? Korpus ini tidak membahasnya secara teknis.
- Bagaimana mengukur kualitas prompt tanpa menilai output?

## Sumber

- [[14-skill-ai|14 Skill AI (Last Minute Creator)]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[higgsfield-poster-umkm|Poster UMKM Tanpa AI Slop (Higgsfield)]]
- [[otak-bisnis|Otak Bisnis AI (Last Minute Creator)]]
