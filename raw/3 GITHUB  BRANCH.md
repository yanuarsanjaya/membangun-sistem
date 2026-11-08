---
title: "#3 GITHUB : BRANCH"
source: "https://www.youtube.com/watch?v=k1QXd-8VbPY"
author:
  - "[[WPU]]"
published: 2019-04-23
created: 2026-11-08
description: "Di video kali ini kita akan belajar mengenai konsep Branch yang ada pada GITHUB--LINKGITHUB : https://github.com/-- PLAYLIST LAIN:- HTML Dasarhttps://www.youtube.com/playlist?list=PLFIM0718"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=k1QXd-8VbPY)

Di video kali ini kita akan belajar mengenai konsep Branch yang ada pada GITHUB  
  
\--  
LINK  
GITHUB : https://github.com/  
  
\--  
  
PLAYLIST LAIN:  
  
\- HTML Dasar  
https://www.youtube.com/playlist?list=PLFIM0718LjIVuONHysfOK0ZtiqUWvrx4F  
  
\- CSS Dasar  
https://www.youtube.com/playlist?list=PLFIM0718LjIUBrbm6Gdh6k7ZUvPIAZm7p  
  
\- Tutorial Sublime Text  
https://www.youtube.com/playlist?list=PLFIM0718LjIWE-Ot9V9qcALx5OMAZY67c  
  
\- CSS Layouting  
https://www.youtube.com/playlist?list=PLFIM0718LjIUu4Ju9GUL5zpLcuq08TKYr  
  
\- Javascript Dasar  
https://www.youtube.com/playlist?list=PLFIM0718LjIWXagluzROrA-iBY9eeUt4w  
  
\- Javascript & DOM  
https://www.youtube.com/playlist?list=PLFIM0718LjIWB3YRoQbQh82ZewAGtE2-3  
  
\- PHP DASAR  
https://www.youtube.com/playlist?list=PLFIM0718LjIUqXfmEIBE3-uzERZPh3vp6  
  
\- OOPHP  
https://www.youtube.com/playlist?list=PLFIM0718LjIWvxxll-6wLXrC\_16h\_Bl\_p  
  
\- PHP MVC  
https://www.youtube.com/playlist?list=PLFIM0718LjIVEh\_d-h5wAjsdv2W4SAtkx  
  
\- CodeIgniter  
https://www.youtube.com/watch?v=dMRCZGGAx74&list=PLFIM0718LjIVpXbAwu\_Cg9PdJO1GvyvCn&index=10  
  
https://www.youtube.com/watch?v=g5JT3EW38KM&list=PLFIM0718LjIVpXbAwu\_Cg9PdJO1GvyvCn&index=11  
  
https://www.youtube.com/watch?v=r-r6IhsE5vg&list=PLFIM0718LjIVpXbAwu\_Cg9PdJO1GvyvCn&index=12  
  
  
\---  
MEDIA SOSIAL  
  
\- http://instagram.com/sandhikagalih  
\- http://twitter.com/sandhikagalih  
\- https://www.facebook.com/WebProgrammingUNPAS  
\- http://codepen.io/webprogrammingunpas  
\- https://github.com/webprogrammingunpas  
  
\---  
UNIVERSITAS PASUNDAN BANDUNG  
http://www.unpas.ac.id/  
http://www.if.unpas.ac.id/  
  
terimakasih dan selamat #ngoding!  
  
@sandhikagalih

## Transcript

**0:00** · Halo teman-teman semua, apa kabar?

**0:02** · Kembali lagi di channel Web Programming Unpas, masih bersama saya Sandhika Galih. Dan di video kali ini kita masih ada di seri mengenai Git dan GitHub. Dan kita sekarang ada di episode ketiga ya, kita akan belajar masih mengenai GitHub.

**0:15** · Kita akan mencoba memahami apa itu branch ya atau cabang dengan menggunakan GitHub. Walaupun sebenarnya konsep branch ini adalah konsep Git. Ya kita bisa melakukan menggunakan Git nanti, tapi supaya kalian gampang memahami konsepnya karena menggunakan visualisasi yang cukup mudah ketika kita menggunakan GitHub. Ya dan sekarang kita lihat dulu apa sih definisi dari branch ini. Ya kalau teman-teman ngikutin video pertama seri ini, mungkin teman-teman sudah pernah melihat istilah dari branch ini ya.

