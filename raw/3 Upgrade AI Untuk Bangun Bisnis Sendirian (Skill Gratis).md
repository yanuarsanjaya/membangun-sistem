---
title: "3 Upgrade AI Untuk Bangun Bisnis Sendirian (Skill Gratis)"
source: "https://www.youtube.com/watch?v=jPCUNBc1Uyw"
author:
  - "[[Last Minute Creator]]"
published: 2026-10-22
created: 2026-11-08
description: "Join newsletter gratis untuk download skill LMC Business Workflows: https://lastminutecreator.id/belajar-bisnisSistem Satu Orang: https://lastminutecreator.id/sso00:00 Prologue00:52 AI Model vs AI"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=jPCUNBc1Uyw)

Join newsletter gratis untuk download skill LMC Business Workflows: https://lastminutecreator.id/belajar-bisnis  
Sistem Satu Orang: https://lastminutecreator.id/sso  
  
00:00 Prologue  
00:52 AI Model vs AI Agent vs Agentic Workflow  
02:02 Upgrade #1: Harness  
04:39 Upgrade #2: Model Context Protocol  
05:32 Upgrade #3: Memory Graph  
06:04 Membangun Tim AI  
16:51 Epilogue  
  
Graphify: https://github.com/Graphify-Labs/graphify  
  
❤️‍🔥 Dukung Channel Ini Dengan Memberikan SUPER THANKS ❤️‍🔥  
  
🙏 KENALAN YUK 🙏  
Threads: https://www.threads.net/@lastminutecreator  
Instagram: https://www.instagram.com/lastminutecreator/  
TikTok: https://www.tiktok.com/@lastminutecreator  
  
Pastikan subscribe agar tidak ketinggalan video-video terbaru dari channel Last Minute Creator :)  
  
Stock videos, images & vectors used in this video are provided by:  
https://freepik.com  
https://flaticon.com  
https://vecteezy.com  
https://pexels.com  
https://pixabay.com  
  
\* Disclaimer: Video ini tidak di sponsori tapi link yang ada di deskripsi ini mungkin adalah affiliate link. Kalau diklik dan barangnya dibeli, saya akan mendapat komisi.

## Transcript

### Prologue

**0:00** · Kalau kita jalanin bisnis sendirian, ada dua hal yang enggak bisa ditambah, yaitu perhatian dan waktu. Konten harus jalan, produk harus dikembangkan, dan distribusi harus dibangun. Dan AI \[berdehem\] seharusnya bisa bantu di situ. Tapi seringnya, kita malah jadi manajer AI. Jelasin ulang konteks, baca hasilnya, revisi, terus jelasin lagi.

**0:19** · Pekerjaan hanya berpindah tempat, waktu, dan perhatian kita habis di situ.

**0:23** · Sementara produk dan marketing belum jalan. Nah, di video ini saya akan tunjukin tiga upgrade AI yang mengubah cara kerjanya. Di akhir video kalian akan bisa bangun tim AI kalian yang saling bekerja sama, yang tentunya bisa memberikan hasil nyata dan bisa dipakai lagi di hari-hari selanjutnya tanpa kalian harus lagi nulis prompt panjang.

**0:42** · Dari ketiga upgrade yang akan dijelasin, ada satu yang paling sering dilewatkan.

**0:45** · Padahal makin lama kita memakai AI, makin besar dampaknya pada biaya dan kualitas hasil. Mari kita mulai dari dasarnya dulu. Kita mulai dari tiga istilah yang sering tercampur. Yang pertama adalah AI model atau model LLM, yaitu otak yang menalar dan mengha- silkan jawaban. Kita kasih pertanyaan, dia kasih jawaban. Dalam chat \[berdehem\] biasa, urutan kerjanya masih kita yang pegang. Kita baca jawabannya, kita pertimbangkan, terus kita jalanin sendiri. Yang kedua adalah AI agent.

### AI Model vs AI Agent vs Agentic Workflow

**1:12** · Modelnya bisa sama, tapi agent bekerja di dalam aplikasi yang memberinya kemampuan untuk bertindak, misalnya membaca file, memakai tool, dan menjalankan beberapa langkah sampai tugasnya selesai. Jadi model yang menalar dan aplikasi agent yang menyediakan kemampuan untuk bertindak.

