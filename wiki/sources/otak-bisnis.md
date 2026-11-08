---
title: "Otak Bisnis AI (Last Minute Creator)"
type: source
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - knowledge-management
  - llm-wiki
  - business
  - obsidian
  - opencode
source_path: 'raw/Saya Bikin "Otak Bisnis" Biar Jago Cari Duit (Tanpa Mikir Keras).md'
source_url: https://www.youtube.com/watch?v=AurCfDffhbA
author: Last Minute Creator
published: 2026-08-20
ingested: 2026-11-08
confidence: high
---

# Otak Bisnis AI (Last Minute Creator)

> Penerapan pola LLM Wiki milik Karpathy untuk bisnis: vault Obsidian plus agen coding yang meng-ingest dokumen, menjawab pertanyaan dari wiki, dan menyimpan jawaban sebagai memori baru.

## Sitasi

- **Penulis:** Last Minute Creator (kanal YouTube)
- **Terbit:** 2026-08-20
- **URL:** <https://www.youtube.com/watch?v=AurCfDffhbA>
- **Salinan lokal:** `raw/Saya Bikin "Otak Bisnis" Biar Jago Cari Duit (Tanpa Mikir Keras).md`
- **Rujukan utama:** gist LLM Wiki Karpathy, <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>

## Ringkasan

Video ini memperkenalkan "otak bisnis": kumpulan pengetahuan, pengalaman, dan keputusan bisnis yang disusun agar AI bisa menghubungkannya dengan cepat. Masalah yang diserang adalah keterbatasan memori manusia dan pengetahuan yang tersebar di bookmark, PDF, aplikasi catatan, dan folder komputer. Chatbot web tidak tahu isi catatan pribadi, sehingga setiap pertanyaan dimulai dari nol.

Solusinya adalah vault Obsidian lokal yang dibuka dengan agen coding (OpenCode, Claude Code, Codex, atau Hermes), lalu diisi mengikuti pola LLM Wiki. Agen membaca sumber di folder `raw`, membangun halaman wiki, dan menjawab pertanyaan dari hasil kompilasi itu. Jawaban yang berguna bisa disimpan kembali, sehingga wiki bertambah sebagai memori.

## Poin kunci

- **Masalahnya bukan kekurangan AI, tapi kekurangan memori terstruktur.** Manusia lupa dan informasi tersebar; chatbot generik tidak punya konteks pribadi.
- **Stack minimal:** Obsidian sebagai editor Markdown lokal, agen coding sebagai operator, dan skill Obsidian agar agen paham cara memakai vault.
- **`agents.md` (atau `claude.md`) adalah pusat kendali.** Isinya aturan yang harus diikuti agen saat mengelola wiki dan menjawab pertanyaan; aturan ini bisa terus diperbarui.
- **Folder `raw` menerima sumber apa pun.** Catatan, PDF, transkrip YouTube, data analitik, dan insight bisa langsung dimasukkan tanpa dirapikan dulu.
- **Ingest menghasilkan memori.** Dokumen diekstrak menjadi halaman wiki; jawaban atas pertanyaan bisnis juga bisa di-ingest lagi agar tidak hilang.
- **Arsip mencegah pemrosesan ulang.** Dalam implementasi video ini, dokumen yang sudah diproses dipindahkan ke folder `archive` dan instruksi ingest diperbarui.
- **Second brain butuh rutinitas.** Selain ingest, ada triase inbox, weekly review, pengecekan bulanan, dan "cek kesehatan" wiki.
- **Agent skills sebaiknya sedikit dan inti.** Video memilih empat skill awal, dipasang di level proyek dalam folder `agents/` agar mudah dipindah ke tool lain.
- **Fondasi manusia tetap penentu.** Jika yang dimasukkan adalah sumber "cara cari uang instan", otak bisnis justru menjadi menyesatkan.

## Klaim dan bukti

