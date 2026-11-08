---
title: "9Router"
type: entity
status: developing
created: 2026-11-08
updated: 2026-11-08
tags:
  - product
  - router
  - proxy
  - open-source
sources:
  - hermes-agent-9router
  - hermes-agent-kerja
  - openclaw-vps
confidence: high
---

# 9Router

> Proxy lokal open source (MIT) yang menyebar permintaan AI ke banyak penyedia dan menyediakan semua model — termasuk tier gratis — melalui satu endpoint.

## Apa itu

9Router adalah tool CLI/web yang berjalan di mesin pengguna (biasanya VPS) dan bertindak sebagai gateway model. Ia menghubungkan langganan (Claude Code, Codex, Gemini, Copilot) atau API key penyedia lain, lalu mengekspos satu API yang bisa dipakai agent. Ia tidak menagih pengguna; biaya tetap berasal dari penyedia model.

## Tiga tier

| Tier | Isi | Cocok untuk |
|---|---|---|
| 1 | Langganan: Claude Code, Codex, Gemini, Copilot | Kualitas tinggi, limit jelas |
| 2 | Model murah berbayar: GLM, MiniMax, Kimi, Qwen | Kerja profesional hemat |
| 3 | Gratis: iFlow, Qwen free, Kiro, OpenCode Unlimited | Belajar dan eksperimen |

## Fitur

- Web UI di port lokal.
- Penyedia dan API key yang bisa ditambah.
- **Combo** dengan strategi fallback, round-robin, atau fusion.
- Usage dan analytics.
- Token saver.
- Berjalan sebagai background service atau di dalam tmux/Termux.

## Catatan keamanan

- Password default `123456` harus segera diganti.
- Dashboard sebaiknya diakses lewat Tailscale, bukan IP publik.
- API key perlu dibatasi dan dirotasi.

## Peran dalam korpus

- [[hermes-agent-9router|Hermes Agent + 9Router]] memasangnya di VPS dan menghubungkannya ke Hermes.
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]] memakai OpenCode Go sebagai penyedia tier 2.
- [[openclaw-vps|OpenClaw di VPS]] memakai OpenCode Go untuk GLM 5.3, tetapi tidak lewat 9Router.

## Koneksi

- [[model-routing|Model Routing]] — konsep yang diimplementasikan.
- [[hermes-agent|Hermes Agent]] — agent yang terhubung.
- [[self-hosting-agents|Self-Hosting Agents]] — tempat ia berjalan.
- [[opencode|OpenCode]] — penyedia model yang sering dipakai.

## Pertanyaan terbuka

- Apakah tier gratis masih tersedia dan berkelanjutan?
- Bagaimana kualitas dan keamanan kode? Proyek open source perlu audit.
- Apakah round-robin dan fusion benar-benar berguna, atau hanya menambah kompleksitas?

## Sumber

- [[hermes-agent-9router|Hermes Agent + 9Router]]
- [[hermes-agent-kerja|Hermes Agent untuk Kerja Nyata]]
- [[openclaw-vps|OpenClaw di VPS]]
