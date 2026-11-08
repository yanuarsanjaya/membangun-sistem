---
title: "TUTORIAL PASANG OPENCLAW DI KOMPUTER KALIAN SENDIRI"
source: "https://www.youtube.com/watch?v=obQSPdSUkqI&list=PLSY7f7O2V4qw&index=6"
author:
  - "[[David Alfa Sunarna]]"
published: 2026-10-09
created: 2026-11-08
description: "VPS 🖥️Promo Code: DAVIDCLAWLink: https://hostinger.com/davidclawManaged Setup 🧑‍💻Promo Code: DAVIDMANAGEDLink: https://hostinger.com/davidmanagedKonfigurasi OpenClaw Gue:https://drive.goog"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=obQSPdSUkqI)

VPS 🖥️  
Promo Code: DAVIDCLAW  
Link: https://hostinger.com/davidclaw  
  
Managed Setup 🧑‍💻  
Promo Code: DAVIDMANAGED  
Link: https://hostinger.com/davidmanaged  
  
Konfigurasi OpenClaw Gue:  
https://drive.google.com/file/d/1CfDgKyq93NnQJx3ftMM0mjGFnujbH67Q/view?usp=sharing  
  
OpenClaw salah satu tool yang bantu gua naikin penghasilan gila-gilaan di tahun 2026. Script konten gua terbantu, kerjaan coding dan urusan client di Web Ekspor juga lebih cepat. Setelah pilihan AI agent makin banyak, OpenClaw masih relevan gak di akhir 2026?  
  
Di video ini gua ajak lu install OpenClaw di VPS Hostinger, hubungkan akun ChatGPT, install tailscale, pilih model yang lebih murah, lalu pakai setting lama dan arsip konten gua sebagai konteks kerja. Kita coba buat script konten dan prototipe aplikasi review revisi website buat kebutuhan Web Ekspor.  
  
Tutorial ini memakai VPS supaya gua punya kendali server dan bisa menjalankan aplikasi tambahan. Update, keamanan, dan maintenance VPS tetap tanggung jawab kita. Biaya server dan akses model AI juga perlu diperhitungkan masing-masing.  
  
Jangan lupa, AI agent tetap perlu arahan dan pemeriksaan hasil. Mulai dari satu pekerjaan, kasih konteks yang jelas, lalu evaluasi dan koreksi supaya pekerjaan berikutnya makin sesuai.  
  
#OpenClaw #Hostinger #AIAgent #VPS #ChatGPT  
\---  
Bikin Website Di Web Ekspor Aja!  
Bikin website paling murah: https://www.webekspor.com  
Admin Web Ekspor: https://wa.me/6281280080275  
\---  
Instagram David Alfa Sunarna: https://www.instagram.com/davidalfasunarna  
Tiktok David Alfa Sunarna: https://www.tiktok.com/@davidalfasunarna  
X David Alfa Sunarna: https://x.com/davidsunarna  
Kerjasama (Manager): https://wa.me/6285121007256  
\---  
Timeline  
00:00 Intro  
03:49 VPS & Managed Setup Hostinger  
07:45 Instalasi OpenClaw  
16:29 Setup Tailscale  
21:32 Memilih Model LLM Bansos  
25:42 Setup Channel Telegram  
28:18 Setup Lama OpenClaw Gua  
42:55 Testing: Bikin Script Konten  
50:23 Testing: Bikin Website  
57:18 Verdict

## Transcript

### Intro

**0:00** · Open Cloud adalah salah satu tools yang buat gua jadi kaya raya di era AI ini.

**0:04** · Mungkin kalian enggak percaya, enggak masalah. Tapi dari segi kapital pribadi gua lumayan naik tahun ini dan start-nya adalah ketika Open Cloud itu muncul sebagai agentic AI yang enggak cuman gimik. Ketika Open Cloud dirilis 24 November 2025 sama Peter Steinberger, gua adalah salah satu heavy user-nya Open Cloud. Karena gua sangat-sangat amaze sama kemampuan dia. Ini sebelum pilihan AI agent tools semakin banyak ya, macam Herme dan lain-lain.

**0:29** · Penggunaan utamanya di mana Bang? Kenapa lu klaim bisa jadi kaya raya? Gua benar-benar bisa mengefisienkan kerjaan gua yang tadinya makan waktu, makan resource orang banyak, cukup dengan Open Cloud selesai. Nanti di video ini bakal gua jelasin juga gimana skrip-skrip konten gua yang viral itu sebenarnya dibuat sama AI. Tapi ada \[musik\] caranya. Gua koleksi data konten gua dulu selama bertahun-tahun yang viral gua filter, gua jadiin skrip, gua lempar ke Open Cloud. Gua manfaatin fitur memori dia. Dulu cuman Open Cloud yang bisa begitu.

**0:55** · Jadi dia bisa tahu persona gua kayak apa, konten gua yang naik kayak apa hook-nya, tengahnya kayak apa, ending-nya kayak apa, CTA harus ke mana.

**1:04** · Dan itu menyebabkan banyak banget endorse. Ketika gua ngerjain endorse, kliennya happy karena skripnya juga cepat. Kemudian penggunaan yang lain di bidang coding. Lu bayangin ya, gua manage bare metal server 64 core, RAM-nya gede banget. Gua lupa kayaknya 512 ya bare metal gua. Cuman modal Open Cloud doang dan itu bisa muat ribuan website di sana. Dan gua bisa fokus ke klien-klien besar tanpa harus punya tim yang besar karena semua karyawan gua gua bekalin AI. Zaman dulu Open Cloud, gua sendiri pakai Open Cloud. Jadi gua dulu selalu pakai Open Cloud.

**1:31** · Ketika dulu Open Cloud masih rilis sampai akhirnya Anthropic ngeluarin pengumuman kalau dia nge-cut OA out ke Open Cloud. Enggak boleh pakai Claude lagi. Di situ gua stop pakai Open Cloud. Sekarang pertanyaan gua, di kuartal terakhir 2026, Open Cloud ini masih relevan apa enggak? Ketika tools yang lain makin banyak dan makin hype dan makin viral.

**1:50** · Nah, gua mau jawab di video ini teman-teman. Gua mau ngasih tutorial kalian gimana caranya instal Open Cloud dan masukin konfigurasi gua dulu ke Open Cloud yang baru nantinya. Penasaran kan?

**1:59** · Karena konfigurasi gua masih ada tuh di Mac Mini gua. Gimana kalau kita ngerjain pekerjaan berulang yang pakai file?

**2:04** · Gimana kita kasih konteks pekerjaan ke dia? Apa aja tools yang ada di Open Cloud sekarang? Jujur gua dulu cabut dari Open Cloud karena enggak ada Claude lagi. Tapi sekarang gua lihat Open Cloud dibeli sama Open AI. Jadi ada koneksi khusus antara GPT model dan Open Cloud.

**2:17** · Sementara GPT 6 Astra atau GPT 6.1 Soul itu bagus banget kemarin di video gua review. Dan Open Cloud ini adalah salah satu project yang ikut mempopulerkan personal AI agent. Walaupun dibeli Open AI, dia dikelola oleh foundation yang independen. Open AI hanya salah satu pendukung besar dan pilihan model tetap terbuka untuk provider lain, teman-teman. Dan tadi gua cerita ya, akses ke Anthropic tuh jalur OAuth-nya ditutup. Tapi Claude ini masih tersedia via API dan itu mahal ya, teman-teman ya. Harus not dulu. Jadi hanya integrasi Claude CLI sekarang yang didukung.

**2:47** · Secara jalur akses beda, biayanya beda.

**2:49** · Kita enggak bakal pakai itu kayaknya.

**2:50** · Terlalu tidak napak tanah. Jadi kita mau lihat pembaruan-pembaruan yang relevan di Open Cloud sekarang, terus browser Open Cloud 2.0 tuh kayak apa, pilihan runtime coding agent-nya kayak apa, dan kita mau cobain pakai ChatGPT karena supporter utamanya. Dan seperti biasa, teman-teman, gua bakal install Open Cloud gua di atas VPS. Kalian yang punya Mac Mini, punya mini PC, boleh silakan install di situ juga. Tapi di video ini gua mau sasar untuk pemula, teman-teman yang mau coba-coba bisa install di VPS harga ratusan ribu doang per bulan. Jadi investasinya enggak harus terlalu banyak.

**3:20** · Kemudian kalian bisa hubungkan juga dengan ChatGPT account plus juga enggak apa-apa awal-awal sekitar 20 dolar. Dan kita juga mau coba lihat opsi model China, mungkin ada yang lebih murah. Dan kita mau atur prioritas modelnya juga nanti. Setelah itu gua bakal masukin konfigurasi gua yang lama dari Mac Mini gua, kemudian kita install di VPS. Apakah Open Cloud-nya gacor?

**3:40** · Coba kita lihat di video ini ya. Semoga bisa membantu kalian karena gua sendiri bersaksi terbantu banget dulu sama Open Cloud. Let's go!

### VPS & Managed Setup Hostinger

**3:50** · Teman-temanku yang budiman, untuk VPS-nya gua pakai Hostinger di sini.

**3:53** · Kita ganti dulu bahasa Indonesia seperti biasa. Gua mau jelasin kalian, Open Cloud kalau di Hostinger ada manage setup-nya juga. Kalian buka produk, langsung ada Open Cloud. Tapi, gua mau contohin di sini kita pakai VPS. Nah, bedanya apa? VPS di-install Open Cloud sama manage setup. Yang pertama, masalah kendali server-nya. Kalau VPS, kita full root access. Kita mengendalikan server.

**4:19** · Dari video kemarin gua udah ajarin berkali-kali cara SSH, cara ngatur server. Udah aman dan ngerti harusnya.

**4:25** · Tapi, kalau pakai manage setup yang Open Cloud, ini enggak ada root.

**4:29** · Infrastructure dikelola sama Hostinger.

**4:31** · Kemudian dari segi cara mulai. Kalau VPS, ya kita install sendiri. Bisa pakai Docker, bisa pakai script dari documentation-nya Open Cloud, macam-macam. Kalau manage setup Open Cloud-nya Hostinger, onboarding-nya otomatis untuk Open Cloud. Kita tinggal pilih provider AI, terus mau channel WhatsApp atau Telegram. Simpel banget.

**4:49** · Kemudian masalah update dan keamanan, teman-teman. Kita bertanggung jawab atas keamanan kita sendiri kalau VPS. Of course, itu kan server kita sendiri.

**4:56** · Sementara kalau manage setup Open Cloud, ya patch keamanan dan update ditangani otomatis oleh Hostinger. Kemudian kalau mau coba-coba AI agent lain atau mau nginstall software lain, ya pakai VPS.

