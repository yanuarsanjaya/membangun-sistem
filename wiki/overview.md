---
title: "Overview"
type: overview
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - meta
---

# Overview

> Sintesis tingkat atas wiki ini: AI terapan untuk bisnis kecil dan pekerja mandiri di Indonesia — dari mengelola pengetahuan, menjalankan agent, sampai menjaga kualitas output.

## Domain dan cakupan

Vault ini dimulai sebagai contoh pola [[persistent-wiki|LLM Wiki]], lalu melebar pada 2026-11-08 setelah delapan sumber masuk. Domainnya sekarang adalah **AI terapan untuk bisnis kecil**: cara pemilik bisnis atau pekerja mandiri memakai agent, menyimpan pengetahuan, memilih model, dan menghasilkan output yang layak dijual.

Sumbernya sebagian besar tutorial YouTube Indonesia dan catatan praktisi, bukan riset peer-review. Wiki ini karena itu mencatat **praktik lapangan** — konfigurasi yang berhasil, biaya nyata, dan kegagalan yang dialami — dengan tingkat keyakinan yang ditandai di setiap halaman. Klaim tentang harga, nama model, dan kepemilikan produk adalah potret akhir 2026 dan perlu diverifikasi ke sumber primer.

Wiki ini bukan chat log dan bukan cermin sumber mentah. Ia adalah lapisan terkompilasi: definisi, entitas, perbandingan, dan sintesis yang terus direvisi saat sumber baru masuk.

## Sintesis saat ini

Korpus ini berbicara tentang tiga lapisan yang saling bergantung.

### 1. Lapisan pengetahuan: otak yang tumbuh

Gagasan pusatnya tetap **kompilasi, bukan retrieval**. Sistem RAG mencari ulang potongan dokumen setiap kali ditanya; wiki yang persisten membaca sumber sekali, mengekstrak yang penting, dan menyimpannya sebagai halaman yang saling terhubung. [[business-brain|Business Brain]] menerapkan pola itu ke bisnis: siapa pemiliknya, apa yang dijual, siapa pelanggannya, keputusan apa yang sudah diambil dan mengapa. [[otak-bisnis|Otak Bisnis AI]] menyebutnya kumpulan pengetahuan, pengalaman, dan keputusan yang disusun agar AI bisa menghubungkannya dengan cepat.

Yang membuat lapisan ini bernilai bukan ringkasannya, melainkan **integrasinya**: [[agent-memory|memori agent]] menyimpan fakta operasional, [[knowledge-management|knowledge management]] menyimpan SOP dan konteks, dan wiki menyimpan sintesis yang bisa dibaca manusia. Peringatan yang berulang: otak yang buruk akan memperkuat kesalahan. Jika sumbernya menyesatkan, wiki-nya "malah jadi tambah menyesatkan" ([[otak-bisnis|Otak Bisnis AI]], 13:52).

### 2. Lapisan eksekusi: agent sebagai pekerja

[[ai-agent|AI Agent]] di korpus ini bukan chatbot, melainkan sistem yang berjalan terus di VPS, menerima perintah dari Telegram atau dashboard, membaca memori dan skill, memilih tool, lalu mengeksekusi beberapa langkah. Anatominya berulang: model, runtime/gateway, [[model-routing|router model]], memori, [[agent-skills|skills]], tool, dan kanal komunikasi.

Dua implementasi mendominasi: [[hermes-agent|Hermes Agent]] yang fleksibel dan murah, serta [[openclaw|OpenClaw]] yang matang tetapi condong ke ekosistem OpenAI. Perbandingannya ada di [[hermes-vs-openclaw|Hermes vs OpenClaw]]. Di belakangnya ada lapisan ekonomi: [[9router|9Router]] menurunkan biaya lewat tier gratis, sedangkan [[self-hosting-agents|self-hosting]] memindahkan biaya dari langganan ke VPS dan perawatan. [[budget-agent-24-7|Anggaran agent 24/7]] merangkum tiga tingkat biaya dan biaya tersembunyinya.

Pola yang muncul: agent yang berguna adalah agent yang **punya konteks dan batas kewenangan**, bukan agent yang paling otonom. Aturan seperti "jangan kirim email tanpa persetujuan" dan akses lewat Tailscale lebih menentukan keamanan daripada merek model.

### 3. Lapisan kualitas: output yang tidak memalukan

[[model-tiers|Model Tiers]] membagi pilihan menjadi murah, menengah, dan frontier, dengan prinsip bahwa model terbaik adalah yang cocok dengan nilai tugas. [[model-pilihan-2026|Perbandingan Terra/Argon/Fable]] menunjukkan biaya bisa berbeda puluhan kali untuk tugas yang sama, dan model termurah sering membutuhkan lebih banyak revisi.

Tetapi kualitas bukan hanya soal harga model. [[prompting|Prompting]] yang menyebut konteks, hasil yang diinginkan, dan batasan menghasilkan output yang jauh lebih baik. [[ai-slop|AI Slop]] adalah lawannya: output generik yang merusak kepercayaan. Sumber [[higgsfield-poster-umkm|poster UMKM]] menunjukkan cara menghindarinya untuk visual — foto produk asli, detail tekstur, dan prompt yang spesifik, bukan template kosong.

### Tangga leverage

