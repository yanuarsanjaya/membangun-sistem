---
title: "TUTORIAL SETUP HERMES AGENT SAMPAI BISA DIPAKAI KERJA BENERAN"
source: "https://www.youtube.com/watch?v=hYufkXGHA6o&t=39s"
author:
  - "[[David Alfa Sunarna]]"
published: 2026-10-23
created: 2026-11-08
description: "VPS 🖥️Promo Code: DAVIDVPSLink: https://hostinger.com/davidvpsLagi ada promo Black Friday di Hostinger, pas buat mulai nyobain VPS dan Hermes Agent! Cobain buka: https://hostinger.com/idBuruan s"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=hYufkXGHA6o)

VPS 🖥️  
Promo Code: DAVIDVPS  
Link: https://hostinger.com/davidvps  
  
Lagi ada promo Black Friday di Hostinger, pas buat mulai nyobain VPS dan Hermes Agent! Cobain buka: https://hostinger.com/id  
Buruan sebelum berakhir!  
  
Besaran diskon bisa berubah tergantung kapan kalian nonton.  
  
Lanjutin tutorial Hermes Agent kemarin, kali ini naik ke model berbayar ekonomis di OpenCode Go, pasang dashboard dan Tailscale, lalu cobain buat kerja sehari-hari. Kita lihat hasil kerjanya yah! Layak gak buat kerja?  
#HermesAgent #Hostinger #9Router #AIAgent #VPS  
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
00:00 Intro  
03:20 Iklan: VPS Hostinger  
08:26 Setup Hermes Dashboard, 9Router, OpenCode Go  
17:45 Instalasi Tailscale  
22:48 Impor Konfigurasi David  
25:16 Testing: Bikin Presentasi  
32:47 Testing: Bikin Script Konten  
37:11 Testing: Coding  
39:56 Verdict

## Transcript

### Intro

**0:00** · Di video kemarin gua ngajarin kalian cara nginstal Hermes Agent terus dikonekin ke Nine Router tapi pakai tier 3 yang gratisan. Dan setelah kita coba sama-sama kemarin teman-teman lumayan frustasi ya, belum enak buat kerja sehari-hari. Jadi di video ini gua mau set up Hermes Agent dengan Nine Router yang proper buat kalian. Tapi ingat ini dis ekonomi dengan IHSG yang turun terus dan kita semua yang harus ngirit, kita tetap harus pilih model yang murah. Jadi gua mau cobain pakai tier 2-nya Nine Router yaitu model-model dari China atau provider API model yang murah.

**0:29** · Gua mau pakai Open Code Go yang mana dia punya berbagai macam pilihan model dan pilihan gua adalah nanti model LLM China. Tapi ini yang berbayar. Jadi daripada gua diprotes gara-gara video kemarin karena setengah jadi Hermes Agent-nya, "Ah, Bang David bikin video Hermes gratisan enggak bisa dipakai, mending gua beli kelas." Daripada kalian beli kelas, ya enggak apa-apa sih kalau beli kelas nanti gua dimarahin sama orang yang jualan kelas. Mending kalian lihat video gua ini aja. Gua mau set up Hermes Agent yang proper dan nanti gua kasih settingan gua juga ke kalian.

**0:58** · Dan gua mau memulai tutorial ini apa adanya teman-teman kayak biasanya. Jadi gua enggak persiapan dulu, gua enggak siapin apa-apa. Pokoknya kita maju aja, kita setting aja. Karena sayang banget kalau Hermes kemarin itu enggak dilanjutin sampai proper. Set up-nya belum beres, kualitas modelnya kita enggak tahu karena gratisan terbatas banget, batas pemakaiannya kayak apa, konteks kerjanya kita belum setting dan tools-tools apa aja yang kita perlu buat kerja di atas Hermes itu kita belum setting kemarin.

**1:24** · Padahal daya tarik Hermes Agent buat gua adalah cara dia mengolah pengalaman kerja menjadi skills dan dari histori kerja itu dia bisa jadiin prosedur yang bisa dipakai lagi. Dia ini juga punya memori untuk konteks penting dan bisa mencari percakapan sebelumnya. Kalau gua kemarin pakai Open Cloud juga frustasi.

**1:41** · Sorry ya banyak video AI gua yang frustasi karena ya ngerjain tutorialnya apa adanya. Karena gua mau ganti Open Cloud Go dan pakai GLM error terus.

**1:48** · Orang dipaksa pakai Open AI di Open Cloud. Gua mau fokus pada pendekatan Hermes sekarang. Mungkin nanti tesnya agak sama ya teman-teman. Kita cobain buat coding, kita cobain buat bikin script konten, kita cobain buat bikin presentasi. Jadi kita semua ngerti bedanya Open Cloud dan Herme Agent itu kayak apa. Dan kita mau lihat apakah Herme bisa memakai lagi pelajaran yang sudah disimpan atau memori-memori sebelumnya bisa diasah jadi skill. Jadi di video ini kalian catat ya, gua mau ngerjain satu, mengganti modelnya jadi Open Code Go di Nine Router dan gua make sure itu bisa jalan.

**2:17** · Yang kedua, gua mau Herme Agent gua ada interface-nya juga kayak Open Cloud. Jadi gua mau install Herme Agent Dashboard, ada kemarin gua cari di internet. Harusnya sih bisa dipasang. Jadi Herme Agent-nya ada dashboard-nya, Nine Router-nya ada dashboard-nya dan gua mau kedua dashboard itu bisa diakses di dalam jaringan pribadi gua lewat Tailscale selain connect ke Telegram gua. Jadi enak banget gua mantau kerja Agent gua.

**2:40** · Habis itu kita mau testing buat kerja.

**2:42** · Bisa enggak tuh Herme Agent capable enggak? Puyeng enggak kalau ganti-ganti model? Lemot enggak? Dan kalau kita berhasil melakukan ini, teman-teman, misalkan kita langganan VPS yang murah lah ya 100.000, 200.000. \[musik\] Kita langganan Open Code Go lah, 10 dolar. Ya katakanlah 200.000. Dengan uang 300 sampai 400.000, kita bisa punya AI Agent yang powerful dan bisa kita pakai buat kebutuhan kita sehari-hari.

**3:03** · Dan itu Agent-tic loh, bukan kayak kita langganan GPT Go yang 70.000-an atau GPT Plus yang 300.000-an something, itu beda. Ini kita punya VPS sendiri, kita punya Herme Agent, kita punya model yang jalan 24 jam 7 hari. Jadi biar kita enggak penasaran, ayo kita mulai aja pelajaran hari ini, Guys.

### Iklan: VPS Hostinger

**3:22** · Seperti biasa, yang pertama kita butuhkan adalah VPS. Kalau kalian sudah lihat video gua yang sebelumnya, gua pakai VPS dari Hostinger. Dan sekarang juga sama, ada pesan sponsor dulu.

**3:32** · Kalian bisa langsung ketik aja hostinger.com davidvps. Orang yang guru SMK kayak gua enggak pernah berpikir ada di titik hidup namanya ada di hostinger.com/davidvps.

