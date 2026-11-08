---
title: "TUTORIAL PASANG AI AGENT MURAH MERIAH (HERMES AGENT + 9ROUTER)"
source: "https://www.youtube.com/watch?v=HVGQULc853Y&t=385s"
author:
  - "[[David Alfa Sunarna]]"
published: 2026-09-18
created: 2026-11-08
description: "VPS Hostinger, diskon 10% pakai kode DAVIDHERMEShttps://hostinger.com/davidhermesBanyak yang bilang gua gak napak tanah di video sebelumnya karena pake Claude Code. Ini video jawaban buat komentar"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=HVGQULc853Y)

VPS Hostinger, diskon 10% pakai kode DAVIDHERMES  
https://hostinger.com/davidhermes  
  
Banyak yang bilang gua gak napak tanah di video sebelumnya karena pake Claude Code. Ini video jawaban buat komentar di video sebelumnya. Gimana caranya kita pasang AI Agent yang murah meriah tapi tetep bisa perform. Kemarin gua pakai Claude paket 200 dolar, wajar kalau banyak yang bilang "Bang, gua gak sanggup, lu mah gak napak tanah". "Yang mahal itu bukan servernya, tapi model AI-nya itumah Claude Code."  
  
Oke sekarang kita bahas AI Agent yang hampir gratis ini. Apakah sebagus Claude Code? Apakah sesimple dan secepat Claude Code? 😏  
  
Script buat benerin reset password error menit 17:33  
  
python3 -c "import sqlite3,json;db=sqlite3.connect('$HOME/.9router/db/data.sqlite');rid,data=db.execute('SELECT id,data FROM settings').fetchone();d=json.loads(data);d\['password'\]='\\$2b\\$10\\$m.FXbHtGJOQcgK0Ung6IhO7.j99yhyGkna5/e//WabqBB9PP6/uYe';db.execute('UPDATE settings SET data=? WHERE id=?',(json.dumps(d),rid));db.commit()"  
  
#HermesAgent #9Router #Hostinger #AIAgent #VPS #ClaudeCode  
  
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
Timeline:  
00:00 Intro  
03:09 Iklan: VPS Hostinger  
07:41 Instalasi Hermes Agent  
14:11 Instalasi 9Router  
28:35 Komparasi Dengan Claude Code  
31:56 Verdict

## Transcript

### Intro

**0:00** · Banyak yang bilang gua enggak napak tanah ketika kemarin gua ngajarin cara nginstal AI Agent di VPS sendiri tapi pakai Cloud the Code. Bang David, siapa yang pakai Cloud the Code 100 dolar dan 200 dolar? Orangnya enggak banyak. Di komentar juga banyak yang bilang, "Next lanjut pakai Herme Agent, Bang, pakai model China." Oke. "Bang, instal Herme Agent terus pakai LLM bansos China."

**0:24** · Oke, gua dengerin kalian. Gua juga tahu enggak semua orang pakai Cloud the Code.

**0:28** · Contoh yang kemarin gua kasih memang titik beratnya itu bukan di VPS-nya, tapi yang mahal itu modelnya. Kalian harus langganan Cloud the Code which is kalau mau maksimal jelas yang 100 dolar atau 200 dolar yang 20 X. Biar gua napak tanah di video ini gua mau ajarin kalian cara instal Herme Agent di VPS yang murah terus kita juga bakal pakai Nine Router yang tier 3 deh, yang bansos, yang kagak bayar.

**0:50** · Gua juga bakal jelasin apa itu Herme Agent, apa itu Nine Router sehingga kalian bisa punya AI Agent tik sendiri yang bisa ready buat kalian 24 jam nyala terus yang bisa diperintah sama kalian via WhatsApp atau Telegram.

**1:05** · Kalau di video ini gua mau jelasin pakai Telegram. Kemudian gua juga mau jelasin biaya modalnya beli VPS-nya berapa dan apa aja yang harus kalian lakukan untuk punya semua itu. Dan tutorial ini cocok banget buat kalian yang masih belajar AI Agent karena enggak semua orang, Bro, beli Cloud the Code yang 100 dolar of course. Dan buat kalian yang mau mulai mungkin memakai LLM bansos dari China itu yang ganti-gantian itu di Nine Router itu adalah salah satu solusi yang terbaik mungkin. Dan untuk membuktikan semuanya itu gua bakal adu nanti.

**1:31** · Bukan adu sih, gua bakal tes Cloud Code versus LLM bansos pakai Nine Router di atas Herme Agent. Bagusan mana coba? Gua bakal buat website sederhana. Apakah hasilnya bagus? Kalau hasilnya enggak jauh beda worth it banget dong punya Herme Agent terus pakai Nine Router tier 3. Jadi video ini gua buat biar gua napak tanah dan mendengarkan suara netizen karena gua suka mendengarkan suara rakyat, anjay.

**1:57** · Dan kalian kalau lihat video ini enggak perlu beli kelas, teman-teman. Karena gua kemarin kesal sama orang yang jualan kelas. Dia jelek-jelekin VPS RAM 1 giga.

**2:05** · Kata dia ngadi-ngadi. VPS RAM 1 giga enggak bisa buat jalanin AI Agent Herme plus Nine Router. Buset dah. Itu 1 giga, Pak, RAM-nya. Herme Agent plus Nine Router jelas enggak bisa. Nah, edukasi yang kayak gini gua enggak mau terjadi.

**2:19** · Kalian sudah beli kelas mahal-mahal, ternyata materinya enggak dikurasi.

