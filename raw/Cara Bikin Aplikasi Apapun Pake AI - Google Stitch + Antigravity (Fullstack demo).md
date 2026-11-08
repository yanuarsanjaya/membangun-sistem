---
title: "Cara Bikin Aplikasi Apapun Pake AI - Google Stitch + Antigravity (Fullstack demo)"
source: "https://www.youtube.com/watch?v=eow7GpWb7UI"
author:
  - "[[Raf Dev]]"
published: 2025-12-14
created: 2026-11-08
description: "Gua cobain design UI pake Google Stitch lalu terapin hasilnya untuk bikin aplikasi full-stack menggunakan Antigravity.Bikin PRD dengan MUDAH!https://ngodingpakeai.comCobain Nano Banana pro dan So"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=eow7GpWb7UI)

Gua cobain design UI pake Google Stitch lalu terapin hasilnya untuk bikin aplikasi full-stack menggunakan Antigravity.  
  
Bikin PRD dengan MUDAH!  
https://ngodingpakeai.com  
  
Cobain Nano Banana pro dan Sora 2 GRATIS serta Claim 500 Credit di PippitAI:  
https://pippitcreator.pxf.io/rafdev  
  
Source code:  
https://github.com/RafiulM/finance-dashboard-new  
  
Komunitas:  
https://sirkel.online/ngoding-pake-ai/about  
  
Diskusi di Discord:  
https://discord.gg/K66VSJnVTH  
  
Timestamps  
00:00 Strategi Workflow Coding AI Full Stack 2025  
03:54 Setup Antigravity & Penjelasan Model AI  
08:23 Brainstorming Ide & Planning dengan Gemini  
13:03 Generate UI Design Instan via Google Stitch  
16:01 Konversi Desain ke Code React dengan AI  
21:30 Planning Back-End & Setup Database Schema  
25:51 Implementasi API Endpoints & Database Migration  
30:04 Integrasi API Back-End ke Front-End  
32:46 Demo Final Aplikasi & Testing Fitur  
34:50 Upload Source Code ke GitHub  
  
  
#antigravity #googlestitch #aidesign #produkdigital #saas #gemini3 #opus4.5 #aicoding #belajarngoding #vibecoding #coding #ngodingpemula #ngodingpakeai #pippitai #nanobanana #nanobananapro #produkdigital #produk

## Transcript

### Strategi Workflow Coding AI Full Stack 2025

**0:00** · Di tahun 2025 banyak banget E coding tools yang ngerilis, banyak provider yang benar-benar gencar ya ngerilis model baru dan coding tools baru. Dan di video kali ini gua bakal nunjukin kalian strategi terbaik ya versi gua dan juga menggunakan workflow gua yang menurut gua itu paling optimal untuk ngebikin apapun ya aplikasi apapun full stack menggunakan AI dan gua juga bakal demoin gimana gua ngelakuinnya ya. Gua sebenarnya udah pernah ngelakuin ini ya, tapi itu cukup outdated ya.

**0:26** · E ya walaupun baru 3 bulan yang lalu gue nyoba pakai Quencli yaitu Euroding Tools yang gratis dan itu tuh mantap banget ya ee hasilnya waktu itu e walaupun gratis ya. Jadi tuh lu benar-benar bisa ngelakuin apa aja sih tanpa modal dan sekarang sebenarnya Quensialnya masih gratis.

**0:44** · Namun banyak tools lain yang udah rilis dengan ya harga yang gratis juga sih sebenarnya, tapi juga ada yang harganya lumayan terjangkau dan banyak tools lainnya yang udah update. Makanya gua bikin video kali ini ya. Nah, ini juga gua berusaha bikin sebeginner friendly mungkin ya. Tapi kalau kalian emang ada pertanyaan bisa langsung tanya aja di Discord gua linknya ada di description di bawah ataupun bisa langsung komentar insyaallah nanti gua balas. Nah, jadi langsung aja masuk ke workflow untuk ngebikin full stack app. Jadi itu sebenarnya kalau untuk full stack itu selalu dibagi jadi tiga tahap ya menurut gua ya.

**1:15** · Yaitu pertama ngelakuin planning ya. Planning di mana itu wajib banget ya sekarang konteks engineering. Kalau kalian enggak tahu bisa langsung tanya Google aja atau tanya AI. Jadi konteks engineering itu intinya ya kalian memberikan konteks yang optimal ya atau yang cukup untuk si AI agar bisa memahami secara bagus ya dan secara detail apa yang kalian pikirkan ya ide kalian dan nantinya akan dijadikan acuan ya untuk ngebikin aplikasi kalian. Nah, itu prinsip konteks engineering dalam AI coding ya.

**1:43** · Lalu setelah itu kalau misalnya plan sudah jelas dan kalian sudah verifikasi ya dan tentunya kalian wajib banget ya melakukan brainstorming lebih lanjut ya agar plannya itu benar-benar mantap itu kalian bisa mulai ee eksekusi em untuk menggunakan atau yang menggunakan tools kalian ya untuk melakukan coding dan membuat front end dan maupun back end. Sejujurnya sih ya lebih banyak lagi ya stepnya daripada ini ya. Enggak cuma tiga ini, tapi biar simpel gua bakal bahas tiga ini dulu ya.

**2:12** · Ini sebenarnya tujuan videonya tuh untuk lebih ke mengarahkan kalian-kalian ya yang mungkin agak masih bingung ya gimana sih bisa manfaatkan AI untuk ngebikin aplikasi full stack ya tanpa perlu ada sentuhan atau ada background bahkan ya background dalam e coding atau pemrograman. Dan selanjutnya nanti sih kalian bisa explore sendiri ya mau itu catatan sama AI. Cuma nanti gua kasih tips and triknya juga sih. Akan ada dua tools utama yang gua akan pakai ya di sini. Ini kalian bisa lihat nih dua logonya. Kalau kalian tahu nih, langsung aja komentar di bawah ya.

**2:39** · Tapi ini ee semua step atau semua langkah di flow ini tuh gua akan menggunakan salah satu atau bahkan kedua tools ini ya. E di mana pertama gua akan mulai dari planning. Jadi planning yang tadi gua bilang ya ini konteks engineering.