**3:42** · Kalau Marques Brownlee okelah udah influencer HP terkenal, mungkin ada spesial link dia. Nah ini gua loh, David. Makanya kalian buka URL ini aja, teman-teman, bakal langsung ke landing page VPS-nya Hostinger. Ini kondisi gua udah login ya, teman-teman. Jadi ada akun gua di sini. Kalian bisa login juga, bisa pakai Google, bisa username password, macam-macam cara login ke Hostinger. Kemudian kita bisa pilih paket. Tadi di awal gua bilang ya budget VPS bisa 100 ribu sampai 200 ribuan dan itu benar. Walaupun sekarang gua pakai KVM 2 dari Hostinger yang mana 2 CPU core dan 8 giga RAM.

**4:13** · Tapi kalian kalau mau pakai yang KVM 1, 1 CPU core dan 4 giga RAM juga cukup. Kalau memang Hermes Agent plus Nine Router kalian tidak dipakai buat Agentic yang berat banget.

**4:25** · Yang berat banget tuh kayak apa sih, Bang David? Misalkan buat konversi video ke teks. Jadi dari video diubah dulu ke audio, dari audio di-decode lagi pakai audio capture sehingga bisa jadi teks, bisa jadi script. Itu berat. Atau dipasangin Blender yang versi terminalnya, versi command line-nya.

**4:42** · Terus kalian connect-in ke GPT-6 Astra, misalkan. Terus buat render 3D di situ.

**4:46** · Nah, itu berat. Jadi kalau cuma tugas sederhana buat kalian ngerjain tugas kuliah, ngerjain tugas kantor, nganalisa dokumen, dan kalian mau itu aman, ada di server kalian sendiri ya pakai VPS yang KVM 1 cukup. Kebutuhan office kantor itu udah cukup banget. Mau ngapain sih?

**5:02** · Kalau heavy usage kayak gua ya, gua KVM 2. Misalkan kita pilih KVM 1.

**5:08** · Harganya yang 24 bulan 3,3 juta, 2 tahun ya. Kalian bisa pakai kode promo David VPS langsung dapat diskon 300 ribu, which is 10%. Kalau paket yang 12 bulan sama aja dapat diskon 10%. Jadi 1,8.

**5:23** · Kalau mau paket yang 1 bulan, misalkan tanpa promo dulu ya, itu ada di 190-an ribu. Jadi tadi gua bilang 190 ribu buat VPS terus Open Code Go-nya 10 dolar jadi 200 ribuan. Jadi sekitar 400 ribu kalian spend buat kalian punya AI Agent yang bener-bener Agentic ya, teman-teman ya.

**5:40** · Nyala terus dan kalian bisa akses dari HP kalian, dari browser. Nanti gua install-in dashboard dan ini berbeda dengan langganan AI biasa. Misalkan kalian langganan Open AI atau ChatGPT yang Go 70.000 atau yang Plus 300.000-an memang bisa kalian konekkan juga ke Herma Agent kalian. Cuman yang pertama pasti account-nya rawan disuspend. Udah kita brutaly aneh saja. Jadi itu beda.

**6:03** · Kalian bisa ganti model macam-macam dan bisa cobain macam-macam. Kalau kalian udah beli VPS di Hostinger, kalian bakal dapat dashboard-nya. Bisa lihat statistiknya, CPU, traffic masuk, traffic keluar, penggunaan memori, sisanya berapa, bandwidth-nya berapa.

**6:16** · Dan di tutorial ini harus pakai VPS ya teman-teman. Gua jujur dari awal. Kenapa ya kita mau instal Tailscale, kita mungkin mau instal tools-tools lain nanti yang membantu pekerjaan kita dengan Herma Agent, kita mau setup main router kita. Jadi ya untuk fleksibilitas yang tinggi ya pakai VPS. Bang, misalkan gua enggak ada uang, gua pakai laptop saja, enggak harus nyala terus enggak apa-apa. Ya enggak apa-apa. It's okay.

**6:37** · Yang penting ada kemauan dan mau belajar. Bang, gua ada mini PC, gua mau nyalain terus. Gua Bang, Bang, gua ada Mac Mini, gua juga mau nyalain terus. Ya enggak apa-apa. Instal di situ juga enggak apa-apa. Cuman kan budget-nya lebih ya kalau mini PC atau Mac Mini.

**6:48** · Asalkan komputer yang bisa stand alone kayak harga IHSG yang diturunkan MSCI jadi stand alone. Aduh, masuk lagi.

**6:56** · Ah, enggak apa-apa. It's okay. Kita belajar sama-sama di sini teman-teman.

**7:00** · Enggak harus canggih. Tapi kalau kalian ada budget dan ingin fleksibilitas yang tinggi dan ingin belajar lebih, beli VPS paling top. Dan kalau kalian pakai VPS Hostinger, kalian bisa langsung buka terminalnya di browser teman-teman. Beh, langsung kan enggak perlu pakai terminal. Misalkan ketik SSH root @ IP address. Enggak perlu begitu.

**7:20** · Jadi kalian simpel pakai browser sambil bisa ngerjain yang lain dengan kapabilitas yang sama seperti pakai terminal. Dan kalian kalau udah buka ini, mau keren? Mau keren banget enggak?

**7:29** · Gua kasih tips nih. Misalkan kalian lagi kuliah nih, kalian duduk paling depan, pastiin ini layar laptop kelihatan semua sama teman-teman kalian yang di belakang atau pamer-pamerin angkat-angkat saja begini. Pastiin dosen kalian ngerti kalian duduk depan, terus kalian ketik komen ini. Kalian ketik htop. Anjay hacker. Hacker bro. Padahal ini cuma task manager-nya Linux atau Ubuntu. Di sini terlihat kan gua ada dua CPU dan memori gua kepakai berapa. Kalian buka ini udah paling top kalian. Top top.

**7:55** · Teman kalian lihat, anjay si David masih kuliah udah jadi hacker. Bab. Gokil.

**8:00** · Kalian di kantor, kalian buka ini, udah kalian fix jadi bocil kematian hacker mengerikan. Kalian pakai topeng anonymous tuh. Layak kalian layak.

**8:08** · Setelah kalian buka terminal begini, saatnya kita set up Herme Agent kita.

**8:12** · Bentar gua ajarin cara keluarnya.

**8:14** · Control C aja, control C. Nanti bisa masuk atau bingung, enggak bisa keluarnya.

**8:20** · Control C control C control C. Wih, udah keluar. Oke, langsung kita set up Herme Agent kita.

### Setup Hermes Dashboard, 9Router, OpenCode Go

**8:28** · Oke teman-teman, karena gua udah lama enggak pakai VPS ini dan ini VPS buat ngajarin kalian, bukan VPS pribadi gua.

**8:35** · Gua mau cek konfigurasi Nine Router-nya dulu. Kan lama enggak dibuka. Wajar dong. Kita ketik Nine Router ya, coba ya. Kita buka web UI-nya. Oke, masih menyala. Hide to tray background. Jadi tadi cara hide to tray-nya teman-teman, gua lupa ngajarin. Tadi dipencet lagi enter.

**8:52** · Gua contohin lagi deh ya. Nah, tadi kan gua web UI open in browser. Nah, jadi kan enggak bisa digoyang-goyang nih.