**5:06** · Kalian bisa punya Open Cloud di situ, bisa punya Herme agent, bisa punya AI agent yang lainnya. Ya kan, bebas server sendiri. Tapi, kalau manage setup, misalkan kalian pilih manage setup Open Cloud, ya kalian cuma dapat Open Cloud di situ. Mengikuti aplikasi dan konfigurasi yang disediakan layanan Open Cloud sendiri. VPS ini cocok untuk siapa? Jelas, developer dan pengguna teknis yang perlu fleksibilitas. Tapi, gua mau ajarin kalian juga cara pakai VPS. Jadi, gua mau juga orang-orang non teknis harusnya bisa manage VPS Ubuntu atau Linux kalian sendiri. Karena itu cuma beda operating system. Kita biasa pakai Mac OS, kita biasa pakai Windows.

**5:39** · Masa kita enggak biasa pakai Linux?

**5:41** · Harus dong. Tapi, kalau kalian masih bingung, kalian bisa pakai manage setup-nya Hostinger, enggak masalah juga. Ini untuk pengguna non teknis yang ingin fokus mengatur asisten AI-nya aja.

**5:51** · Kalau kita buka page yang hostinger.com/id/aiautomationapps, ada apa aja aplikasinya? Ada Herme Agent, ada Open Claw, ada N8N, ada Paper Clip. Cara kerja manage setup ini dia memakai container docker yang terisolasi yang infrastrukturnya diurus hostinger.

**6:06** · Kemudian hostinger juga punya model AI sendiri dan nexos.ai tersedia sebagai pilihan akses model. Nexos.ai ini LLM punyanya hostinger. Tapi sisanya yang sama aja misalkan Open Claw kalian juga bisa login pakai chat GPT. Ya lagi-lagi gua tekankan ya keunggulannya zero setup ya berarti kita tidak perlu memasang dan merawat server sendiri. Tapi provider model serta channel yang dipakai tetap perlu dikonfigurasi. Pilihan channel mengikuti masing-masing aplikasi juga.

**6:30** · Gua ulang lagi tutorial ini memakai VPS.

**6:33** · Kita mau mengadaptasi setting lama gua.

**6:35** · Jadi untuk fleksibilitas gua harus pakai VPS. Dan gua ingin menjalankan aplikasi hasil coding di server yang sama. Gua enggak mau akses server lain kalau kita pakai manage setup. Dan gua mau kalian ngerti cara nginstal Open Claw sendiri di atas Linux tuh gimana. Nanti kalau kalian punya Mac OS, punya MacBook caranya sama juga. Itu alasan memilih VPS untuk demo ini. Jadi bagi teman-teman yang ingin langsung mengatur asisten tanpa mengurus server ya manage setup bisa lebih cocok untuk kalian ya.

**7:00** · Tapi kalau kalian mau upgrade diri, kalian pakai VPS. Oke.

**7:04** · Coba kita lihat produk VPS-nya.

**7:06** · Hosting, VPS hosting.

**7:09** · Teman-temanku yang budiman, untuk Open Claw 1 CPU core 4 GB RAM menurut gua cukup pakai Herme Agent terus dipasang Nine Router. Kalau untuk kebutuhan sederhana ini aja cukup teman-teman.

**7:19** · Tapi gua pakai ini ya. Yang paling murah harganya berapa sih? Coba langganan 1 bulan. Harganya 193.900, 200 ribuan ya teman-teman. Nanti kalian bisa pakai kode kupon ini biar ada diskon lebih. Tapi gua ulangi lagi, gua di sini memakai KVM 2 dengan 2 CPU core dan 8 giga RAM ya teman-teman ya. Cara belinya gimana di hostinger, cara setup-nya gimana, udah gua jelasin di video gua yang sebelumnya ini teman-teman. Kalian bisa lihat.

### Instalasi OpenClaw

**7:46** · Sekarang kita masuk di chapter bagaimana cara menginstal Open Cloud di VPS kita.

**7:50** · Kalau kalian udah beli VPS dan login ke Hostinger, kalian akan lihat panel VPS kalian. Lokasinya ada di sebelah kiri tulisan VPS. Seperti yang gua jelaskan di video gua kemarin, kalian enggak usah ribet-ribet SSH via terminal, bisa langsung via browser kalau pakai Hostinger. Buka aja konsol web-nya. Dia muter-muter, terus bam! Terbukalah SSH terminalnya di browser, tidak usah ribet. Oh ya, buat teman-teman yang enggak mau pusing juga cari apa aja yang dijual di Hostinger, kalian bisa lihat lewat panelnya juga. Misalkan tadi yang gua bilang, apa aja sih manage setup yang dijual?

**8:21** · Langsung ada di taskbar-nya. Kita bisa lihat ada Open Cloud, Herme, N8M, dan Paperclip. Kalau mau pakai manage setup, simpel. Kita balik lagi ke VPS server kita. Bagaimana cara menginstal Open Cloud? Seperti yang gua jelaskan di video-video sebelumnya dan selalu gua edukasi ke kalian, buka aja website-nya. Ini adalah website-nya.

**8:40** · Kita scroll aja ke bawah. Wow, sekarang ada desktop apps-nya, Open Cloud, luar biasa. Tapi kita enggak mau pakai itu.

**8:48** · Nanti kapan-kapan bisa kita coba ya, instal di macOS, di Windows, atau di Linux. Kita mau instal di VPS dulu. Ke mana? Ya ke one liner biasanya. Pakai NPM juga bisa, pakai hackable juga bisa.

**8:58** · Kita pakai one liner aja yang simpel ya.

**9:00** · Pilih macOS dan Linux. Di Windows juga bisa sebenarnya. Bukan rasis ya sama OS ya, karena kita memang pakai VPS dan VPS itu pakai Ubuntu server. Kerjaan enggak susah, tinggal copy nih, button copy.

**9:14** · Kita paste di sini.

**9:16** · Bap.

**9:18** · Udah deh kita instal.

**9:20** · Enter.

**9:21** · Damn.

**9:22** · \[berteriak\] Langsung diinstal. Kita tunggu sampai selesai ya teman-teman. Ketika nginstal kayak gini, saatnya kalian apa? Saatnya kalian pamer ke masyarakat sekitar. Cari restoran yang rame, coffee shop yang rame, pamerin lagi nginstal. Biar semua orang tahu kalau kalian buka laptop itu, kalian mainnya VPS di atasnya ada Linux, Ubuntu server, enggak pakai GUI kalian, enggak pakai interface UI/UX apa itu, hitam putih. Tunjukkan pada dunia sejago itu kalian.

**9:48** · Instalasinya sudah selesai, kita bisa lihat ada logo Open Claw dengan tulisan Open Claw yang besar, wus keren banget. Hai, I'm Open Claw, I kept this system running, let's get you set up. Oke, ada dua pilihan teman-teman.

**10:02** · How would you like to start? Yang pertama quick start, yang kedua custom setup. Gua adalah tipe orang yang kalau ada sesuatu yang simpel, enggak usah dibuat over complicated. Kalian pilih quick start aja, improve-nya day by day, config by config. Enggak harus di awal kalian punya kayak banyak orang-orang pamer tuh, AI agent gua punya AI agent, terus divirtualkan jadi dua lantai, dia kerja di lantai satu, lantai dua.

**10:25** · Ceritanya bisa kayak pada ngobrol masing-masing. Buat apa? Apakah bisa membantu kalian? Apakah dengan punya itu kalian bisa beli Harley baru? Kalian bisa beli Rolex baru? Enggak. Kerjakan sesuatu yang spesifik dengan AI yang bisa ngasilin uang buat kalian, real dengan pekerjaan kalian yang sekarang.

**10:41** · Jadi jangan over complicated thing. Kita pilih quick start aja, malah jadi ceramah gua. How would you like to create? Yang pertama ada one agent, yang kedua ada a small team, a chief of staff plus specialist. Oke, di sini gua mau nyobain fitur Open Claw yang baru.

**10:55** · Karena gua adalah seorang content creator dan juga seorang programmer dan pemilik perusahaan teknologi, gua butuh beberapa agent. Yang pertama ngurusin konten, fokus, yang kedua ngurusin pekerjaan kayak coding dan lain-lain.

**11:08** · Jadi kita set ya rules-nya ya. Jadi ada agent untuk ngurusin konten, ada agent untuk coding ya teman-teman ya. Oke?

**11:14** · Oke, kita pilih a small team, nyobain fitur Open Claw yang baru. Sekarang kita pilih model or out provider. Tadi gua udah bilang gua mau nyobain pakai Open AI atau ChatGPT. Jadi gua mau pakai sign in with ChatGPT karena gua udah ada aplikasi ChatGPT ini lihat teman-teman.

**11:28** · Gua cobain Open AI ya, enter. Codex login, device code, codex login browser, sign in with chat GPT, tapi masih beta, ya. Mmm, gua pakai browser aja, ya, teman-teman, ya. Codex login browser, ya. Gua takut beta tuh masih ada bug.

**11:43** · Coba codex login browser. Oke, ini gua buka di browser gua. Gua pilih account gua, teman-teman. Personal account workspace-nya. Oke.

**11:51** · Callback-nya ini, ya. Paste di authorization code or full redirect URL.

**11:55** · Ini kan ada redirect URL-nya, kita paste aja, ya. Kenapa? Site can't be reached.

**12:00** · Jangan panik dulu. Karena dia ngeluarin OAuth-nya dari local VPS, jadi OAuth response-nya dari chat GPT atau Open AI juga berupa localhost. Kalau localhost dibuka di browser kalian dengan port 1455, otomatis this site can't be reached. Jadi, dicopy paste aja full URL-nya. Jangan khawatir dan jangan takut. Dam. Testing your AI connection.

**12:22** · Wah, sudah terkoneksi dengan Open AI, Guys.

**12:25** · Gokil. Agent model Open AI GPT-6 Astra.

**12:29** · Thinking-nya medium, fast-nya off.

**12:32** · Huh. Oke, continue in your browser. Open this URL in your browser. Oke, teman-teman. Gua coba open, ya. Nanti pasti error. Kenapa error, teman-teman?

**12:42** · Kalau kalian memang menginstal Open Cloud kalian di lokal kalian, pastinya tidak akan error. Karena localhost-nya akan berjalan dan di-host di localhost kalian Open Cloud-nya. Tapi berhubung ini di VPS, jadi pasti akses ke localhost-nya 127001-nya.

**12:58** · Ini mah localhost komputer gua. Jadi, harus diganti IP address VPS kalian. Gua ganti, ya, pakai IP address VPS saya. Di panel Hostinger kalian ada alamat IP, dicopy aja. Kemudian di-paste di sini.

**13:10** · Coba kita open, ya. Enggak bisa juga.

