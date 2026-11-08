---
title: "Claude Code"
type: entity
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - product
  - coding-agent
  - anthropic
  - frontier
sources:
  - model-comparison-2026-11
  - hermes-agent-9router
  - hermes-agent-kerja
  - openclaw-vps
  - jev-ai
confidence: high
---

# Claude Code

> Agen coding dari Anthropic yang dipakai sebagai pembanding kualitas dan tolok ukur biaya dalam korpus ini.

## Apa itu

Claude Code adalah agen coding berbasis terminal yang menjalankan model Claude (Opus, Sonnet, Fable) dengan akses ke file, shell, dan tool. Ia menjadi standar "mahal tetapi efektif" di beberapa sumber: cepat memberi iterasi, menjelaskan asumsi, dan mampu mengerjakan tugas coding multi-langkah.

## Peran dalam korpus

- [[model-comparison-2026-11|Perbandingan Terra/Argon/Fable]] memakai Claude Code dengan Fable 5.1 untuk tugas Blender; hasilnya paling detail tetapi paling mahal dan paling lama.
- [[hermes-agent-9router|Hermes Agent + 9Router]] membandingkan Claude Code dengan Hermes + 9Router gratis; Claude Code menyelesaikan invoice generator dalam 6 menit dan lebih mudah diiterasi.
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]] menyebut Claude Code sebagai standar kualitas yang ingin ditiru dengan biaya lebih rendah.
- [[jev-ai|JEV AI untuk Pemula]] memakai Claude Code untuk mengintegrasikan JEV dan membandingkan kecepatan sortir email.
- [[openclaw-vps|OpenClaw di VPS]] mencatat bahwa Claude hanya tersedia lewat API/CLI setelah OAuth ditutup, dan biayanya mahal.

## Kelebihan menurut sumber

- Iterasi cepat dan umpan balik jelas.
- Mampu menjelaskan asumsi dan langkah.
- Kualitas tinggi pada tugas visual dan coding kompleks.
- Ekosistem tool dan MCP yang matang.

## Keterbatasan

- Harga tinggi: $100–200/bulan untuk paket yang memadai.
- Kuota bisa habis pada pemakaian berat.
- Tidak selalu transparan tentang biaya per tugas.
- Ketergantungan pada satu penyedia.

## Koneksi

- [[model-tiers|Model Tiers]] — contoh kelas frontier.
- [[model-pilihan-2026|Model AI: Terra, Argon, Fable 5.1]] — perbandingan.
- [[opencode|OpenCode]] — alternatif yang lebih murah.
- [[ai-agent|AI Agent]] — kategori umum.
- [[hermes-vs-openclaw|Hermes Agent vs OpenClaw]] — konteks perbandingan agent.

## Pertanyaan terbuka

- Apakah kualitas Claude Code masih sepadan dengan harganya pada 2026, ketika model murah semakin baik?
- Berapa biaya per tugas nyata, bukan per bulan?
- Apakah pembatasan akses OAuth ke OpenClaw akan meluas ke tool lain?

## Sumber

- [[model-comparison-2026-11|GPT-6.1 Terra vs Gemini 4 Argon vs Claude Fable 5.1]]
- [[hermes-agent-9router|Hermes Agent + 9Router]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[openclaw-vps|OpenClaw di VPS]]
- [[jev-ai|JEV AI untuk Pemula]]