**8:58** · Kalau ketik kok digoyang-goyang. Enggak bisa diganti menu lagi nih. Misalkan kalian ketik panah bawah nih enggak bisa. Jangan panik. Ini kan press enter to go back to menu. Berarti lu enter lagi. Nah, menunya jadi bisa dipilih lagi. Kemudian hide to tray. Kalau kemarin gua contohin pakai Termux.

**9:14** · Karena gua enggak mau ribet, gua pengin punya session satu yang aktif dan khusus menjalankan Nine Router. Tapi kemarin ada yang protes di komen gua. Bang, itu kan bisa hide to background. Ya udah, gua turutin. Biar gua enggak diprotes.

**9:26** · Maaf ya, namanya juga manusia. Kadang juga salah. Kita kan tutorial apa adanya. Masukin password yang lama. Oke, masih connect. Ini Nine Router proxy gua teman-teman, masih berjalan seperti sedia kalanya dan gua mau cobain connect-in ke Open Code Go yang pertama gua buka Open Code Go gua dulu, gua login, monthly limit reach, aduh, baru juga ngajarin biar murah, ya sudahlah, yang penting API key-nya yang lama kita hapus dulu deh yang buat Open Cloud dia makan mulu nih.

**9:56** · Remove, remove service account, karena monthly usage gua sudah habis, ternyata Open Code Go tidak sebanyak itu limitnya, baru mau ngajarin.

**10:08** · Sudah disuruh top up lagi, ya sudah enggak apa-apa demi kalian teman-teman, gua bakal top up Open Code Go yang 40 dolar. Kalau kalian masih mau ngakalin Open Code pakai yang gratisan kan banyak tuh, sekarang misalkan GLM 5.3 flash mereka, kemarin mereka baru announce di X itu gratis, silakan enggak apa-apa teman-teman, tapi demi berjalannya tutorial ini dengan lancar kita butuh pelicin yang namanya duit, oke? Kalau kemarin gua chat GPT keluar 100 dolar, ini keluar lagi 40 dolar, enggak apa-apa demi kalian, demi kalian.

**10:36** · Awas saja ads-nya enggak tembus ya, gua mau upgrade to Go Plus, 40 dolar, sekitar mungkin ya 600 sampai 700 ribu, gila kayak hidup cuma buat bayar AI kita, upgrade to Go Plus, bodo amat. Eh, kartu gua enggak bisa bentar-bentar sabar sabar sabar, oke sempat ada masalah di kartu kredit gua tadi teman-teman, kayaknya bini gua belanja kebanyakan, padahal limitnya sudah ratusan juta damn, enggak usah dibuka oversharing, gua sudah benerin kartu gua, coba kita upgrade ke Go Plus ya, confirm upgrade, ya bisa, huh, akhirnya spending gua

**11:08** · untuk AI banyak banget, jadi kalian bayangin saja teman-teman, gua Claude gua max plan yang 20 X 200 dolar, belum tim gua, kemudian ada chat GPT, gua pakai yang pro 100 dolar. Ini langganan lagi Open Code 10 dolar, belum mainan yang kecil-kecil yang lain ada Mini Max, habis duit kita buat langganan AI, tapi enggak apa-apa biar video ini lancar gua tetap langganan dan gua mau tunjukin ke kalian kapabilitasnya Open Code Go. Dan gua enggak di-endorse sama Open Code Go, keluar duit yang ada. Langsung aja kita set up API key-nya, teman-teman.

**11:37** · Service account, add erme, agent David, permission all, allowed IP address. Gua mau pakai IP address-nya VPS gua. Oke, ini key-nya. Setelah key-nya kita simpan, kita balik lagi ke Nine Router, teman-teman. Terus kita pilih provider.

**11:54** · Kalau kita lihat Open Code Go enggak ada di sini. Di mana dia ada? Kita scroll ke bawah show all 39 provider. Kita pilih Open Code Go. Kita add connection aja.

**12:08** · Name Open Code erme David API key yang tadi, kita cek dulu ya. Valid.

**12:17** · Proxy pool-nya non aja. Kita enggak buat proxy pool juga. Ada settingan di sini proxy pool.

**12:23** · Forget about it. Priority one, save.

**12:27** · Oke, pastikan ada model yang mau kita pakai. GLM 5.3, GLM 5.3 flash, Queen 3.7, Max plus 3.8 Max, oke. Good.

**12:38** · I think it's enough. Kalau kita buka halaman Open Code Go di sini, dia ada apa aja sih? Kimi GPT-nya Six Luna doang.

**12:48** · Oh, adanya Haiku aja. Ya udah, enggak apa-apa. Kita pakai yang ini aja sudah cukup. Deepseek-nya ada yang pro enggak?

**12:55** · Oke, ada V4 pro. Oke, that's enough.

**12:59** · Combo yang lama kita hapus. Yang pertama untuk vision dan audio, kita harus add model. Dari Open Code Go ada GLM 5.3 flash. Terus yang untuk audio, enggak ada sih.

**13:11** · Di Open Code, enggak apa-apa. Vision aja, bisa ngebaca gambar dan lain sebagainya. Koreksi kalau gua salah ya.

**13:16** · Kemudian kita buat combo, David combo baru. Add model dari Open Code Go.

**13:23** · Teman-teman, gua suka GLM. Gua pakai GLM, enggak apa-apa dong. Terus backup-nya gua mau pakai Queen 3,8 Max.

**13:31** · Dah. Ini aja sudah cukup. Sudah, create.

**13:34** · Kita pakai fallback dulu ya teman-teman ya. Karena gua mau fokus pakai GLM 5.3, gua mau fokus ini jalan. Jadi enggak round robin, rotate, enggak fusion, panel plus judge. Eh, gua mau fallback dulu yang gampang dan simpel. Nanti yang lain kalian bisa coba sendiri. Gua mau coba setup ulang Herme gua teman-teman.

**13:51** · Jadi Herme setup. Would you like to see what can be imported? Yes. Proceed with migration, gua enggak ngerti gua pilih no dulu.

**14:00** · Quick setup, full setup, blank state.

**14:02** · Eh, gua full setup dulu. Gua mau cek lagi konfigurasi Nine Router gua yang kemarin. Kalau kemarin gua pakai Herme combo kan gua sudah delete. Sekarang ada David combo baru. Gua mau ganti jadi David combo baru.

**14:14** · Terus gua mau pakai XH atau medium ya?

**14:17** · Medium aja ya teman-teman ya. Karena gua pakai Open Code Go yang 40 dolar, kayaknya medium cukup deh. Enggak usah ribet-ribet. Medium. Select terminal backend, keep current, local. Lu mau ada platform untuk configure, Telegram aja sudah cukup deh. Sudah enter aja.

**14:30** · Reconfigure Telegram, no. Restart the gateway to pick up changes, yes. Kita tunggu konfigurasi barunya selesai. Jadi jangan lupa tadi teman-teman, kita ketik lagi Herme setup, enggak usah import konfigurasi lama, terus setup ulang Nine Router-nya. Pilih combo yang baru yang tadi kita sudah set. Jangan lupa. Ini suruh milih tools lagi untuk menavigate, sudah enter aja. Ngikut default-nya aja.