**2:54** · Intinya tuh kalian harus bikin semacam rancangan ya rancangan awal dari aplikasi kalian ya. Yaitu kalian harus jelas ya dengan jelas menunjukkan masalah kalian itu apa sih sebenarnya ya. kan pastinya bikin aplikasi itu pengin menjadi solusi dari satu masalah ya itu harus jelas. Nah, dengan penjelasan ee masalah ini ya AI nanti akan lebih paham apa yang kalian butuhkan dan kalian tentunya juga perlu menjelaskan juga ya kira-kira tuh flow dari aplikasi kalian gimana. Namun kalau kalian belum paham itu nanti kalian enggak apa-apa ya.

**3:19** · Kalau asalkan kalian ada problem yang kalian pengin tackle itu nanti bisa dengan AI-nya ya dia akan figure out lah ya kira-kira appfow-nya itu seperti apa. Dan yang terakhir dan paling penting yaitu adalah core features di mana pastinya ini adalah fitur-fitur utama yang akan ada di aplikasi kalian ya. Jadi di plan ini nanti ada tiga e tiga core points ini dan nanti gua akan nunjukin ya gimana cara benar-benar ngelakuin planning dan juga nunjukin gimana plan yang bagus dan gimana kalian bisa ngedit atau ng menggunakan AI ya untuk ngebagusin lagi si plan kalian. Oke, langsung aja.

**3:51** · Jadi untuk planning gua akan pakai Enta Gravity. Kalau kalian enggak tahu ini gua sempat bikin video full-nya ya di channel gua tentang Google Anti Gravity.

### Setup Antigravity & Penjelasan Model AI

**4:03** · Jadi kalau kalian enggak tahu ini tuh adalah AI IDE ya atau ya bisa dibilang code editor yang powered by AI.

**4:09** · Mirip-mirip seperti cursor dan kalau kalian pernah pai VS Code ini tuh benar-benar forknya VS Code sih sebenarnya. Ini adalah emang VS Code versi ditambahin AI-nya gitu lah. Jadi ada AI agent-nya dan macam-macam lah.

**4:21** · Ada fitur-fitur AI lainnya juga. Nah, jadi intinya Gravity ini itu dari Google ya, dari Google dan juga dia ada beberapa plan sih sebenarnya sekarang ya, ada dua ya sebenarnya e ya tiga sebenarnya kalau nanti gua jelasin yang ketiga ya. Untuk yang pertama ini tuh ada bisa free ya, jadi kalian bisa langsung download aja nyobain ee dia tuh cukup generous sih ya ngasih limitnya ya sesuai dengan apa yang dia ee umumkan di sini ya itu mereka ngasih. Tapi sekarang itu eh sistemnya itu per minggu ya.

**4:50** · Jadi, rate limit kalian itu lebih gede.

**4:52** · Namun, kalian kalau misalnya habis dalam seminggu itu kalian perlu nunggu riset di minggu depannya. Nah, ini gua belum jujur gua belum nyoba yang free ya karena gua pakai yang pro. Tapi ya kalau misalnya bikin satu proyek gua yakin bisa sih dengan si e anta gravity ini ya. Ini alasan utama kenapa gua sangat rekomen orang-orang untuk makai si anti graffiti ya sekarang di akhir 2025.

**5:16** · Karena ini tuh dia ngasih model terbaik ya untuk moding yaitu pertama pastinya untuk UI e itu menurut gua paling top sekarang sih Jamini 3 Pro ya. Itu kreatif banget ya ngasilin UI-nya itu bahkan kadang enggak seperti enggak kelihatan gitu kayak ini itu dibikin AI.

**5:32** · Lalu pastinya nih ada Sonet dan Opus 4,5. Kalau kalian udah lama ya ee pahami AI coding ini tuh benar-benar nomor satu sih. Benar-ben nomor satu sih untuk ngoding ya. Tapi ya masalahnya kalau di tempat lain kayak misalnya cursor segala macam itu tuh mahal ya karena dia nge-charge-nya biasanya per request gitu. Nah, sedangkan kalau misalnya di anti graffiti itu dia nge-charge-nya ya ini pakai limit ya di mana itu akan keet ya. Dan kalau kalian yang pro ee plan yang pro ya nanti gua bakal bahas ya.

**6:01** · Itu dia ngrisetnya bahkan sampai ya setiap 5 jam. Dan itu gua tuh ee hampir enggak pernah sih kena limitnya. paling sekali dua kali sih. Dan itu karena emang gua benar-benar lakuin apa gua benar-benar ngerjain berbagai macam project sekaligus dalam 5 jam tersebut ya pastinya habis sih. Nah, cuma ya enggak lama kemudian habis itu ngriset ya.

**6:21** · Untuk kalian yang mungkin udah nyobain Enta Graffiti namun eh ya yang gratis ya plan gratisnya namun ya sempat kena limit ya itu enggak masalah mereka ada Google AI Pro ya. Eah ini tuh nama ini tuh plan dari Google ya khusus untuk AI.

**6:36** · Namun yang ini tuh gua enggak paham sih, Google tuh benar-benar bakar duit kayaknya ya. Dia tuh juga selain kita dapat akses ke tadi itu ya ee yang riset itu jadi 5 jam untuk anti graffiti untuk akses ke model-model terbaik yang mahal itu juga kalian dapat 2 TB cuy. 2 TB untuk Google Drive. Nah Google Drive, Google Photos dan juga Gmail. Nah, ini gua udah download Anti Gravity. Sekarang gua bakal manduin kalian gimana cara makainya. Ya, pertama ini adalah hal ya screen yang akan kalian lihat pertama kali ya.

**7:06** · Ya, sebenarnya ada onboarding-nya sih, tapi setelah onboardingnya selesai bakal kayak gini.

**7:10** · Yang pertama kalian perlu lakuin itu adalah buka folder baru. E, ya itu kalian bisa bikin bebas ya. Ini gua bakal bikin dashboard finance gitu sih.

**7:19** · Finance AI ya. Sebenarnya belum ada AI-nya, tapi enggak apa-alah. Dashboard finance AI nanti kalian tinggal open aja. ya. Nah, setelah diopen ini bakal lihat workspace baru. Kalian bisa klik di atas ini ya, ada agent manager.

**7:32** · Kenapa gua saranin buka agent manager ini? Karena ini nanti akan lebih fokus ke AI ya, di mana kalian akan lakuin planning dan ini menurut gua view-nya lebih enak aja sih. Nah, ini pertama kalian jangan lupa ya klik eh di sini ya untuk ngeganti workspace karena gua enggak tahu kenapa sampai sekarang itu enggak nge-default ke yang lu baru buka gitu ya e workspace-nya. Jadi kalian harus cari dulu nih ya ini yang terbaru ya paling atas di gua. Nah. Sekarang kalian bisa milih wajib banget ngelakuin planning ya. Yang tadi gua bilang planning itu nomor satu.

