---
title: "OpenClaw"
type: entity
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - product
  - personal-agent
  - openai
  - memory
sources:
  - openclaw-vps
  - hermes-agent-kerja
confidence: medium
---

# OpenClaw

> Personal AI agent yang dirilis November 2025 oleh Peter Steinberger, popular di kalangan early adopter karena memori, persona, dan arsip konteks yang bisa dijalankan 24/7.

## Apa itu

OpenClaw adalah agent pribadi yang berjalan di VPS atau komputer lokal, terhubung ke Telegram/WhatsApp atau dashboard, dan menyimpan konteks dalam file workspace. Menurut [[openclaw-vps|OpenClaw di VPS]], ia dirilis 24 November 2025 dan kemudian diakuisisi OpenAI; pengelolaannya disebut berada di bawah foundation independen, dengan OpenAI sebagai pendukung utama.

## Yang membuatnya menonjol

- **Workspace yang bisa dibaca manusia.** `user.md`, `memory.md`, `soul.md`, `agents.md`, `identity.md`, `dreams.md`.
- **Konteks personal.** Arsip konten dan data bisnis bisa dijadikan referensi.
- **Multi-agent.** Mode "small team" dengan koordinator, researcher, reviewer, dan writer.
- **Dashboard.** Chat, sesi, model, kanal, skill, plugin, MCP.
- **Migrasi.** Workspace lama bisa dipindahkan dengan SCP dan diimpor.

## Sejarah dan batasan

- Dirilis 24 November 2025 oleh Peter Steinberger.
- Anthropic menutup akses OAuth Claude; Claude hanya tersedia lewat API/Claude CLI yang mahal.
- Diakuisisi OpenAI; sumber menyebut model tetap terbuka untuk penyedia lain, tetapi pengalaman pengguna condong ke OpenAI.
- [[openclaw-vps|OpenClaw di VPS]] melaporkan error autentikasi pada sub-agent dan konfigurasi multi-model yang tidak konsisten.

## Koneksi

- [[ai-agent|AI Agent]] — kategori umum.
- [[hermes-agent|Hermes Agent]] — pesaing dan alternatif yang lebih fleksibel.
- [[hermes-vs-openclaw|Hermes Agent vs OpenClaw]] — perbandingan.
- [[agent-memory|Agent Memory]] — struktur memori workspace.
- [[self-hosting-agents|Self-Hosting Agents]] — pola deployment.

## Pertanyaan terbuka

- Status kepemilikan dan tata kelola setelah akuisisi perlu diverifikasi ke sumber primer.
- Apakah keterbatasan model non-OpenAI adalah bug yang akan diperbaiki atau keputusan desain?
- Apakah proyek masih aktif dikembangkan setelah akuisisi?

## Sumber

- [[openclaw-vps|OpenClaw di VPS (2026)]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