**1:27** · Yang ketiga adalah agentic workflow, yaitu sistem dan proses kerja yang kita rancang supaya agent, dan ini bisa beberapa agent juga, bisa mengerjakan tugas-tugasnya dengan baik. Jadi tim agent ini bisa diberi kewenangan untuk merancang, mengatur, dan mengevaluasi urutan langkahnya sendiri secara dinamis. Dan ini yang akan kita bangun.

**1:46** · Tujuan dan batas pekerjaannya tetap kita yang menentukan, termasuk kapan agent harus berhenti dan minta keputusan dari kita. Jadi tetap ada batasan. Nah, supaya proses itu berjalan dengan baik, ada tiga upgrade yang perlu kita siapkan. Dan kita akan mulai dengan upgrade yang pertama.

### Upgrade #1: Harness

**2:02** · Lapisan yang membungkus model yang memberinya bahan, tools, dan batas izin disebut agent harness. Nah, aplikasi harness ini udah banyak tersedia. Ini walaupun punya kelebihan dan kekurangan sendiri-sendiri dan ada perbedaan, tapi pada dasarnya prinsip kerjanya itu sama.

**2:17** · Dan kalian enggak harus jago coding untuk memulai. Aplikasi-aplikasi tersebut sudah punya kemampuan dasar tanpa koneksi tambahan. Tapi kemampuan sebesar ini tentu perlu batas. Di sinilah sandbox berperan. Aplikasi harness juga menyediakan sandbox, yaitu ruang kerja terbatas. Dan kita bisa mengatur apa saja yang boleh dibaca, ditulis, dan dijalankan oleh agent di dalamnya. Hal-hal di luar sandbox, misalnya file pribadi atau akun kita, atau aplikasi yang lain, itu enggak akan disentuh kecuali kita beri akses.

**2:44** · Tapi sekadar pernah menggunakan aplikasi seperti Cloud Code atau Codex, itu bukan berarti bisa melakukan harness engineering. Harness engineering adalah seni membangun sistem pendukung di sekitar aplikasi harness. Bukan hanya memberikan instruksi, konteks, dan tools, tapi agent harus punya sistem pengecekan otomatis. Jadi, kalau dia salah, bisa langsung ketahuan dan tahu kapan harus memperbaiki dirinya sendiri sebelum lapor kepada kalian. Pola dasarnya ada empat langkah: plan, execute, verify, dan improve.

**3:12** · Plan berarti menentukan hasil yang mau dicapai, materi atau bahan, langkah, dan batas pekerjaannya. Termasuk kapan agent harus meminta keputusan kita, alias human in the loop. Saat execute, agent menjalankan rencana dengan konteks dan tools yang tersedia. Lalu saat verify, hasilnya dibandingkan dengan kriteria-kriteria yang sudah ditentukan.

**3:33** · Misalnya dalam bikin materi promosi, reviewer akan periksa kesesuaian fakta dengan informasi produk, kecocokan pesan dengan audiens, dan dasar klaimnya.

**3:41** · Kalau ada yang belum sesuai, maka belum bisa dianggap selesai dan masuk ke improve. Ini executor akan perbaiki bagian yang salah, terus dikembalikan lagi ke reviewer untuk diperiksa lagi.

**3:51** · Dan di sini bisa terjadi yang namanya loop. Tapi ini iterasi nya harus dibatasi biar enggak habis token. Jadi biasanya dibatasi itu sampai dua atau tiga iterasi saja. Nah, baik planner, eksekutor maupun reviewer ini adalah sub agents yang dipanggil oleh agent utama.

**4:06** · Pengaturan urutan pembagian kerja ini disebut orkestrasi. Pertanyaannya, kenapa harus pakai sub agent? Penggunaan sub agent dilakukan untuk mencegah konteks road, yaitu saat konteks menjadi busuk. Konteks road itu penurunan akurasi, kualitas dan konsistensi output saat sesi sudah terlalu panjang atau konteks window sudah penuh. Kalau terus dipaksa, output nya tambah jelek sedangkan kuota token malah lebih cepat habis.

**4:31** · Kalau sampai di sini kalian masih merasa bingung, kalian jangan khawatir karena di bagian praktek nanti semuanya akan lebih jelas. Nah, pertanyaan selanjutnya, gimana kalau agent harus akses aplikasi atau data dari sumber luar? Misalnya kita perlu agent untuk membaca dan membahas email atau mengatur kalender konten kita di Notion atau mungkin membaca data analitik di akun medsos kita. Nah, salah satu cara menghubungkannya adalah melalui MCP atau model konteks protokol. Ini standar untuk menghubungkan agent dengan aplikasi dan sumber luar.