**14:53** · Browser-nya sesuai dengan rekomendasi dia aja. Free local cloud, new sota web harness, gua juga enggak ngerti apa.

**14:59** · Mungkin bisa googling lagi nanti. Kita default dulu ya. Oh, bentar bentar. Ada local browser. Pilih ini aja dulu. Eh, pakai chromium aja. Headless chromium lebih oke. Ini buat image generation ya.

**15:10** · Ehm, kita pakai default dulu. Kita skip dulu ya. Configure later ya. Ya, ini default aja lah.

**15:17** · Text to speech-nya.

**15:19** · Sudah kita default-in dulu aja semua.

**15:21** · Login to, oke.

**15:23** · Satu-satu teman-teman kita baca ya. Tadi ada browser automation, gua pilih chromium browser free. Computer use, driver-nya udah ada. Image generation gua skip. Text to speech, Microsoft Edge TTS no configuration needed. Web search-nya, extract-nya gua pakai DuckDuckGo default-nya. Login to NOSS portal, yes. Login dulu pakai punya gua yang kemarin, oke. Masukin kode.

**15:46** · Connect, waiting for approval, oke.

**15:50** · Udah ke-approve. Ya, udah selesai teman-teman. Setup complete. Nah, ini ada banyak command yang harus kalian simpan nih. Gua mau screenshot aja, biar kesimpan. Jadi kayak ada Herme setup, Herme setup model, terminal, gateway tools, config, config edit, set gateway doctor. Dah, gua mau ketik Herme. Mau chatting sama dia. Anjay, keren banget.

**16:09** · Sekarang kamu pakai model apa? Ya, benar. David combo baru. Ini juga udah berjalan open code go-nya. Coba kita cek di Telegram ya. Kamu apakah online lagi sekarang? Dan router gua nyala, open code go.

**16:25** · Oke.

**16:27** · Good. Kerjaan udah pada balik teman-teman. Herme yang di sini juga udah bisa diakses. Sekarang gua mau install Herme dashboard, ya teman-teman ya. Kalau kita searching Herme dashboard itu apa, Herme web dashboard. Nah, gua pengin banget sebenarnya ada ini di Herme gua dan gua bisa akses di manapun melalui jaringan Tailscale gua. Tapi yang pertama kita install Herme web dashboard dulu. Bukan kita install ya, apakah udah terinstall ya teman-teman?

**16:51** · Kayaknya bisa langsung dijalanin deh.

**16:52** · Building web UI, kita tunggu aja sampai selesai. Tadi ketik Herme dashboard aja ternyata teman-teman. Sepertinya ini command standar mereka terus di-build-in UI sama mereka. Dan kita tinggal tunggu aja sampai selesai. Herme dashboard-nya sudah jadi teman-teman dan ini bisa jalan di lokal gua karena gua pakai port forwarding. Tadi gua coba langsung tembak IP VPS-nya enggak bisa, jadi gua pakai port forwarding. Command-nya kayak kemarin yang gua ajarin di Open Cloud gua, teman-teman. Jadi, SSH -n -l port gua di sini, terus gua mau forwarding ke port lokal gua yang ini.

**17:25** · Kemudian root, kemudian IP VPS-nya. Dan kalian kalau ngelihat tutorial Open Cloud gua kemarin, kalian ngerti banget ini enggak scalable, ini enggak bisa diakses kapan pun, atau bahkan kalau IP-nya terekspos seperti ini, ini bahkan bisa diakses orang lain. Dan ini males juga kalau selalu port forwarding. Jadi, kita perlu instal Tailscale di sini.

### Instalasi Tailscale

**17:47** · Caranya bagaimana instal Tailscale? Ya, tanya AI agent-nya aja, enggak usah repot. Aku mau kamu instal Tailscale di server ini, karena aku ingin bisa akses Hermit Dashboard, kita kasih URL-nya, dan Nine Router Dashboard. URL lokalnya udah gua kasih semua. Di jaringan Tailscale aku. Tolong kamu kerjakan ya, dan sekalian setup.

**18:18** · Udahlah, prompting tuh zaman sekarang enggak usah canggih-canggih. Udah canggih AI-nya.

**18:24** · Kita coba ya, bisa apa enggak ya? Gua juga deg-degan nih. Pertama kali pakai GLM soalnya, di atas Nine Router. Enter aja dah. Oke, kita pantau Nine Router kita. Open Code-nya selalu jalan.

**18:35** · Berapa usage-nya? Usage-nya belum kepakai, masih aman, Guys. Sepertinya banyak usage-nya. Ini jalan terus. Oke, saya kerjakan.

**18:44** · Alright, Tailscale sudah terinstal, sudah terinstal aktif, dashboard jalan normal. Sekarang setup Tailscale serve untuk keduanya. Oke, kita tunggu ya, teman-teman ya. Ini sih cepat juga sih, teman-teman sih. Enggak lambat sih. Gua nyuruh dia konfigurasi Tailscale ya, tadi jam berapa?

**19:00** · 21.35, sekarang 21.41. Cuman butuh 6 menit. Oke banget loh, GLM 5.3 loh, pakai medium, di atas Open Code, dan itu murah. Limit yang terpakai sekitar 2%, which is okay, no problem menurut gua.

**19:13** · Dan dia di reset setiap 45 jam. Dan kalau teman-teman tanya, "Bang, kok beda ya sama setup yang open cloud kemarin tailscale-nya?" Karena ini server yang sama dengan open cloud kemarin, teman-teman. Kebetulan gua belum ganti server. Jadi enggak ada URL, lu buka URL ini terus konekin ke akun tailscale lu kayak kemarin itu udah enggak ada. Dan udah langsung live, teman-teman bisa lihat. Gua coba konekin tailscale gua dulu. Ini IP-nya VPS gua yang ada di tailscale. Kalian enggak bisa akses juga, cuman bisa diakses di jaringan gua. Kemudian gua buka coba. Ada login-nya, Guys.

**19:46** · Nice. Wow. Sudah terkoneksi. Login-nya David, password-nya file di atas. Ya, ini buat keamanan ekstra, teman-teman. Sebenarnya kalian juga enggak bisa akses URL ini anyway. Cuman kan daripada daripada ya.

**19:59** · Sign in pakai password.

**20:03** · Cihuy sekali, teman-teman. Bisa diakses pakai URL. Cakep sekali. Bisa diakses di HP, di laptop gua, di Mac Mini gua asalkan terkoneksi dalam satu jaringan tailscale yang sama. Kita coba nine router-nya ya. Nine router-nya enggak pakai HTTPS. Aman. Nine router-nya juga ada password-nya kok. Oke, gua gatal nine router-nya mau pakai HTTPS. Ya, tapi kata dia aman sih. Udahlah enggak usahlah. Yang penting bisa kita pakai dan kita doang yang bisa pakai. Oke.

**20:33** · Jadi, kedua tools gua dengan memakan 2% limit di Open Cloud Go yang $40, gua sekarang sudah punya dashboard nine router yang terkoneksi dengan tailscale gua dan bisa gua buka di mana saja. Gua sudah punya Herme Agent dan dashboard-nya yang bisa gua buka di mana saja. Enggak percaya? Ya udah. Gua ambil HP nih, gua instal tailscale. Open. Oke.