| Klaim | Bukti atau lokasi | Keyakinan |
|---|---|---|
| Manusia sering lupa dan pengetahuan tersebar di banyak aplikasi. | 0:18 | Tinggi (premis yang wajar) |
| Chatbot web tidak mengetahui catatan pribadi pengguna. | 0:18 | Tinggi |
| Pola LLM Wiki bisa diinstal dalam sekitar lima menit dengan agen coding. | 3:17–3:42 | Medium (pengalaman demonstrasi) |
| Ingest transkrip panjang bisa memakan 10–15 menit. | 6:56 | Medium (perkiraan praktisi) |
| Jawaban yang disimpan kembali menambah memori wiki. | 8:50 | Tinggi (mekanisme yang didemonstrasikan) |
| Dokumen yang sudah diproses sebaiknya dipindah ke `archive`. | 4:25–4:56 | Medium (pilihan implementasi, bukan keharusan pola) |
| Agent skills sebaiknya dipasang di level proyek agar portabel. | 11:51–12:11 | Medium (praktik penulis) |
| Kualitas sumber menentukan kualitas otak bisnis. | 13:28–14:00 | Tinggi (prinsip umum) |

## Kutipan

> "LLM Wiki ini hanya berfungsi sebagai perpustakaan, di mana si AI agent itu menjadi pustakawannya." — 9:08

> "Otak yang inti adalah otak kita sebagai manusia." — 13:28

> "Kalau fondasi belum kuat, nanti yang kita injeksi itu adalah sumber-sumber yang malah menyesatkan." — 13:52

## Catatan implementasi

Alur yang ditunjukkan:

1. Buat vault Obsidian, aktifkan akses CLI/terminal agar agen bisa terhubung.
2. Pasang skill Obsidian dari repo GitHub, lalu restart agen.
3. Minta agen menyiapkan struktur LLM Wiki dari gist Karpathy.
4. Masukkan sumber ke `raw`; gunakan Obsidian Web Clipper untuk artikel dan transkrip YouTube.
5. Minta agen meng-ingest; untuk PDF besar, jangan lakukan banyak sekaligus.
6. Wawancarai diri sendiri agar agen tahu siapa pengguna dan bisnisnya; simpan hasil wawancara ke `raw`, lalu ingest.
7. Ajukan pertanyaan bisnis; simpan jawaban yang layak sebagai halaman baru.
8. Tambahkan command triase, weekly review, dan health check; buat agent skills secukupnya.
9. Lakukan brain dump ke `inbox`, triase harian, dan review berkala.

## Koneksi

- [[karpathy-llm-wiki|LLM Wiki (Karpathy gist)]] — pola asal yang diterapkan.
- [[business-brain|Business Brain]] — konsep yang dibangun video ini.
- [[ai-agent|AI Agent]] — agen yang menjadi operator vault.
- [[agent-skills|Agent Skills]] — prosedur yang dipasang agar agen konsisten.
- [[knowledge-management|Knowledge Management]] — prasyarat yang membuat wiki berguna.
- [[opencode|OpenCode]] — salah satu agen yang dipakai.

## Perbedaan dan pertanyaan terbuka

- **Konflik dengan skema vault ini.** Video memindahkan dokumen yang sudah di-ingest ke `archive`. Skema vault ini menetapkan `raw/` immutable dan tidak boleh diubah. Keduanya masuk akal: arsip mencegah ingest ulang, sedangkan raw immutable menjaga provenance. Vault ini memilih raw immutable dan menggunakan catatan `ingested:` di frontmatter untuk mencegah pemrosesan ulang.
- Apakah "cek kesehatan" dan weekly review cukup untuk mencegah wiki membusuk, atau tetap perlu lint manual?
- Berapa banyak sumber yang boleh di-ingest sekaligus sebelum kualitas integrasi turun?
- Apakah wawancara diri sendiri lebih baik dilakukan sekali di awal atau diperbarui berkala?

## Sumber

- [[karpathy-llm-wiki|LLM Wiki (Karpathy gist)]]