**2:22** · Ternyata materinya cuman buat hook doang. Terus dia menyarankan bikin di lokal pakai Docker baru upgrade ke homelab. Menurut gua investasinya itu masih terlalu besar. Dan ketika kalian instal di laptop, misalkan Herme Agent ataupun apalah Claude Code, kalian enggak bisa akses dari mana pun 24 jam.

**2:38** · Karena kalau laptop kalian mati, ya itu Agent mati. Jadi enggak agentik-agentik amat. Kalaupun kalian harus invest mini PC ataupun Mac Mini, itu harganya akan terlalu mahal. Jadi VPS adalah solusi yang terbaik menurut saya jika kalian mau belajar tentang AI Agent, teman-teman. Jadi please buat teman-teman yang jualan kelas, tolong materinya dikurasi lagi. Bukannya jualan kelas AI itu enggak boleh, tapi pastikan kalian tuh make sense, kalian juga expert di bidang itu. Biar orang yang beli kelas kalian itu tidak sesat. Tanpa berlama-lama kita langsung mulai saja, Guys.

### Iklan: VPS Hostinger

**3:11** · Untuk VPS-nya, video ini bekerja sama dengan Hostinger. Kalian bisa pakai produk VPS mereka. Diganti dulu nih bahasa Indonesia di hostinger.com.

**3:19** · Kemudian ke produk, hosting, dan VPS hosting. Bang, tapi kan Hostinger ada one click Herme Agent. Ada, betul. Di produk ada nih. Lihat, Herme Agent. Tapi di sini gua mau ngajarin kalian dari nol. Biar kalian ngerti apa itu Herme Agent, apa yang terjadi di baliknya, dan kalian bisa mengkonfigurasinya sendiri dengan baik. Karena di era AI yang serba cepat ini, understanding suatu bidang ilmu itu yang basic itu jarang terjadi.

**3:47** · Kita disuguhi semuanya instan. Bukan berarti punya Herme Agent one click dari Hostinger itu salah. Kalau kalian sudah jago silakan, tapi gua mau ajarin kalian dari bawah. Di sini produk yang gua pakai adalah KVM2 atau KVM2 dengan 2 vCPU core dan 8 GB RAM. Menurut saya, bukan menurut saya sih, ini sudah cukup untuk Hermes Agent dan Nine Router.

**4:07** · Enggak gede-gede amat, tapi juga enggak kecil-kecil amat. 8 GB RAM-nya lumayan lega buat jalanin Agent Tik dan berbagai macam task nanti. Kalau kalian ada rezeki lebih, bisa pilih yang 4 vCPU core 16 GB RAM atau sekalian 8 vCPU core 32 GB RAM. Harganya berapa? Harganya Rp 140.000 untuk 24 bulan berlangganan ya, teman-teman. Kalian bisa pakai promo code David Hermes untuk dapat diskon 10% atau kalian juga bisa beli paket yang 12 bulan kalau mau lebih murah. Totalnya hanya sekitar 2,1 juta untuk 1 tahun ya, teman-teman.

**4:38** · Kalian running AI Agent 1 tahun. Ya, segala sesuatu pasti ada investment-nya. Kalau sudah, bisa lanjutkan dan kalian bisa selesaikan pembayaran. Setelah kalian beli, kalian masuk ke panel account Hostinger kalian.

**4:49** · Akan ada tulisan "Setup KVM2 Anda belum selesai." Lanjutin setup-nya. Pilih lokasi server. Tadi kayaknya sudah milih ya, tapi kita bisa milih lagi di Indonesia. Selanjutnya, tadi kita juga sudah milih di check out. Berhubung tadi gua pakai quick check out, enggak sempat milih, kita milih lagi ya. Pakai apa?

**5:05** · Pakai Ubuntu dulu, Ubuntu server. Yang terbaru saja enggak apa-apa. Di sini enaknya Hostinger, kalian bisa set root password kalian sendiri atau kalian bisa login pakai SSH key yang mana itu agak advance, enggak gua rekomendasikan.

**5:17** · Sudah, buat root password saja. Kita buat root password. Selanjutnya, pendeteksi malware gratis pasang saja enggak apa-apa. Docker manager kayaknya enggak usah dulu. Selesaikan setup.

**5:27** · Menyiapkan VPS Anda, kita tunggu sampai prosesnya selesai ya, teman-teman. Oke, setelah setup-nya selesai, kalian akan dihadapkan dengan dua pilihan. Yang pertama adalah dashboard VPS, yang kedua adalah SSH access. Kita sudah belajar tentang SSH access sebelumnya, teman-teman. Ada root dan alamat IP dan password yang kalian buat tadi. Kita mau coba access via SSH dulu teman-teman, biar kita nge-refresh lagi video yang kemarin. Sekedar update, menurut netizen di video kemarin Windows PowerShell juga udah bisa SSH, jadi enggak perlu PuTTY, langsung dari Windows bisa.

**5:57** · Kalau saya pakai MacBook, saya mau coba di MacBook.

**6:01** · Jangan katain enggak napak tanah lagi ya. Kita ketik SSH root dan alamat IP-nya, enter, yes.

**6:08** · Untuk pertama kali, are you sure want to continue connecting? Yes, untuk pertama kali. Masukin password root. Oke, boom, kita connect ke KVM 2 milik Hostinger.

**6:18** · Tapi karena kalian pakai Hostinger ada cara yang lebih gampang buat kalian yang masih pemula. Walaupun ini keren nih terkesan seperti hacker. Kita exit dulu ya. Exit SSH caranya gimana ya? Exit aja, ketik enter, keluar. Ada cara lain melalui dashboard VPS-nya teman-teman.