**20:57** · Get started. Login pakai Google. You're about to connect the device S26 Ultra milik David Alpha 1 tera cash enggak nyicil. Waduh. Connect.

**21:07** · Login successful. Continue. Allow Tailscale to send you notification, allow deh. Oke, sekarang gua buka URL-nya. Tuh, ada, tinggal login. Ini Herme dashboard-nya, ini Nine router-nya. Oke, Nine router-nya juga bisa. Udah ya, terbukti ya. Kita lanjutin di desktop aja ya. Yang penting di HP juga udah bisa kita akses. Selain daripada Telegram-nya juga kita udah bisa akses. Enak banget ya, asal terkoneksi ke jaringan Tailscale yang sama. Tapi kalau Telegram enggak usah pakai Tailscale ya, teman-teman. Karena dia pakai hook Telegram sendiri.

**21:37** · Dah, cukup yang dari handphone. Sekarang kita balik ke Herme dashboard. Ada apa aja sih di Herme dashboard sebenarnya, teman-teman?

**21:45** · Ada chat, kita bisa buat session chat di sini. Kita bisa tahu session kita apa aja di Telegram, kemudian di CLI ada beda recent session-nya. File-nya apa aja di root kita, modelnya kita pakai David combo baru. Terus kita bisa tadi set up, ada compression, ada macam-macam deh kita bisa beda-bedain. Gua pakai auto semua, terus mixture of agent. Yang penting terkoneksi dengan baik, terus ada log-nya, ada cron, ada skill, ada plugin, ada MCP.

**22:12** · Kita bisa connect-in ke apapun yang kita mau connect-in. Ada channel Telegram yang udah aktif, ada webhook-nya, ada pairing ke mana aja, profile, config, key-nya kalau kita mau langsung login, system buat set up, kemudian documentation. Enggak bisa dibuka gara-gara Tailscale pasti. Plugin Kanban, oh buat kerja ini. Achieve man.

**22:35** · Banyak yang bisa kita explore nanti satu-satu aja, teman-teman. Dan gua penasaran ingin coba kerja langsung pakai Herme agent yang udah kita set up ini. Hasilnya kayak apa, apakah bagus, apakah capable buat kita kerja sehari-hari ya tentunya capable banget.

### Impor Konfigurasi David

**22:50** · Oke, teman-teman. Sebelum kita mulai bekerja menggunakan Herme agent, sepertinya gua harus mengimpor konfigurasi lama gua ke dalam Herme agent ini biar enak kerjanya. Kalian juga kalau punya backup kerjaan atau dari agen lain, mau pindah ke agen yang baru, baiknya ya impor aja kerjaan yang lama. Yang gua lakukan adalah di folder root workspace David, kalau kalian lihat video open cloud gua yang kemarin, itu ada konfigurasi open cloud gua.

**23:12** · Jadi gua bilang ada backup open cloud aku yang lama, mungkin tidak akan merepresentasikan kerjaan terbaru aku, tapi dari data data itu kamu bisa pelajari siapa aku, sambil kamu cari di internet juga apa saja bisnis aku, bagaimana cara aku coding, bagaimana cara aku membuat script konten persona AI dan apa yang aku mau, kamu bisa import konfigurasi tersebut yang menurut kamu butuh ke konfigurasi Herme. Kita enter aja ya, eksekusi. Enggak enak ya pakai ini? Menurut gua enakan pakai Telegram deh. Selesai bro, semua sudah kebaca dari 101 file backup langsung jadi cowok agennya. Wes, mantap.

**23:47** · Bisnisnya web ekspor, harganya 1 juta setahun, 12.000 website. Yang sudah di import ke Herme user profile, skill baru David content script. Wes, dia buat skill baru nih, ini kerennya Herme. Auto load tiap lu minta script konten isinya hard low script dan lain-lain, memory notes, lokasi arsip backup, inside bisnis kunci, nice. Yang sengaja tidak ku hitung ya folder secret env good.

**24:10** · Oke, gua pindah ke Telegram aja teman-teman ya, pusing. Tadi gua juga nyobain pakai Telegram dia bisa deteksi image enggak? Ternyata bisa, jadi vision-nya GLM 5.3 vision-nya udah jalan. Aku mau tes ya kerjaan yang tadi. Tadi aku habis import konfigurasi Herme di sesi chat. Coba kamu periksa masuk atau enggak. Gua cek dulu di Telegram. Alright, konfigurasi open cloud gua yang lama gua udah masukin dan udah jalan di sini, kayaknya dia udah tahu.

**24:42** · Gua udah cek-cek kalau aku buat script konten kamu udah ada formulanya kan? Coba aku mau tes memory kamu. Yes, udah ada skill-nya udah masuk David content script. Udah ada bro. Skill David content script udah kepasang dari hasil import. Alright, sekarang kita lanjut kerja ya teman-teman. Gua mau coba membuat presentasi mungkin sederhana dulu dua slide lah ya buat ngelihat hasilnya kayak apa sih dan gua mau compare sama Claude desain gua yang sering gua buat presentasi, apakah dia bisa bersaing dan dia bisa menghasilkan sesuatu yang bagus juga di bidang presentasi. Let's go.

### Testing: Bikin Presentasi

**25:18** · Untuk membuat presentasi teman-teman, gua tuh punya desain sistem Web Export desain sistem gua namakan. Dan ini gua buat ya lumayan susah ya. Ini desain sistem yang mengatur gimana sih color paletnya Web Export, font-nya, styling-nya semuanya ada. Dan gua masukin ke dalam repo ini teman-teman.

**25:36** · Jadi desain sistemnya dalam bentuk source code sehingga simpel. Gua mau coba import ini ke dalam Herme agent gua biar dia ngerti kalau gua buat presentasi, gua selalu pakai desain sistem ini. Coba ya. Sekarang aku ingin atur cara kamu membuat presentasi.

**25:53** · Selain daripada memori yang aku import tadi, aku selalu pakai panduan yang ada di sini. Coba kamu pelajari ya, bisa clone, nanti aku yang login. Pelajari dan catat desain lainnya.

**26:13** · Oke, biar dia pelajari desain sistemnya Web Export dulu teman-teman. Dia mau clone, tinggal gua kenain ke GitHub gua.

**26:19** · Dia mau install dulu terus kasih ke gua panduan login-nya. Gua setup dulu GitHub, login sukses sebagai David Alfath karena gas clone repo desain sistem. Oke, kita tunggu aja. Desain sistem sudah masuk teman-teman. Kemudian aku mau satu kali prom lagi. Kalau kamu sudah mengerti desain sistem yang aku mau, sekarang aku minta kamu siapin dulu. Oke.

**26:47** · Biar dia belajar dulu tools skill apa di Herme yang dia butuhin buat ngebuat presentasi atau slide dengan output PDF.

**26:54** · Kalau enggak nanti lama soalnya. Nanti dia cari tools ini, tools itu. Dia enggak siapin dulu. Tuh, contohnya.

**27:01** · Dia langsung pasang skill PowerPoint.

**27:03** · Jadi, kita tunggu aja lagi teman-teman.