**7:58** · Kalian harus maksimalin eh semuanya itu udah dijelaskan di awal yaitu dengan adanya si plan atau plan mode. Dan untuk model itu kalian bisa pakai Oppos 4,5 ya. Ini paling bagus. Eh, dan gua juga sangat sarankan sih untuk e secara umum sih e default model itu kalian gua saranin pakai Opus 4,5 yang thinking ini.

**8:20** · Nah, tapi sebelumnya nih kalau misalnya kalian emang masih bingung ya kalian tuh pengin bikin aplikasinya seperti apa, mungkin core features-nya dan appfow-nya itu kalian belum terlalu paham ya atau ada bayangannya, gua sangat saranin kalian kalau emang apalagi kalau kalian yang diplan gratis ya itu jangan pakai e Centa Graffity dulu sih untuk nge-brainstorming. Kalian bisa coba di Gemini ataupun di Deepsik atau di Kimi K2 ya, di mana kalian tuh bisa e nyalain thinking di sini itu mantap banget sih untuk ngelakuin planning.

### Brainstorming Ide & Planning dengan Gemini

**8:49** · Di sini gua bakal nunjukin kalian ya gimana cara bisa ngil planning dulu sebelum kalian menggunakan si e anti gravity ini ya.

**8:57** · Jadi ini prom yang gua bikin ya di Kimi.

**8:59** · Ee ini gua cuma bilang ya kayak ya ini seolah-olah gua emang belum ada gambaran sih ya ee apa yang pengin gua buat. Jadi di sini gua cuma mau jelasin ya masalah gua itu apa, terus kira-kira tujuannya itu apa yaitu di sini gua bilang ya gua pengin nge-tracking pengeluaran dan pemasukan dari perusahaan ya. Sedangkan ee untuk appflow dan juga c features-nya gua masih benar-benar buta di sini ya seakan-akan ya. Jadinya gua minta tolong dia ngejelasin kira-kira tuh core features dan itu seperti apa ya. Jadi kita langsung enter aja. Jangan lupa ya nyalain si thinking mode. Terus kita bisa lanjut di sini. Ini hasilnya dari si Kimi Thinking.

**9:29** · Namun menurut gua jujur ya menurut gua sih ini kurang bagus ya dibanding dari Gemini 3 ya yang kalian bisa cek di Google Gemini app di sini ya. Dan gua di akun ini tuh pakai yang gratis ya dan ini bisa akses ke yang thinking. Bahkan gua sampai beberapa kali prom itu kalian bisa lakuin secara gratis ya. Di sini gua udah bikin appflow-nya, terus juga ada core features-nya. Dan gua juga sempat nge-brainstorm dikit ya, ngedit-ngedit dikit. Ini gua minta ya kayak enggak usah banyak-banyak itu fiturnya, dikit aja gitu ya, yang basic aja gitu ya.

**9:56** · Di sini udah ditulis juga dan kalau emang kalian masih agak bingung itu kalian bisa brainstorming itu gua sangat sarankan terutama kalian yang masih pemula masih agak bingung ya atau belum terarah gitu ya. Nah, setelah kalian udah nganggap ini mantap ya si core features dan appflow-nya ini, kalian bisa langsung copy aja sih dari chatnya ya. Di sini kan ada tombol copy kalau di Jamini. Terus kita bisa lanjut ke step planning untuk bagian front end.

**10:22** · Sebenarnya sih jadi eh setelah planning dasar ya itu planning core features dan juga problemnya. Sekarang kita bisa lakuin planning juga ya. Tapi sekarang di front end-nya. Kenapa gua ngpisahin front end and back end itu? Karena menurut gua atau setelah gua beberapa kali ngebikin aplikasi dari nol ya, e itu kalau misalnya kalian langsung sekaligus eksekusi e ya satu prom atau satu plan itu kadang banyak yang miss ya. Jadi saran gua sih kita fokus dulu di front end dan nantinya kita bakal lanjut fokus di back end biar nanti sama-sama ya hasilnya lengkap gitu ya.

**10:56** · Nah, ini balik lagi di anti graffity gua bakal nge-paste dari plan tadi ya yang dari Gemini. Dan di sini gua pakai planning serta opus 4,5. Lalu di paling bawah ini jangan lupa ya kita bilang buat plan untuk bagian front end dulu gitu ya.

**11:13** · Nah, bahas UI dan juga navigasinya.

**11:19** · Nah, ini menjadi plan pertama kita untuk front end.

**11:23** · Kita bakal klik sendal muncul plan baru dari si Anti Gravity.

**11:31** · Plan awal dari Anti Gravity udah diselesaikan ya sama si Opus 4,5. Di sini fokus di front end plan-nya seperti yang tadi gua adaud prom ya di awal. Eh setelah kita lihat di sini ada banyak wirefame ya. Itu yang menarik ya. Gua sangat juga rekomen kalian ya kalau emang mereka enggak bikinin itu bikin namanya TSC wireframe ya. Di mana itu akan menggambarkan layout dari aplikasi kalian nantinya. Eh, contohnya seperti ini ya. E, ini untuk navigasi dan ini ya ada diagram-nya juga.

**11:57** · Ini juga kalau emang belum dibuat sama si AI-nya, gua juga saranin kalian bisa tulis tuh namanya tuh Mermit Diagram ya atau bahkan flowchart aja. Pasti mereka paham sih gitu ya. Dua hal ini tuh menurut gua akan sangat mempermudah kalian untuk memahami plan yang dibuat sama AI ya.

**12:14** · Jadi ini gua udah nge-review sih ini ya.

**12:16** · Jadi untuk flow dari aplikasinya sendiri seperti ini. Dari sini udah kegambar sih ee apa aja halaman-halaman yang dibutuhkan ya. Dan juga ini ada wireframe dari berbagai macam halaman.

**12:26** · Nah, salah satu fitur unggul dari si Anti Gravffavity itu saat planning kalian bisa ngasih komentar di sini kayak kalian tuh lagi ng-revisi skripsi ya gitu. Jadi ini bisa ngasih komentar ini gua nulis ee karena di sini gua lihat belum ada line chart ya atau ya semacam bagan gitu ya. Gua jadi pengen nambahin di sini gua komentar aja. Dan ini sisanya udah selesai sih, udah selesai. Dan sini gua bakal pencet proceed. Di sini dia bakal setelah pencet proceed ya, dia bakal ng buat plan yang baru ya berdasarkan dari revisi yang udah gua kasih.