**6:34** · Coba kita klik ya, kelola VPS. Oke, ini pengalaman saya mengelola VPS selanjutnya untuk kebutuhan pribadi AI dan machine learning, simpan. Bagaimana kualitas layanan VPS Anda? 10. Tuh, bagikan link tuh, diskon hingga 20% dan komisi hingga 180 dolar untuk Anda. Uh, lumayan. Sekarang gua udah ada di dashboard VPS-nya teman-teman. Kita bisa lihat ada username, ada IP-nya, kita bisa reset password root-nya kalau lupa.

**7:01** · Lebih gampang kan? Kemudian kita bisa bisa restart kalau ada masalah, kita bisa perpanjang, bisa upgrade, bisa stop VPS-nya. Yang paling bikin gampang lagi apa? Ada konsol web-nya. Jadi kita enggak usah SSH, langsung dari browser bisa. Kita klik aja, bap.

**7:17** · Ini juga hacker. Buka browser hitam putih. Kalian nongkrong di kafe kekinian, browsernya begini.

**7:24** · Top. Ini kelebihan Hostinger ya teman-teman. Jadi kalian bisa akses VPS-nya via browser. Dan gua mau pakai ini cobain. Setelah kita berhasil SSH via browser menggunakan tools dari Hostinger yang canggih ini, kita tetap keren kok walaupun pakai browser tetap hitam putih begini, gokil.

### Instalasi Hermes Agent

**7:43** · Sudah saatnya kita instal Herme Agent.

**7:46** · Herme Agent ini apa? Buka aja website-nya. Herme Agent ini adalah framework AI Agent open source.

**7:52** · License-nya dari MIT, buatan Nous Research. Apa bedanya dengan Open Claw?

**7:56** · Bedanya dia baru aja rilis Februari 2026. Dan dia punya memori yang nempel.

**8:01** · Oke, Open Claw juga punya. Tapi dia klaim dia bisa bikin skill sendiri dari pengalaman. Dan Herme ini menurut saya, menurut sepengamatan saya, jangan disalahin ya, lebih fleksibel masalah modelnya. Banyak LLM LLM atau model-model bansos Cina yang ada di sini. Jadi kalian bisa pakai ini secara gratis, langganan VPS aja. Itu yang memajukan Herme Agent. Nilai plus-nya di situ. Bagaimana cara menginstal Herme Agent? Seperti yang saya kasih tahu kemarin, kalau kita menginstal apapun biasakan buka website-nya. Kemudian baca dokumentasi.

**8:34** · Ketika kita buka dokumentasinya pertama kali langsung ada instal. Pilih buat Linux karena kita pakai Ubuntu ada script-nya langsung tinggal copy, paste di terminal kalian yang terkoneksi ke SSH VPS kalian.

**8:48** · Kemudian klik enter. Selesai. Kalian langsung jadi hacker hitam putih.

**8:53** · Pastikan kalian menginstal ini ketika kalian sedang nongkrong dan banyak orang di sekitar kalian. Karena kalian akan kelihatan sangat keren, Guys. Beh.

**9:02** · Gokil. Orang lihat pasti kalau nengok MacBook kalian Apaan tuh?

**9:06** · Anjay.

**9:06** · Keren banget tuh orang.

**9:08** · Keren emang keren. Instal Herme Agent, Bro. Dan enggak harus programmer. Gua buat tutorial ini biar semua orang bisa.

**9:14** · Di luar negeri enggak harus programmer ngakses-ngakses VPS gini. Ubuntu server itu hanya OS lain selain Windows ataupun MacBook. Enggak usah kagok, enggak usah gaptek. Enggak ada alasan gaptek. Ingat ya, kita tunggu aja deh instalasinya selesai. Sambil ngopi gitu kan.

**9:29** · \[mendengus\] Huh. Gokil. Hitam putih gini layarnya.

**9:33** · Ketika sudah selesai instal, kalian akan dihadapkan dengan berbagai macam pilihan untuk setup Herme. Jangan kagok, jangan pusing. Sebagai pemula kalian pilih aja rekomendasi dia. Tapi Bang, kita kan mau pakaiin N router. Udah nanti dulu, nanti dulu. Pakai rekomendasi dia dulu. How would you like to set up Herme? Quick set up.

**9:52** · Pakai no support enter aja. Nah, ini pentingnya membaca. Kalian harus baca.

**9:57** · To continue open ini. Open aja. Kemudian pastikan kodenya cocok. Ini kode saya.

**10:05** · Connect. Active account pakai email saya. Kalau kalian belum login nanti suruh login dulu. Login with Google aja enggak usah repot. Oke, connected. Di sini kalian harus milih model. Bang, kita kan mau konekin ke N router. Kok milih model? Nanti dulu, nanti dulu.

**10:19** · Udah tenang aja. Lu tuh tenangin diri lu. Pilih aja model. Yang rekomendasi apa nih? Upstate Solar Pro for free Mate 1 long chat. Mate 1 long chat. Uh, ini adalah LLM bansos semuanya. LLM ini adalah LLM free teman-teman. Pilih aja yang paling atas. Udah santai aja dulu, santai, santai. Ada pertanyaan lagi.

**10:39** · Select terminal back end. Enggak usah panik. Jadi orang enggak usah panikan.

