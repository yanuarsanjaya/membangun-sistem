---
title: "Git & GitHub Dasar (WPU)"
type: source
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - git
  - github
  - version-control
  - tutorial
source_path: "raw/2 BEKERJA DENGAN GITHUB.md"
source_paths:
  - "raw/1 APA ITU GIT & GITHUB?.md"
  - "raw/2 BEKERJA DENGAN GITHUB.md"
  - "raw/3 GITHUB  BRANCH.md"
  - "raw/4 GITHUB  FORK.md"
  - "raw/5 BEKERJA DENGAN GIT.md"
  - "raw/6 GIT BRANCH & MERGE.md"
  - "raw/7 GIT MERGE CONFLICT.md"
  - "raw/8 GIT REMOTE.md"
  - "raw/9 GITHUB PAGES  NGOBAR12  Web Hosting Gratis dengan GitHub Pages.md"
  - "raw/10 MULTIPLE REMOTES.md"
  - "raw/11 REMOTE BRANCH.md"
  - "raw/12 GITIGNORE.md"
  - "raw/13 GIT REBASE.md"
  - "raw/14 GIT & WEB HOSTING.md"
source_url: "https://www.youtube.com/playlist?list=PLFIM0718LjIVknj6sgsSceMqlq242-jNf"
author: "WPU (Sandhika Galih)"
published: "2019-04-16 – 2019-07-01"
ingested: 2026-11-08
confidence: medium
---

# Git & GitHub Dasar (WPU)

> Playlist 14 episode WPU tentang Git dan GitHub, dari membuat repository dan commit sampai branch, pull request, merge conflict, remote, rebase, dan hosting statis.

## Citation

