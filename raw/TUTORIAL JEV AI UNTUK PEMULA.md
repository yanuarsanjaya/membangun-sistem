---
title: "TUTORIAL JEV AI UNTUK PEMULA"
source: "https://www.youtube.com/watch?v=DaspSn5FbgQ&list=PLSY7f7O2V4qw&index=3"
author:
  - "[[David Alfa Sunarna]]"
published: 2026-11-05
created: 2026-11-08
description: "AI yang gak bisa nulis, gak bisa ngobrol, cuma bisa decision making. Namanya Jev, dari TypeSafe AI. Di video ini gua bakal jelasin pakai contoh apa itu Jev biar kalian paham. Gua tunjukkin juga kalau"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=DaspSn5FbgQ)

AI yang gak bisa nulis, gak bisa ngobrol, cuma bisa decision making. Namanya Jev, dari TypeSafe AI. Di video ini gua bakal jelasin pakai contoh apa itu Jev biar kalian paham. Gua tunjukkin juga kalau AI ini murah dan cepet, kita juga gak perlu repot makenya. #Jev #TypeSafe #ClaudeCode #AIAgent #AI #HermesAGent  
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
02:21 Apa itu Jev dari TypeSafe AI?  
09:26 Study Case Penggunaan Jev  
21:02 Verdict

## Transcript

### Intro

**0:00** · Gila kamu, Mas. Kamu yang gila. Baru sekarang loh kamu langganan AI sampai juta-jutaan. Kamu gak pernah perhatiin aku, Mas. Gila kamu, Mas. Kamu yang gila. Akhirnya mereka lempar-lemparan galon. Itu adalah contoh Dramok Teman-teman dengan tema kalau kita kebanyakan ngabisin duit buat langganan AI. Kenapa kita ngabisin duit buat langganan AI? Karena kita enggak ngerti AI mana yang murah dan bagus dan bagaimana cara memakai model-model AI itu yang banyak banget. Contohnya, karena kita enggak ngerti dan kita banyak uang, sok-sokan kita langganan cloue 100$00.

**0:32** · Padahal limitnya kepakai aja enggak pernah. Di satu sisi ada model lain, misalkan model bansos, GLM lah, deep si lah, yang ternyata cukup buat kita. Dan bukan hanya sampai di situ, Teman-teman. Misal kita pakai GLM.

**0:45** · GLM tuh juga banyak, ada 5.3 flash, ada 5.3 biasa. Disesuaikan dengan kebutuhannya. Kemudian untuk tugas-tugas yang sifatnya decision making, yes or no, ada lagi model yang bagus. Namanya Jeff dari typesave.ai. Oke, decision model tuh ada banyak. Ada dari Open AI juga, ada Clef dari Cloud Flare juga.

**1:05** · Tapi Jeff ini benar-benar breakthrough dan benar-benar cepat banget, Teman-teman. Mungkin kalian bakal bingung, "Bang David apaan lagi decision model." Gua bakal jelasin pelan-pelan buat kalian yang awam pun bakal ngerti lewat video ini, Teman-teman. Dan kenapa gua tadi pakai contoh dramok? karena foundernya Diogo Almeida. Orang yang dulu ikut ngebangun Open AI chat GPT yang kita pakai sekarang. Gua enggak ngerti lagi kenapa setiap kali gua lihat dia, dia selalu pakai jaket pink. Dan ada lagi salah satu pentolan Jeff namanya Ely Labs.

**1:32** · Setiap gua lihat dia, rambutnya, alis matanya, bajunya, semuanya pink. Gua juga enggak ngerti kenapa. Jadi contoh Drumgok ini cocok sekali buat personality founder-foundernya Jeff. Karena dandanannya Mas Rusdi sangat suka dan gua enggak bakal bahas seksuality seseorang. Udah stop sampai sini. Stop.

**1:49** · Itu cuman bercandaan Dramok aja.

**1:51** · Kebetulan cocok sama founder-foundernya.

**1:53** · Gua enggak bahas lebih lanjut. Terserah mereka mau suka siapa dan terserah mereka mau memilih hidup bagaimana. Yang penting mereka menghasilkan produk Jeff.