**27:04** · Ya, banyak nunggu ya enggak apa-apa namanya juga kita lagi tutorial ya. Oke, sekarang dia sudah siap dan punya semua tools untuk membuat presentasi. Ini yang harus gua tekankan ke teman-teman. Jadi, ketika kita set up AI agent dengan suatu tujuan tertentu, make sure dia punya semua bekal yang kita butuhkan untuk membuat presentasi. Jangan sampai nanti ketika buat hasilnya jelek, kalian marah-marah ini modelnya jelek nih, agent-nya jelek. Padahal kalian sendiri yang enggak bisa set up-nya. Nah, kalau kalian buat presentasi, kalian ibaratkan diri kalian, kalian butuh apa aja. Oh, gua butuh desainnya kayak gini.

**27:35** · Gua butuh arahannya kayak gini. Ya, masukin, jelasin. Jangan malas. Ya, kalau malas ya, lu enggak ada bedanya sama AI slop.

**27:43** · Otak lu yang jadi slop cuma diganti AI doang. Ya, kayak gua tadi. Gua impor settingan gua yang lama. Gua masukin desain sistem yang sudah gua buat. Gua terus tanya ke dia lagi, lu butuh apa lagi? Lu instal dulu dah. Ya, begitu. AI itu cuma eksekutor. Otaknya ada di kalian. Ya, kalau otak yang ini nge-slop ya, ini hasilnya slop juga. Itu sekedar saran dari gua ya. Oke, sekarang gua mau bandingin sama Claude Design. Kebetulan gua lagi ada kerjaan teman-teman. Karena ini tutorial enggak ada persiapan, kita langsung to the point aja. Gua habis ngebuat presentasi tentang caranya berkonten. Jadi, gua mau suruh dia ngebuat presentasi yang header-nya aja.

**28:16** · Kemudian yang ini attention game ini aja weh. Keren. Coba keren mana ya? Kita mau coba ya. Oke, ini aja. Aku ada tugas ngisi acara. Coba kamu buat header-nya saja. Judul slide-nya saja yang bagus dengan desain sistem web ekspor. Kemudian slide kedua. Ada 14 slide dengan besar. Ingin aku masukkan gambar 4 influencer yang paling berpengaruh. Kemudian di tengahnya overlay image itu ada tulisan besar attention game.

**28:47** · Poinnya menunjukkan kalau konten itu ya attention game, mereka harus ngerti itu dulu. Sudah, coba buat dua slide saja dulu, langsung jadi PDF ya. Oke, coba kita bandingin sama Claude Code tools yang sudah matang tapi harganya mahal banget. Ya, Claude dengan desain sistem gua kalau ngebuat dan prompting revisi-revisi dari gua ya pasti jelas bagus banget. Sudah kita jujur saja, kita pastikan buat PPT atau presentasi sekarang kan pakainya AI. Tapi hasilnya jangan AI selop dong.

**29:15** · Jangan kayak buatan baby boomers yang pakai chat GPT Go, jangan. Harus bagus kayak gini.

**29:23** · Pakai desain sistem, pakai tools yang benar. Sekarang kita tunggu dia kerja sampai jadi. Kita juga penasaran kayak apa pastinya. Sudah jadi guys, coba kita buka.

**29:32** · Bagus loh, enggak jelek loh. Tuh misalkan Mr. Beast, Khabane Lame, PewDiePie, Charli D'Amelio attention game. Konten itu ya attention game, pahamin dulu sebelum apa-apa. Konten creation the new gold mining, enggak jauh beda sih.

**29:46** · Dan ini tinggal diganti warna merah, digelapin lagi, oke. Jadi teman-teman, kalian enggak harus langganan kayak misalkan Claude yang mahal banget ataupun chat GPT yang 100 dolar. Kalian bisa akalin segala sesuatunya secara ekonomis, pilih VPS yang murah, pilih model yang murah. Mungkin ada yang lebih murah dari Open Code Go dan kalian bisa mungkin komen di sini yang lebih murah, yang lebih worth it apa. Asalkan modelnya bagus dan menurut gua sekarang model tuh sudah bersaing ya. Jadi kayak lu enggak usah bingung lagi yang bagus Queen apa, apa, apa, apa, sama saja semuanya. Yang membedakan tuh apa?

**30:17** · Tadi gua sudah bilang ya, lu punya peralatan yang cukup enggak buat ngerjain suatu tugas tersebut. Kalau lu buat presentasi, lu punya desain sistemnya enggak coba? Dia mau pakai font apa, referensi desainnya kayak apa, warnanya kayak apa, lu punya enggak semuanya?

**30:32** · Terus lu sudah siapin dia belum secara proper buat ngebuat presentasi? Tadi kan gua sudah siapin, terus dia ngerti enggak persona lu siapa? Dia ngerti enggak lu kerja di mana? Dia ngerti enggak tujuan lu buat presentasi itu apa? Itu yang membedakan, teman-teman.

**30:45** · Jadi ya hasilnya kayak gini bakal tetap bagus. Ini gua cuma sekali prompting loh. Sekarang gua mau buat ini lebih scalable. Kalau kamu bolak-balik biar aku bisa preview hasilnya dan kasih ke kamu secara cepat. Jadi gua mau mereplikasi cara kerja Claude Code yang canggih ini yang bisa langsung jadi hasilnya di kanan. Coba bisa enggak dia kerjain pakai apa dia? Biar dia aja yang mikir.

**31:12** · Kita tunggu lagi. Ada caranya biar bisa review desainnya secara cepat. Dia kasih solusi ke kita. Kan ini sudah connect ke Telnet. Lu bisa buka URL preview-nya buat desain. Ya sudah gua buka aja.

**31:23** · Slide 1, slide 2. The best. Dengan adanya ini lu bisa langsung revisi secara cepat tanpa dia harus output PDF dan bisa langsung diunduh PDF terbarunya. Lu sudah mereplikasi Claude Design yang harganya mahal. BTW kalau kalian langganan Claude 300.000 itu enggak akan pernah cukup. Jadi minimal 100 dolar, gua langganan 200 dolar.

**31:42** · Kalian sudah mereplikasi Claude 100 dolar, 200 dolar ke sistem yang hanya 400.000-an. Wow, itu suatu prestasi loh.

**31:48** · Bahkan kalau kalian pilih option-option yang lebih murah lagi VPS-nya, modelnya mau kalian murahin lagi. Mungkin 200.000. Kalian sudah bisa replicate kemampuan Claude Design jadi AI. Itu yang penting apa? Ngerti tools-nya dan tahu cara makainya. Ini yang mau gua tekankan di tutorial ini, teman-teman.

**32:05** · Murah juga bisa bagus. Kalau kalian ngerti Telnet, kalau kalian ngerti prompting-nya bisa direplikasi semuanya.

**32:11** · Pinter kok dia itu. Oke, sudah sampai situ aja, teman-teman, untuk yang presentasi. Jadi kesimpulannya ya impor setting gua yang lama dari Open Cloud, agent ini ngerti siapa persona gua.