**0:45** · Jadi contohnya kalau misalnya kita punya sebuah repository atau repo di dalam GitHub kita. Terus kita sudah melakukan beberapa kali commit, itu nanti kalau kita lihat tab network-nya itu tampilnya seperti ini ya. Jadi ada satu garis yang nanti garis itu kita akan sebut sebagai cabang utama atau GitHub dan Git nyebutnya master branch. Gitu ya dan titik-titik warna biru ini adalah commit-nya. Gitu jadi ceritanya kita sekarang sudah melakukan tiga kali commit. Nah nanti dari master branch ini kita bisa membuat sebuah cabang.

**1:18** · Gitu dan cabang ini itu independen, dia bisa jalan dengan menggunakan commit-nya sendiri. Nah ini dilakukan ketika nanti kalian mau membuat sebuah fitur baru pada repository kalian tanpa mengubah master branch-nya, jalur utamanya.

**1:34** · Karena mungkin misalnya kalian belum yakin apakah fitur ini bisa diimplementasikan atau tidak. Gitu ya itu bisa menggunakan branch.

**1:41** · Dalam satu repo itu kalian bisa membuat beberapa branch.

**1:45** · Nanti kita lihat implementasinya gimana ya.

**1:48** · Nah teknik branch atau branching ini kalau teman-teman lihat definisinya tadi kan simpelnya adalah pada saat kita membuat Git branch.

**1:56** · Ya baik itu pakai GitHub atau pakai website lain ya seperti GitLab atau Bitbucket atau secara lokal di komputer kalian. Nanti kalian nginstal Git terus melakukan branching, itu bisa juga.

**2:08** · Dan intinya branch ini adalah ketika kalian membuat snapshot tanpa mengganggu jalur utama branch-nya atau tadi kita sebutnya master branch itu. Dan ini kita lakukan tadi yang pertama ketika misalnya kalian mau bikin fitur yang eksperimental.

**2:23** · Kalian enggak tahu nih apakah nanti fitur nya bisa diterapin atau enggak.

**2:26** · Ketika nanti fitur nya enggak bisa diterapkan atau enggak selesai begitu ya kalian bisa hapus saja branch-nya dan kembali ke jalur utamanya. Atau ketika ada orang lain yang mengerjakan repo yang sama. Misalnya kalian bekerja dalam tim. Begitu ya. Nah, nanti si tim ini memiliki satu repo. Nanti repo nya bisa kita bikin cabang. Misalkan cabang A dikerjakan oleh si A, cabang B dikerjakan oleh si B. Nah, nanti di akhir mungkin kita akan menggabungkan fitur-fiturnya dengan melakukan merge ya.

**2:58** · Dan istilah itu sudah kita bahas di video pertama. Ya, jadi ini adalah istilah dari eh branch. Buat kalian yang masih bingung enggak apa-apa ya, mungkin nanti setelah kita coba implementasinya akan semakin jelas.

**3:11** · Nah, nanti juga kita akan belajar bagaimana caranya menggabungkan commit dari branch kembali ke master branch-nya. Nah, itu nanti disebut dengan merge atau merging gitu ya. Nah, sekarang supaya kalian langsung kebayang gimana implementasinya kita langsung coba aja kembali membuka website GitHub yang sudah kita coba dari video sebelum ini.

**3:33** · Baik teman-teman, di sini saya sudah buka GitHub saya yang sudah kita buat bareng-bareng di video sebelumnya.

**3:38** · Kalian juga bisa langsung akses di sini ya github.com/webprogrammingunpas.

**3:43** · Nah, harusnya kalian juga sekarang sudah punya akun GitHub dan membuat satu buah repository. Dan buat kalian yang enggak sabar untuk langsung nyobain gimana cara menghubungkan antara website GitHub dengan Git yang ada di lokal kalian. Ya, harap bersabar ya. Ini kita belajarnya dari sangat dasar sekali. Mungkin nanti kalau sudah berhubungan dengan source code itu kita bahas ketika kita sudah menginstal Git di komputer kita. Jadi, tujuan kita adalah supaya kebayang saja secara visual gimana sih maksud dari terminologi-terminologi Git-nya ya. Oke, kembali ke sini.

**4:14** · Jadi, kalian harusnya sudah punya akun GitHub yang di dalamnya minimal kalian sudah punya sebuah repository.

**4:24** · Ya.

**4:24** · Di video sebelumnya kita buat satu repository yang namanya WPU Resolusi.

**4:29** · Ya, kalau kita buka ini ceritanya isinya adalah repository yang menyimpan rencana ke depan dari channel Web Programming UNPAS ya. Di dalamnya saya punya dua buah file. Yang pertama ada README yang dibuat otomatis oleh GitHub-nya. Dan memang biasanya setiap repository ini punya README.