**2:00** · Lainnya itu kepercayaan masing-masing karena kita mau belajar di sini. Jadi hari ini gua mau kasih contoh nyata Jeff ke kalian dan bakal gua pakai buat kehidupan sehari-hari dan bakal gua integrate ke Herme Agent gua. Mungkin nanti ada cloue juga bisa kalian install skill-nya kalau kalian pakai cloude. Dan seperti apa sih use case Jeff yang paling bagus itu? Kita simak sama-sama di video ini.

### Apa itu Jev dari TypeSafe AI?

**2:23** · Jadi Jeff itu apa? Menurut Elly Laabs, salah satu foundernya Jeff dari typesave. Di awal kita bakal kesulitan ngerti apa itu Jeff. Sama halnya kayak teknologi Docker kalau kalian tahu atau AWS lambda di mana itu serverless function buat nge-serve API. Awalnya kita bakal enggak ngerti ini apaan sih gunanya buat apa. Tapi sekarang coba kita lihat siapa yang enggak pakai doker. Orang gila mana yang kepikiran gua mau virtualin coding environment-nya programmer-programmer. Ah, jadi mereka enggak usah ribet lagi kalau mau deploy ke staging production. Gua udah virtualin itu semua lewat doker. Orang gila mana yang kepikiran itu?

**2:54** · Programmer Indonesia enggak mungkin kepikiran. Ada satu teman gua pernah ngomong kalau kita ini semuanya rata-rata di Indonesia programmer cosplay. Kenapa dia bilang cosplay? Karena kita hanya understand layer atasnya aja dari coding. Apalagi di zaman EA ini kita enggak akan semakin understand fundamental. Untuk melahirkan produk-produk kayak Docker EWS lambda ataupun Jeff kita harus ngerti fundamental. Nah, di sini gua mau ajarin kalian fundamentalnya LLM tuh kayak apa sih sebenarnya? Buat kalian yang mau belajar, gua saranin buka website-nya typesave.

**3:25** · Oke, baca ini system one model and Jeff. Coba baca dulu biar kalian ngerti. Karena video ini singkat, gua mau kasih aja ke kalian. Jeff itu, EA yang enggak bisa ngomong, enggak bisa nulis, enggak bisa ngobrol, dan enggak bisa ngerangkum. Dia diciptakan untuk satu hal aja. Memutuskan, decision. Jika ada suatu hal, dia harus memilih ini tuh A atau B. Dia dibuat buat itu aja. Bang David, gua masih bingung. Oke, kita praktik langsung. Setelah kalian baca ini kalian udah baca misalkan, terus kalian pergi ke API Console. Nah, di API console ini ada namanya playground.

**3:58** · Sepertinya kalian enggak harus top up balance dulu enggak apa-apa, tapi gua udah top up di sini. nih. Jadi buat support mereka juga. Nah, kalian bisa top up, kalian pergi ke biling, gua udah masukin payment method gua, kalian bisa add fun minimal cuman 5 kok, jadi Rp100.000-an. Dan ini gua pakai macam-macam AC cg kagak habis-habis masih ada 10 dolar. Jadi irit banget.

**4:19** · Oke, sampai situ ya. Jadi tetap harus support namanya ada usaha ya di-support 5 Rp100.000 okelah buat kalian belajar.

**4:26** · Kalau udah kalian pergi ke playground di sini gua udah siapin, Teman-teman, contoh-contoh komen, spam, judul. Gua mau minta Jeff ini deteksi dan kita lihat coba seberapa cepat. Kita ambil sampel yang pertama, ya. Gua langsung paste di sini aja. Nama platformnya gua kasih Tol 88 karena orang yang main judul tuh Tolol emang. Dan ini salah satu contoh komen spam judul. Nah, di question gua mau yang pertama aja paling gampang. Evaluate how true something is.

**4:54** · Mengevaluasi ini tuh bener enggak sih.