**13:13** · Kalau menghadapi masalah kayak gini, teman-teman, jangan panik. Kita harus berusaha mencari penyebab masalahnya.

**13:18** · Karena di situlah perbedaan orang yang bisa berpikir dan yang tidak. Sekarang kalau gua buka IP-nya, IP-nya port-nya Open Cloud tetap enggak bisa kebuka.

**13:25** · Jadi, gua mau tahu alasannya kenapa.

**13:27** · Oke, berhasil terbuka, teman-teman.

**13:29** · Kenapa enggak terbuka? Sepertinya port-nya masih ditutup sama Hostinger untuk alasan security. Jadi, kita pakai port forwarding. Port forwarding itu apa? Kita bisa baca baik-baik di sini, teman-teman. Open from your computer.

**13:43** · Jadi, kita copy paste saja ini. Nah, ini gua sudah copy paste nih. Ini ada salah gua.

**13:48** · SSH -L -L. Jadi, dari port VPS-nya akan di-forward ke port lokal kita. Terus ini akses SSH-nya. Gua sudah jalanin kan username sama IP-nya. Terus ketika gua masukin password, ini port sudah berhasil di-forward. Nah, ini harus kalian simpan ya setting-annya biar kalian bisa akses GUI Open Cloud kalian dari mana saja. Oke, sudah selesai. Ini sudah terbuka. Apa yang terjadi ketika sudah terbuka? Ya, gampang. Seperti ini.

**14:12** · Kita bisa atur macam-macam dan ini ada koordinatornya. Mungkin bisa diganti-ganti ya agent-nya. Ini researcher-nya, reviewer-nya, terus writer-nya. Terus kita juga bisa set new agent. Kita ke koordinatornya dulu. Oke?

**14:26** · Sekarang Open Cloud kalian sudah berjalan. Kalian pakai port forwarding.

**14:30** · Tapi kok di SSH kalian kok kotor begini ya? Kayaknya dia jalan terus deh. Terus ada tulisan, "Gateway is running in the foreground. Press Ctrl C to stop. To keep the gateway running in the background later, Open Cloud gateway install. Run Open Cloud to open the TUI or Open Cloud dashboard to reopen the web dashboard." Loh, coba kita stop ya.

**14:50** · Mati enggak nanti?

**14:53** · Mati. Jadi, enggak scalable kan. Nah, kita butuh Open Cloud kita jalan di background. Caranya gimana? Tadi sudah dikasih tahu dong sama Open Cloud-nya.

**15:01** · Open Cloud gateway install. Coba saja kita install. Open Cloud gateway install.

**15:07** · Enter. I don't sleep. I just enter low power mode and dream of clean diff. Oke, gateway service install. Runtime readiness has not been checked. Startup may still be in progress. Check with Open Cloud gateway status and Open Cloud health. Cloud gateway status.

**15:23** · Coba kita refresh.

**15:25** · Oke, jalan. Nah, kalau kalian sudah instal Gateway, Open Cloud kalian akan jalan di background, teman-teman. Kalau kalian mau stop, tinggal Open Cloud Gateway stop, Open Cloud Gateway start, Open Cloud Gateway restart. Nah, itu buat ngatur Gateway-nya. Tapi yang kita butuhkan adalah Open Cloud jalan di background. Sekarang masalah port. Ini kan kita di localhost yang di port forwarding. Harusnya kalau kita ganti ini pakai IP VPS, idealnya harusnya bisa dibuka. Tapi gua tahu kenapa by default enggak bisa dibuka. Karena kalau bisa dibuka, ini bisa diakses di publik.

**15:56** · Dan kita harus set login-nya dulu di dashboard. Berhubung gua enggak mau set, teman-teman. Gua takut juga nanti siapa tahu gua salah ngeblur IP atau apa. Demi keamanan VPS gua juga. Gua mau prefer pakai port forwarding, teman-teman. Biar tetap aman. Oke? Dan kalian juga gua saranin pakai port forwarding dengan komen yang harus kalian catat ya, ini ya. Oke, komennya kalian catat. Karena ini yang paling aman. Nanti gua tulis di deskripsi deh kalau kalian bingung.

### Setup Tailscale

**16:31** · Tapi jujur kalian pasti pengin dong dashboard Open Cloud ini bisa diakses di mana saja sama kalian saja, bukan sama orang lain. Gimana caranya itu, Bang?

**16:40** · Pakai namanya Tailscale. Gua ajarin cara instalnya. Cara instalnya gimana ya?

**16:45** · Tanya AI-nya lah. Di zaman sekarang ngapain pusing-pusing. Gua sudah buatin prom. Aku Aku kamu lagi. Aku mau kamu instal Tailscale di server ini ya. Biar dashboard Open Cloud ini bisa aku akses dari jaringan Tailscale aku. Bisa kamu kerjakan dan sekalian set up. Gua pilih GPT-6 Astra. Mungkin extra high ya.

**17:02** · Karena dia gua ajak nge-set up Tailscale. Jadi biar bagus hasilnya.

**17:07** · Maksimum apa extra high ya?

**17:10** · Karena gua langganan yang 100 dolar, maksimumlah ya. Jangan kayak orang susah ya. Tapi teman-teman yang mungkin pakai plus, mungkin bisa high atau extra high aja. Tapi gua mau pakai maksimum.

**17:19** · Default-nya full access, oke.

**17:22** · Send. Low. Dia balas, "Bisa aku cek server dan konfigurasi OpenCloud dulu, lalu pasang Tailscale dan siapkan akses dashboard khusus lewat Telnet. Kalau perlu login, aku kirim tautan otorisasi di chat ini." Sambil menunggu, teman-teman, saya sarankan buat akun Tailscale. Tailscale itu apa? Ya ini buka tailscale.com. Jadi Tailscale ini apa? Intinya dengan Tailscale, kalian punya private network sendiri. Misalkan komputer ini sudah ada Tailscale, Mac Mini gua ada Tailscale, VPS gua punya di-install Tailscale juga.

**17:51** · Dan dalam satu akun gua, bisa saling terkoneksi lewat jaringan internalnya. Orang lain enggak bisa akses, tapi gua bisa akses.

**17:59** · Misal gua mau remote nih Mac Mini gua dari jauh, gua bisa pakai Tailscale.

**18:03** · Misal gua mau remote nih VPS gua, tapi gua enggak mau remote public gini pakai browser. Gua maunya remote SSH, tapi kalau pakai jaringan public dan gua enggak connect Tailscale, gua enggak mau ada orang yang bisa remote. Jadi gua mau cuman gua aja yang bisa remote server gua. Intinya gitu, pakai Tailscale bisa.

**18:19** · Sudah kita login aja lah, kebanyakan teori, enggak paham-paham nanti.

**18:23** · Dijelasin langsung lebih gampang. Gua sudah login Tailscale gua dan ini banyak, teman-teman, mesin-mesin gua yang sudah terkoneksi ke Tailscale, mostly VPS. Bakal gua sensor ya demi keamanan. Oke, kita balik ke OpenCloud.

**18:32** · Tailscale sudah di-install sama agen gua. Servisnya aktif otomatis saat server menyala. "Sekarang aku hubungkan server ke Telnet kamu. Silakan buka tautan login Tailscale ini. Masuk ke akun Tailscale kamu lalu setujui penambahan server SRF ini." Oke, gua masuk, gua buka link-nya. Jadi gua bakal nambah device ke akun Tailscale gua.

**18:52** · "You're about to connect the device" ini namanya "to the" ini email gua, akun gua, Telnet. Oke, gua connect aja ya.

**18:59** · "Your device is logged in to the" akun gua, Telnet. Jadi dia sudah masuk ke Telnet gua. Visit the console aja, teman-teman, buat ngelihat. Oke, gua bakal pilih server yang baru tadi, gua klik, dan dia bakal dapat IP-nya, teman-teman. IP Tailscale-nya. Silakan kalian akses IP ini enggak bakal bisa karena ini ada di jaringan pribadi gua.

**19:18** · Oke, gua balik ke OpenCloud. Server sudah terhubung ke Telnet kamu. Aku lanjut mengaktifkan HTTPS untuk dashboard di ini tanpa membuka akses publik. Jadi, ini link-nya hanya bisa diakses di jaringan Tailscale gua. Cara ngaksesnya gimana? Dari lokal komputer kita, kita download aplikasi Tailscale di Windows ada, di MacBook ada, teman-teman. Tinggal buka aja, terus tinggal di-connect. Nah, ini device yang baru, teman-teman. Gua udah connect ke Tailscale. Jadi, komputer gua ini udah connected ke Tailscale. Tinggal nunggu ininya jadi, terus gua bisa akses dari mana aja pakai akun Tailscale gua tentunya.

**19:49** · Dia ada nyuruh gua lagi, "Tailscale sudah terpasang dan server berhasil masuk ke Telnet kamu. Masih perlu satu persetujuan. Aktifkan Tailscale serve atau HTTPS di sini.

**20:00** · Enable HTTPS and funnel. Tailscale serve is ready to use." Setelah selesai, balas "Sudah." Agar aku tuntaskan konfigurasi dan pengujiannya. Sudah. Enak banget hidup di zaman AI, Guys. Enggak usah tuh kalian buka VPS, konfigurasi Tailscale install, enggak usah. Kalau udah terpasang OpenCloud, ini jagonya OpenCloud di sini emang. Dari dulu gua emang amaze banget. Kalian tinggal suruh dia aja. "Aku lanjutkan konfigurasi HTTPS dan tes akses dashboard lewat Tailscale." Kita tunggu aja. Setelah gua menunggu, sepertinya sudah selesai, Guys. Coba gua akses URL-nya ya. Gua akses, apakah bisa?

**20:34** · Wah.

**20:35** · Gokil. Sekarang dashboard-nya OpenCloud udah ada di jaringan Tailscale gua dan gua bisa akses dari device mana pun yang terkoneksi dengan akun Tailscale gua.

**20:45** · "Dari HP bisa, Bang?" Bisa. Gua tunjukin ya. Gua cobain dari handphone ya. Gua buka dari handphone gua pakai Safari, belum bisa karena gua belum connect ke Tailscale. Jadi, gua buka aplikasi Tailscale di iPhone gua, gua connect pakai akun gua. Sekarang kita buka lagi.

**20:59** · Refresh.

**21:02** · Idih, sebel. Bisa diakses dari HP. Ini URL-nya bisa kalian ganti anyway, teman-teman. Kalau mau URL yang lebih cantik, tinggal tanya dia aja. Dengan ini gua enggak harus konekin ke Telegram, gua enggak harus mantau VPS terus 24 jam, gua tinggal buka HP asal konek ke Tailscale. Ini kelebihannya Tailscale dan menurut gua juga salah satu poin positifnya Open Cloud yang mana dashboard-nya lumayan oke. Very nice, sudah bisa diakses ke mana aja.

