---
title: "GPT-6.1 Terra vs Gemini 4 Argon vs Claude Fable 5.1"
type: source
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - model-selection
  - pricing
  - benchmark
  - blender
source_path: "raw/GPT-6.1 TERRA VS GEMINI 4 ARGON VS CLAUDE FABLE 5.1.md"
source_url: https://www.youtube.com/watch?v=_P8W2XOfsXs
author: David Alfa Sunarna
published: 2026-11-07
ingested: 2026-11-08
confidence: high
---

# GPT-6.1 Terra vs Gemini 4 Argon vs Claude Fable 5.1

> Perbandingan praktis tiga kelas model AI pada satu tugas 3D (booth Web Ekspor di Blender via MCP), dengan fokus pada biaya per pekerjaan dan kecocokan tugas, bukan peringkat absolut.

## Sitasi

- **Penulis:** David Alfa Sunarna
- **Terbit:** 2026-11-07
- **URL:** <https://www.youtube.com/watch?v=_P8W2XOfsXs>
- **Salinan lokal:** `raw/GPT-6.1 TERRA VS GEMINI 4 ARGON VS CLAUDE FABLE 5.1.md`

## Ringkasan

Video menguji tiga model pada prompt yang sama: membuat booth pameran Web Ekspor berukuran 12 × 9 meter di Blender, menggunakan MCP sehingga model harus menulis Python dan menerjemahkan instruksi menjadi desain visual. Tujuannya bukan mencari model "paling keren", melainkan memberi justifikasi sebelum berlangganan: mana yang cukup untuk kebutuhan dan budget tertentu.

## Hasil pengujian

| Model | Kelas harga | Waktu | Hasil | Perkiraan biaya per tugas |
|---|---|---|---|---|
| GPT-6.1 Terra | Murah; input $1 per 1 juta token | 4 menit 52 detik | Paling lemah: layar menghadap depan, tanpa atap/lampu, logo hilang, exploded view buruk | ±$0,30 (Rp5.000) |
| Gemini 4 Argon | Google AI Pro Rp300.000/bulan (5 TB) | 29 menit 5 detik | Jauh lebih baik dari Terra; denah lengkap, render dan exploded view rapi | ±$2,64 dengan cache; ±$6,26 tanpa cache (Rp100.000–120.000) |
| Claude Fable 5.1 | Claude Max $200/bulan | 52 menit 29 detik | Paling detail: pencahayaan, interior, sekat bambu, tata letak gudang | ±$21–25 (Rp385.000–450.000) |

## Poin kunci

- **Harga per token bukan harga per pekerjaan.** Terra terlihat sangat murah, tetapi hasilnya perlu banyak iterasi; Fable mahal, tetapi menghasilkan detail yang tidak perlu diperbaiki berkali-kali.
- **Kelas model menentukan jenis tugas.** Terra diposisikan untuk pekerjaan praktis dan visual sederhana; Argon dan Fable untuk tugas berat dan multimodal.
- **Langganan mengubah ekonomi.** Google AI Pro Rp300.000/bulan memberi akses Argon dengan limit yang dinilai longgar; Claude baru berguna pada paket $100–200/bulan.
- **Model murah tetap berguna.** Terra cukup untuk kalender, membaca struk, analisis gambar sederhana, dokumen ringkas, dan pengingat.
- **Keputusan sebaiknya berbasis kebutuhan.** Jangan berlangganan karena tren atau karena kelas mahal "isinya sama saja".

## Klaim dan bukti

| Klaim | Bukti atau lokasi | Keyakinan |
|---|---|---|
| Terra 10× lebih murah daripada Astra dan 50% lebih murah dari Sol. | 0:16–1:06 | Tinggi (angka yang ditampilkan) |
| Terra menyelesaikan tugas dalam 4:52 dengan biaya ±$0,30. | 3:34–5:35 | Tinggi (demo langsung) |
| Argon menyelesaikan tugas dalam 29:05 dengan hasil lebih baik. | 8:19–10:32 | Tinggi (demo langsung) |
| Fable 5.1 membutuhkan 52:29 dan biaya $21–25. | 11:49–13:28 | Tinggi (demo langsung) |
| Model mahal tidak otomatis cocok untuk semua tugas. | 6:20–6:51 | Tinggi (kesimpulan penulis) |
| Argon "worth it" pada harga Rp300.000/bulan. | 9:05–10:32 | Medium (penilaian pribadi) |

## Kutipan

> "Model AI itu enggak keren-kerenan ya. Pakai sesuai dengan kebutuhannya." — 6:20

> "Yang penting kan price to value yang kita keluarin itu worth it." — 11:04

> "Understanding lu terhadap model dan video gua ini yang mengedukasi lu." — 13:47

## Koneksi

- [[model-tiers|Model Tiers]] — kerangka murah/menengah/frontier yang dibuktikan video ini.
- [[model-pilihan-2026|Model AI: Terra, Argon, Fable 5.1]] — perbandingan terfokus.
- [[david-alfa-sunarna|David Alfa Sunarna]] — penguji dan penulis.
- [[claude-code|Claude Code]] — alat yang dipakai untuk menjalankan Fable.
- [[model-routing|Model Routing]] — cara memakai beberapa model sekaligus untuk menekan biaya.

## Perbedaan dan pertanyaan terbuka

- Ini uji satu tugas (Blender/MCP), bukan benchmark menyeluruh. Hasil untuk teks, coding, atau bahasa Indonesia bisa berbeda.
- Harga dihitung dengan tarif API dan asumsi kurs Rp18.100/USD; harga langganan dan kuota bisa berubah.
- Transcript kadang menyebut "Gemini 6 Astra" dan "Claude Fable" tanpa versi; halaman ini mengikuti judul dan konteks video.
- Apakah biaya iterasi (waktu manusia) dihitung? Video menghitung biaya token, bukan waktu pengguna.

## Sumber

- [[hermes-agent-9router|Hermes Agent + 9Router]] — sumber lain yang membandingkan model murah vs Claude Code.
- [[openclaw-vps|OpenClaw di VPS]] — sumber yang menguji GLM vs GPT-6 Astra untuk teks dan coding.