**4:56** · Nah, instruction-nya gua ganti langsung ya. Is this online gambling spam comments. Apakah ini komentar spam judi online? Gua mau tanya itu aja kita run ya. 82% true yang amazing. Kalian lihat di sini dia menjawab dalam waktu 18 m teman. 1 detik ada 1000 ms. Dia menjawab 18 m. Cepat banget. Jadi kalau ada yang bilang nih susah banget nih ngeblok komentar spam judi online. Kalau comigj bilang kayak gitu kasih ini enggak mungkin itu susah.

**5:23** · Yang ada itu enggak mau. 18 mills satu komen masih bilang komentar judi online tuh susah dihilangkan. Bullshit itu. Bohong. Tapi pertanyaannya apakah boomers-boomers di sana ngerti Jeff? Kagak ngerti. Kayak GPT-nya aja gratisan. Damn. Enggak apa-apa gua keras. Bodo amat. Teknologi udah sampai sini. Pem judi online masih ada setiap hari di YouTube atau platform sosial media gua. Oke, kalau masih kalian enggak percaya, gua kasih contoh yang lebih komprehensif. Eh, tapi udah kepikiran ya Jeff ini buat apa ya?

**5:52** · Takutnya esensinnya enggak masuk.

**5:53** · Intinya dia buat GCion aja. Oke, gua sampai lupa jelasin ke kalian kalau Jeff itu dia hanya understand input bentuknya Jason. Jason ini apa? Ya gini, structured data. Jadi ini e state-nya udah gua set. Misalkan platformnya Instagram, content type-nya posten, total comennya ada empat. Dan ini secara coding gampang ya ng-structornya dan masukinnya. Apalagi ada AI sekarang dan gua mau set question-nya tuh kayak apa.

**6:17** · Gua mau set question-nya ini. Jadi dari komen-komen ini gua mau ngerti apakah Instagram komen ini termasuk online gambling promotional spam. Coba evaluate ya specific komen ini ya. Coba cari gambling slang, gambling platform promotion kemenangan yang dilebih-lebihkan ya. Depo 125 dapat R miliar tolol. Intinya gitu. Kalau kriterianya true ya ini spesific komen promosi judi online. Kalau false ya bukan gua run ya empat komen ya teman-teman ya. Seberapa cepat? 25 ms.

**6:46** · Lihat akurasinya lebih tinggi lagi. 93% 87% 91% 93%. Sangat-sangat akurat. Jadi kalau ada yang bilang nih susah banget nih ngeblokir komen judi online itu bullshit. Ada teknologi namanya Jeff.

**6:58** · Dan sebelum Jeff udah banyak decision model lainnya yang dikeluarkan platform lain. Yang ada itu enggak pengin aja bukan enggak bisa. Semoga edukasi gua ini masuk. Jadi dari sini bisa kita simpulkan kalau sistem one model ini lebih dekat ke developer. Tapi di zaman yang serba e ini semua orang tuh jadi developer loh. Kalian aja bisa bikin aplikasi sendiri lewat Hermagine kalian.

**7:18** · Kalian bikin website mungkin bisa 10 menit jadi website sekarang. Jadi siapa yang bisa menggunakan Jeff ini? Gampang jawabannya. Suruh AI kalian yang canggih itu. Misalkan di Herme kalian pakai GLM 5.3 kalian pakai GPT6 Astra Soul atau yang baru ada Tera. Nanti udah rilis Ding Tera atau Gemini for Argon kalian suruh aja ngobrol sama Jeff ketika ada tugas untuk decision sorting. Suruh Jeff kerjain itu akan makan waktu lebih sedikit, lebih murah dan lebih efisien.

**7:47** · Nanti akan gua jelaskan dan praktik, Teman-teman. Jadi Diogo Almeida ini walaupun setiap hari dia pakai jaket warna pink, dia ini pintar banget. dia itu udah muak sama LLM yaitu yang sistem two yang dirancang buat ngobrol sama manusia dan ggak efisien karena dia harus ngerangkai katalah, ngebuat kesimpulan lah, balikin result-nya ke kita yang kita bisa baca lah. Itu lama banget. Dan yang bikin paling lucu, LLM sekarang dibuat untuk menjadikan kita seperti dewa. Kalian coba ngobrol deh sama LLM kalian. Kalian pasti dipuja-puja, ide kalian pasti diterima terus.