**4:47** · Nah, kalau kalian punya README, secara otomatis yang terlihat atau yang dibuka sama GitHub-nya itu adalah README-nya. Gitu. Jadi, biasakan nanti membuat README-nya sedeskriptif mungkin, sejelas mungkin ya menjelaskan repository kalian ini buat apa, gimana cara pakainya. Apalagi ketika kalian mau bikinnya open source supaya orang lain juga bisa pakai. Ini kalau kalian lihat saya membuat deskripsinya ya kurang bagus ya, hanya singkat saja. Selain README, saya juga punya file utamanya yaitu WPU Resolusi.txt.

**5:20** · Nah, ini ke depannya boleh kalian anggap sebagai source code kalian.

**5:24** · Ya, jadi ini sebuah folder yang di dalamnya nanti mungkin banyak file-file web-nya. Bisa ada HTML, PHP, JavaScript, CSS, dan lain sebagainya. Lalu di video sebelum ini kita juga coba bikin file ini yang txt lewat GitHub-nya.

**5:38** · Ya, jadi sama sekali belum ada hubungannya sama komputer kita di lokal.

**5:42** · Lalu di video sebelumnya juga kita sudah mencoba membuat beberapa kali commit ya untuk mengedit file kita, file resolusi.txt.

**5:52** · Kalian bisa klik tadi tulisan commit terus kalian bisa lihat wah ini ternyata sudah dilakukan beberapa kali commit.

**5:59** · Dan di commit-nya kelihatan siapa yang melakukan commit-nya. Jadi suatu saat kalian bekerja tim ketahuan siapa yang edit file mana di bagian mana ya.

**6:09** · Kalau pengen tahu apa yang dilakukan oleh commit-nya silakan diklik aja commit-nya.

**6:13** · Tuh kelihatan ya. Kalau ada tanda plus warna hijau ini artinya ada baris baru yang ditambahkan dan tanda minus atau warna merah ini adalah baris yang hilang.

**6:24** · Oke, dan sekali lagi Git hanya menyimpan perubahannya. Git-nya tidak mengeksekusi file-nya.

**6:30** · Ya jadi dia hanya menyimpan histori perubahannya. Oke sekarang yang akan kita lakukan gini ceritanya kita kembali lagi ke repo kita.

**6:37** · Ceritanya saya kepikiran untuk membuat sebuah fitur lah istilahnya begitu ya.

**6:42** · Saya nanti mau bikin satu file baru untuk menyim pan kira-kira rencana ke depan dari channel Web Programming Unpas terkait kontennya mau apa. Misalkan saya rencana mau bikin video apa nih. Oke tapi saya mau mau bikinnya itu sebagai branch baru karena saya mikir eh saya enggak yakin nih apakah rencana ini akan diterapkan atau tidak ceritanya gitu aja ya. Nah caranya untuk membuat branch baru ada dua. Kalian bisa melakukan editing dulu misalkan kalian nambahin satu file baru atau ngedit file yang sudah ada nanti begitu commit ya misalkan saya edit nih saya cobain edit.

**7:18** · Kalau saya scroll ke bawah ada dua pilihan lihat ada commit directly to the master branch.

**7:25** · Jadi commit-nya dilakukan di branch master-nya. Ya ingat master branch ini adalah branch default yang udah dibikinin sama si Git-nya.

**7:33** · Atau yang kedua bikin branch baru berdasarkan commit ini.

**7:38** · Itu yang pertama caranya ya kalian nanti klik ini atau kita kembali lagi ke repo-nya.

**7:44** · Kalian klik di sini di branch ini.

**7:47** · Klik.

**7:48** · Terus ada tulisan switch branches.

**7:51** · Nah, di sini kalian bisa cari branch atau membuat baru ketika belum ada.

**7:56** · Misalnya saya tulis rencana minus konten.

**8:01** · Saya mau bikin nama branch baru rencana konten. Kalau belum ada, nanti otomatis dia tulis create branch rencana konten.

**8:08** · Coba kita pilih ya.

**8:10** · Kalian juga silakan coba bikin branch baru. Klik. Nah, nanti tampilannya akan sama.

**8:15** · Ya, jadi seolah-olah seperti diduplicate gitu si repo-nya atau snapshot-nya diduplicate.

**8:20** · Tapi sekarang kita ada di branch rencana konten.

**8:23** · Nah, sekarang ceritanya saya mau bikin file baru. Coba kalian klik create new file.

**8:28** · Ya, misalkan saya mau bikin WPU rencana konten {titik} txt. Oke, ceritanya saya mau bikin baru. Saya tulis judulnya rencana konten WPU begitu ya.