**12:54** · Nah, sekarang udah jelas ya ditambahin ada line chart di sini ee dan ini menurut gua udah oke ya semuanya. Sekarang kita bisa lanjut ke step berikutnya yaitu kalau kita lihat di sini itu adalah kita bisa menggunakan namanya itu ini tools kedua yang akan gua bahas yaitu adalah stitch. Jadi fungsi stage ini adalah ngebuat semacam UI design ya dari aplikasi kalian. E semacam ya kayak Figma lah tapi ini full AI ya. Jadi kalian enggak perlu lagi ngedesain manual ataupun ya ngedit-ngedit sendiri ya. Kalian tinggal nge-prom nanti ngghasilin.

### Generate UI Design Instan via Google Stitch

**13:24** · Ini contohnya yang udah dihasilin dari prom gua sebelumnya. Ini cuma gua bikin satu prom sini. Itu udah nampilin kayak gini cuy. Ini mantap banget. Dan ini udah kalau enggak salah tuh udah ada ininya ya. Udah ada code-nya juga ya. Ada HTML-nya kalau enggak salah. Gua cek dulu, ya. Di sini ada view code. Nah, ini bisa ngelihat HTML-nya full. Jadi, kita bisa langsung kopas aja. Ini kita kasih ke AI nanti dibakal bakal dibikinin dan kita bisa integrasi ke back end. Namun karena gua udah bikin plan yang berbeda ya untuk ee aplikasi yang gua bakal buat di video ini, gua bakal nge-copy plan ini sih sebenarnya ya.

**13:55** · Jadi ya ini sebenarnya kalian tinggal kopas aja bagian-bagian yang penting ya. Dan di sini gua lihat tuh yang penting tuh kalian jangan sampai copy bagian teknisnya ya. Karena itu menurut gua terlalu ya enggak relevan sih kalau misalnya untuk UI desain ya. Kecuali kalian emang ada warna tertentu nanti kalian bisa sebutin juga. Nah, tapi kalau ini gua bakal cuma sampai sini sih sampai bagian dia ngebahas semua wireframe dan juga semua e detail-detail penting kayak misalnya tadi appflow dan juga ada si core features-nya ya.

**14:23** · Gua copy di sini dan gua bakal balik lagi ke sini dan gua paste. Nah, di sini gua bakal lanjut ya e biar dia ngebikin desainnya dulu dan jangan lupa ya ini bisa ada mobile app dan juga web. Gua bakal pilih yang web design nih. Gua pakai 3.0 Pro karena ya itu paling mantap sih ya sekarang ya.

**14:41** · Jadi langsung aja kita generate dan gua bakal tunggu sampai nanti selesai ya desain pertama. Nah, ini udah kelar ya.

**14:47** · Mantap banget sih menurut gua sih ini ya Google Stitch ini ya. Ini tuh dia walaupun masih beta tapi bro ini gua cuma satu prom tadi ya yang hasil plan kita ini hasilnya seperti ini. Dia langsung benar-benar nge-generate semua halamannya sih. Ini gua agak takjub juga sih gua soalnya masih agak minim ya pengalamannya menggunakan aplikasi ini.

**15:06** · Namun kalau kita lihat di sini tuh mirip-mirip desain kayak yang di drible lah ya gua ngelihatnya ya. Cuma ini mungkin lebih fungsional ya karena ini sesuai dari apa yang sudah kita planning ya. Kayak misalnya ini udah ada line chart dan ada tabel segala macam. Ini juga dari sisi theme-nya atau temanya itu gua tadi enggak terlalu ini ya ng-mention ya dan tapi dia karena mungkin ada intuisi sendiri atau ada ya mungkin default di system prom-nya ini dia ngebuat warnanya itu hijau mungkin karena duit ya atau finance gitu.

**15:32** · Dengan adanya desain-desain ini kita sebenarnya sudah bisa mulai sih ngekonversi biar bisa jadi code atau istilah lain itu adalah slicing ya. Walaupun di sini sebenarnya udah ada code-nya ya yang tadi kalian lihat di sini wal tapi di sini kan ee dia itu benar-benar hanya HTML ya, sedangkan kita sebenarnya pengin pakai framework ataupun library untuk mempermudahkan si AI-nya ataupun nanti kita sendiri ya dalam mengembangkan aplikasinya. Nah, sekarang untuk kita bisa slicing ya di anti gravity kita cukup pencet more.

### Konversi Desain ke Code React dengan AI

**16:01** · Di sini sekarang ada fitur baru namanya itu export ya bisa langsung ekspor ke zip di sini. Jadi, gua langsung aja nih ekspor ke zip. E, kita eksport. Dan ini kalau kita buka itu harusnya ada HTML plus si fotonya ya. Nah, ini benar ya, ada screen-nya dan juga HTML-nya. Nah, dengan ini kita bisa langsung buka entagraffiity lagi dan gua bakal buat chat baru. Bisa langsung klik sini aja ya, conversation baru. Di sini gua buka eh code ini dan juga si screen.

**16:27** · Ini kita bisa sebenarnya tuh mulai satu persatu dulu ya. Jadi, satu halaman satu halaman. Namun karena ini di awal, gua bakal ngmention beberapa hal di prom-nya.

**16:40** · Oke, ini udah gua prom. Jadi tadi gua enggak bisa touch HTML ya eh file-nya.

**16:45** · Jadi gua langsung aja kopas full code HTML-nya untuk halaman pertama yaitu yang dashboard di sini ya. Dan ini gua juga udah attach screen-nya eh biar dia ada gambaran yang kira-kira seperti apa secara visual. Sini gua sempat juga mention ya untuk menggunakan React di Fight dan di mono reipo itu. Kenapa?

**17:02** · Pertama React itu adalah kalau kalian enggak tahu yaitu library UI ya. Eh library JavaScript untuk UI yang paling banyak digunakan ya di dunia. Jadi gua yakin resource-nya itu paling banyak di bisa diakses ya sama si AI-nya ini sendiri. Jadi akan lebih bagus hasilnya.