**8:18** · Enggak ada kan yang protes, enggak ada yang akan kasih sanggahan, "Eh, lu goblok. Enggak mungkin begitu."

**8:23** · Enggak ada kan? Enggak ada karena terlalu didesain menjadi manusia.

**8:27** · Menurut gua, LLM yang bagus adalah yang bisa membantah kita. Kalau kita kasih apa, ya dia bantah. Enggak kayak gini caranya. Lu tuh salah. That's a good LLM. Dan Jeff ada di layer bawahnya lagi. Dia cuman buat decision. Dan Jeff ini sangat murah dan sangat cepat, Teman-teman, ya. Dari playground ini udah kelihatan, ya. Oke, sampai situ dulu. Mungkin udah ngerti ya bagaimana Jeff pekerja ya. Jadi dia buat decision aja, dia buat shorting. Misalkan ada email 1000, gua mau lihat dong mana email yang spam dia bisa. Asal question kita jelas, state kita juga jelas. Oke sampai situ dan kita enggak usah pusingin state dan question ini.

**8:58** · Kita suruh AI aja yang crafting. Setelah kalian ngerti nih Jeff kayak apa nih, mudah-mudahan kalian ngerti dan understand nih. Karena banyak video YouTube yang lainnya ya yang ngejelasin Jeff tuh muter-muter. Gua pengin kalian ngerti dan secara sederhana understand Jeff aja. seperti kalian understand docker, seperti kalian understand AWS lambda atau serverless function. As simple as that. Oke, kalau kalian udah ngerti sekarang di video ini kita bakal masuk ke praktik, Teman-teman. Let's go.

### Study Case Penggunaan Jev

**9:28** · Oke, di praktik kali ini gua bakal integrate Herme agent gua sama Jeff.

**9:33** · Bang, gua enggak pakai Herm Agent bisa pakai cloue. Kalau kalian buka console.typesave.Ii, AI aksesnya dari sini nih, API Console.

**9:42** · Kalian bakal dikasih quick start buat cloue code. Gua ajarin satu-satu biar enggak pusing. Misalkan di cloude code dulu, gua udah buat folder namanya Jeff Showcas. Kalian run aja cloude di sini.

**9:53** · Yes, I trust this folder. Atau di VPS kalian juga boleh. Gua sekarang pakai opus 5. Auto mode on, effort-nya x high aja cukup. Kemudian gua copy agent prom.

**10:04** · Kalian langsung paste aja di sini. dia bakal nginstal cloude plugin type save AI yang mana ada Jeff di situ. Itu buat cloude. Gimana kalau buat Herme Agent?

**10:15** · Kalau buat Herme Agent ada repository yang menarik buat gua dari username Care Popule namanya Herme Jeff Skills.

**10:22** · Buka-buka GitHub jadi ingat teman gua Raymond. Hai Raymond gua enggak mau bahas. Silakan kalian bahas sendiri.

**10:27** · Sebagai orang yang pernah dirujak netizen programmer IT di Indonesia masalah engine XCDN. Gua appreciate keberanian dia untuk berani diskusi dan open Zoom. atau Discord dan ngobrol langsung. Respect aside of the case that he made. Programmer Indonesia galak-galak. Enggak bisa kita salah sedikit disalahsin terus sama mereka nantinya. Oke, ini adalah GitHub-nya Herme Jeff Skill. Gua mau pakai ini, Teman-teman. Cara instalnya gimana? Ya udah tinggal ngomong aja ke agen-nya, enggak usah bingung. Jadi kalau kalian lihat di Telegram ini, Teman-teman, gua sebenarnya udah research dulu, tapi menurut bot gua paling bagus tuh ini.

**10:57** · Ya udah, lu suruh instal aja, mending install ini. Yang lama hapus aja. Nanti dia bakal minta namanya type save API key. Nanti kalian kirim aja API key-nya ke dia. Caranya adalah pelan-pelan ya, kalian ke API key, terus kalian create key. Misalkan namanya apa? KME agent 2.