### Upgrade #2: Model Context Protocol

**5:00** · Kemampuan suatu MCP itu tergantung pada koneksi dan izin yang tersedia. Ada yang bisa hanya membaca data, ada yang bisa melakukan tindakan lain. Nah, sebagian dari MCP ada juga yang membutuhkan akun, paket berbayar atau kredit penggunaan.

**5:16** · Tapi banyak juga yang gratis ya, bahkan kita bisa bikin sendiri. Kalau kalian pernah nonton video saya yang tentang bisnis brand dan sudah ikutan membuat, ini nanti kita akan jadikan MCP. By the way, MCP itu enggak wajib untuk setiap workflow, kita hanya pakai kalau diperlukan saja.

**5:31** · Sekarang agent punya tempat kerja, bahan dan akses. Tapi data kita akan terus bertambah. Hasil riset, ide dan analisis bisa menumpuk dari minggu ke minggu.

### Upgrade #3: Memory Graph

**5:40** · Nah, apa yang terjadi kalau agent harus membaca semuanya tiap kali bekerja? Dan ini adalah upgrade yang tadi saya sebut paling sering dilewatkan.

**5:48** · Upgrade ketiga menyangkut ingatan. Agen itu tidak membawa ingatan dari satu sesi ke sesi berikutnya. Dan setiap kali mulai bekerja, dia perlu membaca ulang bahan-bahan yang relevan. Saat bahannya sedikit itu enggak kerasa ya, tapi saat materi riset dan hasil kerja kita terus bertambah, itu semakin banyak yang harus dibaca. Dan semakin besar penggunaan token yang mengakibatkan juga semakin sulit bagi agen untuk menemukan bagian yang benar-benar penting. Salah satu pendekatannya adalah memori graph. Bahan kita diubah menjadi peta hubungan yang saling terhubung.

### Membangun Tim AI

**6:19** · Nah, saat dibutuhkan, agen menelusuri hubungan yang relevan.

**6:23** · Jadi, dia enggak perlu membaca semuanya dari awal. Tapi ada beberapa batas yang perlu kalian ketahui. Untuk membangun memori graph itu tetap menggunakan model di awalnya. Jadi, tetap ada token dulu ya pas lagi pertama kali dibangun.

**6:35** · Selain itu juga model akan mengkonsumsi token saat datanya harus di-update. Nah, sekarang kita terapkan ketiga upgrade tersebut pada satu pekerjaan nyata, dari rencana sampai pemeriksaan dan pemakaian ulang. Untuk praktik di video ini, saya akan nunjukin cara membangun sebagian karyawan AI aja biar videonya enggak terlalu panjang. Nah, nanti di video selanjutnya saya juga akan jelasin cara bikin karyawan AI yang mampu melakukan video editing dan juga mesin grafik.

**7:01** · Jadi, AI-nya itu bisa ngedit di aplikasi video editing.

**7:04** · Workflow yang akan saya buat itu membutuhkan koneksi ke Business Brain yang tutorialnya pernah saya buat di masa lalu. Nah, karena workflow ini butuh MCP Business Brain, jadi hal pertama yang saya lakukan adalah menambahkan dulu fungsi MCP ke Obsidian agar data-data Business Brain bisa diakses oleh agen apapun project-nya, apapun aplikasinya. Di Obsidian ini saya masuk ke settings, lalu ke community plugins. Ini saya perlu exit dulu restricted mode.

**7:30** · Nah, sekarang kita bisa browse plugins yang dibuat oleh para pengguna Obsidian.

**7:35** · Saya ketik MCP di sini dan saya pilih MCP connector.

**7:40** · Ini tinggal klik install Lalu klik enable.

**7:44** · Oke, sekarang sudah ter-install dan harusnya di bawah ini ada menu baru.

**7:49** · Nah, untuk nyambungin MCP Obsidian ke aplikasi Harness yang mau kita pakai, ini tinggal klik aja salah satu di sini.

**7:56** · Di tutorial ini saya akan pakai Codex, jadi saya klik Codex di sini. Lalu pilih install into Codex user config.

