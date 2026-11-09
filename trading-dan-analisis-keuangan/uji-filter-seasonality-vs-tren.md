# Uji Filter Seasonality (Musiman) vs Filter Tren — BTC Support Bounce

## Pendapat Awal
User mengusulkan filterbull/bear memakai indikator seasonality (kalender musiman).

## Data Seasonality BTC (Rata-rata return bulanan 2021-2026)
- Bulan terbaik: Mar (+0.42%), Oct (+0.37%), Feb (+0.33%), Jul (+0.28%)
- Bulan terburuk: Jun (-0.34%), May (-0.21%), Dec (-0.10%), Aug (-0.01%), Apr (-0.02%)

## Hasil Backtest A/B
### Dengan filter Seasonality
- Bulan baik: 27 trade | WinRate 33.3% | Net +0R
- Bulan buruk: 34 trade | WinRate 29.4% | Net -4R

### Dengan filter EMA50 (Regime Tren)
- Harga di atas EMA50 (trend naik): 16 trade | WinRate 18.8% | Net -7R
- Harga di bawah EMA50 (trend turun): 45 trade | WinRate 35.6% | Net +3R

## Kesimpulan
1. Seasonality di BTC 2021-2026 terlalu lemah (jarak antar bulan hanya 0.3-0.4%) untuk jadi filter bull/bear. Gain kecil tapi TIDAK konsisten statistik (cuma 6 observasi per bulan).
2. Filter Regime lebih informatif, tapi arahnya berlawanan intuisi: Support Bounce BTC malah lebih menguntungkan saat harga di bawah EMA50 (karena reversal-type trade lebih bekerja baik saat reversal area di bear range/lower zone).
3. Rekomendasi: pakai kombinasi dua lapis (layer) regime filter:
   - Lapis 1 (Direction/Rejim): SMA 200-week untuk tren besar.
   - Lapis 2 (Momentum): EMA 20-day untuk posisi saat trade.
   - Seasonality hanya sebagai penyeimbang kecil (kondisi tambahan boleh skip entry jika bad season), bukan utama.

---
Linked notes: [[index]] | [[hasil-backtest-5-tahun]] | [[analisis-drawdown-2026]]