**8:43** · Nah, apa saja nih ceritanya rencana kontennya? Misalnya ke depannya saya mau bikin video mengenai JavaScript misalnya ya.

**8:52** · Nanti saya bikin JavaScript.

**8:54** · Terus ke depannya saya juga mau bikin video mengenai PHP frameworks misalnya.

**9:00** · Terus misalnya saya mau interview lagi, interview.

**9:03** · Atau misalkan saya tambah lagi selanjutnya saya mau bikin vlog.

**9:07** · Sudah, ini ceritanya rencana untuk konten ke depannya WPU. Misalnya begini ya. Kalau sudah seperti biasa, scroll ke bawah kita commit.

**9:16** · Misalkan membuat file WPU rencana konten txt. Sudah ya, ceritanya commit-nya sederhana saja satu baris. Kalau mau ditambahin deskripsi, silakan tulis di bawahnya. Nah, sekarang lihat nih di bawahnya otomatis tulisannya berubah.

**9:31** · Tadinya ke master branch, sekarang sudah langsung pindah ke rencana konten.

**9:35** · Karena saat ini yang aktif adalah branch rencana konten ya. Coba kita klik commit new file.

**9:42** · Sudah nih ya. Lihat nih. Ada beberapa yang berbeda dengan sebelumnya. Yang pertama jelas file-nya tambah baru. Yang kedua, sekarang kita ada di branch rencana konten.

**9:53** · Dan ini lihat nih, ada satu tombol tambahan. Katanya ada compare dan pull request. Nanti kita akan bahas belakangan ya.

**10:01** · Yang penting gini sekarang, saya punya dua branch.

**10:04** · Nih kalau kalian klik branch-nya. Kalau saya pindah ke master, klik, lihat, rencana kontennya enggak ada.

**10:11** · Jadi di jalur utamanya enggak ada rencana konten, hanya ada di branch rencana konten.

**10:16** · Nah, ketika saya berpindah branch, ini di Git namanya check out ya. Paham teman-teman? Jadi kalau saya sekarang melakukan perubahan di branch ini enggak akan ngeganggu branch utamanya.

**10:26** · Dan sekarang, kalau saya klik inside lagi, di atas, terus saya ke network lagi, nih lihat teman-teman.

**10:36** · Sekarang, jalurnya nambah.

**10:39** · Tuh sekarang jadi ada yang warna biru ini ya.

**10:41** · Nih jadi ada cabangnya ke bawah tuh.

**10:43** · Yang hitam adalah master branch, ke bawah yang biru branch baru, rencana konten.

**10:50** · Paham ya sampai sini ya.

**10:52** · Nah, sekarang kalau misalkan kita coba lakukan beberapa kali commit, coba balik ke repo-nya, kita pindahin dulu nih jangan lupa ke rencana konten, check out dulu.

**11:02** · Ke rencana konten, kita edit lagi.

**11:05** · Dan ini sebenarnya kalian bisa ngedit file yang mana aja ya. Itu snapshot-nya disimpan. Nanti si repo-nya tahu kalian ngedit file mana, bagian mana. Misalnya kita edit nih.

**11:15** · Kita detailkan. Misalkan untuk yang JavaScript, ceritanya saya mau bikin yang pertama nih, ini sudah sebenarnya sudah masuk ke rencana. Saya mau bikin mengenai ES6 atau sintaks JavaScript yang baru. Nah, terus habis ini mungkin kita akan masuk ke framework JavaScript. Gitu cuma saya belum tahu mau masuk framework-nya yang mana ya, karena banyak banget yang bagus-bagus. Sudah, misalkan saya nambahin dua ini saja. Terus saya checkout lagi.

**11:41** · Menambahkan detail ya, detail materi JavaScript.

**11:47** · Kita commit, lihat, hati-hati. Bukan di master lagi, tapi di rencana konten.

**11:52** · Commit.

**11:53** · Sudah ya.

**11:54** · Ini kalau kalian klik history file-nya, nanti ketahuan sudah berapa kali berubah. Ya, kalau dilihat sama saja.

**12:01** · Kayak video sebelumnya, ini sudah nambahin dua.

**12:04** · Oke, balik lagi ke repo-nya.

**12:06** · Sudah nih, ceritanya kalian sudah menambahkan fitur baru di rencana konten.

**12:12** · Ya, kalau kita lihat lagi insight-nya nanti nambah commit yang warna birunya.

**12:16** · Insight, network.

**12:19** · Tuh, nambah sekarang si commit-nya ada dua.

**12:22** · Paham ya, sampai sini ya. Nah, sekarang ceritanya gini.