**21:27** · Sekarang kita akan next step-nya, gua mau pasang model lain selain Open AI.

### Memilih Model LLM Bansos

**21:34** · Dashboard-nya Open Cloud sudah terpasang di jaringan Telnet gua. Sekarang saatnya kita pakai model Bansos.

**21:41** · \[berteriak\] \[tertawa\] Jadi enggak cuman Open AI dengan ChatGPT modelnya, gua mau ada fallback-nya, yaitu model LLM Bansos China. Beb, untuk ganti model caranya gimana? Sekarang sudah ada UI-nya semua. Enak enggak kayak zaman dulu Open Cloud-nya.

**21:57** · Kita ke setting, terus kita ke model.

**22:00** · Nah, ini kan ada banyak nih sebenarnya.

**22:01** · Ada decision model juga nih. Make type choice, scores, and this no judgement, itu juga ada sebenarnya. Nah, kita mau fokus di fallback modelnya ya. Kita add account dulu, teman-teman. Add account-nya otomatis pertama langsung Open AI, tapi kita bisa back di sini. Di sini tuh ada yang menarik dua buat gua.

**22:17** · MiniMax sama Open Code Go. Kita buka satu-satu ya. MiniMax, Open Code Go.

**22:23** · Kalau MiniMax ini plan ya, misalkan ya, monthly ajalah kemahalan. 11 dolar, tapi kita cuman bisa pakai MiniMax-nya.

**22:31** · Tapi kalau Open Code menurut gua, nah, bisa dikoreksi ya, teman-teman. Ini Go-nya ini bisa dapat banyak nih model LLM Bansos China-nya. 10 dolar lagi.

**22:41** · Enggak tahu cepat habis enggak ya, tapi kalau cuman buat fallback sih kayaknya oke ya. Atau mau dibuat yang utama?

**22:46** · Enggak apa-apalah pakai model China Bansos, paling data kalian diambil sama Xi Jinping. Enggak enggak enggak, bercanda bercanda. Bercanda ya, yang itu bercanda ya. Nanti gua disalahin pemerintah RRC lagi. Kita pakai Open Code Go aja ya, Guys. Oke, kita subscribe to Go. Enggak usah top up top up-an, langsung Open Code Go aja. orang cuman nyobain doang. Subscribe to go.

**23:04** · Bayar lagi setiap gua buat video selalu bayar. Awas aja kalau ads-nya enggak nutup ya. Duit kita cuman habis buat langganan AI, Guys. Kita pilih mau pakai yang mana, pay. Kita coba bayar pakai kartu kredit gua. Sukses bayar pakai kartu kredit BCA KrisFlyer Black, anjay.

**23:24** · Bayar mulu. Oke, sekarang saya sudah subscribe ke open code go. Teman-teman bisa lihat ya, kita pilihnya open code.

**23:32** · Berarti kita klik aja.

**23:34** · Butuh API key. Oke, kita buat API key-nya open cloud. Terus kita add API key, teman-teman.

**23:43** · Open cloud.

**23:45** · Permission all. Expiry date enggak usah.

**23:48** · Create key.

**23:49** · Copy ya. Kita masukin key-nya. Save provider.

**23:55** · \[berteriak\] Sudah berhasil terkoneksi ke open code gua, teman-teman. Sudah ada di sini.

**24:00** · Kalau kita pilih modelnya juga sudah ada. Banyak sekali bansos-bansosnya juga banyak. Kita set dulu ya. Mungkin kita bisa set sebagai fallback dulu. Gua suka pakai GLM sih, jujur. GLM 5.3 aja. Sudah gua set ya, teman-teman ya. Model GPT-6 Astra, fallback-nya GLM 5.3. Atau mau yang utama GLM? Mau nyobain? Ya sudah, enggak apa-apa. Kita balik aja. Kita pakai GLM 5.3 yang small background-nya GLM 5.3 flash ya. Fallback-nya baru kita pakai GPT.

**24:31** · Kagak ada. Wah, ininya ke-disconnect kayaknya. Kita connect provider dulu deh. Oke.

**24:36** · Sudah terkoneksi lagi open AI-nya. Gua enggak tahu kenapa tadi ter-disconnect.

**24:40** · Gua refresh lagi ya, coba ya.

**24:41** · Fallback-nya kita baru pakai open AI GPT-6 Astra dulu kali sebagai fallback.

**24:46** · Oke, sepertinya semuanya sudah oke. Kita refresh coba. Terus kita tanyain lagi ke agent kita, "Kamu pakai model apa sekarang?"

**24:56** · Low aja. Kita tunggu jawabannya ya.

**24:58** · Sudah dijawab guys, aku sekarang pakai model Open Cloud Google LM 5.3. Oke, enggak apa-apa kita stick ke model Bansos dulu ya, karena murah dan lebih membumi menurut gua teman-teman. Oke, tadi kita bahas fallback. Fallback itu apa sih sebenarnya? Fallback ini ngebantu ketika model utama kita mencapai limit atau error, langsung diarahkan ke model yang kedua. Jadi bukan kita kasih prompt terus milih mana yang paling pintar, oh ternyata model fallback-nya yang bisa jawab paling pintar, enggak. Fallback itu artinya cadangan. Kalau bahasa Genzi-nya namanya back burner. Jadi kalau sudah punya pacar, dia punya cadangan nih, disebutnya back burner. Bap!

**25:29** · Oke, kita deal ya, kita pakai model GLM 5.3 dulu, model dari China sana buat ngerjain tugas selanjutnya yang gua bakal kasih ke Open Cloud gua.

### Setup Channel Telegram

**25:43** · Tidak afdol rasanya kalau kita punya agentic AI, bahkan Open Cloud tidak terkoneksi ke channel Telegram atau WhatsApp. Di chapter ini gua mau jelasin kalian gimana sih caranya connect-in ke Telegram, yang mana gampang banget.

**25:57** · Karena apa? Karena sudah ada dashboard-nya. Even kalian tanya langsung ke modelnya juga bisa. Kalau mau manual kita pergi ke settings, channels, Telegram. Set up, channel set up, continue, continue. Kita pilih default primary ya. Open Telegram and chat with Bot Father. Open Telegram dulu, kita search saja Bot Father. Suruh ngapain tuh? New Bot lah, biasalah.

**26:20** · Namanya adalah kasih nama bot-nya Open Cloud VPS David underscore bot aja. Oke, kita dapat token-nya, ini berguna teman-teman. Kita save dulu ya. Nah, copy the token. Oke, continue. Enter Telegram Bot Token. Kita masukin ya, di sini set. Continue, continue, continue.

**26:37** · Configure DM access policy no, default pairing yes. Start. Kita ke bot-nya terus tadi di start ya teman-teman.

**26:44** · Continue dulu. Pairing recommended.

**26:46** · Administration from chat. Chat access let someone talk to your agent. A comment owner can also update Open Cloud. Oke, Oke, dulu. Send Telegram default message to agent coordinator dulu ya. Channels updated finish. Coba kita lihat dulu. Oh.

**27:01** · Open Cloud access not configure. Your Telegram user ID ini pairing code. Oke, ribet kan kalau pakai UI malah enakan langsung tanya agent-nya lah. Udahlah, bingunglah. Run aja nih. Approve.

**27:13** · This Telegram pairing. Kita tanya AI-nya ajalah di zaman sekarang tuh udah enggak relate emang UI kayak begitu. Udah dikerjain sama AI kita, approve Telegram-nya. Gua tanya you there now?

**27:25** · Ini langsung ke-reflect ya, teman-teman ya. Yes, I am here. Your Telegram is now connected to the Open Cloud gateway. So, message you send here reach me directly.

**27:33** · Anything you'd like me to do? Oke, udah aman. Sekarang kita set mungkin thinking-nya ke high aja. Biar kalau dia jawab di Telegram ya lumayan pintar lah, enggak low kayak tadi. Lama jawabnya.

**27:43** · Kenapa tetap butuh Telegram? Ya, misalkan kalau kita di luar pakai handphone juga bisa kita ngerjain sesuatu pakai HP kita ini. Ya, lu buka aja Telegram, buka tadi bot-nya. Ya udah tanya aja. Aku lagi siapkan data untuk memperkenalkan siapa aku ya. Ditunggu saja. Anjay, ngabarin ke AI. Kirim.

**28:03** · Kekirim juga di Telegram laptop gua, kekirim juga di dashboard chat Open Cloud-nya. Dia balas, siap aku tunggu.

**28:10** · Kirim saja kapan pun data perkenalannya sudah siap. Mantap, sudah terkoneksi ke Telegram dan kita pakai model GLM 5.3 tadi.

### Setup Lama OpenClaw Gua

**28:20** · Oke, selanjutnya di chapter ini gua bakal masukin setting-an Open Cloud lama gua ke Open Cloud gua yang baru ini, teman-teman. Tapi sebelum itu kita harus ngerti basic-basic memorinya atau session atau manage personality di Open Cloud tuh kayak apa sih? File-nya kayak apa aja sih dan lokasinya di mana? Kita secara teknikal harus ngerti. Kalau kita buka dokumentasi, teman-teman, Open Cloud ini ada yang namanya session dan memory. Ini yang membuat Open Cloud unik ketika pertama kali rilis. Yang pertama ada user.md. Sesuai namanya kalau gua sih ya zaman dulu ya di user.md ini ya gua jelasin siapa itu gua.

**28:51** · Itu sudah pasti wajib ya. Kemudian ada memori.

**28:56** · Jadi memori itu apa saja yang sudah pernah kita kerjain di log di situ nanti. Dan memori ini bisa di-backup atau kayaknya sekarang otomatis backup ya berdasarkan hari dan tanggalnya.

**29:04** · Kemudian ada dreams. Ini yang paling baru kayaknya di OpenClaw sekarang. Jadi ketika dia lagi enggak ngapa-ngapain, OpenClaw ini ada tiga state ya. Tidur ringan, REM, dan tidur nyenyak. Gua juga enggak tahu kenapa di kayak gituin.

**29:16** · Selama di proses tersebut dia bakal nyatat log apa saja yang dia kerjakan.

**29:20** · Jadi kita bisa pantau tuh kok di dreams dia ngerjain sesuatu yang enggak gua suruh ya. Nah itu kelihatan di situ.

**29:27** · Jadi itu diary dia, rangkuman sehari-hari apa yang dia kerjakan ketika dia tertidur. Ini berguna banget buat transparansi sama audit aktivitas dia.

**29:35** · Jadi harus diaktifin ya teman-teman.