- **Author:** WPU / Web Programming UNPAS (Sandhika Galih)
- **Published:** 16 April – 1 Juli 2019
- **URL:** [Playlist Git & GitHub](https://www.youtube.com/playlist?list=PLFIM0718LjIVknj6sgsSceMqlq242-jNf)
- **Local copies:** 14 file di `raw/`; hanya episode 2 dan 3 yang memuat transkrip. Episode lain hanya berisi deskripsi YouTube, tautan, dan informasi kanal.

## Cakupan sumber

| Episode | Topik | Transkrip |
|---|---|---|
| 1 | Apa itu Git & GitHub | Tidak |
| 2 | Bekerja dengan GitHub: akun, repository, commit | Ya |
| 3 | GitHub Branch: branch, checkout, pull request, merge, conflict | Ya |
| 4 | GitHub Fork | Tidak |
| 5 | Bekerja dengan Git (lokal) | Tidak |
| 6 | Git branch & merge | Tidak |
| 7 | Git merge conflict | Tidak |
| 8 | Git remote | Tidak |
| 9 | GitHub Pages untuk hosting gratis | Tidak |
| 10 | Multiple remotes | Tidak |
| 11 | Remote branch | Tidak |
| 12 | `.gitignore` | Tidak |
| 13 | Git rebase | Tidak |
| 14 | Git dan web hosting | Tidak |

Karena 12 episode hanya berupa metadata, halaman ini **tidak** merangkum isi yang tidak ada. Ia mencatat kurikulum, dua episode yang bertranskrip, dan istilah yang diperkenalkan judul-judulnya. Detail konsep diambil dari episode 2 dan 3 serta pengetahuan umum Git yang sesuai.

## Key takeaways

- **Git menyimpan perubahan, bukan file final saja.** Setiap commit adalah snapshot dengan hash, pesan, penulis, dan diff. Riwayat bisa dilihat per file atau per repository (episode 2, 11:58–13:54).
- **Repository adalah folder proyek berversi.** GitHub adalah tempat hosting repository; pekerjaan bisa dilakukan langsung di web atau di komputer lokal (episode 2, 3:38–6:51).
- **Branch adalah jalur pengembangan independen.** Ia memungkinkan eksperimen tanpa mengganggu jalur utama; `checkout` berpindah antar-branch (episode 3, 0:45–2:58, 10:16).
- **Pull request adalah permintaan untuk menarik perubahan.** Branch meminta pemilik jalur utama menarik perubahannya; di GitLab istilahnya merge request (episode 3, 13:51–16:32).
- **Merge conflict terjadi saat dua branch mengubah baris yang sama.** Konflik diselesaikan manual, lalu di-merge (episode 3, 23:01–24:56).
- **Fork menyalin repository orang lain** agar bisa dikembangkan sendiri atau diusulkan kembali lewat pull request (judul episode 4).
- **Remote, rebase, `.gitignore`, dan GitHub Pages** melengkapi alur kerja: menghubungkan repo lokal ke server, merapikan riwayat, mengabaikan file, dan mempublikasikan situs statis (judul episode 8–14).

## Claims and evidence

| Klaim | Bukti atau lokasi | Keyakinan |
|---|---|---|
| Repository adalah folder proyek; GitHub meng-host-nya | Episode 2, 3:38–6:51 | Tinggi |
| Commit mencatat perubahan dan siapa yang melakukannya | Episode 2, 11:58–13:29 | Tinggi |
| Setiap commit punya hash sebagai identitas | Episode 2, 13:29–13:54 | Tinggi |
| Branch adalah snapshot independen dari jalur utama | Episode 3, 0:45–2:58 | Tinggi |
| `checkout` berarti berpindah branch | Episode 3, 10:16 | Tinggi |
| Pull request meminta pemilik master menarik perubahan | Episode 3, 13:51–16:32 | Tinggi |
| Merge conflict muncul saat baris yang sama diubah dua branch | Episode 3, 23:01–23:57 | Tinggi |
| Fast-forward vs three-way merge | Episode 3, 25:11–25:41 | Sedang (disebut, tidak dijelaskan detail) |
| Fork, remote, rebase, gitignore, Pages | Judul episode 4, 8–14 | Rendah (tidak ada transkrip) |

## Quotes

> "Git hanya menyimpan perubahannya. Git-nya tidak mengeksekusi file-nya." — Episode 3, 6:24

> "Branch ini adalah ketika kalian membuat snapshot tanpa mengganggu jalur utama." — Episode 3, 2:08

> "Pull request ini adalah sebuah cara kita untuk meminta agar pemilik dari repo-nya atau master branch-nya menarik perubahan kita." — Episode 3, 26:42

> "Merge conflict terjadi ketika baris yang sama diubah oleh dua branch yang berbeda." — Episode 3, 27:04

## Connections

- [[git-version-control|Git Version Control]] — konsep di balik commit, branch, merge, dan rebase.
- [[github-workflow|GitHub Workflow]] — alur kolaborasi dan publikasi di GitHub.
- [[github|GitHub]] — platform yang dibahas.
- [[wpu|WPU (Web Programming UNPAS)]] — pembuat seri.
- [[pemrograman-untuk-builder|Pemrograman untuk Builder]] — mengapa version control berguna bahkan bagi non-programmer.
- [[ai-coding-agent|AI Coding Agent]] — agent coding bekerja di atas repository dan riwayat Git.

## Open questions

- Seri ini dibuat pada 2019 dan memakai istilah **master branch**. GitHub sekarang memakai `main` secara default; istilah dan tampilan di video sudah berubah.
- 12 dari 14 episode tidak memiliki transkrip, sehingga konsep seperti rebase, multiple remotes, dan `.gitignore` belum bisa dirangkum dari sumber ini.
- Tidak ada pembahasan tentang GitHub Actions, code review tim, atau keamanan repository.
- Apakah alur web-first (edit langsung di GitHub) masih relevan sekarang, ketika agent coding lebih sering bekerja di repo lokal?

## Catatan kualitas sumber

Video ini adalah tutorial pemula yang jelas dan visual, tetapi sudah berumur. Konsep intinya (commit, branch, merge, pull request) tetap berlaku; detail UI, nama branch default, dan fitur GitHub perlu diverifikasi ke dokumentasi resmi. Halaman ini menandai bagian yang hanya berasal dari judul episode sebagai keyakinan rendah.
