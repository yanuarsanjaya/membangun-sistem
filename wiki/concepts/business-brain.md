---
title: "Business Brain"
type: concept
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - knowledge-management
  - llm-wiki
  - business
  - second-brain
sources:
  - otak-bisnis
  - 14-skill-ai
  - hermes-agent-kerja
  - karpathy-llm-wiki
confidence: medium
---

# Business Brain

> Penerapan pola LLM Wiki untuk bisnis: vault Markdown yang menyimpan pengetahuan, pengalaman, dan keputusan, dikelola oleh agen sehingga pertanyaan bisnis dijawab dari konteks yang sudah dikompilasi.

## Apa itu

Business brain adalah "otak kedua" yang berisi siapa pemilik bisnis, apa yang dijual, siapa pelanggannya, apa yang sudah dicoba, dan apa yang berhasil. Bentuknya bukan aplikasi khusus, melainkan folder Markdown (biasanya Obsidian) dengan aturan main di `AGENTS.md`, sumber mentah di `raw/`, dan halaman pengetahuan di `wiki/`.

[[otak-bisnis|Otak Bisnis AI]] menyebutnya "kumpulan pengetahuan, pengalaman, dan keputusan bisnis yang disusun agar AI bisa menghubungkannya dengan cepat". [[karpathy-llm-wiki|Karpathy]] menyebut pola dasarnya "persistent, compounding artifact". Business brain adalah pola itu dengan domain bisnis.

## Mengapa penting

Manusia lupa. Pengetahuan bisnis tersebar di bookmark, PDF, DM, spreadsheet, dan kepala. Chatbot web tidak tahu salah satunya. Akibatnya, setiap keputusan dimulai dengan mencari ulang, dan pengalaman tidak pernah menjadi aset.

Business brain mengubah pengalaman menjadi infrastruktur:

- **Keputusan punya jejak.** Alasan di balik harga, positioning, atau konten tersimpan dan bisa dirujuk.
- **Pertanyaan tidak dimulai dari nol.** Agen membaca wiki sebelum menjawab.
- **Jawaban bisa menjadi memori.** Analisis yang berguna disimpan kembali sebagai halaman.
- **Pengetahuan bisa diwariskan.** Tim atau penerus bisa membaca reasoning, bukan hanya hasil.

## Siklus kerja

| Rutinitas | Frekuensi | Fungsi |
|---|---|---|
| Ingest | Saat ada sumber baru | Mengubah dokumen menjadi halaman wiki |
| Tanya jawab | Kapan saja | Menjawab dari wiki, bukan dari tebakan |
| Brain dump | Harian | Menangkap ide dan tugas ke `inbox` |
| Triase | Harian | Merapikan inbox menjadi catatan, proyek, atau arsip |
| Weekly review | Mingguan | Meninjau progres, keputusan, dan prioritas |
| Health check | Bulanan | Mencari halaman yatim, klaim basi, dan kontradiksi |

Rutinitas ini penting karena wiki tanpa perawatan akan membusuk. [[index-and-log|Index dan log]] menjaga navigasi, sedangkan [[ingest-query-lint|Ingest, Query, Lint]] adalah loop dasarnya.

## Isi yang layak disimpan

- Profil diri dan bisnis: siapa, menjual apa, kepada siapa, dengan harga berapa.
- Positioning, brand voice, dan design system.
- Catatan pelanggan: keluhan, pertanyaan, keberatan.
- Data penjualan dan analitik yang sudah dianalisis.
- Keputusan besar dan alasannya.
- SOP dan playbook yang terbukti.
- Referensi konten yang berhasil, beserta analisis mengapa berhasil.

Yang tidak layak: sumber "cara cepat kaya", klaim tanpa bukti, dan data pribadi sensitif yang tidak perlu.

## Fondasi manusia

Sumber paling tegas di bagian ini: business brain hanya sebaik otak yang memberi makan. Jika pemilik bisnis belum punya fondasi, wiki akan memperkuat kesalahan. [[otak-bisnis|Otak Bisnis AI]] memperingatkan bahwa memasukkan sumber menyesatkan membuat "otak bisnis-nya malah jadi tambah menyesatkan" (13:52).

Karena itu urutannya: pahami bisnis → kurasi sumber → baru otomatisasi. [[14-skill-ai|14 Skill AI]] menempatkan knowledge management di level Builder, setelah kemampuan berpikir dan sebelum orkestrasi.

## Hubungan dengan konsep lain

- [[knowledge-management|Knowledge Management]] — disiplin yang mendasarinya.
- [[agent-skills|Agent Skills]] — cara menyimpan prosedur agar bisa dijalankan agen.
- [[agent-memory|Agent Memory]] — memori operasional agent, pelengkap wiki.
- [[ai-leverage-levels|AI Leverage Levels]] — posisi business brain dalam kerangka skill.
- [[prompting|Prompting]] — kualitas pertanyaan menentukan kualitas jawaban.

## Perbedaan dan pertanyaan terbuka

- **Raw immutable vs arsip.** Video Otak Bisnis memindahkan dokumen yang sudah diproses ke `archive`; vault ini mempertahankan `raw/` immutable. Keduanya mencoba mencegah ingest ulang dengan cara berbeda.
- Apakah business brain sebaiknya satu vault atau terpisah per bisnis?
- Berapa banyak kurasi manual yang diperlukan sebelum wiki layak dipercaya?
- Bagaimana mengukur nilai business brain? Sumber hanya memberi anekdot, bukan metrik.

## Sumber

- [[otak-bisnis|Otak Bisnis AI (Last Minute Creator)]]
- [[14-skill-ai|14 Skill AI (Last Minute Creator)]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[karpathy-llm-wiki|LLM Wiki (Karpathy gist)]]