[[ai-leverage-levels|AI Leverage Levels]] menyusun semuanya sebagai tangga: **User** memakai chat, **Thinker** memakai AI untuk berpikir, **Builder** membangun sistem pengetahuan dan SOP, **Orchestrator** menjalankan banyak agent dan model. Tangga ini bukan syarat administratif; ia menjelaskan mengapa kebanyakan orang berhenti di level User dan mengapa nilai terbesar muncul saat pengetahuan dan prosedur mulai disimpan.

## Halaman kunci

- [[business-brain|Business Brain]] — pola LLM Wiki diterapkan ke pengetahuan dan keputusan bisnis.
- [[ai-agent|AI Agent]] — anatomi agent yang berjalan 24/7 dan tiga pola pemakaiannya.
- [[ai-leverage-levels|AI Leverage Levels]] — tangga User, Thinker, Builder, Orchestrator.
- [[hermes-vs-openclaw|Hermes Agent vs OpenClaw]] — perbandingan dua framework agent.
- [[model-pilihan-2026|Model AI: Terra, Argon, Fable 5.1]] — kelas model dan biaya nyata.
- [[budget-agent-24-7|Berapa Budget untuk AI Agent 24/7?]] — tiga tingkat anggaran.
- [[persistent-wiki|Persistent Wiki]] — gagasan dasar yang masih menjadi fondasi.

## Keadaan saat ini

- Sumber: 9
- Konsep: 16
- Entitas: 9
- Perbandingan: 2
- Pertanyaan: 1
- Meta: 2
- Total halaman konten: 39 (42 termasuk overview, index, dan log)
- Terakhir diperbarui: 2026-11-08

**Antrean.** Dokumen baru terus muncul di `raw/` selama sesi ini — seri tutorial Git/GitHub dan tutorial AI/bisnis — dan belum di-ingest. Lihat [[lint-2026-11-08-post-ingest|Lint Report 2026-11-08 (Post-Ingest)]].

## Kontradiksi yang tercatat

1. **Raw immutable vs folder arsip.** [[otak-bisnis|Otak Bisnis AI]] memindahkan dokumen yang sudah diproses ke `archive/` agar tidak di-ingest ulang. Vault ini mempertahankan `raw/` immutable dan mengandalkan log serta index. Keduanya mencegah pengulangan dengan cara berbeda; tidak ada yang salah, tetapi konsekuensinya berbeda untuk audit.
2. **Model vs konfigurasi.** [[openclaw-vps|OpenClaw di VPS]] menyimpulkan "model itu enggak ngaruh-ngaruh amat; yang ngaruh itu konfigurasi kita" (46:21), tetapi sumber yang sama juga menemukan perbedaan kualitas pada tugas visual. [[model-tiers|Model Tiers]] menahan kedua klaim: konfigurasi dominan untuk tugas rutin, model tetap terasa pada tugas kompleks.
3. **Gratis vs berbayar murah.** [[hermes-agent-9router|Hermes + 9Router]] menunjukkan agent 24/7 bisa jalan nyaris gratis, sedangkan [[hermes-agent-kerja|Hermes untuk Kerja Nyata]] naik ke $10–40/bulan karena tier gratis terasa lambat. Perbedaannya bukan ideologi, melainkan nilai waktu dan jenis tugas.

## Pertanyaan terbuka

- **Keamanan.** Sumber menyebut Tailscale, aturan keras, dan supervisi, tetapi belum ada model ancaman lengkap untuk prompt injection, kebocoran kredensial, dan tool berbahaya.
- **ROI.** Hampir semua klaim manfaat bersifat anekdot. Belum ada metrik yang menghubungkan agent dengan pendapatan atau jam kerja yang dihemat.
- **Kesegaran harga dan model.** Nama, harga, dan kemampuan model berubah cepat; halaman harus diberi tanggal dan diverifikasi ulang sebelum dipakai untuk keputusan besar.
- **Kualitas sumber.** Tutorial YouTube punya insentif komersial (afiliasi, kursus, produk). Klaim seperti akuisisi OpenClaw oleh OpenAI perlu dicek ke sumber primer.
- **Konteks lokal.** Seberapa banyak praktik ini berlaku untuk UMKM tanpa staf teknis, koneksi tidak stabil, dan anggaran di bawah $10/bulan?
- **Arsitektur memori.** File Markdown, database vektor, atau wiki terstruktur — korpus ini condong ke Markdown yang bisa dibaca manusia, tetapi belum ada perbandingan empiris.

## Cara pakai

1. Taruh sumber di `raw/inbox/` dan jalankan `/ingest <path>`.
2. Tanya `/ask <pertanyaan>` dan ikuti sitasinya ke halaman wiki.
3. Jalankan `/lint` setelah beberapa ingest, atau saat wiki terasa tidak konsisten.
4. Buka `wiki/views.base` untuk tabel halaman berdasarkan tipe, status, dan tanggal.

## Sumber

- [[karpathy-llm-wiki|LLM Wiki (Karpathy gist)]]
- [[otak-bisnis|Otak Bisnis AI (Last Minute Creator)]]
- [[14-skill-ai|14 Skill AI (Last Minute Creator)]]
- [[model-comparison-2026-11|GPT-6.1 Terra vs Gemini 4 Argon vs Claude Fable 5.1]]
- [[jev-ai|JEV AI untuk Pemula (TypeSafe)]]
- [[hermes-agent-9router|Hermes Agent + 9Router (Murah Meriah)]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[openclaw-vps|OpenClaw di VPS (2026)]]
- [[higgsfield-poster-umkm|Poster UMKM Tanpa AI Slop (Higgsfield)]]