**12:25** · Fitur baru rencana konten ini, kalian sudah suka nih. Kayaknya oke nih, bisa diimplementasikan yang rencana konten ini.

**12:33** · Saya mau kembalikan dia masuk ke jalur utamanya, masuk ke dalam master branch, mau dipakai di project kalian.

**12:41** · Ya, supaya si master branch-nya menggunakan fitur dari branch-nya. Kita akan melakukan merging namanya ya, menggabungkan dua buah branch. Caranya itu kalian klik tombol yang ini.

**12:52** · Jadi, kalian akan melakukan sesuatu yang disebut dengan pull request. Ya, kalau misalkan kalian lihat di GitLab, kalau enggak salah ini namanya merge request.

**13:00** · Tapi intinya sama saja.

**13:02** · Coba kita klik dulu ya. Klik compare and pull request. Jadi, ada dua buah branch, master dan rencana konten.

**13:09** · Isinya ada yang beda.

**13:10** · Nah, coba kita gabungkan.

**13:12** · Klik. Nanti akan masuk ke sesuatu yang disebut dengan open a pull request. Ya, terus nanti di bawahnya ada ilustrasinya nih, kita akan memasukkan branch rencana konten ke dalam master, ngegabungin masuk ke master.

**13:28** · Nah, di sebelah kanannya nah ini GitHub atau Git ya, cukup cerdas untuk ngecek dua commit ini atau dua branch ini bisa digabung enggak? Karena kemungkinan ke depannya enggak bisa digabung. Kenapa?

**13:42** · Karena ada baris yang sama berubah. Nah, itu nanti kalian akan masuk ke dalam sesuatu yang disebut dengan merge conflict. Gitu.

**13:51** · Ya, tapi nanti itu kita lihatlah. Nah, sekarang katanya ceklist nih able to merge, artinya enggak ada problem, enggak ada conflict. Git-nya bisa melakukan merging secara otomatis.

**14:01** · Sekarang, kenapa disebut pull request?

**14:03** · Oke, karena secara default begini.

**14:06** · Meskipun ini kalian yang melakukannya sendiri ya, di repo kalian, di akun kalian itu kita tetap harus melakukan sesuatu yang namanya pull request. Pull request itu gini, ceritanya kalau kita bikin branch, branch itu harus minta izin dulu ke yang punya repo-nya supaya perubahan di branch bisa masuk.

**14:26** · Gitu.

**14:27** · Jadi, kenapa namanya pull request?

**14:28** · Karena branch ini me-request meminta agar si pemilik master-nya menarik perubahan dia, gitu. Ngerti enggak? Makanya namanya pull request.

**14:39** · Saya yang punya branch minta ke yang punya master, tarik dong nih perubahan saya, gitu.

**14:46** · Ya, karena ke depannya mungkin aja kalian merubah repo orang. Ya, kan enggak mungkin otomatis kalian bisa push gitu ya perubahannya ke repo orang.

**14:56** · Harus dikonfirmasi dulu oleh pemiliknya.

**14:59** · Nah, sekarang meskipun kita yang punya repo-nya, kalian yang punya master dan kalian yang punya branch tetap metodenya adalah pull request. Jadi, branch me-request, ambil nih perubahannya. Nah, nanti ada pesannya. Pesan si branch ke master.

**15:15** · Misalkan menambah file rencana konten .txt dan menambahkan beberapa baris.

**15:26** · Misalkan gitu ya. Nah, nanti pesan pull request-nya akan ke kirim ke pemilik master, ya.

**15:33** · Sekarang yang punya branch kita, yang punya master kita. Jadi, mungkin kalian agak aneh ya, enggak apa-apa. Kita coba create pull request.

**15:40** · Nanti kalau sudah ada pull request-nya kalian akan diarahkan ke tab ini, pull request.

**15:47** · Tuh kan dari repo nih ya. Kalau kalian dari repo nanti ini ada pull request.

**15:51** · Nah, mungkin aja nanti ke depannya kalian pull request-nya banyak. Kalau kode kalian udah banyak yang modifikasi gitu. Jadi, kalau kalian lihat ini, "Wah, ada pull request nih." Klik.

**16:01** · Nanti lihat. Ini ada pull request-nya.

**16:03** · Ada yang nambahin nih, file rencana konten. Coba kita lihat.

**16:09** · "Oh, ini gitu." katanya ya.

**16:11** · Nah, kalau kalian sudah oke dengan perubahannya karena kan tadi tidak ada konflik ya langsung aja kalian merge.

**16:17** · Klik merge. Terus ada ini kalau kalian mau membalas pesan si merge-nya.