**17:19** · Lalu ya dia juga akan mempermudah kita sih nanti dalam mengembangkan si aplikasinya karena ya dia ada berbagai macam e practices yang bisa dilakuin yang kita enggak bisa lakuin kalau misalnya cuma pakai HTML gitu ya. Lalu kenapa gua pakai Fight yaitu e bundler e pokoknya itu jadi lebih enak lah kalau kalian misalnya ngebuat aplikasi-aplikasi web itu ada hot reload terus juga nanti gampang nge-build dan untuk ng-edeploy-nya akan dipermudah juga ya. Dan terakhir ini kenapa gua pakai mono Ripo itu karena kalau kalian enggak tahu e biasa kan Ripo biasa itu satu aplikasi ya satu repository ya.

**17:48** · Eh, tapi kalau misalnya dengan Monoripo ya ini karena gua bakal nanti ada bagian servernya juga. Eh, gua jadi bakal ngebuatnya si React dan juga si aplikasi web servernya atau yang akan handle MPI itu atau backend ya bisa dibilang ya, itu akan ada di satu repository. Nah, kita langsung aja bisa nge-send dulu ini dan dia dan jangan lupa kita pakai planning dan untuk eh karena ini pakai front end atau ngebikin UI ya, gua bakal milih Jamin 3 Pro yang high ya karena menurut gua ini jauh lebih jago sih dalam hal UI ya.

**18:18** · Jadi, gua langsung aja ini sekarang kita sendikin plannya dulu ya. Ini plan yang udah dibuat sama si Gemini 3 Pro. Gua lihat sih udah oke ya sebenarnya karena ya pasti udah oke karena tadi udah cukup detail ya prom-nya ee dengan code yang gua kasih dan juga e instruction yang di atas tadi ya. Sekarang gua tinggal proceed aja.

**18:41** · Tapi kalau kalian emang ngerasa ini masih kurang pas ya kalian bisa langsung review lagi dan kasih komentar seperti yang tadi gua demonstrasikan ya di awal untuk plan yang pertama tadi ya. Kalau misalnya udah oke langsung aja pencet proceed dan kita tinggal tunggu sampai nanti dia kelar implementasiin segalanya ya.

**19:00** · Kayak gini ya. Kalau misalnya udah selesai si Anta Gravffity ngejalanin plannya dia bakal ngebuat ya sebenarnya sih ada walkthrough ya di sini ya kalau kalian lihat ya. Cuma gua enggak bisa.

**19:09** · Oke, searang bisa gua akses. Jadi, walkthrough, dia cuma ngejelasin apa aja yang dibikin dan diubah ya sama dia. Dan di akhir itu dia nunjukin gimana cara ngejalanin serta ya menginisialisasi proyeknya lah ya. E, nah setelah gua lihat di sini kan cuma simpel aja sih, tinggal nge-install ya, install dan juga PNPM Dev. Kalian bisa buka editor kalian ya. Di sini gua udah buka dan tadi gua udah jalanin. Sebenarnya sih, gua cuma coba ya. dan itu udah berhasil ya, tinggal instal PNPM dev.

**19:36** · Habis itu di sini bakal muncul link kalian tinggal copy ya atau bisa langsung conttrol klik atau komen klik di sini dan ini bakal kebuka di browser kalian ini udah full jadi ini dia sekarang pakai R ya namun ya belum ada fungsinya apa-apa ya karena ini baru ya HTML doang ya yang dari sini tapi kalau kalian lihat tuh ini benar-benar sama ya kayak ini ya. Nah, udah mantap ya. Dan pastinya ini udah akan lebih mudah di ee kembangkan ya karena udah implement React dan di sini juga udah ada tabelnya segala macam ya.

**20:09** · Di sini ada sedikit bug lah tapi enggak masalah ya. Nah, sekarang sisanya gua bakal e nerapin dulu ya semua screen-nya. Tapi mungkin enggak semua sih gua tambahinnya cuma beberapa yang penting aja sih untuk video ini ya. Nah, gua tadi udah jalanin beberapa prom lagi ya di mana gua cuma kopas aja sih ini masing-masing halaman ya. Gua copas, gua paste ke entry gravity dan ini hasilnya sekarang ya. Gua mau demoin dikit ya.

**20:33** · Ini masih front and only. Jadi ini udah ada login screen bisa ya login dan ini ada sign up juga ya kalau belum punya akun. Terus ya login ya wajarlah. Terus ini tampilan pertama ini udah dibenerin juga sih. Eh ada yang belum ya ternyata sor. Nah, terus ini untuk halaman kedua ya udah ditambahin transactions dan ini ada reports, reporting dan juga untuk setting dan ada udah sih itu aja ya dashboard pertama habis itu ya.

**20:59** · Nah, kita lihat sekarang ini transaksi bisa mencetak pemasukan, pengeluaran report juga ini bisa diekspor ke CSV dan ada sedikit overview-nya ya. Terakhir ini kategoris nawahin kategori untuk nanti disimpan atau diset ya pas kita ngelakuin transaction. Dan ini juga ada dropdown seperti ini. Cuma ini mungkin fungsinya belum kita terapin ya. Dan ini untuk logout ya wajar aja sih gitu.

**21:26** · Nah, sekarang setelah frontend-nya udah semua sesuai ya dengan plan kalian dan sekarang bisa mulai implementen back end-nya di mana nanti ada database dan juga API end points. Mari kita mulai ya untuk planning bagian back end-nya.

### Planning Back-End & Setup Database Schema

**21:40** · Cukup buka aja Enter graffiti dan ini bisa seperti biasa bikin conversation baru. Dan sekarang gua bakal bikin promp-nya sedikit.

**21:49** · Ini prom-nya yang gua tulis sebenarnya simpel aja ya karena kan kita udah bikin front end-nya. Sebenarnya ada dua opsi sih di mana kalian bisa ngikutin yang gua tulis di sini ya. Di mana gua cuma nyuruh dia ng lihat aja gitu kan nge-analisis apa yang udah diimplemen ya di aplikasi kita yaitu yang tadi udah diimplementen di front end-nya ya di sini. Dan itu kan udah kelihatan semua ya, ada dashboard, terus apa aja yang mungkin perlu dibuat di back end-nya. E menurut gua sih AI udah jauh lebih canggih sekarang ya untuk melakukan itu dengan mudah.

