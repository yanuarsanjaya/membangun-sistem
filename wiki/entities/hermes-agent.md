---
title: "Hermes Agent"
type: entity
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - product
  - agent-framework
  - nous-research
  - open-source
sources:
  - hermes-agent-9router
  - hermes-agent-kerja
  - jev-ai
confidence: high
---

# Hermes Agent

> Framework AI agent open source (MIT) dari Nous Research yang menekankan memori persisten, skill yang bisa tumbuh dari pengalaman, dan fleksibilitas model.

## Apa itu

Hermes Agent adalah framework agent yang dirilis Februari 2026 oleh Nous Research. Ia berjalan di Linux (VPS atau mesin lokal), terhubung ke Telegram/WhatsApp atau dashboard, dan mendukung berbagai penyedia model melalui API langsung atau router seperti [[9router|9Router]].

## Kemampuan yang disorot

- **Memori persisten.** Mengingat pengguna, pekerjaan, dan konteks antar-sesi.
- **Skill dari pengalaman.** Klaim bisa mengubah histori kerja menjadi prosedur yang bisa dipakai lagi.
- **Fleksibilitas model.** Bisa memakai model gratis, model China murah, atau model frontier.
- **Kanal pesan.** Telegram, WhatsApp, CLI, dan dashboard.
- **Tool dan MCP.** Browser, shell, file, cron, plugin, dan integrasi eksternal.
- **Dashboard.** Sesi, model, log, skill, plugin, MCP, dan konfigurasi.

## Peran dalam korpus

- [[hermes-agent-9router|Hermes Agent + 9Router]] menguji versi gratis dan menyimpulkan bahwa tier gratis cocok untuk belajar, tetapi lambat untuk kerja.
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]] memakai OpenCode Go + GLM 5.3, memasang Tailscale, dan menguji presentasi, script, serta website.
- [[jev-ai|JEV AI untuk Pemula]] mengintegrasikan JEV sebagai skill untuk keputusan massal.

## Perbandingan dengan OpenClaw

| Aspek | Hermes Agent | OpenClaw |
|---|---|---|
| Lisensi | MIT | Open source (detail perlu verifikasi) |
| Rilis | Februari 2026 | November 2025 |
| Fleksibilitas model | Tinggi | Condong ke OpenAI |
| Setup multi-model | Lebih mudah menurut sumber | Lebih ribet |
| Memori | Persisten | File workspace |
| Kanal | Telegram, WhatsApp, dashboard | Telegram, WhatsApp, dashboard |

## Kutipan

> "Herme Agent ini adalah framework AI Agent open source. License-nya dari MIT, buatan Nous Research." — [[hermes-agent-9router|Hermes Agent + 9Router]], 7:46

## Koneksi

- [[ai-agent|AI Agent]] — kategori umum.
- [[openclaw|OpenClaw]] — pesaing utama.
- [[9router|9Router]] — router yang sering dipasangkan.
- [[self-hosting-agents|Self-Hosting Agents]] — cara menjalankannya.
- [[agent-skills|Agent Skills]] — mekanisme skill.
- [[agent-memory|Agent Memory]] — memori persisten.

## Pertanyaan terbuka

- Apakah klaim "membuat skill dari pengalaman" terbukti, atau masih eksperimental?
- Bagaimana kualitas dan keamanan plugin pihak ketiga?
- Apakah proyek ini memiliki tata kelola dan rilis yang stabil?

## Sumber

- [[hermes-agent-9router|Hermes Agent + 9Router]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[jev-ai|JEV AI untuk Pemula]]