**16:23** · Misalkan, "Terima kasih, fiturnya bagus sekali. Saya mau pakai di branch saya."

**16:27** · misalkan gitu ya. Boleh, tapi ini karena kita yang bikin ya langsung confirm aja enggak apa-apa.

**16:32** · Klik confirm. Nah, nanti ada tulisan ya, "Pull request successfully merged and closed." Jadi, hilang.

**16:39** · Tuh, pull request-nya jadi hilang.

**16:40** · Dan sekarang seharusnya kalian udah bisa nebak nih.

**16:44** · Master berubah. Tuh.

**16:47** · Ya, sekarang sama persis dengan yang ada di rencana konten.

**16:51** · Gitu, karena sudah digabung. Nah, kalau kita ke insight lagi terus ke network lihat nih, teman-teman.

**16:58** · Kalian bisa lihat panahnya masuk kembali ke dalam master. Begitu ya. Jadi, itu adalah teknik kita nge-merge. Nah, kalau sudah beres nih berarti kan branch rencana konten kayaknya udah enggak dipakai lagi. Bener enggak? Tapi, dia belum terhapus ya.

**17:14** · Untuk menghapus branch-nya kalian bisa masuk ke sini, ke branches.

**17:19** · Klik branches-nya, katanya ada dua nih.

**17:22** · Master sama rencana konten. Nah, kalian boleh hapus nih.

**17:27** · Ya, sebenarnya enggak dihapus pun enggak apa-apa, tapi dia akan tetap ada. Tapi kalau dihapus nanti hilang dia dari eh network-nya. Klik aja delete branch, nanti dia hilang.

**17:37** · Sekarang branch-nya kembali satu.

**17:40** · Begitu teman-teman ya, jadi sekarang enggak ada lagi tuh branch rencana kontennya.

**17:44** · Paham ya, itu cara kita melakukan merge.

**17:47** · Nah, tapi merge yang kita lakukan tadi itu ideal, enggak ada error-nya. Mungkin aja ke depannya kalian mengalami konflik dan mungkin aja kalian punya lebih dari satu branch. Nah, sekarang kita coba ya.

**18:00** · Misalnya ini kita coba kasih satu commit dulu ya, misalkan ini mau saya edit lagi.

**18:06** · Misalkan saya mau nambahin satu konten, misalnya saya nambahin satu materi deh.

**18:12** · Ini ini cita-cita saya sebenarnya membuat ini tapi sampai sekarang saya belum mengolah materinya ya. Ada fundamental data structure atau struktur data dasar gitu ya.

**18:23** · Ini seru sih belajarnya walaupun ya memang konseptual gitu, bukan eh aplikatif. Nah, nambahin kita commit baru menambahkan materi dasar struktur data. Ya, kita commit ke master biar nambah aja di network-nya gitu.

**18:43** · Nah, sekarang sudah nih ceritanya saya mau bikin dua branch sekarang.

**18:47** · Ceritanya saya mau serahkan ke dua orang di tim saya nih, coba kalian kembangkan fitur yang ada di dalam repo kita. Nah, jadi nanti dua orang ngedit file yang sama. Misalkan kita bikin branch baru, misalnya saya kasih nama aja gini, coba fitur satu.

**19:07** · Ya, jadi saya punya satu nih.

**19:09** · Bikin lagi, coba fitur ini otomatis kalau kalian pakai spasi nanti dibikinin dash ya atau tanda minus. Coba fitur dua.

**19:20** · Op, from-nya salah. Kita balikin dulu ke master ya.

**19:24** · Nanti jadi cabang dari fitur satu ya. Saya penginnya cabang dari master. Pindahin dulu ke master.

**19:30** · Baru kita bikin coba fitur dua. Ini lihat nih from-nya.

**19:37** · Supaya cabangnya dari master.

**19:39** · Sudah.

**19:40** · Sip ya, sekarang saya punya tiga buah branch.

**19:43** · Kalau kita balik ke repo-nya sekarang branch-nya tiga. Nah, sekarang nih kita coba satu-satu. Ceritanya untuk yang fitur satu saya serahkan ke si A misalnya ya. Nah, si A ini akan ngedit file yang sama.

**19:56** · Rencana konten.

**19:58** · Nah, dia mau ngedit gini katanya. Oh, pas lihat oh ini saya mau tambahkan framework JavaScript misalnya nanti di dalamnya kita belajar mengenai view misalkan.

**20:09** · Oke. Terus PHP framework-nya nanti kita belajar Laravel misalkan.