**32:21** · Dengan adanya desain sistem yang jelas jadi agent ini bisa ngebuat presentasi yang desainnya konsisten. Kemudian dengan adanya tools yang sudah disiapkan sebelumnya untuk membuat presentasi sehingga cepat dan prompting yang jelas dari gua Hermes Agent ini dengan Nine Router yang mana gua pakai open code bisa menghasilkan presentasi yang sangat bagus menurut gua. Ini belum gua improve loh. Jadi kalian juga bisa pakai di rumah, bisa coba sendiri.

### Testing: Bikin Script Konten

**32:48** · Oke, sekarang kita ke next testing. Gua mau coba nge-generate script konten untuk kebutuhan gua sehari-hari. Kita mulai aja. Untuk mulai membuat konten, gua kasih prompt. Sekarang tugas selanjutnya membuat script konten. Aku ingin kamu siapkan apa saja yang dibutuhkan untuk membuat script konten.

**33:04** · Kirim output-nya berupa docx. Oke, kita tunggu sampai selesai as usual, teman-teman. Karena dia butuh proses untuk berpikir dan melakukan research tentunya. Sudah jadi script-nya, teman-teman. Jadi alur kerja dia adalah dia me-load skill David content script yang tadi kita set up awal ya. Sudah tahu ya tadi set up-nya ya. Kemudian dia research AI Indonesia 2026 gimana, strategi nasionalnya gimana, dia compare dengan keadaan di Silicon Valley US.

**33:35** · Terus dia resume hasil research dia apa aja isinya. Kemudian kita bukalah, gua penasaran. Tahun bukan bulan, setahun. Big Tech Silicon Valley bakal belanjain lebih dari 1 triliun dolar untuk AI tahun ini 2026. Apa sih enggak jelas nih hook-nya. Setahun bukan bulan, setahun. Buang ke berapa dan itu cuma biaya fisiknya. GPU, gedung listrik, penggunaan bukan kurang sih. Kurang. Jujur kurang.

**33:59** · Bahasanya sih. Kita harus kasih revisi ke dia. Bahasa Indonesia kamu sangat berantakan. Tidak layak untuk disebut script yang proper. Coba kamu pelajari bagaimana cara berbahasa Indonesia dulu.

**34:14** · Dengan baik terlebih dahulu. Pasang atau apapun yang kamu butuhkan biar bisa berbahasa Indonesia yang baik. Last bahasa Indonesianya. Ya ginilah sama agent. Setiap hari ya gua juga begini.

**34:28** · Kalau dia jelek ya gua marahin aja. Ya lu Lu lu pikir lah gimana lu cara berbahasa Indonesia? Fair criticism, Bro. Gue seriusin dan rencana pasang language tool.

**34:37** · Grammar checker open source yang support bahasa Indonesia. Terus gue belajar PUEBI, Pedoman Umum Ejaan Bahasa Indonesia. Terus audit script tadi dan benerin. Gas. Ya udah, bener. Ya, lu lu bayangin aja, Guys. Lu bayangin ini.

**34:48** · Setahun, bukan bulan, setahun. Big Tech Silicon Valley bakal belanjain itu apa sih?

**34:54** · Enggak bisa lah bahasa Indonesia begini.

**34:56** · Harus dibenerin dulu. Nah, lagi-lagi apa? Manusianya. Kenapa seorang manusia dengan bantuan AI tidak bisa menghasilkan AI slow tidak seperti baby boomers di luar sana. Aduh, ngejekin boomers lagi. Ya, karena dia berpikir, karena dia mengevaluasi lagi apa yang dikerjakan sama AI-nya. Dan itu yang kita lakukan sekarang. Dan kita tunggu aja sampai dia selesai. Apakah script-nya membaik? Harusnya sih iya.

**35:20** · Dia sudah selesai. Akhirnya dia pasang Hanspel plus kamus bahasa Indonesia untuk deteksi typo dan kata asing sudah teruji. Language Tool 6.6. Dia di web check, dia buat sendiri code-nya.

**35:33** · Oke, coba kita buka. Nah, ini baru bener. 1 triliun dolar per tahun, bukan per bulan, per tahun.

**35:41** · Big Tech Silicon Valley bakal menghabiskan lebih dari 1 triliun dolar untuk AI tahun ini 2026. Nah, ini bisa di-improve lagi. Yes, itu dana yang dihabiskan untuk AI tahun ini 2026. Ini bagus banget ada komparasi yang jelas langsung. Khas konten gue banget karena setting-annya udah ada. Dan itu baru biaya fisiknya, GPU, gedung, listrik.

**36:00** · Ini tinggal di-improve lagi one by one, chapter by chapter jadi script yang keren. Karena dari awalnya udah bagus.

**36:06** · Dan biar video ini enggak kelamaan, teman. Tapi kalian understand kan apa yang gue kerjakan kan tadi kan. Jadi ketika ada sesuatu yang gue enggak suka dari AI gue ya, gue suruh dia benerin.

**36:15** · Gue suruh dia pasang tools yang bisa membantu dia buat mengerjakan hal itu lebih baik lagi. Jadi bukan masalah modelnya doang. Masalahnya orang yang mengendalikan model tersebut bisa atau enggak. Itu aja sih sebenarnya yang mau gue tekankan ke kalian ya, teman-teman.

**36:28** · Jadi jangan kayak, "Emm, hasilnya jelek, ganti model lagi, jelek lagi, ganti model lagi." Capek lu ganti model.

**36:35** · Settingan baku lu dulu dibenerin, baru nanti lu compare model tuh terakhiran aja kalau settingan lu udah klik. Itu baru bisa kelihatan tuh mana yang enak banget. Di zaman sekarang ini dengan AI RS yang gila ini, rata-rata udah sama semua hasilnya. Mending lu percaya gua dah. Walaupun gua enggak jualan kelas.

**36:50** · \[berteriak\] Oke. Ngebuat script udah, ngebuat presentasi udah. Sekarang saatnya pekerjaan ketiga, kita buat coding. Bisa enggak dia, capable enggak dia buat coding? Mampu enggak dia nih Herme Agent buat coding dan melakukan tugas-tugas kita. Jadi kita tinggal duduk-duduk, tinggal enak-enak, semua kode di-scan, dikerjain sama dia. Bisa enggak coba?

**37:09** · Kita coba ya.

### Testing: Coding

**37:13** · Untuk pembuatan website, gua udah ada brief sederhana, bikinin website buat Nusa Rimba Coffee. Profil bisnisnya ini, nama kopinya ini, arah desainnya begini, isi dan fitur website hasil yang diminta. Oke, kita masukin aja ke Telegram. Pakai desain sistem Web Exporter yang buat presentasi. Aku mau bikin kamu bikin website berdasarkan brief ini. Gua ganti pakai prototype ya, teman-teman ya. Bikin prototype website eksportir dari brief ini, tapi gua mau tetap pakai desain sistemnya Web Exporter.

**37:43** · Ikuti cara kerja Web Exporter yang sudah gua kasih buat katalog tiga produk dan inquiry per produk. Jangan menambah klaim bisnis yang tidak ada di brief. Jalankan preview, periksa versi HP dan semua tombol, lalu laporkan hasil tes serta informasi yang masih kurang.

**37:56** · Coba kirim. Kita tunggu aja, teman-teman, dia ngerjain website-nya dan result-nya kayak apa. Dan ini hanya contoh sederhana ya, teman-teman.

