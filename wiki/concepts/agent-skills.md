---
title: "Agent Skills"
type: concept
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - agent-skills
  - sop
  - procedure
  - automation
sources:
  - otak-bisnis
  - 14-skill-ai
  - hermes-agent-kerja
confidence: high
---

# Agent Skills

> Prosedur atau SOP yang ditulis untuk AI agent: berisi kapan dipakai, langkah-langkah, tool yang dibutuhkan, dan standar hasil, sehingga tugas berulang tidak perlu dijelaskan dari nol setiap kali.

## Apa itu

Agent skill adalah dokumentasi yang memberi agent kemampuan spesifik. [[14-skill-ai|14 Skill AI]] mendefinisikannya sederhana: "SOP yang dijelasin ke AI" (11:04). Bedanya dengan prompt biasa adalah skill disimpan, bisa dipanggil ulang, dan biasanya punya struktur: nama, deskripsi, kapan digunakan, langkah, contoh, dan batasan.

Dalam praktik:

- [[otak-bisnis|Otak Bisnis AI]] membuat empat skill inti untuk ingest, triase, weekly review, dan health check, dipasang di level proyek dalam folder `agents/` agar portabel.
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]] mengimpor skill "David content script" dari konfigurasi lama, lalu memakainya untuk menghasilkan script dengan gaya yang konsisten.
- [[jev-ai|JEV AI untuk Pemula]] memasang skill JEV agar agent tahu kapan dan bagaimana memanggil model keputusan.

## Mengapa penting

- **Konsistensi.** Hasil tidak bergantung pada ingatan atau mood prompt hari itu.
- **Efisiensi.** Penjelasan panjang dipindahkan ke file, bukan diulang setiap sesi.
- **Kualitas.** Skill bisa memuat quality bar, contoh baik/buruk, dan larangan.
- **Portabilitas.** Skill berbasis Markdown bisa dipindah antar-agent (Hermes, Claude Code, OpenCode).
- **Belajar dari pengalaman.** Hermes mengklaim bisa mengubah pengalaman kerja menjadi skill; manusia tetap harus meninjau hasilnya.

## Struktur yang baik

| Bagian | Isi |
|---|---|
| Nama | Singkat, menjelaskan tugas |
| Deskripsi | Satu kalimat tentang kemampuan |
| Trigger | Kapan skill dipakai |
| Input | Data atau file yang dibutuhkan |
| Langkah | Urutan eksekusi |
| Tool | Perintah, API, atau MCP yang dipakai |
| Quality bar | Apa yang membuat hasil dianggap selesai |
| Larangan | Hal yang tidak boleh dilakukan |
| Contoh | Output yang baik dan buruk |

## Kapan membuat skill

- Tugas berulang dengan langkah yang stabil.
- Tugas yang punya standar kualitas jelas.
- Tugas yang melibatkan tool spesifik.
- Tugas yang sering salah karena instruksi tidak lengkap.

Jangan membuat skill untuk tugas satu kali, eksplorasi, atau pekerjaan yang belum punya proses jelas. [[14-skill-ai|14 Skill AI]] menyarankan membuat skill secukupnya dan menambah setelah pola berulang muncul.

## Proses pembuatan

1. Kerjakan tugas secara manual beberapa kali.
2. Catat langkah, keputusan, dan kesalahan.
3. Tulis draft skill.
4. Uji pada kasus nyata.
5. Perbaiki berdasarkan kegagalan.
6. Simpan di level proyek; promosikan ke global hanya jika sudah stabil.

Ini setara dengan melatih karyawan baru: bukan sekali jadi, tetapi iterasi sampai hasilnya konsisten.

## Hubungan dengan konsep lain

- [[ai-agent|AI Agent]] — runtime yang menjalankan skill.
- [[knowledge-management|Knowledge Management]] — skill adalah bentuk pengetahuan prosedural.
- [[business-brain|Business Brain]] — tempat skill disimpan dan dirawat.
- [[prompting|Prompting]] — skill mengurangi ketergantungan pada prompt ad hoc.
- [[ai-leverage-levels|AI Leverage Levels]] — skill adalah ciri level Orchestrator.

## Perbedaan dan pertanyaan terbuka

- Berapa banyak skill sebelum agent kesulitan memilih yang relevan?
- Bagaimana menangani skill yang saling bertentangan?
- Apakah skill sebaiknya ditulis manusia, dihasilkan agent, atau keduanya?
- Bagaimana menguji skill secara sistematis, bukan hanya dari satu keberhasilan?

## Sumber

- [[otak-bisnis|Otak Bisnis AI (Last Minute Creator)]]
- [[14-skill-ai|14 Skill AI (Last Minute Creator)]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