**11:21** · Kalian create key. Nanti key-nya ini bisa kalian copy dan kalian kirim ke agen kalian buat dimasukin. Bang, tapi kan enggak aman lewat Telegram. Aman.

**11:31** · Nanti kalau agent kalian udah selesai proses key-nya kayak punya gua ini dihapus aja. Gua sebenarnya kirim di sini nih, di atas ini nih. Udah gua hapus. Aman. Clear. Kemudian setelah itu kalian make sure Jeff kalian udah terinstall dengan baik di Herme Agent.

**11:48** · Oke, karena gua udah install sebelumnya teman-teman dan gua mau video ini tetap singkat aja. Sekarang kita tes ya di HerM agent kita ya. case yang tadi.

**11:57** · Ignore chat gua sebelumnya karena gua udah testing juga buat make sure ke kalian kalau apa yang gua lakukan ini valid. Gua ada ini, gua mau copy. Coba tes Jef lagi dong. Nah, kalau di Telegram kalau kalian mau masukin source code, usahakan petik dulu tiga kali terus paste terus petik lagi tiga kali di bawah. Jadi nanti dia bakal jadi source code. Nah, ini adalah state yang tadi gua masukin di playground. Nah, aku mau tahu dong dari state data ini, apakah komen ini termasuk komen spam judi online?

**12:31** · Kasih tahu aku juga seberapa cepat Jeff proses ini. Oke, kalau kalian tadi petik tiga, hasilnya akan rapi kayak gini, Teman-teman. Jadi bacanya enak. Oke, kita tunggu Herm kita jawab. Oke, hasil run keduanya totalnya 1,79 detik. Run pertama kemarin 0,43 second. Selisihnya diis time. Oke, enggak apa-apa. It's oke. Latency API Jeff-nya itu 503 ms. Jadi yang lama itu bukan proses Jef-nya, tapi latency API-nya, which is cepat juga kok. Dan keyakinannya 86%.

**13:02** · Oke, mungkin itu enggak begitu relate testingnya, tapi enggak apa-apa. Kita harus coba testing tersebut buat memvalidasi Jeff ini berjalan benar enggak di Herme Agent kita. Oke, nanti gua kasihlah ke kalian atau kalian buat sendirilah testingnya.

**13:16** · Cash-nya gampang. Sekarang kita lari ke cloude. Setting-nya lagi berjalan. Kita tunggu aja buat selesai ya, Teman-teman ya. Gua menemukan hal yang unik ketika kita install di cloue code kayaknya dia udah ngerti account type save mana yang kita pakai. Gua enggak ngerti tadi perbedaan prom-nya apa. Dia udah ngerti kita tadi mainan playground buat mengklasifikasi Instagram komen sebagai komen judi online. Oke, gua mau tanya ya. Kamu tahu dari mana akun type save aku? Aku kan belum kasih API key. Coba kita tanya dia ya.

**13:46** · Ya menurut gua kalau kalian enggak yakin dengan security gua belum ngasih apa-apa kok dia udah baca account TPS gua ya. Ya kalian tanyain ajaalah ke dia. Coba kita tunggu dia jawab. Eh takutnya kan dia baca-baca account kita kan baca-baca history Chrome kita. Kalau kita buka gima.

**14:04** · Oh gua tahu enggak enggak. Dia dia belum ngerti account tesave gua, tapi dia ada di folder Jeff Showcase yang mana di folder Jeff Showcase ini gua ada playground.jason Jason yang mengklasifikasi Instagram comand. Oke, no problem. Update installed, restart to apply. Jadi aman ya, Teman-teman ya. Dia enggak tahu account kita kalau kita belum kasih API key. Restart dulu dah.

**14:27** · Oke, gua mau sediain API key-nya buat cloue code. Gua mau bedain. Create ke clou code. Here's the API key. Please make sure you keep it properly. Oke, kita tunggu. Oke, sepertinya sudah selesai setup. Gua mau tadi tes playground.jonjason Jason gua apakah bisa dibaca sama cloue code? Kalau sudah Jeff pakai kasih tahu aku seberapa cepat dia proses keputusan decision tersebut. Bam. Kita tunggu lagi. Sudah selesai, Guys.