**22:17** · Namun kalau misalnya emang aplikasinya cukup besar ya yang kalian buat dan itu masih front end-nya doang, kalian bisa sih pakai lagi ya plan yang di awal tadi ya, yaitu yang kalau gua sendiri sih buatnya tadi di Jemina ya, yaitu yang menjelaskan app flow serta core features atau mungkin kalau kalian ada dokumentasi lainnya bisa ditambahkan juga. Namun karena gua yakin sih dari menganalisis front end itu udah bisa menentukan ya apa aja yang dibutuhkan di backend-nya.

**22:43** · Jadi gua pakai approach ini dan untuk tag-tagnya sendiri ini sebenarnya kalian bisa brainstorm sendiri lah ya sama chatbot kalian. E namun kalau gua seperti biasa gua nge-implement apa yang paling sering digunakan aja sih. Dan juga kalau kalian lihat di sini itu sebenarnya ada beberapa yang gua cukup nyaman menggunakannya ya. Dan juga pengalaman gua sendiri sih ini emang paling enak digunakan dan juga untuk deployment-nya itu juga e lebih mudah ya. Jadi ini yang gua pakai tentunya paling wajib tuh kalian perlu pakai framework ya.

**23:12** · Ee gue sangat sarankan jangan ya inilah pokoknya dengan ada framework ini tuh akan jauh mempermudah kalian nantinya akan ee dalam tahap e pengembangan lanjutan dan juga EAI-nya juga akan lebih enak sih dalam ee mengembangkannya ya. Lalu untuk database serta ORM itu wajib banget ya kalian pakai ORM. Kalau kalian enggak tahu ORM itu apa bisa tanya AI ya. Tapi ya secara singkat ORM itu mempermudah kalian atau aplikasi kita ya itu untuk berinteraksi dengan database melalui code.

**23:43** · Jadinya nanti semua skema database-nya dan juga semua operasi insert dan segala macam itu enggak perlu lagi pakai raw query ke database-nya. akan lebih terstruktur dan juga akan lebih mudah untuk e typings-nya ya untuk dipahami juga sama AI-nya. Dan terakhir untuk authentication gua pakai Better O karena menurut gua sih ini nomor satu sih e untuk di TypeScript ya. Tentunya e Better O ini gampang banget nanti kalian integrasi.

**24:08** · Kalau kalian pengin pakai Oot kayak Google atau GitHub atau Twitter itu gampang implementasinya dan juga secara umum ee dia juga support banyak banget database dan juga ORM. Dan makanya ini semua tiga ini tuh ee semua tuh saling ee sebenarnya semuanya sih ini empat ini tuh saling berhubungan ya di mana itu mereka saling ee memiliki compatibility yang cukup baik ya satu sama lain gitu.

**24:30** · Nah yang terakhir ini untuk best practices-nya tuh sebenarnya menurut gua sih kalau dari AI yang eh baru-baru ini tuh cukup bagus ya eh untuk memahami eh best practices dari berbagai macam framework. Namun biasanya tuh gua perlu secara eksplisit ngejelasin ya kalau gua tuh pengin ada pemisahan antara services dan eh routes ya atau end points di mana kalau ya singkatnya sih ini ee biar nantinya kalau misalnya kita ingin menggunakan suatu function lagi gitu ya di endpoint yang berbeda itu bisa tinggal manggil service tertentu ya.

**25:00** · E namun kalau kalian masih agak bingung ini mungkin ee ya kalau kalian pemula mungkin ini agak aneh ya itu kalian bisa chatan aja sih tanya lagi ke AI ee apa yang gua maksud di sini. Jadi ee balik lagi ya ee ini semua ini udah gua tried and tested lah ya dan ini menurut gua paling oke ya.

**25:18** · Dan selanjutnya kita pastinya harus pakai planning ee kembali karena ini prom pertama dan balik lagi kita harus pakai konteks engineering untuk memaksimalkan ee hasil dan meminimalisir halusinasi. Dan ini kita akan pakai modelnya itu Opus 4,5. Karena secara umum sih e Opus 4,5 ya. Untuk backend pengalaman gua sih paling oke karena dia emang eh coding moral terbaik ya. Dan kita bisa lanjut aja sekarang kita sendnya sampai selesai nanti kita review dulu.

### Implementasi API Endpoints & Database Migration

**25:51** · Nah, ini yang gua suka ya. Ini plan dari Op 4,5 dan wah mantap sih menurut gua ini ya dari segi analisisnya udah on point ya. Jadi, udah udah tahu ya apa aja yang dibutuhin untuk masing-masing halaman. Ee dari high level ya secara high level dijelasin di sini dan setelah itu dijelasin skema dari database-nya.

**26:09** · Tapi kalau kalian yang mungkin kurang ini awam ya, masih agak awam gitu ya ee terhadap database, intinya itu database itu tempat ya pastinya tempat kita nyimpan data ya. Dan database itu ada strukturnya dan ada yang istilahnya itu skemanya di mana itu ya kita harus nentuin apa aja yang perlu disimpan ya.

**26:24** · Dan itu bisa dibilang eh colums ya kalau misalnya di Postgress atau SQL eh based database gitu ya. Kayak contohnya ini ada pastinya user itu memiliki kalau gua biasa zoom in di sini ya, itu user ada memiliki nama pastinya email segala macam ini ya merepresentasikan masing-masing objek yang nantinya akan dipakai gitu ya di aplikasi kita atau disimpan ya datanya.

**26:46** · Dan selanjutnya ini ada perubahan dan strukturnya. ini ya sebenarnya ee hanya menjelaskan aja sih best practices-nya yang udah diimplementen ya yang tadi gua udah bilang yaitu memisahkan antara services dan juga em routes-nya ya. Di sini udah jelas dilakukan. Setelah itu ini ada

**27:05** · skema ini sebenarnya sama sih dari yang tadi ya dari database ini ya database skim cuma ini dalam versi cod-nya dan ini karena pakai drizzle warm jadi didefinisikannya itu dalam eh typescript ya di sini out.ts dan nanti pastinya ada file-file lainnya. Dan terakhir untuk endpoints kalau kalian belum paham juga ya. Jadi API endpoints itu anggap aja semacam ya cara si back end server ini berkomunikasi dengan si front end ya.

**27:31** · Kalau misalnya back end itu adalah dapur ya, front end itu tempat ee meja ya, meja di mana user-user kalian itu berada. Dan si endpints ini atau API itu fungsinya yaitu sebagai pelayannya ya yang mengantarkan makanan dari si eh backend atau si kitchen atau dapur ya ke meja masing-masing user.

