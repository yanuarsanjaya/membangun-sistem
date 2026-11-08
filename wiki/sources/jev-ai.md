---
title: "JEV AI untuk Pemula (TypeSafe)"
type: source
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - decision-model
  - typesafe
  - classification
  - agent-integration
source_path: "raw/TUTORIAL JEV AI UNTUK PEMULA.md"
source_url: https://www.youtube.com/watch?v=DaspSn5FbgQ
author: David Alfa Sunarna
published: 2026-11-05
ingested: 2026-11-08
confidence: high
---

# JEV AI untuk Pemula (TypeSafe)

> Model keputusan dari TypeSafe AI yang tidak mengobrol, tidak menulis, dan tidak merangkum; ia hanya menjawab pertanyaan ya/tidak atau skor probabilitas atas data terstruktur, dengan latensi milidetik dan biaya sangat rendah.

## Sitasi

- **Penulis:** David Alfa Sunarna
- **Terbit:** 2026-11-05
- **URL:** <https://www.youtube.com/watch?v=DaspSn5FbgQ>
- **Salinan lokal:** `raw/TUTORIAL JEV AI UNTUK PEMULA.md`

## Ringkasan

JEV (dari TypeSafe AI, didirikan antara lain oleh Diogo Almeida, mantan peneliti OpenAI) adalah "decision model" atau model sistem satu. Ia menerima `state` dan `question` dalam bentuk JSON, lalu mengembalikan probabilitas bahwa suatu kondisi benar. Video mendemonstrasikan klasifikasi komentar spam judi online, pengecekan kekuatan password, validasi email, dan penyortiran 273 email lamaran kerja.

## Poin kunci

- **Satu tugas: memutuskan.** JEV tidak bisa menulis, mengobrol, atau merangkum. Ia dirancang untuk keputusan berulang dalam jumlah besar.
- **Input terstruktur.** `state` berisi data (misalnya platform, jenis konten, daftar komentar) dan `question` berisi kriteria keputusan.
- **Latensi rendah.** Satu komentar diproses dalam 18 ms; empat komentar dalam 25 ms; 273 email disortir dalam 0,45 detik.
- **Murah.** Saldo $5 bisa bertahan berbulan-bulan; ada free tier.
- **Integrasi lewat agen.** Pengguna tidak memanggil JEV langsung; agen (Hermes, Claude Code) yang menyusun state, memanggil JEV, dan menafsirkan hasil.
- **Cocok untuk klasifikasi sempit.** Spam, email, tiket customer service, leads, sentimen, validasi input.
- **Tidak cocok untuk aritmetika, perbandingan tanggal, atau input panjang dan berisik.** Akurasi turun jika konteks penuh noise.

## Klaim dan bukti

| Klaim | Bukti atau lokasi | Keyakinan |
|---|---|---|
| JEV hanya melakukan keputusan, bukan generasi teks. | 2:23–3:25 | Tinggi (deskripsi produk) |
| Satu komentar spam diklasifikasi dalam 18 ms dengan keyakinan 82%. | 4:56 | Tinggi (demo playground) |
| Empat komentar diproses dalam 25 ms dengan akurasi 87–93%. | 6:17–6:46 | Tinggi (demo playground) |
| Hermes + JEV menyortir 273 email dalam 0,45 detik; 214 lamaran valid. | 17:09–17:47 | Tinggi (demo) |
| Biaya sangat rendah; saldo $5 hampir tidak berkurang. | 3:58–4:19; 17:30 | Medium (pengamatan penulis) |
| JEV lemah pada aritmetika dan perbandingan tanggal. | 21:44 | Tinggi (diakui vendor menurut penulis) |
| Model besar (Claude) butuh 13 menit untuk tugas sortir yang sama. | 20:05 | Medium (satu percobaan) |

## Kutipan

> "AI yang enggak bisa ngomong, enggak bisa nulis, enggak bisa ngobrol, dan enggak bisa ngerangkum. Dia diciptakan untuk satu hal aja: memutuskan." — 3:25

> "LLM yang bagus adalah yang bisa membantah kita." — 8:27

> "Gunakan JEV untuk hal khusus, untuk decision aja." — 21:44

## Koneksi

- [[decision-model|Decision Model]] — konsep yang dirumuskan dari sumber ini.
- [[jev-typesafe|JEV (TypeSafe AI)]] — entitas produk.
- [[ai-agent|AI Agent]] — lapisan yang memanggil JEV.
- [[hermes-agent|Hermes Agent]] — tempat JEV diintegrasikan lewat skill.
- [[model-routing|Model Routing]] — pola "model utama + model keputusan" untuk menghemat limit.

## Perbedaan dan pertanyaan terbuka

- Angka akurasi berasal dari demo dan bukan evaluasi independen. Performa pada data dunia nyata bisa berbeda.
- Klaim "free tier" dan "saldo $5 bertahan berbulan-bulan" tidak disertai rincian kuota.
- Apakah JEV lebih baik daripada classifier murah lain (misalnya model kecil fine-tuned) untuk tugas yang sama? Video tidak membandingkan.
- Risiko utama: keputusan otomatis pada data sensitif (lamaran kerja, kredit, moderasi) membutuhkan audit dan jalur banding.

## Sumber

- [[hermes-agent-9router|Hermes Agent + 9Router]] — konteks integrasi agen.