**14:57** · Jadi, Jeff melakukan analisa komentar spam judi online ini per komentar ada di 290 ms.

**15:06** · Ini bisa dipercepat tentunya pasti gampang sekali caranya. Dan Cloue menyelesaikan semua ini dalam 2 menit 39 detik. Nah, ini adalah masalah LLM system 2, teman-teman. Lambat. Dan menurut gua Cloue sama Herme agent gua masih cepat. Herm agent gua bohong nih, Bang David. Lu enggak percaya? Oke, gua tunjukin ya. Gua kasih tugas yang sama ke dia jam 11.32 tadi siang. Dia bisa jawab jam 11.32 juga. Jadi di menit yang sama dia udah koordinasi sama Jeff dan menghasilkan result.

**15:37** · Ini pertama kali gua kasih tugas loh pakai skill yang tadi Herme Jeff skill. Sementara cloude code dia selesaiin ini dalam 2 menit 39 detik.

**15:46** · Semakin pintar model tersebut gua pakai opus 5. Ya, gua enggak tahu ya. GLM 5.3 juga pintar. Tapi semakin banyak kemampuan LLM tersebut akan semakin kompleks dia berpikir dan akan semakin lama nge-return jawaban ke kita walaupun udah diintegrate sama Jeff. Nah, di sinilah kenapa gua kasih contoh drama-drama. Gila kamu, Mas. Kamu yang gila. kamu langan AI juta-jutaan sampai enggak pernah transfer aku lagi. Anjay.

**16:10** · Karena kita ngehabisin uang kita untuk AI di tempat yang salah. Di edukasi ini, gua mau kasih tahu ke kalian, banyak AI yang murah dan bisa menghasilkan kapabilitas yang sama. Oke, satu di situ. Sekarang gua mau kasih contoh ke kalian. Hermi agent gua udah terkoneksi ke email gua. Dan kemarin di insta story gua, gua baru aja ngebuka lowongan driver pribadi dan kantor. Karena yang daftar banyak banget, ratusan orang kayaknya 200-an lebih. Untuk sortir email-nya sendiri gua bingung dan ketutup sama email kerjaan gua. Gua mau suruh Jeff buat nge-sortir mana email yang apply sebagai driver biar mudah.

**16:43** · Karena gua Insta Story di tanggal 26 Oktober, maka cari emailnya dari tanggal 26 Oktober 2026 saja. Pakai Jeff aja buat tahu seberapa banyak orang yang apply sebagai driver. Aku mau tahu seberapa cepat dia short email. Wis, kita tunggu jawaban dari Herm gua. Oh ya, sebelumnya gua udah tarik data email memang. Jadi ada di case ya, Teman-teman. Jadi, GLM gua 5.3 model utamanya. Dia enggak narik email lagi.

**17:09** · Udah ada email di tanggal tertentu di case gua. Oke, kecepatannya buat ng-sortir email apply driver ini gila banget sih, Teman-teman. 0,45 detik, cok. Gila, latency API-nya 296 ms, 273 email disort dengan 0,45 detik dengan biaya yang sangat murah. Seberapa murah?

**17:30** · Even balance gua gak berkurang 10 dolar.

**17:33** · Gua gak ngerti ini free tire limitnya seberapa besar tapi balance gua gak berkurang. Jadi angka finalnya ada 214 pelamar driver yang valid sejak 26 Oktober 2026. Dia shorting dari 273 email.

**17:47** · Bayangin lu punya email Rp50.000 Rp100.000 lu sorting something. Mana yang spam, mana yang marketing akan cepat banget pakai Jeff dan murah banget. Itu adalah kemampuan Jeff yang sesungguhnya teman-teman. Oke, Bang David. Gua masih enggak ngerti lagi nih.