**10:42** · Santai aja. Local run directly on this machine default. Ya udah. Keep current local. Ini developer-nya Herme tuh pasti udah ngerti juga. Udah lu pilih rekomendasi aja deh. Enggak usah bingung. Sekarang yang agak advance nih teman-teman. Kita mau konekin eh Herme agent ini ke Telegram bot kita. Nah, ini harus step by step teman-teman. Dengerin baik-baik. Ini enggak susah, gampang.

**11:05** · Connect a messaging platform. Oke, kita pilih Telegram ya. Setup messaging now recommended. Setup. Oke, kalian pilih messaging mana yang mau dipakai. Kita pilih Telegram. Nah, untuk mencentang di SSH kita pencet spasi teman-teman.

**11:21** · Ingat, pencet spasi. Tuh, sampai Telegram-nya ada bentuk centangnya.

**11:24** · Kemudian enter. Bab. How would you like to create your Telegram bot? Scan a aki code, confirm in Telegram, dan no token copy paste needed. Ya pilih nomor satu lah. Nih ini buka, sama aja kok kayak yang buka QR code-nya. Karena tadi gua belum instal, pip instal QR code, jadi QR code-nya belum muncul. Enggak apa-apa, enggak masalah. Kita buka aja link tadi, terus create bot, namanya apa? Oh David Herme agen dong.

**11:56** · Create.

**11:59** · David Herme agen is ready. Click start below to test your new chatbot. Its behavior is defined by nose hosted Herme bot. Start. Gua udah start tapi enggak mulai. Ternyata masalahnya ada di sini teman-teman. Ada pop up connect Herme ini to your Herme set up. Gua belum connect. Connect this bot dulu.

**12:19** · Terus kalau kita balik ke terminal kita, allow this telegram account to use the bot. Yes, bro. Baca baik-baik nih ya.

**12:27** · Additional allowed user ID, comma separated. Opsional, enggak usah.

**12:31** · Use your user ID as the home channel.

**12:34** · Yes. Kita coba dulu ya.

**12:37** · Halo. Nah, sekarang dia typing teman-teman. Dia akan balas message kita. Halo, saya bisa bantu berbagai hal. Ketik help untuk lihat perintah yang tersedia. Beh.

**12:49** · Udah connect. Enggak usah panik kalau ada apa-apa. Kalau ada masalah kita periksa dulu masalahnya apa. Kita coba buka satu-satu kurangnya di mana. Itu adalah anak IT. Itu cara kerja orang pintar. Kemudian kita balik lagi ke terminal kita, would you like to install the gateway as a background services.

**13:05** · Kita mau ini jalan di background services. Of course, yes.

**13:09** · We install it. Sekarang kita punya Herme yang berjalan. Aku boleh kenalin diri aku enggak? Anjay.

**13:18** · Tuh dia balas, boleh banget ceritain yang kamu nyaman share.

**13:22** · \[tertawa\] Ini jawabannya masih AI banget. Dia pakai Mdes, terus menurut saya jawabannya AI banget, belum natural.

**13:31** · Kita bisa setting kok, aman. Dan teman-teman ini penting buat gua jelasin karena kita tadi milih pakai Nouse Portal. Sebenarnya kita bisa langganan juga model atau subscription tier dari Herme Agent ini. Jadi ini cara mereka monetize platform mereka. Mereka buat subscription. Kita baca ya. Misalkan kalau kita langganan plus yang $20, kita punya kredit $22 sebulan. Ada 200 lebih model dan lain-lain kalian bisa baca sendiri. Tapi di sini kita kan mau pakai Nine Router. Jadi jangan senang dulu kalau tadi udah bisa jawab AI Agent-nya, itu belum goal kita.

**14:02** · Kita harus setup Nine Router dulu. Nah, apa itu sih sebenarnya Nine Router? Dibahas di mana-mana Nine Router. Nine Router tuh apa sih?

### Instalasi 9Router

**14:13** · Coba aja kita buka. Nine Router itu adalah proxy lokal open source lisensinya MIT. Gratis dan enggak pernah menagih penggunanya. Kalau ini kan tadi masih ada balance-nya, bisa beli kreditnya. Nah, Nine Router ini enggak.

**14:27** · Kenapa dia bisa gratis? Ya, sebenarnya kita langganannya di langsung penyedia AI-nya. Nine Router ini tugasnya menyebar permintaan ke banyak penyedia AI. Jadi kalau satu kena limit, otomatis bisa pindah. Sistemnya gimana Nine Router ini? Ada namanya tier. Tier-nya itu ada tiga, teman-teman. Yang pertama tier one subscription, kalian punya cloud code bisa dikonekin, kalian punya codex bisa dikonekin, kalian punya Gemini, punya Copilot bisa dikonekin.

**14:52** · Jadi kalau kalian langganan cloud code yang 300.000 doang, codex yang murah doang, kalian bisa satuin tuh di Nine Router. Dia yang akan nyebar request-nya secara otomatis. Jadi kalau satu kena limit, langsung lari ke yang lainnya.

**15:03** · Konsepnya gitu. Kemudian tier dua. Nah, tier dua ini biasanya LLM dari China.

**15:07** · Bukan LLM bansos. Ini masih bayar.

**15:09** · Contohnya kayak GLM, MiniMax, Kimi yang murah-murah aja bulanannya. Ada tier yang lebih gokil, tier tiga. Free, gratis. Ini pakai beberapa penyedia model kayak Iflow, Kwen, Kiro, Open Code Unlimited. Cuman ya kita perlu note ini terbatas teman-teman. Kemampuannya juga terbatas, bukan yang terbaru. Dari segi kehebatan juga enggak akan sehebat tier 1, tier 2. Kita akuin aja.

**15:35** · Tapi gratis.