**29:37** · Kalian enggak mau kan tiba-tiba nanti agent kalian ngirim pesan ke mantan kalian terus ngajak balikan kan enggak mau. Jadi harus diaudit setiap hari. Ya enggak usah setiap hari lah harus sering-sering dibaca saja. Oke, gimana cara ngaksesnya? Di mana lokasinya?

**29:50** · Kalau kalian kembali ke VPS, kita belajar teknikal dulu. Gua lagi ada di VPS dan gua sudah remote VPS gua.

**29:56** · OpenClaw itu file-nya di-hidden by default. Kalau di Linux, folder yang hidden itu awalnya ada tanda titik. Jadi kita harus masuk ke CD {titik} OpenClaw.

**30:07** · Ini semua file OpenClaw ada di sini.

**30:10** · Enter. Oke, isinya apa saja di dalamnya Bang David? Kita LS saja list folder.

**30:14** · Ada macam-macam teman-teman, tapi kita enggak usah peduliin. Kita fokus ke folder yang namanya workspace. Itu ruang kerja kita. CD workspace. Kita list folder lagi ya. Karena tadi kita setup multiple agent, jadi kita fokusnya ke koordinator saja ya yang utamanya ya.

**30:29** · Researcher, reviewer, writer nanti dulu.

**30:31** · Nanti dulu. Kita ke koordinator. CD koordinator. Kita LS lagi ya. Nah, lengkap di sini semua. Jadi ada agents.md. Agents.md itu lebih ke siapa kamu? Bot ini mau dinamain siapa?

**30:44** · Misalkan di Telegram, tadi kan namanya Open Cloud VPS David. Kita bisa kasih personality ke dia. Dia mau jawabnya gaya anak motorlah, gaya yang mungkin manja, itu juga bisa. Atau gaya yang garang, atau gaya yang lemah lembut, kalian bisa set up. Biasanya di agents.md. Kemudian di dreams.md, tadi gua udah jelasin ya, dia bakal nyatet aktivitas selama dia enggak dipakai.

**31:04** · Jadi aman, kalau dia ngapa-ngapain ketahuan. Kemudian identity.md. Ini kayaknya mirip sama agents.md. Enggak tahu bedanya di mana, nanti kita lihat aturan lama gua aja ya. Kemudian memory.md, dia bakal nyatet apa aja yang udah pernah dikerjain dan ini penting banget kalau kalian migrasi Open Cloud ke Herme, bisa dicatat dan pindahin aja kerjaan kalian. Kemudian soul.md, kita bisa nge-set jiwa agent kita kayak apa.

**31:27** · Ini sebenarnya juga overlap sama agents.md sih menurut gua. Settingannya terlalu kompleks dan nanti coba kita lihat ya bedanya di mana di settingan lama gua. Kemudian user.md, ini yang penting, ini ngejelasin siapa kita teman-teman. Kemudian ada memory, itu backup memory-nya. Sekarang kita langsung aja ke settingan lama gua teman-teman. Gua udah masukin di laptop gua ini dan gua taruh di Visual Code, semoga kelihatan ya. Kita buka dulu ya yang rada-rada mirip ya. Agents.md dan soul.md.

**31:56** · Oh, salah. Gua salah, sorry. Agents.md itu nge-treat gimana agents-nya itu harus menjalankan tugasnya. Contoh, before doing anything else, lu harus read soul user, terus nge-read memory, terus enggak usah sama permission, just do it. Oh, gua nge-set agent gua tuh harus gimana. Oke, jadi bukan persona agent-nya. Memory gimana ngaturnya, safety-nya gimana, kalau default-nya kayak apa sih coba ya. Kita cat aja deh.

**32:21** · Cat agents.md. Oh, agak sedikit ya.

**32:24** · Pakai yang punya gua aja. Teman-teman nanti bakal gua sanitize settingan Open Cloud gua dan gua share ke kalian ya.

**32:29** · Semoga kalian bisa pakai juga. Oke, itu agents.md. Sorry teman-teman tadi gua salah. Enggak apa-apa namanya tutorial kan wajar ada salah. Kita kan manusia kan. Jadi gua juga membuat tutorial itu tujuannya gua enggak mau sempurna. Gua mau belajar bareng-bareng sama kalian.

**32:41** · Kemudian kita buka yang kedua, soul.md.

**32:44** · Nah, ini adalah persona agent-nya.

**32:47** · Oh iya, dulu gua namain performance bagger. Jadi dia tuh road scholar, the high-tech mechanic. Jadi kok itu kan gua suka banget sama Harley ya. Jadi dia itu anak motor banget jawabnya. Terus kayak cowok banget. Vibe-nya gritty, experience, reliable, and sharp-witted.

**33:01** · Oke, mission to assist the user with high performance intelligence. Oke, ini keren banget sih. Nih gua udah buat dulu, gua ketik terus gua research di AI, gua ketik lagi.

**33:11** · Lama banget gua ngabisin waktu buat explore AI ini, ingat banget zaman dulu.

**33:14** · Kemudian kita ke file apa lagi teman-teman? tadi gua udah buka juga. identity.md ya, ini cuman lebih ke who am I sih tak. Lu tuh performance bagger, AI assistant. Lebih mirip ke soul juga sih sebenarnya, agak overlap sih. Terus setting avatarnya, mungkin lebih ke teknikalnya ya. Lu siapa, avatar lu ini gitu. Oke, enggak apa-apa.

**33:38** · Bisa kita lanjut? Sebelum ke memori gua mau ke user.md dulu ya teman-teman ya.

**33:43** · user.md ini menjelaskan siapa kamu. Gua udah set nama gua David, lokasi gua di mana, nomor HP gua lah, nomor HP istri gua, terus gua Harley-Davidson enthusiast, gua juga seorang konten kreator, tech entrepreneur, journey gua sebagai konten kreator tuh gimana, terus kisah hidup gua gimana aja gua tulis di sini. Dan link Instagram, sosial media gua gua tulis semua di sini teman-teman.

**34:05** · Oke, memory.md.

**34:07** · Nah, memory.md ini apa? Gua tuh nge-set hard rules juga di memori. Enggak boleh nge-send email sebelum nunjukin draft-nya ke gua. Enggak boleh nge-post Twitter ataupun Instagram ataupun outbound communication tanpa approval gua. Terus gua enggak suka nih AI pakai m-dash. Ini masih banyak pakai m-dash nih, lihat nih, pakai m-dash nih. Najis banget kan m-dash tuh gua enggak suka nih. Kayak strip panjang gitu loh. AI banget m-dash itu. Kalian kalau pakai AI, tolong m-dash-nya atau M-Dash-nya itu di-remove ya, teman-teman ya. Itu kelihatan banget buatan AI. Ya, gue itu siapa? David.

**34:37** · Gue ulangi lagi di memori, terus ini kerjaan gue tentang web ekspor, apa aja. Kemudian kalau di-breakdown lagi, web ekspor tuh apa aja sih order-nya? Ternyata kelapa tuh order-nya banyak banget, terus unclassified. Nah, ini gue harus pecah lagi nih. Terus generic ekspor, agrikultur. Jadi, domain-domain-nya tuh gue gue udah breakdown pakai AI gue. Ya, itulah gunanya AI. Dan gue masukin ke memori. Jadi, data analitik-nya web ekspor, bisnis gue sendiri itu lengkap banget memang. Terus yang lainnya, mmm standar sih pekerjaan gue yang disimpan sama dia. Dan list-list konten gue.

**35:07** · Oke, ini memori gue ya. Gue enggak akan share dong memori-nya. Masa memori-nya di-share? Paling nanti yang general aja gue sanitize dulu datanya ya. Nanti gue share ke kalian, teman-teman. Oke, terus gue punya apa lagi? Gue punya viral konten reference index, teman-teman.

**35:23** · Jadi, karena gue adalah seorang konten kreator, gue dulu berpikir, gimana ya cara gue bisa generate script yang bagus pakai Open Cloud ini? Terus gue berpikir, konten gue kan selama bertahun-tahun kan banyak yang viral.

**35:35** · Nah, yang viral itu gue kumpulin, teman-teman, script-nya. Terus kalau gue enggak ada script-nya, gue convert ke audio, dari audio gue convert ke teks.

**35:42** · Itu kerjaannya panjang banget. Terus gue compile, gue masukin ke Open Cloud suruh analisa konten yang viral kayak apa.

**35:49** · Jadi, gue punya reference konten yang viral, teman-teman. Dan dulu setiap konten-konten viral gue cek dan gue catat, ini viral, ini enggak, ini viral, ini enggak. Jadi, ini banyak konten-konten lama gue yang gue catatin ya. Ya, inilah cara kalian menggunakan AI yang benar. Dan karena dulu ini viral konten reference index-nya tuh panjang banget, jadi gue pisah ke folder sendiri. Jadi, di workspace Open Cloud gue tuh ada folder namanya konten. Nah, di konten ini ada endorsement dan non-endorsement. Nah, non-endorsement aja deh ya nih. Konten-konten gue gue notes semua. Nih, konten-konten gue zaman dulu nih, bulan 3 kan?

**36:20** · Ada buktinya kan? Enggak bohong kan? Nih, gue buat semua dan gue catat semua. Dan konten viral script MD couple konten.

**36:28** · Jadi viral script kayak gimana, banyak banget di lines dan lain-lain, cara dia viral gimana, kenapa konten yang ini viral, kenapa yang ini enggak, pokoknya analisanya ada di sini semua sebelum gua pindah tools lain dulu. Kemudian ada couple konten, nah gua kalau konten sama istri gua tuh yang Harley-Harley tuh, itu gimana, kenapa bisa viral, hook-nya di mana, itu ada semua di sini. Gitu dan kenapa tadi gua klaim mendapatkan uang yang lumayan banyak ya gara-gara Open Cloud ini. Yang pertama tadi kan ada data analytics swap ekspor gua ya. Jadi dulu tuh ngedata analitik itu susah banget.

**36:59** · Baca Google analitik aja susah, ngompel data sales susah. Semenjak ada Open Cloud gua masukin data gua semua dia langsung keluar analisa dan itu berguna banget bagi bisnis gua. Gua jadi tahu harus jualan website ke siapa, apa yang harus gua kerjakan dan itu ngimprove banget sales-nya. Kemudian dari segi konten juga jadi naik. Gila, bener-bener gua ngebuat script-nya cepet, script-nya hasilnya bagus lagi.

**37:19** · Jadi kontennya itu viral, viral, viral, viral. Nah, script gua yang e-KTP dulu aja itu dibuat pakai Open Cloud dulu.