**8:03** · Ini detail setting-an MCP-nya. Nah, di sini saya klik aja install. Oke, sudah beres gitu doang. Tapi kalau aplikasi Harness kalian enggak ada di sini, maka kalian harus baca dulu dokumentasi cara install MCP di aplikasi kalian. Alamat MCP-nya ada di bawah sini.

**8:18** · Terus jangan lupa, ini kalian scroll lagi ke atas dan copy token-nya.

**8:23** · Nah, ini adalah contoh konfigurasi MCP untuk aplikasi Open Code. Saya sekalian bikin juga untuk Open Code ya, karena saya sering pakai.

**8:30** · Di aplikasi ChatGPT, saya cek dulu setting-annya untuk mastiin MCP-nya sudah benar-benar terhubung.

**8:36** · By the way, setting-an ini berkaitan dengan sandbox yang saya jelasin tadi ya. Jadi, di sini full access-nya saya matikan. Ini kalau dinyalakan, CIAI akan terlalu bebas pakai komputer kita. Nah, untuk cek MCP di ChatGPT, kita masuk ke plugins.

**8:49** · Terus di atas sini pilih MCP.

**8:52** · Kita bisa lihat bahwa ChatGPT sudah tersambung ke MCP Business Brain di Obsidian.

**8:57** · Oke, sekarang saya akan set up project untuk tim konten saya. Untuk melakukan hal tersebut memang harus dalam project ya, jadi semua catatan dan memori akan tersimpan rapi.

**9:06** · Yang tadi kelupaan belum pindahin ini ke Codex. Sebenarnya Codex ini cocok untuk bikin aplikasi, tapi saya memang lebih suka pakai Codex dibanding ChatGPT Word.

**9:15** · Nah, kita lihat dulu file-file yang sudah saya tempatkan di folder project ini ya, jadi kalian tahu. Tadi itu saya buat dulu file agency.md.

**9:22** · Ini isinya cuma gini doang ya. Yang pertama adalah informasi tentang pembuatan dan eksekusi workflow harus menggunakan skill LMC Business Workflows. Jadi, ini skill yang saya buat dan kalian nanti bisa download skill-nya secara gratis. Terus di dalam folder docs ini isinya adalah konteks bisnis LMC. Ini deskripsi singkat aja sebetulnya ya.

**9:41** · Dan untuk skill LMC bisnis workflow ini saya tempatkan di sini.

**9:45** · Skill ini untuk bantu memudahkan aja dalam membuat struktur workflow yang lebih baik. Bukan berarti semuanya bisa berlangsung berjalan secara otomatis.

**9:53** · Oke, sebelum bikin workflow saya akan minta agent untuk memperjelas konteks tentang bisnis LMC serta channel YouTube LMC. Jadi saya minta dia untuk query ke MCP bisnis brand dan juga research ke channel saya. By the way di sini kita juga bisa ngatur permission, apakah harus selalu minta izin atau hanya minta izin saat ada hal yang dirasa kurang aman aja.

**10:14** · Saya coba jalankan sekalian ngetes koneksi ke MCP bisnis brand ya.

**10:18** · Ini prompt memang agak panjang, tapi ini hanya untuk awal-awal aja saat project baru dibangun.

**10:23** · Nah, udah selesai. Di sini kita bisa lihat agent banyak meng-query dokumen-dokumen LMC yang ada di bisnis brand. Jadi data-data LMC serta perkembangannya itu saya inject secara rutin ke bisnis brand.

**10:34** · Terus di sini si agent juga ada menghubungi MCP vidIQ. Ini sebetulnya saya enggak minta, tapi kebetulan di kodex ini saya pernah enable plugin vidIQ. Jadi si agent otomatis cari juga lewat MCP vidIQ.

**10:47** · Oke, sekarang konteks bisnis LMC di project ini udah lebih lengkap. Agent udah menambahkan beberapa dokumentasi hasil riset juga dan kalau saya buka agent.md katanya udah di-update juga oleh agent.

**10:59** · Sekarang saya akan minta agent untuk bikin workflow pekerjaan thumbnail video LMC karena ini adalah tugas repetitif yang sebetulnya saya agak malas untuk melakukannya.