**15:36** · Contoh nih kayak yang free forever, dia ada Kiro AI, iFlow, Quen dan lain sebagainya. Gimana caranya instal Nine Router di VPS kita? Lagi-lagi apa? Buka dokumentasi aja, enggak usah bingung jadi orang. Dokumentasinya langsung ke GitHub. Jangan takut ngelihat GitHub itu. Scroll ke bawah, ada Redmi. Baca baik-baik. Baca bagaimana dia bekerja.

**15:58** · This is your CLI tools. Kita langsung ke quick start aja instal globally teman-teman. NPM instal -g Nine Router.

**16:05** · Udah langsung aja. Kita instal langsung di VPS Hostinger. Kita clear dulu ya teman-teman ya biar clean. NPM instal -g Nine Router. -g itu artinya apa? Global.

**16:16** · Jadi bisa diakses sama siapa aja di VPS kalian. Sama user siapa aja. Itu artinya -g atau global. Enter. Dia lagi instal.

**16:25** · Kita tunggu. Wow, ada masalah. Oke. One package has install script not yet covered by allow script. Ini komen kalau cuman boleh script-nya sekali. Ini kalau buat global instal. Ya udahlah. Kita instal buat semuanya lah. NPM config set allow script Nine Router location user.

**16:42** · Oke, kita instal lagi buat global. Coba kita lihat. Sepertinya sudah selesai.

**16:46** · Coba kita akses ya Nine Router.

**16:50** · Anjay.

**16:52** · Ada interface-nya. Web UI. Open in browser.

**16:56** · Web UI aja. Nah, ini ada kan localhost kan? Nah, localhost-nya ini kita ganti pakai IP VPS-nya.

**17:03** · Coba kita buka dulu. Pasti error. Kita ganti pakai IP VPS-nya ya teman-teman.

**17:10** · IP publiknya.

**17:14** · Nah. Password. Oke. Kita baca dulu di bawah default password 123456.

**17:21** · Masukin dulu aja. Ye, harus diganti dulu. Kenapa tadi enggak bisa login pakai default password 123456? Tenang, enggak usah panik. Gua udah ubek-ubek GitHub, ada one liner-nya buat nge-fix.

**17:33** · Gua bakal taruh di deskripsi, teman-teman. Kita jalanin aja, pencet enter.

**17:38** · Udah selesai, kalian bisa login dengan default password.

**17:42** · Nine router.

**17:48** · Web UI.

**17:49** · Oke.

**17:50** · Refresh, sudah hilang, bisa ketik 123456.

**17:54** · Login.

**17:55** · Bab, tapi ada satu masalah, teman-teman.

**17:57** · Coba kita keluar dulu ya dari sini ya.

**18:00** · Logout. Ini tuh sepertinya agak susah kalau jalan di background. Nah, kita butuh tools apa biar dia bisa jalan terus? Termux solusinya. Exit dulu.

**18:09** · Exit-nya caranya gimana? Control C aja udah, control C nanti dia exit sendiri.

**18:13** · Oke. Kita clear lagi.

**18:16** · Kita install Termux ya. Termux install Ubuntu.

**18:21** · Sudo apt install Termux.

**18:25** · Oh, udah ada Termux-nya di Hostinger.

**18:28** · Oke.

**18:29** · Termux create new session.

**18:37** · Termux new min S.

**18:40** · Nine router.

**18:42** · Siap.

**18:44** · Kita jalankan Nine router.

**18:51** · Aktifin web UI-nya.

**18:54** · Udah. Termux exit session. Control B D.

**18:58** · Control B D.

**19:00** · Bab, bakal nyala terus Nine router kalian. Masukin password, dah kalian enggak perlu pusingin, dia bakal jalan di background sendiri. Agak advance ya?

**19:09** · Bisa. Bisa.

**19:11** · Tenang. Oke, sebenarnya ada apa saja sih di Nine Router? Kita harus pahami satu persatu. Tapi pertama kita harus ganti password dulu, teman-teman. Ini wajib kalian lakukan demi keamanan Nine Router kalian. Kalau kita lihat di sini ada API endpoint, yang mana ini nanti akan diakses sama Herbie Agent kita untuk mengakses model yang disediakan oleh Nine Router. Kemudian kita bisa pilih provider berbagai macam, tapi kita mau pakai free trial ya di sini ya, teman-teman ya. Dan yang paling penting dia itu ada token saver.

**19:44** · Kita bisa pakai RTK by default. By default ada open code yang free, tapi kita mau coba aktifin Cloudflare, teman-teman. Biar kita bisa pakai GLM sama Kimi mereka. Anjay. Coba kita get API key.

**20:02** · Kita pakai account API token saja.

**20:04** · Create token.

**20:06** · Read all resources deh.

**20:08** · Review token.

**20:11** · Create token.

**20:14** · Jadi ada dua, teman-teman, API token sama account ID. Kita masukin dua-duanya.

**20:21** · Buat add connection.

**20:27** · Kita cek.

**20:30** · Jalan. Kita save.

**20:34** · Sekarang kita punya connection ke Cloudflare. Begitu juga dengan yang lain, misalkan Nvidia NIM. Kita buat saja deh. Free access for Nvidia developer program members prototyping and testing get API key.

**20:45** · Save all. Kita bikin-bikin saja.

**20:48** · Get API key.

**20:50** · Generate key.

**20:53** · Kita copy ya. Kita masukkan ke Nine Router.

**21:00** · Cek.

**21:01** · It's working. Save.

**21:04** · Oke.