**37:24** · Tapi gua kasih restriksi biar gua enggak kena masalah dan hasilnya kan viral kan dan disebarluaskan di mana-mana dan itu adalah bukti kalau kita bisa memanfaatkan AI dengan baik ya benefit-nya ada di kita semua. Oke, sekarang gua mau coba masukin settingan lama ke Open Cloud gua yang baru. Lihat nanti dia seberapa mirip sama Open Cloud gua yang lama yang ada di Mac Mini gua dulu. Untuk memindahkan folder Open Cloud lama gua yang gua beri nama workspace David ke VPS gua, kita harus pakai namanya SCP secure copy protokol command.

**37:55** · Jadi ngopi file dari lokal ke folder di VPS server kita melalui SSH.

**38:01** · Oke, gua udah kasih command-nya SCP documents workspace David spasi username VPS-nya di folder root ya. Sorry ada salah guys, ternyata error karena yang gua transfer ini folder bukan file. Jadi butuh min R di depan. Lah kita mah kalau salah ngomong salah bro, min R SCP. Beh, kalian ngerjain ini di coffee shop. Beh, disembah kalian sama orang. Masukin password-nya.

**38:25** · Copy. Beh, ini baru hacker. Lihat nih, transfer dari lokal ke server pakai komen. Masih zaman pakai file explorer atau kalian pakai file zilla. Enggak zaman, Bro. SCP.

**38:38** · Lihat seberapa keren gua sekarang.

**38:40** · Lihat, gua pamer-pamerin ini di coffee shop. Ini baru keren, Bro. Kalian harus bisa begini ya, teman-teman ya. Karena di luar negeri ini tuh hal yang biasa.

**38:49** · Cuman transfer-transfer begini. Di Indonesia kok orang enggak pada tahu, padahal googling aja selesai. Kita tunggu ya transfer file-nya selesai ya, teman-teman ya. Gua udah excited banget nih. Nih lihat nih, Guys, angka-angka begini ditransfer ke server. Widih widih widih widih.

**39:02** · Gokil, Bro. Ini baru programmer IT. Ini juga yang jualan kelas 1 jam jadi programmer juga enggak bisa nih begini nih. Ini baru programmer sejati, Bro.

**39:11** · Selesai. Ush. Ini baru seorang programmer. Transfer file-nya lokal MacBook langsung ke server. Enggak pakai file zilla, pakai terminal dong. Genkie.

**39:20** · Orang skill issue gitu dong. Kita harus begini. Jangan malah beli kelas 1 jam jadi programmer.

**39:25** · Ah, oke lanjut, teman-teman. Bercanda mulu. Sekarang kita kembali ke dashboard open cloud kita yang koordinator. Gua tambahin ya. Perhatikan a prom-nya. Di folder root workspace David ada konfigurasi open cloud lama aku. Tolong kamu pelajari ya dan update workspace koordinator dengan konfigurasi ini.

**39:44** · Please notice beberapa pekerjaan atau deadline mungkin tidak relevan ya karena terakhir aku aktif menggunakan open cloud di awal tahun kemarin. Jadi ambil saja apa yang esensial dan fundamental untuk mengetahui siapa aku sebelumnya dan cara kerja aku memakai open cloud.

**39:57** · Oke, kita set GLM 5.3. Kita set ultra biar dia berpikirnya cepat dan pintar.

**40:04** · Sorry, bukan cepat ya. Dia berpikirnya lebih pintar karena ini butuh ultra sepertinya buat analisis dan coba kita jalanin.

**40:10** · Damn.

**40:12** · Huh. Dan kalian bisa lihat ya, teman-teman ya. Kita transfer file ke server-nya atau VPS-nya Hostinger juga lancar banget dan ya daripada kalian pakai VPS abal-abal maaf ya maaf ya kalau gua sih pilih yang nyaman pilih yang aman ya udah pakai perusahaan besar Hostinger dengan standar mereka kalian bisa baca sendiri yang aman dan selalu aktif dipakai juga lancar kalau gua ya sambil promosi sedikit-sedikit ya sekarang lagi dipelajarin kita tunggu aja dia mempelajarinya gimana yang jelas

**40:38** · setiap step-nya dia update ke kita aku pelajarin folder konfigurasi lamamu sekarang terus dia nge-read from workspace David Soul.md dan lain-lain ini bakal panjang nanti kita langsung lihat aja result-nya ya teman-teman ya nanti kalau enggak video ini kepanjangan oke dia udah selesai untuk menganalisa dan dia sudah masukkan persona yang lama

**40:57** · settingan yang lama ke open cloud yang baru semua file udah aku pelajarin aku ambil dan simpan user MD memori terus yang tidak aku bawa itu status deal dan deadline masalah brand dan lain-lain kerjaan lama enggak dibawa sama dia semua itu tetap utuh di folder lama sebagai arsip referensi sudah aku catat tapi tidak dianggap sebagai status aktif pintar banget kan dia nah tiga hal yang butuh keputusan kamu persona asisten lama performance bagger oke persona asisten lama tolong aktifkan aku kangen sama dia anjay nomor dua aturan model

**41:30** · lama ditinggalkan saja karena kan kita pakai baru kan GLM 5.3 dan open AI dengan GPT-6 Astra aturan model lama tinggalkan saja integrasi tools lama setup nanti saja oke kita kirim coba nanti dia berubah jadi anak motor enggak enter dia sudah selesai menjawab langsung jadi anak motor kickstand up

**41:49** · bro dia sudah balik di garasi asli gua kangen banget udah lama enggak pakai sudah aku kerjakan persona performance bagger aktif soul dan identity sudah aku pasang ke workspace koordinator jadi mulai sekarang semua sesi pakai suara dia lagi direct brotherly dan tetap presisi soal mesin aturan model lama ditinggalkan mesin sudah menyala dan idling halus di server baru ini kalau ada jalur yang mau ditarik tinggal bilang kita gas bareng bap bap bap tapi kan gua tadi pakai GLM ya, lumayan banyak dan ultra. Kita mau tahu dong sisa limit Open Cloud gua kita di berapa? Coba kita buka ya, gua refresh 46%. Lumayan boros sih.

**42:19** · Namanya juga bansos 10 dolar sebulan, kalau VPS-nya 10 dolar juga ya berarti kan sekitar 400 ribuan kita bayar sebulan. Dan udah dapat kapabilitas seperti ini loh, ini udah cukup banget menurut gua kalau buat pekerjaan ringan sehari-hari. Tinggal kita atur bobotnya aja, jangan ultra terus, high aja cukup. Nanti settingan generalnya yang udah gua sanitize datanya udah gua cleansing, udah gua bersihin bakal gua share ke kalian ya teman-teman ya. Buat referensi kalian aja kalau mau setup Open Cloud, biar hasil jawabannya itu bagus. Nanti gua taruh link-nya di deskripsi.

### Testing: Bikin Script Konten

**42:56** · Sekarang kita ke chapter, gua mau coba ngebuat script reels atau short video menggunakan Open Cloud dengan model GLM 5.3, tapi pakai settingan lama gua, pakai viral konten script gua yang tadi gua udah jelasin. Pokoknya pakai formulasi konten gua yang udah gua simpan di Open Cloud gua. Sebelum itu gua mau cek dulu, dia punya enggak? Dan dia udah catat belum? Kamu punya dan catat informasi gaya konten aku kan?

**43:19** · Coba kita tanya ya. Kita pakai high aja teman-teman, karena limit kita semakin habis. Coba kita enter. Enggak enak ya kalau kejar-kejaran dengan limit. Apa gua update ya paketnya ya? Jadi yang 40 dolar ya. Menurut kalian update enggak guys?

**43:32** · Nih 40 dolar tuh udah hampir sejuta loh.

**43:34** · Masa hidup kita cuman buat beli, aduh langganan ChatGPT 700 ribuan ding.

**43:39** · Enggak usah deh ya, nanti dulu ya guys ya. Kita fokus selesaiin konten ini dulu. Punya dan sudah tercatat penuh bro. Barusan aku rampungkan juga impor formulanya biar utuh di garasi baru viral script couple konten. Jadi kalau kamu minta bikin script baru formulasi lengkapnya sudah siap di tars, sudah siap tars di mesin, apaan sih? Tinggal sebut topiknya langsung aku gas dengan gaya dan pola yang sudah terbukti. Oke, aku ingin kamu buat short video script tentang model AI open source bernama Jeff.

**44:12** · Coba deh kamu cari referensi yang bagus kapabilitas Jeff coba bikinin script-nya buat aku dengan gaya aku. Ada edukasinya juga. Tujuannya mengedukasi bukan jualan kelas.

**44:31** · \[berteriak\] \[tertawa\] Oke, maksimum ya. Biar dia lebih oke karena kita butuh research. Coba kita lihat limit kita udah di 54% kayaknya masih cukup deh. Oke, kita running ya.

**44:43** · Oh ya, lupa. Aku mau hasil script-nya dikirim di sini dulu. Enggak usah kamu buat docx, md ataupun pdf. Oke, kita jalanin. Hap.

**44:51** · Kita tunggu ya teman-teman. Akhirnya sudah selesai. Kita lihat sisa limit kita. Masih aman baru di 73% 2 3 jam lagi reset. Masih oke. Dia research tentang Jeff itu model dari mana buatan siapa, type safe AI.

**45:07** · Komunitasnya lagi rame, sumber primer udah kepegang, ada faktanya, klaim vendor-nya. Oke, judulnya AI yang ngalahin GPT-5 tapi enggak bisa diajak ngobrol. AI ini baru ngalahin GPT-5, Gemini-3 dan Gemini-3 dan sama DeepMind di satu leaderboard reset. Anjir dan dia sengaja enggak bisa diajak ngobrol. Hmm, masih kurang natural ya kata-katanya ya.

**45:27** · Tapi enggak apa-apa nanti bisa kita koreksi. Dan dia ngomong anjir lagi.

**45:30** · Enggak boleh.

**45:31** · Lupa gua kasih restriksi. Jadi kalau gua buat script tuh biasanya biasanya ada VO, ada on screen teks-nya, ada alternatif visualnya. Buat editor ini dua ini untuk editor. Dia jelasin kenalan, masalahnya, edukasi inti, cara kerjanya, bukti yang paling nyangkut.

**45:45** · Nah, ini ini harus diedit nih. Yang paling nyangkut tuh jelek banget bahasanya. Oke, demo, disclaimer, punchline, edukasi. Aman sih ini gua bisa langsung shooting bahkan. Tinggal dikasih contoh-contohnya doang ini. Oke, dia udah tahu intinya Jeff itu apa, dia buat ngambil decision, dia bisa buat prediktif apa yang akan terjadi dari data ini. Ya, itu gunanya Jeff Good. Ini gua bisa langsung syuting. Ya, hasilnya oke ya, karena gua sudah punya setting-an sebelumnya. Dan ini membuktikan memakai model apa saja, hasilnya bakal sama, teman-teman. Gua enggak percaya, Bang David, coba pakai model yang canggih, GPT-6 Astra. Oke.