**18:00** · Ini buat apa sih, Mos? Cuman buat shorting email doang. Oke, anggap Jeff ini kalau kalian coding itu adalah switch function yang canggih. Maksudnya gimana, Bang David? Switch function yang canggih? Oke, gua kasih contoh ke kalian. Kita lari lagi ke playground ya, Teman. Kita misalkan ketik password 1 2 3. Evaluate how true something is. Is this a strong password? Jawabannya 3%.

**18:23** · True-nya berarti bukan strong password.

**18:25** · Lah, gunanya buat apa? Jadi kalian kalau buat sistem buat ngedeteksi password yang strong atau weak, enggak usah lagi buat regex pusing-pusing, enggak usah lagi buat if else statement, enggak usah lagi buat switch statement. Kalau password-nya lebih panjang dari karakter, maka strong switch lagi. Kalau password-nya gini, nanti di-convert lagi ke regex buat deteksi mana yang huruf besar, huruf kecil. Function-nya kebanyakan. Langsung aja lempar ke Jeff.

**18:49** · Jeff, ini password strong atau enggak?

**18:50** · Enggak strong. Lempar ke UI. Ini kalian ibaratin if else aja atau switch statement yang canggih yang pakai AI.

**18:57** · Kalau misalkan kalian tanya ini strong password enggak ke cloue? Ya bisa. Tapi jawabannya lama dan mahal. Fungsinya Jeff ya ini misalkan kalian ada case lagi. Oke case sederhana deh. Ini sebenarnya gampang pakai regex juga bisa. Oke gini aja deh. David @itemail.com.

**19:15** · Is this a valid email? Nah, 5% true.

**19:18** · Misalkan kalau kayak gini 91% true buat mensortir suatu keadaan. Oh, ini emailnya valid. Oke, masuk ya. Dan case-nya enggak cuman email, enggak cuman password. Ada macam-macam case dalam coding kalian di mana kalian butuh sorting sesuatu atau mendecision sesuatu secara cepat. Dari sekumpulan set of data, kalian mau lihat apakah data ini masuk ke dalam requirement A atau B, itu bisa pakai Jeff. Jadi Jeff ini kalian enggak perlu komunikasi langsung sama dia. Kalian suruh code kalian atau AI agent kalian yang buat coding itu komunikasi aja sama Jeff.

**19:46** · Semoga kalian paham ya, Teman-teman sampai sini ya, Teman-teman. Sebenarnya gua penasaran pengin cobain ini pakai Cloue, tapi kayaknya hasilnya sama aja. Dan kalau kalian tahu, gua udah melakukan ini menggunakan Cloue dan dia kerjain ini ketika shorting. Gua tanya ya, kamu kemarin pasing email lamaran butuh berapa lama?

**20:05** · Gak usah fable anjir ini opus aja kelamaan kasih aku waktunya dong coba kita tunggu dia kemarin shorting email lamaran berapa lama gua udah dapat datanya teman-teman dia baca isi email semua pelamar aja butuh waktu 13 menit oke kita anggap itu juga shorting-nya 13 menit versus 0,46

**20:28** · menit tadi di Herme agent gua sejauh itu bedanya jadi yang dimaksud dengan sistem one model dengan spesifikasi tertentu aja lu cuman buat decision aja ini benar atau salah. Apakah ini lamaran driver benar atau salah? Udah itu aja tugas lu.

**20:42** · Jangan ke mana-mana. Oke, udah ngerti ya teman-teman ya. Jadi bukan berarti kita kalau langganan cloue 200 terus kita bangga kita punya model yang paling canggih. Bukan seperti itu cara kerja AI ini. Bukan canggih-canggihan, bukan mahal-mahalan. Tapi siapa yang paling pintar menggunakan tools yang tepat di momen kerja yang tepat. Itu yang membedakan kita sama orang yang ngerti AI dari hasil jualan kelas. Damn.

### Verdict

**21:04** · Oke, kita masuk ke kesimpulan aja.

**21:06** · Menurut gua, Jeff ini cocok buat keputusan berulang dalam jumlah besar.

**21:09** · Jumlah besar ini bisa raksasa masif.