**27:49** · Nah, itu ee ini bisa dilihat ya, ini masing-masing endp itu punya purpose-nya sendiri dan juga ada metodenya sendiri ya. ada post di mana post itu untuk ngebuat atau nge-create atau insert ya suatu data ke database ataupun ya melakukan operasi-operasi yang semacamnya gitu ya.

**28:07** · Dan ada juga get di mana get ya dari istilahnya sendiri itu adalah mendapatkan gitu ya atau mengambil ya mengambil mau itu mengambil data dari dar dari database ataupun operasi lainnya yang ee bermiripan ya. Kurang lebih seang e penjelasannya kurang bagus ya kalian bisa chatan aja sih langsung sama gravity jelasin gitu ya kayak gua tuh e orang awam atau gimana tolong jelasin ee lebih jelas gitu ya. Nah itu nanti bakal ngasih penjelasan yang lebih bagus atau kopas aja terus kirim ke chatboot favorit kalian ya. Tapi overall ini udah oke sih.

**28:37** · Gua gak perlu lagi ini nge-review, sori ngomentar atau apa, gua langsung proceed aja. Terus kita tinggal ya nyantai dikit ya, nunggu sampai kelar.

**28:49** · Implementasi back end-nya udah selesai ya berdasarkan plan yang tadi dibuat ya.

**28:53** · Dan ini di akhir itu dia nunjukin gimana cara set up-nya. Tapi tadi ada beberapa hal yang kurang sih gue temuinnya, yaitu dia belum bikin cara untuk ngemulai database-nya. Jadi, gua tadi nge-prompting dikit ya di sini di mana gua ya bilang aja gitu kayak gua tuh belum bisa ngejalanin doker kompos ya atau Postgras-nya gitu.

**29:14** · Jadi gua minta untuk nambahin di dokter kompos biar gampang ya dan gua bisa langsung connect dan dia langsung e ngasih tahu gimana caranya connect dan ngejalanin servernya atau post eh postgas database-nya ya. Di sini juga gua lanjutin dengan membuat migration serta mengimplementasiin atau nge-push ya istilahnya nge-push migration-nya biar ke database-nya itu udah kepopulate sama kolom-kolom dan ya skemanya gitu ya yang tadi udah diplanning di awal ya.

**29:39** · E ini ya sebenarnya ini standar sih ya dari backend server eh atau database lah ya dan ada adanya migration system itu adalah best practices-nya. Kalau kalian belum paham ya itu gua kasih pointers-pointers aja sih dan kalian bisa ekspor sendiri ya karena itu ya sebenarnya simpel sih cuma mungkin perlu baca sedikit lah ya atau perlu penjelasan AI ya. Terus gimana untuk bagian API end points-nya? Ini sebenarnya tuh kalau ya optimalnya sih kita lakuin testing ya menggunakan kayak Postman segala macam atau Curl itu juga bisa minta AI untuk testing.

### Integrasi API Back-End ke Front-End

**30:11** · Tapi karena di sini gua biasanya tuh langsung aja sih terapin ya gua langsung integrasi backend API-nya ini eh gua kopas aja atau enggak ya gua minta si AI untuk nge-implement eh berbagai macam endp ini di front end ya biar nanti kalau misalnya kita udah ke dashboard segala macam itu semua udah connect ke back end-nya. Jadi, ini data pakai data real yang ada di database.

**30:36** · Jadi, gua bakal nge-prompting sekali atau dua kali ya untuk ngebuat plan agar bisa ngeimplementasiin apa API and points yang sudah dibuat ya di back endpakai di front end.

**30:51** · Nah, ini promp yang gua pakai. Jadi, gua yakin banget sih Oppos 4,5 tuh bisa langsung analyze apa yang udah diimplement ya di server tadi ya atau di IPI e routes-nya. Jadi, ini gua langsung mention aja file-nya. biar dia langsung enggak perlu nyari-nyari lagi ya. Dan gua juga bilang untuk implement di front end-nya. Dan terakhir di paragraf ini ya, gua nge-mention gimana cara ngeimplementasiin end points-nya atau cara ngelakuin data fetching-nya. Jadi kalau kalian enggak tahu ini ada library namanya 10 Stack Query.

**31:18** · Ini tuh mempermudah banget ya untuk e kita ngembangin atau ngelakuin data fetching karena state-nya itu dan juga e loading state dan ya pokoknya caching-nya itu segalanya itu udah di-handle sama si library ini. Dan gue juga suruh untuk nerapin practices lainnya ya, seperti ini untuk ngemisahin client service-nya yaitu untuk API client-nya itu dipisah ya dari hooks-nya di mana nanti dari eh 10 stack ini itu akan dibuat di dalam berbagai macam custom hooks. Kita bisa lanjut ya dengan Opus 4,5.

**31:48** · Lalu gua juga jalanin planning ya agar nanti bisa review dulu sebelum dieksekusi. Ini plan yang dibuat ya sama si Opus ya. Ya, ini bisa dilihat udah semua eh fitur atau semua method-nya itu dibuat di plan ini.

**32:03** · Dan sekarang lagi dieksekusi. Tadi gua langsung proceed aja. Dan juga dia ngebuat task list gitu ya. Jadi udah lengkap bangetlah di sini kalian bisa buka task list ya. Nah, ini task list-nya. Kalian bisa lihat ya apa aja yang bakal dilakuin sama si Anti Gravffity. Eh, dan sekarang kita tinggal tunggu aja sih sampai semuanya selesai dan pas udah selesai kita bisa lakuin testing. Gue jalanin total tiga prom ya.

**32:23** · Yang pertama itu yang tadi ngebikin implementation plan. Terus gua proceed aja sih. Dan ini task yang udah diclearin ya semuanya udah selesai. Tapi pas gua nyoba pertama kali itu ternyata ada beberapa halaman belum kesambung ya sama yang udah dibikin untuk integrasi ke backend. Jadi gua bikin prom sekali lagi terus habis itu gua tes udah bisa.

**32:40** · Namun ada sedikit problem di dashboard-nya di mana itu enggak nge-update chart-nya. Jadi gua bikin lagi nih prom sekali dikit aja sih. Dan ini udah selesai semua ya. Udah mantap ya. Nah sekarang kita sign up ya kalau belum sign up. E tapi kalau udah bisa langsung sign in aja. Ini gua bakal sign in pakai email yang gua udah daftar tadi. Di sini password-nya. Sign in aja.

### Demo Final Aplikasi & Testing Fitur

**33:02** · Nah, udah langsung ke halaman ini ya.