**11:08** · Nah, saat bikin workflow baru prompt-nya itu memang agak panjang karena saya harus jelasin dulu alur pengerjaannya sama agent. Dan alur pengerjaan ini berdasarkan apa yang saya lakukan sehari-hari, bukan sekadar meniru orang lain. Jadi workflow yang bisa diotomatiskan itu adalah pekerjaan yang memang kita udah ngerti alurnya.

**11:25** · Nah, sekarang workflow-nya udah dibuat, udah beres ini. Di sini \[berdehem\] jadi si agent membuatkan SOP kerja yang detail tentang pengerjaan thumbnail untuk channel saya.

**11:33** · Novel agent sam dirinya juga sudah di-update ya. Ini sudah memiliki informasi tentang workflow thumbnail yang baru saja dibuat. Jadi yang nanti saat menjalankan workflow, saya cukup memberikan prompt seperti contoh yang diberikan agent ini. Jadi ini prompt pendek.

**11:46** · Nanti kita akan coba workflow-nya dan lihat hasilnya. Sekarang saya akan bikin dulu workflow kedua. Saya akan buat sesi baru biar enggak terjadi context road.

**11:55** · Workflow kedua ini adalah alur kerja ideasi konten untuk channel saya. Karena untuk bisa bikin thumbnail video, tentunya harus ada ide kontennya dulu.

**12:02** · Jadi di workflow ini, saya minta agent untuk memanggil workflow thumbnail tadi setelah ide konten ditetapkan. Saat menjalankan bisnis itu memang banyak tugas terpisah ya yang sebetulnya saling berkaitan. Dalam kata lain, output dari tugas A itu bisa menjadi input bagi tugas B.

**12:17** · Oke, sekarang pembuatan workflow ideasi konten sudah beres. Alur yang saya inginkan itu agent cari dulu 30 ide yang sesuai untuk channel AMC, lalu panggil sub agents untuk review dan menyaring menjadi tiga ide pemenang. Dari situ, sub agent harus menghasilkan brief untuk masing-masing ide. Ini termasuk konsep thumbnail serta variasi judul, lalu diserahkan kepada agent thumbnail designer.

**12:39** · Nah, sekarang kita akan coba jalankan workflow-nya di sesi baru. Untuk menjalankan workflow, tinggal ketik seperti ini saja karena SOP detailnya sudah dibuat dengan jelas. Untuk effort-nya saya akan set ke high.

**12:51** · Ini sebetulnya tergantung juga jenis pekerjaannya ya. Tapi karena ide konten itu harus bagus, saya ingin si agent untuk berpikir lebih keras. Dan karena sebenarnya ini ada dua workflow, proses pengerjaannya bisa berlangsung lama.

**13:02** · Selain itu juga bisa makan banyak token.

**13:05** · Nah, ini sudah beres. Pengerjaannya hampir sejam. Sekilas memang kelihatan lama banget, tapi sebetulnya enggak.

**13:12** · Karena ini sudah ada tiga ide konten, masing-masing dengan brief, plus total 30 variasi judul, dan sembilan variasi desain thumbnail. Nah, dan tadi saat dikerjakan saya rebahan dulu sambil nonton. Oke, sebelum kita menilai kualitas hasilnya, kita lihat dulu anggota tim alias sub agents. Ini kalau kita lihat di sini ada enam karyawan tim yang gotong royong mengerjakan. Setiap karyawan punya tugasnya masing-masing.

**13:35** · Dan ini adalah tiga ide yang menjadi kandidat untuk dibuat. Ini tentunya saya akan pertimbangkan dulu ya.

**13:40** · Masing-masingnya sudah dibuatkan tiga variasi thumbnail. Dan semua thumbnail yang dibuat desainnya konsisten, ada wajah saya serta sesuai dengan gaya LMC saat ini. Jadi yang namanya konteks itu memang penting supaya hasil kerja ya itu tidak sama dengan pekerjaan orang lain.

**13:56** · Dan coba saya lihat brief dari salah satu ide.

**13:59** · Ini cukup detail ya, bahkan dibuatkan juga draft outline untuk kontennya. Dan di bagian bawah ada 10 variasi judul, jadi nanti saya bisa pilih salah satu.

**14:08** · Secara kuantitas dan format hasil atau bentuk hasilnya, ini sudah sesuai dengan keinginan saya. Cuma secara kualitas menurut saya masih belum. Ya hampir menuju ke sanalah ya. Gaya penulisan judulnya sih sudah mirip, cuma masih kurang menarik dan agak kurang jelas ya.