**38:02** · Pengerjaan coding itu lebih dari ini.

**38:04** · Ini cuman single prompt jadi website sebenarnya enggak relate. Pekerjaan coding yang asli ya, kalian clone repo-nya, kalian kerjain dari awal, kalian punya desain Figma-nya atau desain sistem yang jelas, kalian buat requirement-nya page per page. Itu agak panjang nanti. Enggak selesai-selesai ini video YouTube. Gua cuman mau nunjukin kapabilitas sederhananya aja.

**38:24** · Intinya begitu. Dan masalah kalau "Bang, bisa enggak dikonekin ke repository terus dia ngelakuin bug fixing, dia ngimprove sesuatu?" Sangat-sangat bisa dan tidak ada masalah. Tapi gua enggak ingin mencontohkan itu ya, teman-teman.

**38:34** · Gua ingin mencontohkan kapabilitas sederhananya aja dalam membuat website.

**38:38** · Intinya di situ dan kita tunggu hasilnya sampai selesai. Sudah selesai, Guys, dalam waktu 10 menit. Cepat juga dia kerja ya. Dikasih preview-nya di sini seperti biasa, Nusa Rimba Coffee. Wus!

**38:50** · Bagus dong hasilnya.

**38:53** · Lebih bagus dari Open Cloud kemarin karena kita kasih design system yang jelas dari web export, kemudian kita kasih brief yang jelas dan ini prototype aja, demo. Product, ordering details, about, contact us.

**39:06** · Ya, oke. Untuk starting ini oke dan bisa di-improve ke mana-mana. Of course, dia ngebuat gambar sendiri mencoba tapi hasilnya jelek banget. Ini bisa diganti.

**39:14** · Ya, tapi ini kapabilitasnya ya, teman-teman. Jadi, untuk membuat website, teman-teman IT mungkin punya cara yang lebih baik dan setiap orang punya caranya sendiri, punya kompilasinya sendiri bagaimana menghasilkan yang lebih baik. Jadi, tes ini hanya sekedar tes awal, tes di layer atas, ngebuat website prototype dan menunjukkan kapabilitas Herme dengan tools-tools yang ada ya sangat-sangat capable dan bisa. Kemudian untuk bug fixing-lah, untuk improving feature, untuk masuk ke sprint, lu ngerjain suatu kerjaan lu, banyak tools yang bisa di-install di Herme kalian untuk mengerjakan itu semua.

**39:45** · Mungkin kita bisa bahas nanti secara teknikal coding ya, teman-teman ya. Tapi karena keterbatasan waktu ya, seperti tadi dulu dan kita akan sampai ke kesimpulan.

### Verdict

**39:58** · Kesimpulannya apa? Untuk menyingkat durasi tutorial gua, gua berusaha seminimal mungkin karena dari pengalaman Open Cloud kemarin sampai 1 jam. Gua enggak tahu ini sampai berapa menit nantinya. Semoga tetap ringkas dan padat dan bagus. Kita tadi udah melakukan setup ke Herme agent kita. Yang pertama kita ingin option yang lebih murah, kebetulan teman-teman limit gua yang 10 dolar habis jadi gua tadi top up ke yang 40 dolar. Kalau yang 40 dolar untuk kerja kayak tadi, kayak apa sih sebenarnya cuman terpakai 22%.

**40:26** · Tapi menurut gua untuk pekerjaan tadi yang 10 dolar aja cukup paling limitnya mau habis sedikit. Jadi totally fine.

**40:35** · Kemudian 9 router ini kita set up menggunakan open code go, kita kasih tail scale-nya. Kemudian kita pasang juga Herme agent dashboard, kita kasih tail scale-nya juga. Dan kita import settingan kita yang lama sehingga dia menjadi lebih pintar, menjadi lebih mengerti siapa saya, siapa seorang David dan apa aja yang dia kerjakan dan bagaimana cara dia mengerjakannya.

**40:55** · Kita tadi buat presentasi teman-teman dan hasilnya oke, kita kasih tahu dia ada desain sistemnya, lu tools-nya apa aja, habis itu kita buat script konten dan hasilnya juga oke setelah kita tuning lagi. Kemudian kita buat website yang terakhir dan hasilnya juga enggak mengecewakan. Jadi dengan budget yang murah VPS 100-200 ribu dan modal yang 100 sampai 200 ribu juga bahkan ada yang lebih murah kalian bisa utek-utek sendiri ternyata bisa menghasilkan kemampuan yang bagus dan kita bisa bekerja beneran di atas itu.

**41:26** · Nah ini adalah edukasi yang gua mau teman-teman semoga dengan edukasi ini dengan rilisnya video ini kalian bisa mencoba sendiri di rumah, utek-utek sendiri di rumah dan serunya di situ. Bersyukur banget setelah gua rilis beberapa tutorial AI banyak yang nyapa gua di jalan Bang David thank you ya gua udah cobain Herme-nya, gua udah cobain open cloud-nya ternyata biayanya bisa murah kok enggak harus mahal. Ternyata edukasi kayak gini bisa gua pelajarin sendiri ya enggak harus ribet gua gua bisa setting VPS sendiri Bang gila dan gua ngerasa keren di coffee shop.

**41:54** · Hal-hal kayak gitu membuat gua bangga jujur teman-teman dan senang bahkan melebihi uang senangnya karena bisa membantu orang mengerti AI di zaman yang AI race ini balapan teman-teman kita di Silicon Valley berlomba buat produk AI di negara kita masih sangat ketinggalan dan itu adalah tujuan gua membuat video-video ini, teman-teman. Dan jangan lupa video ini disponsori oleh Hostinger juga, bekerja sama. Kalian kalau tertarik menggunakan VPS, bisa pakai VPS-nya Hostinger dengan link yang ada di sini, hostinger.com/davidvps.

**42:25** · Dan ada diskonnya, teman-teman. Dan reliable banget tadi gua udah cobain, lancar banget kan pakai VPS-nya Hostinger. Ya, itu saja teman-teman mungkin. Terima kasih yang udah nonton sampai sini. Gua doain kalian cobain Herramienta AI kalian sendiri-sendiri dan bisa lebih produktif menggunakan AI dengan pengajaran-pengajaran yang tadi gua berikan. Dan ini sifatnya sharing.

**42:44** · Kalau gua ada salah, kalian udah sebut aja di kolom komentar. Kita diskusi yang baik. Kalau gua ada yang kurang juga, ada cara yang lebih baik bahkan, sebut aja di kolom komentar. Biar semuanya lebih clear. Thank you so much yang udah nonton sampai sini. Dan kalau kalian tahu teman-teman, ngebuat video kayak gini tuh lama. Jadi gua respect, gua ngebuat video ini dari jam 08.00 malam, sekarang jam 12.00. Jadi kayak 4 jam gua otak-atik ini sampai jadi video.

**43:07** · Walaupun nanti hasil videonya mungkin enggak sampai 1 jam. Tapi enggak apa-apa, it's okay. Semoga kalian sehat terus, semoga kalian sukses terus. Dan jangan lupa subscribe dan aktifin lonceng biar channel gua makin berkembang. Gua David Alfa Sunarna undur diri. Thank you so much. Maju terus AI di Indonesia. Amin.