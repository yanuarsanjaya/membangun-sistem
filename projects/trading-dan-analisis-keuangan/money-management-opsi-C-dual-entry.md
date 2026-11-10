# Money Management Opsi C (Dual Entry: Breakout + Bounce)

## Struktur Modal Rp 100.000.000
- Risiko per trade: 1.5% (Rp 1.500.000)
- TP:SL = 2:1 → Profit per trade yang menang: Rp 3.000.000
- Maksimal 2 posisi terbuka bersamaan → risiko ekspose maks RI 3.000.000 (3%)

## Posisi Batch (satu aset boleh punya 2 entry aktif, tapi risiko GABUNG tidak boleh > 1.5%)
- Jika dua entry berada untuk satu aset yang sama, bagi risk di dua bagian: 0.75% + 0.75%, bukan 1.5% + 1.5%
- Prioritas entry: pertama yang dieksekusi menang kapasitas penuh 1.5%, entry kedua mundur ke 0.75% (half-cap) untuk jaga total risiko aset tidak lampaui 1.5% + sistem lain 1.5%

## Ukuran Dana per Posisi (formula umum)
- Risk 1.5% = Rp 1.5jt. Dana posisi = risk / jarak SL dalam desimal
- SL jarak 5%  -> dana posisi Rp 30.000.000
- SL jarak 3%  -> dana posisi Rp 50.000.000
- SL jarak 1.5%-> dana posisi Rp 100.000.000 (full ekspose, tidak dianjurkan untuk begitu banyak aset)

## Diversifikasi Ekspose (saat 4 aset aktif)
- BTC, ETH, XAUT (crypto) max total ekspose 40% modal (Rp 40jt)
- BBRI (saham) max ekspose 30% modal (Rp 30jt)
- Sisa 30% (Rp 30jt) tetap cash / reserve margin
- Kalau crypto sedang bearish broad yang semuanya sedang koreksi, tidak semua boleh terkumpal menumpuk risiko.

## Alur Prioritas Ketika 2 Sistemotp
- SETUP SISTEM BREAKOUT dan SETUP BOUNCE muncul pada aset yang sama & waktu sama -> pilih 1 (bounce terdekat / breakout yang terdekat dengan resistance tresh 1-3%).
- SEBELUM entry, pastikan SL_IDR pos & TP_IDR pos jelas, tidak merubah setelah order dipasang.
- Setiap hari Senin review (atau cron harian) posisi pasif -> catat yang menunggu, yang TP hit, yang SL hit.

Referensi sistem: [[sistem-final-layered-filter]] | [[uji-breakout-dan-hybrid]] | [[masterplan-modal-50juta]]