**21:05** · Ada beberapa model yang bisa dipakai, GLM bisa, Dipsik, Nemotron, Kimi, macam-macam.

**21:13** · Sudah ya, tiga saja dulu. Jangan kebanyakan. Nah, cara pakainya mau gimana? Gampang, kita buat namanya combo. Combo ini apa? Jadi, kita bisa menentukan strategi gimana dia merotasi model-model AI-nya. Bisa pakai fallback, round robin, fusion. Coba kita create combo lah, biar enggak usah kebanyakan teori. Namanya Hermes combo.

**21:37** · Modelnya apa? Add model. Kita mau apa nih? Yang gratisan dulu ya. Jujur, gua tuh suka GLM.

**21:44** · Ya, kita pakai GLM ya. Terus yang kedua, kita bisa pakai di akun lain mungkin kita pakai Kimi.

**21:53** · Oh, enggak usah. Coba Nemotron 3 Ultra.

**21:56** · Yang lainnya kita bisa pakai Open Code, ya, Muse Spark 1.3 lah. Sudah kita pakai.

**22:03** · Nih, ada GLM, Nemotron, sama Muse Spark.

**22:08** · Mmm, kayaknya harus nambah ini sih, Kimi K26.

**22:13** · Pakai ini deh.

**22:14** · Oke.

**22:16** · Kimi-nya taruh atas. Jadi, di bawah GLM saja.

**22:19** · Oke, Hermes combo, create ya. Nah, nah, kalau kita pakai fallback, jadi pakai urutan ya. Yang pertama GLM, kedua Kimi, terus Nemotron, terus yang baru yang terakhir. Atau kita bisa pakai round robin. Kita rotate. Kita pakai round robin saja ya, biar seru ya. Biar load-nya kebagi rata. Tapi kalau gua mau pakai round robin, ini Muse Spark-nya gua hapus saja deh. Jadi, kita sisain GLM, Kimi, sama Nemotron saja.

**22:45** · Oke, Hermes combo, anjay.

**22:47** · Bam! Kita juga bisa track usage-nya nanti, teman-teman, lewat usage and analytics. Kemudian saatnya kita connect ke Hermes-nya. Gimana caranya? Gampang.

**22:59** · Hermes setup.

**23:02** · Hermes setup, enter. Nah, di bagian provider-nya kita ganti pakai custom direct API.

**23:11** · Nah, kita masukkan API base URL-nya.

**23:14** · Karena ini pakai IP-nya VPS, kita bisa masukin sini, tapi ini bisa kita ganti sama localhost 127.0.0.1.

**23:26** · Kita coba aja dulu.

**23:27** · Enter ya.

**23:28** · Bab.

**23:30** · API key.

**23:31** · Boleh.

**23:33** · Create key aja.

**23:35** · Hermes key.

**23:41** · Dah.

**23:42** · Auto detect current.

**23:45** · Nah, ini yang penting teman-teman.

**23:47** · Jadi, dia bakal nge-detect Nine Router kita punya model apa aja. Tapi kan tadi kita udah buat combo ya.

**23:53** · Combo-nya ingat kan? Masa lupa? Ada Hermes combo kita.

**23:58** · Kita pakai round robin. Yang pertama GLM, yang kedua Kimi, yang ketiga Nemotron. Kita mau pakai combo-nya dong.

**24:05** · Percuma kalau pakai Nine Router, kita cuman pilih satu model. Pakai Hermes combo. Bab. Leave blank aja ini mah buat auto detect. Display name local, mmm mmm mmm mmm Nine Router aja.

**24:18** · Jay.

**24:19** · Select reasoning effort. Saya suka yang max jujur, tapi kan ini gratisan. Jadi, pakai X high aja. Oke?

**24:27** · Setuju dong?

**24:28** · Setuju.

**24:30** · Select terminal back end. Ya udah, keep current aja local.

**24:36** · Tadi Telegram. Udahlah.

**24:40** · No, enggak usah.

**24:42** · Restart the gateway to pick up changes.

**24:44** · Yes.

**24:45** · Kita tunggu ya, teman-teman ya. Kita pilih configure CLI-nya mau bisa apa aja. Video generation, Twitter, text-to-speech.

**24:55** · Udah gini ajalah dulu. Nah, browser-nya itu kita mau pakai apa ya?

**25:00** · Udah lah default aja. Configure Telegram.

**25:05** · Udah done dulu aja.

**25:07** · Nice. Coba kita tes di Herme-nya. Sudah terlihat gateway online kembali di chat Telegram-nya. Kita mau lihat.

**25:16** · Sekarang kamu pakai model apa ya?

**25:21** · Dia jawab, "Saya pakai Herme combo provider custom." Oke. Sekarang kita kenalkan diri kita. Gua bakal pakai perkenalan yang sama dengan Cloud Code gua kemarin. Ini gua ganti di memori kamu.

**25:37** · Oke.

**25:40** · Dah.

**25:43** · Gua udah perkenalan diri. Sama persis.

**25:45** · Oke.

**25:46** · Nah, kerennya di Nyan Router ini selama dia mikir, nanti bakal kelihatan usage-nya tuh. Uh, lihat teman-teman.

**25:53** · Dia lagi pakai Nyamotrone 3 Ultra berarti dari Nvidia.

**25:58** · Gokil enggak? Gratis loh di zaman sekarang ini. Kalian cuman beli VPS-nya aja. Udah banyak berubah kan zaman?

**26:03** · Jawabnya sih lama sih, Guys, jujur. Dan ini Cloudflare ada error. Gua mau matiin dulu.