**46:19** · Kita kerjakan. Bedanya di mana ya?

**46:21** · Penasaran kan pasti? Sebenarnya model itu enggak ngaruh-ngaruh amat. Yang ngaruh itu konfigurasi kita. Coba kita kerjain pakai Open AI. Gua ubah dulu setting-annya. GPT-6 Astra. Fallback-nya baru GLM 53. Coba kalau GPT-6 Astra gua bisa ultra ya, teman-teman, dan face mode. Karena gua langganan yang 100 dolar.

**46:38** · Sombong amat.

**46:39** · Enggak, biar cepat saja ini, gua malas nunggu. Aku sekarang ganti model pakai GPT-6 Astra. Coba kamu buat lagi script-nya dari awal. Pokoknya ulangin. Aku mau tahu hasilnya. Ini prompt-nya gua kasih juga nih.

**46:58** · Nanti konteks dia hilang. Oke, jalankan.

**47:01** · Kita tunggu ya. Hasilnya apakah sama, lebih bagus atau jauh berbeda? Coba kita tunggu saja. Oke, sudah jadi.

**47:08** · Dia lebih lama ngerjainnya, karena gua pakai yang ultra, mungkin research-nya lebih dalam. Script-nya AI pintar ngomong, boleh dikasih wewenang atau enggak? Kalau yang ini, AI yang ngalahin GPT-5, tapi enggak bisa diajak ngobrol.

**47:20** · Mungkin angle-nya agak sama ya, yang pertama menunjukkan kalau ada AI canggih nih, tapi enggak bisa diajak ngobrol.

**47:25** · Yang kedua, si GPT-6 Astra ini ngomong, ada AI yang kalau agentic pintar ngobrolnya pintar. Tapi boleh enggak kasih dia wewenang? Dan hook-nya menurut gua lebih bagus yang GPT-6 Astra ya, AI salah jawab, lu bisa masih bisa protes.

**47:37** · Tapi kalau AI salah proses refund pelanggan, yang protes bagian finance.

**47:40** · Good banget, AI jago ngomong belum tentu boleh dikasih wewenang. Oke. Terus ide di balik Jeff buat ke model yang bisa buat keputusan terstruktur, mereka menyebutnya sistem one. Nah, ini ada juga versi Jeff dari Auto Trust, beda pembuat, bukan rilis resmi type safe, kayaknya ini gua buang saja, enggak relate, gua enggak mau contohin ini, gua mau Jeff dari Type Safe. Menurut gua tadi prom gua juga mungkin kurang lengkap ya, Jeff dari mana? Bayangin toko online lu dapat pesanan, sudah bayar kok ditagih lagi, kita kasih tiga pilihan pembayaran, pengiriman, teknis.

**48:06** · Dia enggak cuman bisa nyortir pesan, dia kasih skor berdasarkan kriteria. Nah, ini mulai enggak jelas nih, ini jeleknya GPT nih. Kalau dia ngasih contoh, bahasanya tuh kurang oke menurut gua.

**48:15** · Tapi probabilitas bukan jaminan benar, dari tingkat keyakinannya software bisa diatur, kasus jelas diteruskan, kan enggak jelas orang. Lebih bagus GLM malah menurut gua. GLM ini ngapain? Oke, dia kasih cara pakai nya. Terus dia kasih bukti benchmark-nya. Nah, terus habis itu dia ngasih contoh-contoh peneliti yang sudah pakai Jeff. Jadi secara praktikal saja dia kasih contoh, jadi gampang jelasin ke audiensnya.

**48:36** · Kedua skrip ini masih bisa direvisi lagi tentunya teman-teman, tapi dari hal ini kan kita tahu kan Open AI ini oke, hook-nya bagus tadi. Tapi ketika penjelasan dia kasih contoh bahasa Indonesianya kagak nyambung, ini selalu terjadi di Open AI. Refine lagi kita harus tune lagi. Gua ngerti banget karena gua pakai macam-macam model. Tapi kalau GLM walaupun bansos, dia langsung kasih contoh loh, dipakai ini, dipakai ini, dipakai itu dan bahasanya jelas menurut gua. Dan ini kalau di return menurut gua GLM yang bagus. Jadi teman-teman harus pintar-pintar di sini, bukan berarti kalian pakai model paling canggih hasilnya paling bagus.

**49:06** · Menurut gua GPT 6 Astra itu masih bagus di 3D modeling. Kalau teks base gini, research script, apalagi bahasa Indonesia, menurut gua masih kurang. Jadi gua mau balik lagi ya pakai GLM, bagusan model bansos. Ganti lagi GLM 5.3. Menyenangkan sekali mainan AI ini. Kita bakal ngulik-ngulik terus enggak ada selesainya ya teman-teman. Jadi begitu ya, gua pakai formulasi viral konten skrip gua saja masih harus gua lihat, masih harus gua supervisi, mana yang lebih bagus model ini menjawab apa, model ini menjawab apa.

**49:37** · Dan yang paling ngerti itu kita sendiri. Jadi kalau kita memakai AI, tolong disupervisi sama diri kalian sendiri. Ini itu cuman tools, ini itu cuman alat. Gua contohin, semenjak gua pakai Open Cloud tadi di awal, banyak endorsan gua, rame, orang pada endorse, seneng, scriptnya cepet, tapi kan dibalik itu kan gua juga meriksa, dibalik itu gua juga berpikir, gimana memformulasikan viral konten gua, terus script yang dihasilkan gua revisinya dimana, prompting aja gua tadi pikirin, itulah fungsi kita sebagai manusia di

**50:08** · era AI ini, jadi jangan kayak boomers-boomers itu, semua bisa diselesaikan pakai AI, hasilnya AI slop, bagaimana kita menghasilkan output yang berkualitas, bagus, bisa dijual, menghasilkan nilai ekonomi bagi kita itu memakai AI yang benar, dan kalian harus seperti itu ya teman-teman.

### Testing: Bikin Website

**50:25** · Di chapter ini kita bakal coba memakai Open Clo kita buat coding atau mengerjakan website ataupun apalah yang bisa kalian kerjakan sehari-hari, tapi disini berhubung gua orang jualan website, gua pengen coba buat mock up, mock up website untuk pemain arang briket di Indonesia, gua udah siapin promnya teman-teman, kita baca aja sama-sama ya, buat mock up desain website penjual arang briket menggunakan HTML, CSS dan Javascript sederhana dalam satu file HTML, gunakan desain modern, profesional dan lain-lain, isi halamannya apa, gunakan bahasa Inggris

**50:55** · berikan kode lengkap aja yang bisa langsung dibuka di browser aja teman-teman, lebih aman, kita jalanin di lokal aja nanti, oke coba gua running ya, GLM 5.3, maksimum sisa limitnya 73%, tapi enggak apa-apa, harusnya masih oke sih, high apa maksimumnya, maksimum aja deh, oke kita jalanin lah, coba lihat kayak apa 20 minutes later Ada sedikit masalah teman-teman, jadi tadi gua udah cobain prom, terus bener-bener enggak respons GLM 5.3 gua

**51:21** · dari Open Clo, terus gua ganti lagi ke GPT Astra, gua tanya kenapa dan lain-lain dan akhirnya gua konfigurasi lagi, ini lagi dicoba, semoga enggak ada masalah lagi dan gua mau jalanin prom yang tadi lagi teman-teman, nah ini mungkin kelemahan Open Clo ya yang gua enggak suka ya, dia nge-set, misalkan agennya ada 5, terus gua ganti model di koordinator lewat UI dashboardnya ini, gua ganti model ke GLM tadi, tapi agen-agen yang lainnya enggak tahu modelnya apa, jadi ada bug di situ dan menurut gua mungkin ini yang membuat Open Cloud ditinggalkan ya.

**51:49** · Jadi, dia nyediain dashboard tapi menurut gua konfigurasinya enggak lengkap. Contohnya kayak tadi Telegram. Telegram juga agak susah loh menurut gua. Enaknya tanya aja sama agent-nya. Dan ini mungkin yang ngebuat Herme dengan berbagai macam fleksibilitas modelnya bisa kita konekin ke Nine Router dan lain-lain itu jadi maju gitu. Karena lebih gampang nge-setup modelnya dan jarang error ya kalau gua pakai Herme ya kayak gini-gini. Ini kan ngabisin waktu banget tuh akhirnya tadi API key-nya Open Cloud gua masukin ke global scope.

**52:16** · Jadi, setiap agent bisa ngerti kalau mau pakai model Open Cloud GLM 5.3 pakai API key yang ini. Padahal kan sudah ada setting ya diganti di model sini ya. Enggak maksud gua kenapa lu enggak kayak setting-nya apa, lu pakai yang mana, terus kalau ada masalah lu solve sendiri lah. Nah, itu kelebihannya Herme kayaknya dia bisa berkembang seiring dengan penggunaannya. Ya, namanya tools ya itu plus minusnya ya teman-teman.

**52:41** · Jadi, kalian wajib tahu juga. Tapi, yang jelas tadi kalau pakai GPT 6 Astra dari OpenAI enggak ada masalah apa-apa tuh.

**52:47** · Sekarang masih gua benerin dan akhirnya pekerjaan utama kita tadi enggak selesai malah ribet di config-nya kan. Padahal gua cuman mau pakai GLM. Limit gua sampai habis loh tadi nge-config dan gua sudah top up kredit lagi. Akhirnya kan bete kan. Tapi, coba gua usahain ya kita bisa enggak nge-resultin website pakai GLM.

**53:05** · Teman-teman, tadi gua sudah selesai setup GLM-nya diset ke global terus gua kasih data prompt buat ngebuat website-nya tetap enggak bisa. Katanya gara-gara konteksnya penuh. Jadi, gua harus buat new session chat. Gua buat new session chat juga. Kalian bisa lihat di sini namanya website time out.

**53:22** · Padahal kalau pekerjaan ringan dia bisa.

**53:24** · Ini GLM 5.3 loh model gede loh. Kalian boleh bantu komen deh apa setting-an Open Cloud gua salah ya? Ada kok kreditnya kok 7 dolar tadi gua top up lagi memang sudah habis go-nya. Ini ngabisin waktu menurut gua dan annoying banget. Coba kalian bantu komen ya apakah memang Open Cloud ini didesain lebih optimal kalau pakai model OpenAI karena dia dibeli sama Open AI. Dan ini juga salah satu alasan teman-teman yang membuat gua cabut pakai Open Cloud.