**20:15** · Nah, terus menurut si A katanya saya perlu menambahkan misalnya materi mengenai Python.

**20:22** · Oke. Ceritanya sudah.

**20:24** · Terus dia commit saja ya.

**20:26** · Menambahkan materi baru.

**20:30** · Ini kata si A. Oke.

**20:32** · Nah, terus katanya oh ini ada yang kurang. Saya lupa nambahin misalnya framework JavaScript-nya kita akan belajar juga React misalnya.

**20:40** · Nah, terus commit lagi.

**20:43** · Sudah, commit lagi. Jadi yang fitur satu ada dua commit.

**20:46** · Sip. Nah, sekarang coba kita masuk ke fitur dua.

**20:50** · Jadi yuk lihat nih ada pull request ya.

**20:53** · Biarkan dulu.

**20:54** · Sekarang kita masuk ke si B. Nah, si B juga akan ngedit file yang sama.

**20:59** · File-nya masih begini kan?

**21:00** · Nah, si B ngeditnya gini.

**21:02** · Framework-nya akan saya edit juga katanya. Tapi yang mau dipelajari sama si B adalah Angular.

**21:08** · Oke, lalu yang kedua adalah React.

**21:11** · Sama.

**21:12** · Nah, terus menurut si B kayaknya kita enggak butuh nih eh belajar mengenai struktur data dasar. Dia ngapus ini misalnya. Terus PHP framework-nya sama dia juga mau belajar mengenai Laravel.

**21:25** · Oke, sudah si B hanya ngeditnya seperti ini.

**21:28** · Sekarang coba kita commit. Ya, mengubah isi dari misalkan pesan commit-nya beda.

**21:35** · Rencana konten.

**21:38** · Sudah, sekarang kita commit ke fitur 2.

**21:40** · Sip, jadi sekarang kita sudah punya 2 branch sama master ya. Nah, kalau kita lihat insight-nya coba kita ke insight dulu sebelum kita nanti merging.

**21:49** · Masuk network. Sekarang kalian lihat nih, cabangnya jadi 2.

**21:53** · Ini cabangnya ke bawah nih.

**21:55** · Yang biru ke sini ada 2 commit. Yang hijau ke bawahnya. Nah, sekarang kita akan menggabungkan ketiga branch ini.

**22:04** · Cara menggabungkannya ini harus satu-satu. Kalian akan gabungkan master dengan yang mana dulu? Mau dengan yang fitur 1 atau dengan yang fitur 2. Kita coba gabungkan dulu dengan yang fitur 1 ya.

**22:15** · Kalian klik compare and pull request.

**22:17** · Nanti dia cek bisa di-merge enggak? Ada konflik enggak? Oh, katanya enggak ada.

**22:23** · Sip ya. Enggak ada konflik langsung boleh create pull request saja.

**22:27** · Minta agar cabang yang fitur 1 masuk ke dalam master.

**22:32** · Cek lagi, kalau sudah tinggal di-merge.

**22:35** · Confirm saja.

**22:36** · Ya, ini pesan-pesannya saya biarkan default. Sudah beres nih. Kalau balik ke repo pilih master sekarang isi dari rencana kontennya sudah gini, sudah nambah. Sama dengan fitur 1.

**22:48** · Oke, kalau kita ke insight network yang warna biru sudah masuk.

**22:54** · Sudah nih. Sekarang tinggal kita masukin yang fitur 2 ke sini.

**22:58** · Coba balik ke repo-nya lagi.

**23:01** · Kita pull request lagi.

**23:03** · Ya, kita pull request. Harusnya sekarang ada konflik nih. Tuh. Jadi enggak bisa langsung di-merge katanya.

**23:09** · Harus ada yang kita lakukan dulu. Tapi di sini tulis, "Don't worry, you can still create the pull request." Pull request-nya masih tetap bisa dilakukan, tapi enggak bisa langsung di-merge. Ya, coba kita pull request.

**23:21** · Nanti masuk ke sini ya, ke tab pull request kalian.

**23:24** · Tapi isinya gini.

**23:25** · Ada konflik. Dan kalian sebagai pemilik master itu yang harus me-resolve atau menyelesaikan masalahnya. Jadi konfliknya harus kita selesaikan secara manual. Oke, jadi kalau kalian klik resolve conflict ini nanti kita akan diarahkan ke code editor. Nah, ini teman-teman lihat nih. Sekarang kita disuruh milih mau pakai yang mana nih.

**23:49** · Nih ada ada tanda eh lebih kecil dari dan lebih besar dari, terus di tengah-tengahnya ada tanda sama dengan.

