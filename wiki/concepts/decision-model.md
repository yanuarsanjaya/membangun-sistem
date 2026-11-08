---
title: "Decision Model"
type: concept
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - decision-model
  - classification
  - system-one
  - typesafe
sources:
  - jev-ai
  - model-routing
confidence: medium
---

# Decision Model

> Model AI yang dirancang hanya untuk mengambil keputusan terstruktur — ya/tidak atau skor probabilitas — bukan untuk menulis, mengobrol, atau merangkum.

## Apa itu

Decision model adalah lawan dari model generatif serba bisa. Ia menerima `state` (data terstruktur dalam JSON) dan `question` (kriteria keputusan), lalu mengembalikan probabilitas bahwa kondisi itu benar. Contohnya [[jev-typesafe|JEV]] dari TypeSafe AI.

Perbedaan dengan LLM biasa:

| Aspek | LLM (system two) | Decision model (system one) |
|---|---|---|
| Output | Teks bebas | Probabilitas / label |
| Tugas | Menulis, mengobrol, merangkum | Mengklasifikasi, menyortir, memvalidasi |
| Latensi | Detik sampai menit | Milidetik |
| Biaya | Per token, relatif mahal | Sangat rendah |
| Kelemahan | Sycophancy, halusinasi, lambat | Sempit, lemah pada aritmetika dan input berisik |

## Mengapa penting

Banyak pekerjaan AI sebenarnya bukan pekerjaan menulis. Menyortir email, mendeteksi spam, memvalidasi input, dan menentukan apakah sebuah tiket masuk kategori A atau B adalah keputusan, bukan generasi. Memakai LLM besar untuk tugas seperti ini lambat dan mahal.

[[jev-ai|JEV AI untuk Pemula]] mendemonstrasikan perbedaannya: menyortir 273 email lamaran dengan JEV memakan 0,45 detik, sedangkan Claude membutuhkan sekitar 13 menit untuk tugas yang sama (20:05). Pada volume besar, perbedaan ini menentukan kelayakan operasional.

## Pola pemakaian

1. **Agent menyusun state.** Manusia tidak memanggil decision model langsung; agent mengubah data mentah menjadi JSON.
2. **Question harus spesifik.** Kriteria harus jelas dan bisa dievaluasi.
3. **Gunakan untuk keputusan berulang.** Spam, leads, tiket, sentimen, validasi.
4. **Tetapkan ambang.** Skor 0,9 bisa diterima otomatis; skor 0,6 masuk antrean manusia.
5. **Audit sampel.** Uji akurasi pada data nyata secara berkala.

## Kapan tidak dipakai

- Aritmetika dan perbandingan tanggal (diakui lemah).
- Input panjang, berisik, atau ambigu.
- Keputusan bernilai tinggi tanpa jalur banding.
- Tugas yang membutuhkan penjelasan naratif.

## Hubungan dengan konsep lain

- [[jev-typesafe|JEV (TypeSafe AI)]] — implementasi utama.
- [[model-routing|Model Routing]] — pola model utama + spesialis.
- [[ai-agent|AI Agent]] — pemanggil decision model.
- [[model-tiers|Model Tiers]] — kelas biaya dan kemampuan.

## Perbedaan dan pertanyaan terbuka

- Apakah decision model lebih akurat daripada classifier klasik atau model kecil fine-tuned? Belum ada perbandingan independen di korpus.
- Bagaimana menangani distribusi data yang berubah (drift)?
- Apakah keputusan otomatis pada data sensitif (lamaran kerja, kredit) dapat dipertanggungjawabkan tanpa audit manusia?
- Seberapa besar penurunan akurasi pada input berisik? Sumber hanya menyebut "turun", tanpa angka.

## Sumber

- [[jev-ai|JEV AI untuk Pemula (TypeSafe)]]
- [[model-routing|Model Routing]]