**53:47** · Semenjak Anthropic enggak ngebolehin lagi login pakai OAuth di Open Cloud harus pakai API key yang mana mahal banget. Gua ngerasa Open Cloud gua ini kalau pakai model alternatif itu sering banget error. Dulu bahkan kalau pakai Open AI aja error guys. Ya, kalau cuman optimas pakai Open AI ya percumalah masa agent AI cuman bisa satu model enggak seru dong, seruan Hermes dong. Ya udah kita ganti Open AI coba ya. Karena mau enggak mau chapter ini harus diselesaiin. Ini prompt gua, gua pakai GPT 6 Astra Ultra fast mode. Oke, coba kita running ya dan kita buat website di Open Cloud pakai GPT 6 Astra. Tuh, langsung bisa jawab dia.

**54:21** · Gua pakai GLM tadi sampai budek loh. Gua buat satu file HTML lengkap dengan katalog. Tuh, ada task progress-nya.

**54:33** · Coba teman-teman ya, asli gua mau tutorial ini senatural mungkin. Kalau gua enggak bisa, gua stuck ya gua bilang stuck. Gua stres nih gua dari tadi config. Coba kalian bantu komen teman-teman apakah memang sepengalaman kalian pakai Open Cloud itu lebih optimas kalau pakai modelnya Open AI dan model lain tuh kayak disingkirkan gitu atau kayak ribet makainya. Gua ngerasa sih gitu ya. Enggak ada yang salah settingan Open Cloud gua, pakai API key, kredit masih ada. Eh, ketika pakai Open AI GPT 6 Astra langsung ada task progress-nya bahkan. Gua pakai GLM gua tungguin bermenit-menit tadi habis kali gua sejam. Coba kita tungguin aja deh guys.

**55:02** · Jadi teman-teman kalau kalian merasa tadi gua mungkin salah konfigurasi GLM-nya atau ada yang kurang boleh komen aja ya teman-teman ya. Gua mau tutorial ini kita belajar bareng-bareng tidak ada yang saling menggurui. Gua juga manusia biasa yang ya mungkin ada kesalahan config atau memang Open Cloud-nya yang nyebelin. Ya gua cuman manusia biasa aja tapi punya Harley Bap. Sambil kita nunggu nih website-nya jadi agak lama juga. Lihat nih ada error lagi nih. Kayaknya hal yang sama. Child session design website bracket Nusantara failed. No root compatible authentication source is configured for Open AI. Kan secara logika enggak masuk akal ya.

**55:33** · Misalkan nih, lu ngerjain sesuatu pakai model GPT-6 Astra, terus untuk ngerjain hal tersebut dia ngebuat small agent lagi buat bagi-bagi tugas. Nah, small agent-nya ini kagak dikasih tahu authentication Open AI-nya apa. Ini kan error-nya basic ya, ini kan kesalahan Open Cloud-nya lah jelas. Ya, kalau lu kerja pakai small agent, lu utus beberapa agent dari tugas gede, ya lu kasih authentication lah otomatis. Itu by default kan secara logika ya udah masuk kan harusnya. Kenapa gua jadi marah-marah ya? Oke, udah selesai akhirnya.

**56:04** · Teman-teman, setelah kita nunggu beberapa step, walaupun tadi masih ada error yang annoying ya, child session-nya itu enggak ada authentication buat Open AI-nya. Sumpah itu annoying banget sih dan basic logic kenapa lu enggak benerin itu. Udah kasih hasilnya begini, gua kita open aja, udah kita download, kita buka ya, mock up.

**56:23** · Masih AI menurut gua, tapi bisa di-improve.

**56:26** · Ya, bagus, no problem sih buat single page. Bisa langsung jadi, cuman tadi masalahnya di apa hayo? Di authentication-nya aja. Gua mau nyobain pakai GLM enggak dikasih, akhirnya pakai Open AI bisanya. Ini tinggal di-improve, tinggal direpetisi bisa jadi website yang cepat sih dan ini tergantung prompt juga dan kebutuhan kliennya teman-teman.

**56:43** · Dan gua yakin kalau gua serius dan ngebuat SOP buat tim yang kayak di Web Expert sekarang, website-nya bakal jauh lebih bagus, tapi enggak pakai Open Cloud.

**56:50** · Yang gua sebutkan requirement-nya juga udah dikasih sama dia semuanya, ada produk, keunggulan, cara pesan, hubungi kami, click to action ke WhatsApp-nya itu dikasih. Jadi bisa langsung WhatsApp buyer, penjelasannya, gambarnya cuman ya kurang oke lah. Harga briketnya, pesan via WhatsApp ya ini masih butuh ini masih banyak butuh improvement, tapi enggak apa-apa buat awal it's okay dan langsung jadi HTML-nya. Kalian bisa improve jadiin WordPress lah, jadiin CMS yang lain atau jadiin modern JavaScript, whatever it is, bisa jadi.

### Verdict

**57:20** · Sekarang kita ke kesimpulan. Kita udah ngelakuin tes semuanya, kita udah set up banyak tadi dan mungkin video ini bakal panjang banget. Gua respect ke kalian yang nonton sampai sini. Jadi, apakah Open Cloud masih relevan untuk pekerjaan berulang yang butuh konteks, file, tools dengan model yang bisa disesuaikan di zaman sekarang di 2026. Untuk pekerjaan sederhana menurut gua iya. Untuk konfigurasi ya masih ribet seperti Open Cloud, tidak sesimpel Hermes. Kita harus banyak setup persona, memori dan lain-lain. Tapi nanti gua bakal share setup-an gua yang kemarin kalau kalian tetap mau pakai Open Cloud.

**57:49** · Kemudian tadi juga kita sudah connect-in eh ke Tailscale yang mana berjalan di atas VPS Hostinger. Kita akses dari lokal kita bisa. Kemudian kita bisa pilih model lain. Kita tadi pakai provider Open Code Go. Kita pakai GLM 5.3 dan lancar-lancar saja sampai pembuatan script konten saja. Kita sudah masukin tadi setting-an gua yang lama. Habis itu ketika kita buat website error konteksnya dan lain sebagainya, gua enggak mau banyak bahas karena gua juga bete dan itu yang ngebuat syuting gua lama hari ini.

**58:19** · Dan kita pakai Open AI dan hasilnya ya begitu. Menurut gua juga medioker tapi ya enough. Itu tergantung prompting-nya saja nanti improve-nya bagaimana.

**58:28** · Menurut gua Open Cloud ini kalian bisa pilih berdasarkan kebutuhan kerja kalian. Kalau kalian kerjanya bukan programming, cuman buat script saja, tek-tokan setiap hari, menurut gua cepat. Kayaknya kalau buat coding, hal-hal yang berat, menurut gua dengan yang gua coba tadi pilihannya cuman Open AI agak terbatas ya. Kita mau ngebuat agent yang banyak dengan model yang beda-beda juga ribet. Tapi kembali lagi ya ke pengalaman gua ya.

**58:49** · Karena dulu Open Cloud baru rilis dan gua pakai orang-orang early adopter ya, gua bisa nge-setup dia dengan baik yang mana butuh waktu berhari-hari dan begadang yang banyak untuk ngebuat script yang cocok. Tadi gua sudah contohin kan GLM 5.3 buat script saja enggak kalah sama Open AI. Jadi tergantung kita setting-nya bagaimana. Dan web export juga terbantu dalam segi coding. Dulu ya, kalau sekarang banyak tools yang lebih efektif dari tadi. Presentasi juga mungkin bisa kita buat serta masalah-masalah klien kita. Kemudian masalah provider, ya gua kan selalu ngomong ya perubahan akses provider itu perlu dievaluasi.

**59:21** · Open AI dan model China tadi ada di Open Cloud, tapi menurut gua pengalaman gua tadi sepertinya lebih condong ke Open AI yang dipakai dan gampang setup-nya. Itu aja masih error di sub agent tadi belum dikasih authentication. Ya, Open AI kita sadari ya biayanya mahal. Dan menurut gua kalau Anthropic dengan Claude-nya masih buka all out access ke Open Cloud, menurut gua Open Cloud kayaknya masih bakal tetap ramai. Karena ternyata yang pintar itu Claude-nya. Enggak enak gua ngomong gini sebenarnya.

**59:48** · Jujur ya, di kesimpulan ini memang semenjak Anthropic cabut all out-nya itu dan kita enggak bisa pakai Claude kecuali pakai API key, gua pindah ke Anthropic Claude full di situ. Pakai fitur-fiturnya Claude aja udah cukup. Dan semenjak ada Herme, gua pakai Herme buat agentic sehari-hari sama istri gua. Karena Herme ini fleksibilitasnya tinggi dan bisa disetting nine router, kita bisa setting macam-macam, enak banget. Mungkin itu kesimpulannya teman-teman. Pokoknya kalian kalau nonton dari awal sampai akhir ngertilah apakah Open Cloud masih relate di zaman sekarang ini. Kembali lagi ke kebutuhan kalian ya, teman-teman. Kemudian masalah di host-nya.

**1:00:19** · Kalau kalian tadi mau VPS atau manage setup, ya tergantung kebutuhan kalian. Tapi kalau seribet tadi sih sekompleks tadi, setting macam-macam, mendingan kalian pakai VPS deh. Bisa setting sendiri kalau kalian tekniknya bagus. Kalau kalian secara teknikal ngerti. Tapi kalau kalian kayaknya pakai manage setup tadi ya dengan keribetan tadi, kecuali kalian enggak mau ribet pakai Open AI aja udah selesai, ya manage setup kayaknya bisa. Karena infrastrukturnya udah diurus sama Hostinger. Gitu aja teman-teman. Terima kasih yang udah nonton sampai sini ya.

**1:00:45** · Lumayan panjang video ini, tapi terutama tadi kan ada ilmu tentang Tailscale itu penting banget. Kalian bisa setup VPS-VPS kalian, local machine kalian jadiin satu virtual network dan kalian bisa akses di dalam virtual network itu secara aman. Itu penting banget buat agentic AI di zaman sekarang. Dan gua ingin edukasi ini dipakai di pekerjaan nyata kalian. Kalau kalian penasaran pakai Open Cloud ya, silakan pakai aja.

**1:01:05** · Dan video ini bekerja sama dengan Hostinger, teman-teman. Jadi, jangan lupa check out VPS-nya. Pakai VPS dari Hostinger. Kalian enggak bakal nyesel karena reliable banget. Gua tadi terbukti kan, gua transfer file aja langsung pakai SCP dan enggak ada masalah sama sekali dan enggak pernah down sama sekali. Agent gua yang ada di VPS Hostinger selalu nyala, selalu enggak ada kendala. Mungkin begitu saja teman-teman kesimpulan dari gua. Terima kasih yang sudah nonton sampai sini, jangan lupa subscribe dan aktifin lonceng biar channel gua makin berkembang. Sampai jumpa di edukasi AI selanjutnya dan edukasi ini harusnya buat semua orang. Thank you.