**23:54** · Nah, ini artinya yang beda tuh ini.

**23:57** · Nah, sekarang kalian pilih mau tetap ada struktur datanya atau enggak ada.

**24:03** · Mau Angular atau mau Vue.

**24:06** · Nah, ini kita yang suruh milih. Nah, caranya tinggal diedit aja manual.

**24:10** · Misalkan saya mau pakainya yang Vue dan struktur datanya tetap ada. Boleh dihapus aja.

**24:15** · Nih, ini bisa diedit.

**24:18** · Tuh.

**24:19** · Sudah?

**24:20** · Nah, sekarang kalau sudah beres menurut kalian, ini kalian bisa mark as resolve.

**24:25** · Jadi ceritanya sudah beres masalahnya.

**24:27** · Tinggal kita merge.

**24:29** · Ya, jadi kalau ada konflik harus diselesaikan dulu secara manual. Klik commit merge.

**24:35** · Kalau sudah beres, sudah enggak ada konflik, baru kita merge lagi.

**24:38** · Confirm.

**24:39** · Sip ya, sekarang kalau kita kembali ke repo-nya sudah beres. Rencana kontennya berubah sesuai dengan merge yang dilakukan. Ya, jadi ada Vue Angular-nya hilang, struktur datanya saya pengin tetap ada dan ada Python, misalnya gitu.

**24:56** · Paham ya? Kalau kita ke Insight lagi, masuk network, yang teman-teman lihat, sudah di-merge.

**25:03** · Mungkin teman-teman ini agak aneh nih, kenapa si master-nya membuat sebuah commit dulu, padahal tadi kayaknya kita enggak melakukan commit di master ya.

**25:11** · Nah, ini ada dua tipe dari merging, ada yang disebut fast forward dan eh three-way merging, tapi itu kayaknya nanti saya akan bahas lebih detail ketika kita sudah masuk ke Git-nya.

**25:22** · Kalau kita menggunakan Git lalu merging, ini kalian harus paham nih, kenapa kok eh beda gitu ya. Kan kalau tadi yang fitur satu, dia langsung masuk nih ke master.

**25:33** · Ini namanya fast forward merging, tapi begitu fitur dua mau merging, ya sebetulnya enggak bisa gitu aja merging.

**25:41** · Ya, ini ada yang disebut dengan three-way merging.

**25:44** · Nah, tapi intinya sekarang semuanya sudah masuk ke master.

**25:48** · Gitu ya. Dan terakhir, kalau kalian sudah enggak butuh branches-nya, sudah beres, boleh di-delete aja.

**25:54** · Masuk ke branches, delete fitur dua, dan delete fitur satu.

**25:59** · Begitu teman-teman ya. Jadi, itu kita sudah melakukan merging dengan beberapa kasus.

**26:06** · Oke, jadi itu ya teman-teman ya. Dan sebelum kita akhiri, mungkin kita rekap dulu sedikit mengenai branch ini. Tadi katanya branch adalah jalur eh development bebas dari sebuah commit.

**26:16** · Lalu ada lagi yang disebut dengan checkout. Ini penting ketika kita berpindah ke branch satu atau branch lainnya. Bahkan sebenarnya checkout ini bisa pindah ke commit. Mundur gitu ke commit yang mana, tapi nanti ini akan kita bahas lebih detail eh ketika kita belajar Git ya. Karena kalau commit-nya pakai GitHub kan gampang, tinggal pilih combo box gitu, branch mana. Tapi kalau eh pakai konsol nanti pakai Git, agak sedikit kompleks. Terus next, kita juga belajar mengenai pull request.

**26:42** · Ingat ya, pull request ini adalah sebuah cara kita untuk meminta agar pemilik dari repo-nya atau master branch-nya menarik perubahan kita.

**26:57** · Terus ada merge untuk menggabungkan dua buah branch tadi dan pada umumnya kita akan menemukan sebuah merge conflict.

**27:04** · Ketika apa? Ketika baris yang sama diubah oleh dua branch yang berbeda.

**27:10** · Nah, itu kita harus resolve dulu conflict-nya.

**27:13** · Oke, jadi mungkin itu saja untuk video kali ini. Mudah-mudahan teman-teman paham mengenai implementasi sederhana dari branch ini.

**27:20** · Silakan teman-teman coba lagi saja untuk membuat branch supaya kalian lebih paham lagi ya. Jadi, itu saja. Terima kasih teman-teman sudah eh menyaksikan video ini. Kita akan ketemu lagi di episode berikutnya. Saya Sandhika Galih pamit dan seperti biasa teman-teman, jangan lupa titik koma.