**26:10** · Dan kayaknya combo ini gua mau edit.

**26:15** · Jadi yang dari Cloudflare ini gua mau matiin dulu.

**26:19** · Gua mau ganti pakai Open Code Free. Mewspark. Menurut saya cukup dua dulu. Mewspark-nya gua taruh atas deh.

**26:30** · Save.

**26:32** · Oke.

**26:33** · Coba kita dia bisa langsung auto berubah enggak?

**26:37** · Oke, good. Edit.

**26:41** · Nambah lagi deh.

**26:43** · Mimo Auto.

**26:45** · Backup tiga.

**26:48** · Backup ketiga. Ya, Nah, kelemahannya kalau gratisan tetap akan lama. Jadi, ya teman-teman menurut saya sepengamatan saya, ya tetap harus pakai provider yang berbayar, yang oke. Oke, akhirnya pesan gua tadi perkenalannya dijawab sama dia walaupun agak lama dan gua sambil tuning. Gua tanya 23.7, dia jawab 24.5, ya. Gua akuin tadi gua sambil tuning yang free-nya. Gua belum nemu setelan yang pasnya biar dia bisa cepat gimana.

**27:15** · Tapi ini menjadi alasan kenapa gua di awal langsung nunjukin kalian Cloud Code karena itu yang paling efektif. Kalian tinggal bayar aja udah selesai. Tapi, Bang, Herme kan lebih lengkap dan lain-lain. Dia bisa punya skill yang banyak. Dia bisa punya tools A, B, C, D, E. Oke, benar. Herme itu lebih lengkap. Tapi kalau kalian cuman invest 9 router yang free, kalian akan habis waktu di config free tier-nya.

**27:38** · Ngurusin combonya gimana yang terbaik, itu makan waktu dan enggak cepat. Kalau kalian langsung langganan misalkan ada out provider Cloud Code atau kalian langganan Open AI Codex, langsung connect-in bikin combo sederhana, langsung jalan pasti cepat karena bayar.

**27:53** · Jadi, menurut gua tetap harus invest di model yang berbayar, bukan LLM bansos untuk pekerjaan yang serius, bukan untuk pekerjaan yang mungkin trial, ya, teman-teman, ya. Karena lama sekali dia balas. Namanya juga free. Lu dapat gratisan, Bro. Bansos, Bro. Sebenarnya kapabilitas Herme lebih dari ini, teman-teman. Mungkin akan gua bahas di video selanjutnya, ya, teman-teman. Tadi kita set up aja udah lama banget dan setelahnya mungkin akan gua kasih tes sederhana, ya, perbandingan Cloud Code yang kemarin gua instal dan Herme itu dengan 9 router free edition. Gua mau kasih challenge sederhana sebenarnya bagus yang mana secara kompleksitas, secara jawaban, secara nalar.

**28:25** · Kita pikir. Walaupun udah ketahuan, ya, jawabannya, tapi kita kan penasaran, ya, bagus yang mana. Coba kita tes, ya.

### Komparasi Dengan Claude Code

**28:35** · Oke, tiba saatnya kita testing keduanya, teman-teman. Di Cloud Code gua, gua sudah siapkan prompt. Bikin satu halaman invoice generator buat freelancer.

**28:44** · Ketentuan teknisnya semua dalam satu file HTML, HTML, CSS, dan JavaScript ditulis di dalam aja enggak apa-apa.

**28:51** · File yang sama enggak usah pakai library atau CDN apapun. Simpan sebagai index.html di folder var www di Ubuntu server-nya. Setelah selesai jalanin di server intinya. Gua penasaran hasilnya bagus yang mana. Nah, disclaimer dulu karena gua pakai model gratisan di Nine Router, yaitu Open Code dan Nvidia Nemotron. Jadi ada keterbatasan response time mungkin. Jadi kita enggak usah compare seberapa cepat dia ngasilin result ya. Yang penting hasilnya kayak apa aja kita penasaran mau lihat. Gua jalanin ya di Cloud Code ya.

**29:21** · Gua pakai Opus 5 Max, kemudian gua run.

**29:29** · Gua jalanin juga di Telegram perintah yang sama.

**29:34** · Gua running.

**29:36** · Kita cek Nine Router kita di usage-nya.

**29:40** · Oke, lagi jalan dia. Tinggal kita tunggu hasilnya kira-kira bagus yang mana dan kalau buat kerja beneran pantas yang mana.

**29:49** · Bisa kita lihat teman-teman, untuk Cloud Code dia sudah selesai. Dia cuman butuh waktu 6 menit buat menghasilkan mock up HTML.

**29:59** · Oke, not bad.

**30:02** · Ya, namanya juga invoice generator sederhana. Tapi yang jadi masalah adalah Hermit Agent kita dengan Nine Router yang free stuck kerjaannya.

**30:14** · Gua harus setup lagi. Gua lagi coba tambahin Open Router, kemudian gua mau edit di Hermit Combo.

**30:21** · Kayaknya gua mau nambahin model Open Router-nya. Akhirnya jadi juga guys setelah gua uta-atik banyak banget. Gua tambahin tadi Open Router, Nemotron juga buat backup.

**30:33** · Nah, mungkin teman-teman bisa kasih insight juga ya buat gua ya. Provider apa yang paling bagus free? Gua lihat sih Kiro AI ini sih, tapi pakai AWS, AWS account-nya.

**30:45** · Agak lumayan ribet sih, dia ada Claude bahkan.

**30:48** · Tapi gua enggak tahu ya secepat apa ya, mungkin teman-teman bisa bantu komen ya.