**21:11** · Misalkan komentar spam judi online jumlahnya jutaan komen setiap hari.

**21:16** · Gampang pakai ja. Di zaman sekarang tuh enggak mungkin alasan komen spam judi online masih ada di mana-mana. Yang ada mereka enggak mau ngerjain dan enggak mau ngeluarin anggarannya. Ada buktinya pakai Jeff bisa cepat. Ngerti enggak Jeff masalahnya? Terus buat apaagi, Bang? ya, lu bisa nge-sortir customer service lu, inbox perusahaan lu, mana yang ini komplain, mana yang ini leads, mana yang harus lu follow up. Lu bisa shorting semuanya secara cepat dan murah pakai Jeff. Apalagi misalkan kalian mau analisa suatu data, sentimennya seperti apa, bisa pakai Jeff.

**21:44** · Kalian tulis question-nya, state-nya yang jelas, question-nya juga yang jelas, dan kalian gunakan AI agent kalian untuk komunikasi dengan Jeff. Jangan langsung. Dan teman-teman jangan salah menggunakan Jeff. Mereka sendiri mengakui kalau Jeff ini lemah di hitung-hitungan aritmetika dan membandingkan tanggal. Akurasi juga turun kalau inputnya panjang dan berisik banget, banyak noise-nya. Oke, Teman-teman ya. Jadi, gunakan Jeff untuk hal khusus, untuk decision aja. Apa yang butuh di-decide dalam pekerjaan atau workflow kalian pakai Jeff biar gampang gua tulis di sini, Teman-teman.

**22:17** · Jadi kalian harus punya AI agent yang mana gua tadi pakai Herme ya. Dalam Herme ini kalian harus punya model. Settingan gua adalah tadi GLM 5.3 menggunakan N router. Nah, model ini kalian harus bisa ngomong dengan skill Jeff-nya menggunakan skill ya ngomongnya ya tadi udah ada ya repository-nya ya.

**22:38** · Jadi ketika ada tas masuk model kalian ngomong misalkan kerjaan nih tas pasti lari ke EAI agent terus dilempar ke model langsung ke model aja. ya. Nah, model ini yang milih ini bakal diproses sama dia apa diproses sama Jeff kemudian di-eturn lagi hasilnya. Intinya seperti itu ya. Gunanya apa sih, Bang? Yang ngehemat limit kalian lah. Kayaknya Jeff ini ada free tire-nya. Coba kalian riset sendiri ya, Teman-teman. Tapi kalian tadi ngisi 5 dolar aja kayaknya beberapa bulan enggak habis deh. Semoga itu bisa menjawab rasa penasaran kita sama Jeff dari Typesave. Dan ini adalah teknologi baru menurut gua ya.

**23:09** · Walaupun beberapa platform juga mengeluarkan yang sama, tapi enggak ada yang viral banget kayak Jeff. Dan semoga dengan adanya teknologi baru seperti ini, gua berharap sekali banyak sekali perbaikan terutama dari take downside judi online yang merugikan masyarakat, komentar judi online yang merugikan masyarakat, semuanya bisa disortir pakai Jeff dan itu sangat-sangat posibel.

**23:29** · Sehat-sehat teman-teman buat kalian yang nonton video ini sampai habis, semoga bisa langsung kalian praktikkan di AI agent kalian sendiri yang kemarin udah gua ajarin pakai Herme, pakai open cloud, panjang-panjang semuanya bisa pakai Jeff dan gua harap kalian praktikkan itu ya, Teman-teman. Jangan cuma nonton video ini aja. Semoga edukasi gua ini bisa reach banyak orang dan orang gak harus beli kelas buat belajar Jeff. Bettek banget gua jujur. Dan kalian bisa gunakan Jeff dalam kehidupan kalian, dalam pekerjaan kalian, dan membuat kalian semakin sukses. Amin.

**23:58** · Jangan lupa subscribe dan aktifin lonceng teman-teman biar channel gua makin berkembang dan gua bisa beli motor baru.

**24:05** · Udah jujur aja. Gua David Alpa Sunarna pamit dan undur diri. Bye bye.