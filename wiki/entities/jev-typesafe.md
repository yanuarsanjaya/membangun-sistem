---
title: "JEV (TypeSafe AI)"
type: entity
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - product
  - decision-model
  - typesafe
  - api
sources:
  - jev-ai
  - model-routing
confidence: medium
---

# JEV (TypeSafe AI)

> Model keputusan dari TypeSafe AI yang mengubah pertanyaan ya/tidak menjadi probabilitas, dengan latensi milidetik dan biaya rendah.

## Apa itu

JEV adalah produk utama TypeSafe AI, perusahaan yang didirikan antara lain oleh Diogo Almeida (mantan peneliti OpenAI) dan disebut "Ely Labs" dalam transkrip. Ia bukan LLM generatif: input berupa `state` dan `question` dalam JSON, output berupa probabilitas atau label.

## Kemampuan

- Klasifikasi spam, leads, tiket, sentimen.
- Validasi input: password, email, format data.
- Penyortiran email dan dokumen dalam jumlah besar.
- Keputusan berulang dengan kriteria jelas.

## Batasan

- Lemah pada aritmetika dan perbandingan tanggal.
- Akurasi turun pada input panjang dan berisik.
- Tidak cocok untuk penjelasan naratif.
- Perlu integrasi lewat agent atau kode.

## Harga dan akses

- Saldo minimum $5; menurut sumber bisa bertahan berbulan-bulan.
- Ada free tier, tetapi kuotanya tidak dirinci.
- API console menyediakan playground.
- Integrasi tersedia untuk Claude Code dan Hermes (lewat skill komunitas).

## Peran dalam korpus

[[jev-ai|JEV AI untuk Pemula]] mendemonstrasikan klasifikasi komentar judi online (18–25 ms, akurasi 82–93%), penyortiran 273 email lamaran (0,45 detik, 214 valid), dan validasi password/email. [[model-routing|Model Routing]] menempatkannya sebagai spesialis yang dipanggil agent.

## Kutipan

> "Dia diciptakan untuk satu hal aja: memutuskan." — [[jev-ai|JEV AI untuk Pemula]], 3:25

## Koneksi

- [[decision-model|Decision Model]] — kategori.
- [[ai-agent|AI Agent]] — pemanggil.
- [[hermes-agent|Hermes Agent]] — tempat integrasi.
- [[model-routing|Model Routing]] — pola model utama + spesialis.

## Pertanyaan terbuka

- Apakah ada evaluasi independen atas akurasi JEV?
- Bagaimana harga per 1.000 keputusan dibanding classifier lain?
- Apakah data pelanggan dipakai untuk pelatihan?
- Bagaimana menangani keputusan yang salah pada data sensitif?

## Sumber

- [[jev-ai|JEV AI untuk Pemula (TypeSafe)]]
- [[model-routing|Model Routing]]
