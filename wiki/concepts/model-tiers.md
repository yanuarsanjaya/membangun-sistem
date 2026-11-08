---
title: "Model Tiers"
type: concept
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - model-selection
  - pricing
  - capability
  - cost
sources:
  - model-comparison-2026-11
  - hermes-agent-9router
  - openclaw-vps
  - hermes-agent-kerja
confidence: high
---

# Model Tiers

> Pembagian model AI berdasarkan harga dan kemampuan — murah, menengah, frontier — serta prinsip bahwa pilihan terbaik adalah yang cocok dengan tugas, bukan yang paling canggih.

## Apa itu

Dalam korpus ini, model tidak dibagi berdasarkan merek, tetapi berdasarkan kelas ekonomi dan kecocokan tugas:

| Kelas | Contoh | Harga indikatif | Cocok untuk |
|---|---|---|---|
| Murah | GPT-6.1 Terra | $1 per 1 juta token input | Tugas rutin, dokumen ringkas, reminder, analisis gambar sederhana |
| Menengah | GPT-6.1 Sol, GLM 5.3, Gemini 4 Argon (via langganan) | $2–20/bulan atau $2 per 1 juta token | Kerja harian, coding ringan, script, presentasi |
| Frontier | GPT-6.1 Astra, Claude Fable 5.1 | $100–200/bulan | Tugas kompleks, visual detail, coding berat |

Angka ini berubah cepat; yang stabil adalah pola: setiap kelas punya titik di mana biaya tambahan tidak lagi sebanding dengan kualitas tambahan.

## Mengapa penting

[[model-comparison-2026-11|Perbandingan Terra/Argon/Fable]] menunjukkan tiga model bisa menyelesaikan tugas yang sama dengan biaya berbeda 70 kali lipat. Model termurah menghasilkan output yang butuh banyak revisi; model termahal menghasilkan detail yang tidak perlu diperbaiki. Keputusan yang rasional bergantung pada:

1. **Nilai output.** Apakah hasilnya dijual, dipakai klien, atau hanya untuk diri sendiri?
2. **Biaya iterasi.** Berapa lama manusia harus memperbaiki output murah?
3. **Frekuensi tugas.** Tugas harian lebih baik memakai model murah; tugas langka boleh memakai model mahal.
4. **Batas langganan.** Langganan memberi kuota, bukan harga per token; pemakaian berat bisa lebih murah lewat langganan.

## Pola yang muncul

- **Model murah untuk tugas kecil.** Terra cukup untuk kalender, struk, dokumen ringkas, dan pengingat.
- **Model menengah untuk kerja sehari-hari.** GLM 5.3 dipakai untuk script, presentasi, dan setup server dengan biaya rendah.
- **Model frontier untuk tugas visual dan kompleks.** Fable menghasilkan detail interior yang tidak dicapai model lain.
- **Model berbeda untuk tugas berbeda.** GLM lebih baik untuk bahasa Indonesia praktis; GPT-6 Astra lebih baik untuk hook dan tugas visual tertentu.
- **Konfigurasi mengalahkan merek.** [[openclaw-vps|OpenClaw di VPS]] menyimpulkan "model itu enggak ngaruh-ngaruh amat; yang ngaruh itu konfigurasi kita" (46:21), meskipun ia juga menemukan perbedaan kualitas pada tugas spesifik.

## Cara memilih

1. Tentukan tugas dan nilai outputnya.
2. Uji model murah lebih dulu.
3. Ukur berapa iterasi yang dibutuhkan.
4. Naik kelas hanya jika biaya iterasi lebih besar daripada selisih harga.
5. Pertimbangkan langganan jika pemakaian sering.
6. Jangan membeli kelas mahal hanya karena takut ketinggalan.

## Hubungan dengan konsep lain

- [[model-routing|Model Routing]] — cara memakai beberapa kelas sekaligus.
- [[model-pilihan-2026|Model AI: Terra, Argon, Fable 5.1]] — perbandingan terfokus.
- [[decision-model|Decision Model]] — model khusus untuk keputusan, bukan generasi.
- [[prompting|Prompting]] — kualitas prompt bisa mengangkat model murah.
- [[self-hosting-agents|Self-Hosting Agents]] — biaya total agent, bukan hanya token.

## Perbedaan dan pertanyaan terbuka

- Harga dan nama model dalam korpus ini berasal dari 2026 dan akan cepat berubah.
- Uji yang ada bersifat anekdotal dan sering hanya satu tugas; tidak ada benchmark independen.
- Apakah model murah dengan prompt bagus selalu mengalahkan model mahal dengan prompt buruk? Sumber cenderung mengatakan ya, tetapi tidak mengujinya secara ketat.
- Bagaimana menghitung biaya waktu manusia dalam perbandingan?

## Sumber

- [[model-comparison-2026-11|GPT-6.1 Terra vs Gemini 4 Argon vs Claude Fable 5.1]]
- [[hermes-agent-9router|Hermes Agent + 9Router]]
- [[openclaw-vps|OpenClaw di VPS]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
