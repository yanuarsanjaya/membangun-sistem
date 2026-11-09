# Sistem Final: L-Slayer Filter (Regime + Bounce + Musiman)

## Hasil Uji A/B dan Konfigurasi Final (Backtest 2021-2026)

| Aset | Regime Filter | Layer Musiman | Trade | Win Rate | Net |
|---|---|---|---|---|---|
| BTC | Dipilih saat harga DI BAWAH SMA200 (beli dip koreksi) | Skip Mei & Juni | 29 | 41.4% | +7R |
| XAUT | Dipilih saat harga DI BAWAH EMA50 | Skip Mei & Juni | 31 | 41.9% | +8R |
| BBRI | Dipilih saat harga DI ATAS SMA200 (macro uptrend) | Tanpa filter musiman | 18 | 50.0% | +9R |

**ETH: DIKELUARKAN dari swing trading** — sistem support bounce lemah di semua variasi filter (WR 21-33%, Net --4R s/d --12R). ETH hanya dipegang sebagai investasi pasif, bukan trade swing aktif.

## Ringkasan Portofolio (Tanpa ETH)
- Total: 78 trade | **Win Rate 43.6%** | **Net +24R**
- Tidak ada tahun minus: semua tahun PROFIT (2026 justru +3R, tidak lagi BEP/minus)

## Performa Tahunan (Net, dalam R)
- 2021: +2R | 2022: +2R | 2023: +4R | 2024: +7R | 2025: +6R | 2026: +3R

## Proyeksi Nominal (Risiko 1.5% per trade)
- Modal Rp 100jt: +Rp 36 juta kumulatif 6 tahun (rata-rata Rp 6 juta/tahun, ~Rp 500rb/bulan)
- Modal Rp 50jt: +Rp 18 juta
- Modal Rp 10jt: +Rp 3.6 juta

## Alasan Layer Saat Ini
- Lapis 1 (Regime): SMA200/EMA50 menentukan REJIM pasar (dipilih per aset karena karakter berbeda).
- Lapis 2 (Eksekusi): Support Bounce dengan TP:SL 2:1.
- Lapis 3 (Musiman): Skip Mei-Juni (only BTC & XAUT) karena lemah secara statistik -> hanya pemanis kecil.
- BTC & XAUT justru lebih menghasilkan di bawah tren (reversal bounce), BBRI justru lebih baik di atas SMA200.

## Catatan Kejujuran (Overfitting Risk)
- Filter per-asset dipilih dari data yang sama (in-sample optimization) -> potensi overfitting. Konfirmasi validitas: perhatikan live performance 3-6 bulan.
- Win rate naik dari ~35% (sistem lama) ke 43.6% = kenaikan signifikan, tapi eksekusi real trading bisa berbeda dari data.

---
Linked notes: [[index]] | [[uji-filter-seasonality-vs-tren]] | [[hasil-backtest-5-tahun]] | [[analisis-drawdown-2026]]