**33:04** · Jadi tadi gua udah bisa ee ngelakuin transaksi dan ini udah nunjukin semuanya ya. Ee bukan transaksi si tapi tracking lah. Tracking transaksi. Dan ini tuh mirip banget ya sama yang udah dibuat di sini ya. Jadi itu gua suka banget ya.

**33:17** · Ini mantap banget sih menurut gua ya. Ee era AI sekarang tuh udah aduh udah gokil sih menurut gua ya. Ini gua sekarang tunjukin ya gimana cara ngenambahin record-nya ya. Tinggal ke transaction terus ini ada income atau expense. Dan kalau belum bikin kategori bikin dulu kategorinya di settings. Ini udah bikin dua ya sesuai dengan apa yang tadi di sini udah kita buat ya di sini ya. Udah mirip banget ya. Hampir persis sih cuma ya sedikit beda spacing segala macam.

**33:41** · Tapi enggak apa-apa ini udah gua tambah ini kalau mau tambah lagi bisa di sini ya. Ni tes create ini udah muncul. Terus kalau misalnya transaction ini untuk tracking ya. Langsung aja bisa tes di sini mungkin ee 10.000 eh 10 dolar ya dan ini income tanggalnya mungkin bisa kemarin ya terus save aja dan ini udah nah udah kalau refresh udah keesave ya ke database. Ini juga database-nya kita lihat ya udah ada semua nih categories dan attachments. Eh attachment belum keimplemen ya tapi enggak apa-apa.

**34:10** · Terus user eh transactions ini tadi udah transaksi ya, semua udah ke-save, udah ke link juga ke user dan juga ke kategori. Sekarang kita cek lagi eh fitur lainnya itu report ya atau laporan. Kita bisa eksport ya ke CSV ini semua. Eh kalau misalnya ada filter bisa diapply. Kalau enggak langsung aja ekspor. Di sini gua udah coba tadi.

**34:33** · Sekarang kita ee coba ini kan CSV ya.

**34:35** · CSV tapi bisa kita convert untuk melihat datanya di e kolom si uper colom-nya.

**34:42** · ini langsung next aja, next, finish. Dan ini udah muncul ya. Jadi udah selesai ini aplikasi full stack-nya. Sekarang ee yang tinggal kalian lakuin itu eh upload ke GitHub ya. Jadi gua end dulu ini caranya gampang ini tinggal git init aja sih. Git init itu untuk nge-initialize e repository-nya di lokal. Dan sekarang kita bisa bikin e komit pertama yaitu pertama git atau kalau kalian pemula ya.

### Upload Source Code ke GitHub

**35:08** · Nah, gua saya sangat saranin langsung aja di sini ya di sini. Nah, tapi ini kan ada ini ya, ada banyak banget nih e changes-nya. Ini kalian bisa bikin namanya itu git ignore ya. E git ignore itu gampang aja tinggal kalian ke root sini terus tambahin ini dgit ignore.

**35:23** · Nah, sini terus kalian tambahin aja note module sih ini seharusnya langsung eh sama invv pastinya dan ini pastinya eh sori eh dvi udah selesai. Sekarang kita tambahin ya di sini d eh tambahin semua sini mungkin harus ini ya enggak harus sebenarnya udah oke sih harusnya kayak ini ya. Nah, sekarang kita tinggal tambah semua. Ee oke. Nah, udah oke oke udah keegit ignore ya semuanya tadi.

**35:47** · Jadi ini sisa file-file yang baru ya selain dari node modules ini dan EN invv. Sekarang kita tinggal bikin komit pertama yaitu ya init aja sih paling ya.

**35:56** · Init terus komit. Oh ini ada yang baru juga ya ketinggalan init du lah ya kita buat. Nah ini terus publish branch. Nah tapi sekarang kita perlu e bikin dulu ya di GitHub ya untuk nyambungin ke GitHub.

**36:08** · Ini gua bakal bikin public ya, jadi kalian bisa akses di description di bawah. Kalian bisa bikin GitHub terus bikin repository ya di tombol ini create new ya nanti bisa bikin di sini. Ini gua udah bikin. Dan kalau karena udah ada di lokalnya gua tinggal copy komen yang di bawah ini. Tinggal gua buka lagi gravity terus gua paste aja sih komennya ini ya.

**36:28** · E gua paste gua enter semuanya. Sekarang udah harusnya ke-push ya. Keepush di sini. Ini bisa diakses sama kalian tinggal klik aja linknya di bawah. E ini nanti bisa kalian clown sendiri terus bisa running sendiri ya. Tinggal jalanin rme-nya nanti gua bikin sendiri sih gitu ya. N udah keupload ya. Kalian bisa tinggal clone sendiri di lokal kalian kalian bisa pakai, bisa kembangin bebas, kalian bisa deploy sendiri pun bebas ya kalian nanti gua bikin semacam Redmi ya di sini untuk guide gimana cara mulai eh aplikasinya di lokal kalian.

**36:59** · Jadi seperti itu ya flow gua sekarang ya dalam mengerjakan aplikasi full stack menggunakan AI yaitu gua pastinya akan sering lebih sering lagi menggunakan si Google Stage ini ya. Dan ini kalau kalian enggak tahu ini tuh gratis ya. E yang tadi gua pakai tuh e satu prom doang itu gratis ya. Gua enggak tahu sih sebenarnya limitnya berapa, tapi kalian bisa coba aja ee ini ee lalu kita convert ya dan awal dari awal itu HTML kita tinggal paste aja tadi ke Enta Gravity untuk lakuin semua planning-nya.

**37:24** · Terus gua juga tadi lakuin planning di awal tuh menggunakan Jem 3 ya. Ini juga yang gratisnya nih. Kalian bisa lihat ya gua di sini tulisannya upgrade karena ini akun gua yang gratis. Lalu setelah kita jalanin prom-prom di Anta Graavity bersama dengan planning tentunya dengan model terbaik yaitu Opus 4,5 dan untuk UI itu 3 Pro hasilnya seperti yang tadi udah gua demoin. Jadi itu sangat gua sarankan ya e flow-nya sekarang. Kalau kalian ada pertanyaan atau ada feedback langsung aja kasih komentar di bawah.

**37:51** · Insyaallah gua balas. Tapi kalau kalian pengin diskusi lebih lanjut e soal EA According Tools atau pengin informasi promo soal EA tools atau tools lainnya bisa langsung join Discord kita yang ada di description di bawah. Terima kasih ya.