**14:23** · Dan kalau kita perbesar salah satu thumbnail, ini menurut saya kualitas thumbnailnya masih harus diperbaiki.

**14:29** · Tapi untuk level konsepsi ini tetap acceptable ya. Dan kalau pakai skill yang saya buat untuk memperbaiki workflow itu bisa buka sesi baru.

**14:37** · Tentunya tadi ada beberapa hal yang harus diperbaiki ya. Tapi untuk tutorial ini, saya akan minta izin untuk tidak menggunakan plugin atau MC Fit IQ. Saya akan minta perbaiki ini saja. Ini karena Fit IQ itu makan kredit dan sebetulnya saya enggak pernah minta. Di sini kita memang masih harus jelasin ya, tapi minta perbaiki hal-hal yang masih kurang saja. Dan di tahap awal itu memang pasti kayak gini. Tapi nanti kalau hasilnya sudah benar-benar oke, kita enggak perlu jelasin lagi dan kita bisa otomatiskan.

**15:03** · Kalau di Kodeks atau ChatGPT, ini tinggal masuk ke menu schedule untuk mengotomatiskan.

**15:08** · Kita bisa kasih tahu kayak AI apa yang mau diotomatiskan, ini kapan harus berjalan, terus sama workflow-nya dan budgetnya kita kasih tahu saja. Nah nanti dia akan bikin schedule otomatisnya. Ini Ini bisa review lagi settingan schedule-nya ya.

**15:22** · Kita bisa edit lagi kalau perlu.

**15:24** · Semakin banyak konteks, semakin banyak workflow yang kita bikin, ini output-nya juga akan tambah banyak. Nah, di sinilah saatnya kita lakukan upgrade yang ketiga, yaitu pasang memori. Yang saya pakai saat ini adalah Graphify.

**15:38** · Ini untuk instal kalian bisa baca readme-nya. Untuk link repo-nya nanti saya akan pasang di bawah ya, di deskripsi. Nah, kalian juga bisa minta agen untuk menginstalkan Graphify. Saya enggak bisa nunjukin karena sudah instal di komputer saya sejak lama.

**15:51** · Nanti setelah kalian instal, masuk ke folder project workflow lewat terminal.

**15:55** · Ini tadi saya simpan di D ya.

**15:57** · Terus di sini ketik Graphify instal min-min platform Codex. Kalau pakai aplikasi lain, ganti Codex dengan nama aplikasi kalian. Nah, di readme Graphify juga ada daftarnya lengkap ya, ini tinggal kalian cek aja. Nah, dan setelah beres setup di project, saya akan masuk lagi ke Codex. Di sini saya akan pakai versi CLI aja ya, biar cepat. Setelah Codex-nya beres loading, ini kita ketik aja dolar Graphify, terus titik. Ini kalau di Codex ya. Tapi kalau di aplikasi lain seperti Cloud Code ataupun Code, ketik slash Graphify, terus titik.

**16:29** · Nah, kalau di Codex ini memang beda sendiri ya.

**16:32** · Untuk proses ingest ini sebetulnya hanya dilakukan pertama kali saja. Jadi, setelah ini beres kalian enggak usah lakukan lagi dan memori graph-nya itu akan bekerja secara otomatis. Nah, jadi kalau dokumen sudah nanti banyak, ini bisa menyelamatkan penggunaan token. Ya, walaupun \[berdehem\] enggak 100% tapi lumayan membantu.

### Epilogue

**16:51** · Satu hal yang perlu diingat, agen Teknoflow itu membantu eksekusi. Tapi supaya menghasilkan uang tetap perlu offer yang bernilai, jalur distribusi dan respon pasar. Produk yang sudah selesai dibuat pun masih harus diuji.

**17:03** · Ada enggak sih orang yang membutuhkan dan bersedia membayar? Nah, kalau kalian masih membangun fondasi bisnis digital dari skill, offer, audiens sampai distribusi, kalian bisa pelajari sistem satu orang. Ini terdiri dari panduan lengkap sebanyak 200 halaman lebih, terus juga ada prombook dan juga ada Sasa Workspace yaitu konten kalender berbasis notion. Anda jangan lupa juga kalau kalian belum pernah bikin bisnis brand, kalian bisa lanjutin nonton video yang ini.