**30:52** · Akhirnya sudah selesai dan gua mau coba buka alamat bukanya ini.

**30:57** · Gua ganti sama IP server-nya nanti.

**31:03** · Kebuka hasilnya kayak apa?

**31:05** · Dan ternyata tidak jauh berbeda guys.

**31:09** · Bagus bagus saja sih menurut gua.

**31:12** · Bahkan lebih lengkap yang ini eee buatan yang Herme Agent ini, daripada Claude Code ini terlalu sederhana menurut gua. Dia bisa tambah baris.

**31:22** · Ini juga bisa sih.

**31:24** · Ya bisa simpan PDF. Sama. Cuma desainnya ya sama-sama saja. Jadi kalau untuk tugas sederhana ya menurut gua ya teman-teman ya, provider free-nya Nine Router wajib kalian coba sih. Kalau kalian mau ngirit nih, gua tadi belum coba semua, ada Kiro AI, masih ada Ulama Cloud, ada Vertek, lu bisa coba semua, lu bisa pasang semua dan lu bisa masukin ke combo semuanya biar enggak ada delay.

**31:47** · Cuman tadi karena gua lagi setup, jadi gua nanya-nanya terus, ini prosesnya sudah sampai mana ya? Ternyata sudah selesai.

### Verdict

**31:56** · Oke, kita masuk di chapter penutup, sepertinya semuanya sudah tahu jawabannya ya. Jelas Claude Code unggul dan superior. Dengan respon 6 menit, kita bisa lakukan iterasi banyak.

**32:05** · Seperti yang gua bilang kemarin, fungsinya di manusianya. Misalkan Claude Code ya, dia 6 menit sudah ngasilin return. Dan dia kasih input lagi banyak loh. Misalkan nih, cara ngerjain dia gimana, bukanya di sini, yang ada di halaman apa, yang dia asumsiin sendiri apa, kita bisa iterasi terus secara cepat. Dan itu untuk kebutuhan profesional berguna banget, sangat-sangat berguna dong. Karena by default dia langsung bisa diajak mikir bareng sama kita. Sementara yang tadi gua coba di Herme Agent plus Nine Router yang free, ya dia pasif-pasif agresif.

**32:38** · Dia enggak kasih apa-apa, dia enggak kasih feedback, tinggal kita suruh nunggu, bahkan kita penasaran masih jalan apa enggak nih, kita utek-utek lagi, utek-utek lagi, baru dia kasih result. Result-nya pun enggak lengkap, cuman alamatnya, asumsinya dia apa, ya jauhlah penjelasannya dari Claude Code dan hasilnya lama. Teman-teman, jadi buat teman-teman yang masih belajar, pelajar dananya terbatas ya pakai Herme Agent dengan Nine Router yang free tier, itu bagus banget. Kalian bisa ngerti Agent AI itu seperti apa, kalian punya waktu untuk ngulik, kesabaran untuk nyobain tools yang gratis satu per satu.

**33:11** · Tapi untuk profesional, saran saya bagusnya ya pakai Herme Agent ditambah dengan Nine Router tapi yang tier 2 mungkin. Tier 2 tuh apa? Ya tier 2 tuh model-model AI yang murah. Ya kalau mau lebih profesional lagi ya subscription Claude kalian konekin ke Claude Code, Codex, Gemini, Copilot, terserah kalian.

**33:30** · Tapi kalau jujur dalam hati gua, Claude Code bisa cover semuanya. Semua kapabilitas Herme bisa dibuat tools-nya sama Claude Code, gua udah cobain sendiri. Cuman kalau kalian mau gampang langsung bisa connect Telegram, connect WhatsApp ya Herme jawabannya Herme Agent dan bisa-bisa diulik banyak banget.

**33:46** · Kalian bisa instal macam-macam sih sebenarnya, tapi ya waktunya udah habis di video ini teman-teman buat ngajarin kalian tadi cara nginstal Herme Agent, cara nginstal Nine Router dan ngebandingin kedua-duanya. Teman-teman, gua pengen edukasi kayak gini itu bisa dinikmatin sama semua orang. Gua tadi berusaha menjelaskan dengan bahasa yang segampang mungkin dan kalau ada kesalahan teman-teman boleh koreksi dan gua mohon maaf teman-teman, gua juga ada keterbatasan. Sehari-hari gua enggak ngulik-ngulik banget juga, tapi gua ngerti aja cara gimana maininnya, cara gimana makainya dan gua mau share ke kalian.

**34:16** · Nah, sekarang tugas kalian adalah pilih VPS yang terbaik, tadi ada dari Hostinger udah terbukti ya SSH-nya bisa dibuka terus pakai browser enggak ada disconnect-disconnect, enak. Terus kalian bisa ngulik Herme Agent sendiri, ngulik Claude Code sendiri, ngulik Nine Router sendiri, cari free trial yang paling bagus, dan cari metode kerja yang paling bagus menggunakan Hermit dan Nine Router ini. Semoga teman-teman video ini membantu kalian. Gua berharap banget edukasi ini nyampe ke mana-mana.

**34:42** · Jadi, Agent Tik AI itu bisa dinikmatin semua orang, bukan menjadi hal yang eksklusif atau bahkan dijual kelasnya secara mahal. Enggak usah. Lihat video ini aja, kalian bisa instal sendiri. Thank you, teman-teman, kalau yang udah nonton sampai sini. Gua David Alva Sunarna undur diri. Jangan lupa subscribe dan aktifin lonceng biar channel gua makin berkembang. Thank you.