---
title: "Cara bikin AI gak lupa dan sinkron ke banyak perangkat dan agent lain"
source: "https://www.youtube.com/watch?v=5x6m3qkA7wg&t=30s"
author:
  - "[[Raf Dev]]"
published: 2026-11-08
created: 2026-11-08
description: "10% OFF Hostinger VPS: https://hostinger.com/rafdevhermes (Promo code RAFDEVHERMES)Buat PRD Untuk AI Coding diskon hingga 51%: https://bikinpakeai.com/second-brainBikin UI dari template Anti SLOP di"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=5x6m3qkA7wg)

10% OFF Hostinger VPS: https://hostinger.com/rafdevhermes (Promo code RAFDEVHERMES)  
Buat PRD Untuk AI Coding diskon hingga 51%: https://bikinpakeai.com/second-brain  
Bikin UI dari template Anti SLOP diskon 50k: https://bikinpakeai.com/desain/second-brain  
  
Bayar sekali, chattan sama banyak model AI:  
https://www.andalai.id/?utm\_source=youtube&utm\_medium=video&utm\_campaign=openclaw-vs-hermes  
  
Komunitas Discord AI Coding Terbesar di Indonesia:  
https://discord.gg/K66VSJnVTH  
  
Timestamp  
00:00 Second Brain untuk AI Agent  
02:18 Mengenal Obsidian  
04:37 Hubungkan Obsidian ke Agent  
05:47 Setup Multi-Device  
07:17 Hermes Agent di VPS  
09:17 Sinkronisasi dengan Syncthing  
11:52 Workflow Riset di Hermes  
14:12 Lanjut ke Claude Desktop  
15:42 Penutup  
  
#hermesagent #hermes #ngodingpakeai #desainpakeai #claude #aicoding #vibecoding #personalagent #obsidian #secondbrain

## Transcript

### Second Brain untuk AI Agent

**0:00** · Peace be upon you, and Allah's mercy and blessings. So, in this video, I’m going to discuss something that can make your AI agents extremely powerful. It’s about the concept of a second brain.

**0:10** · This concept can solve two problems that I’m sure you’ve experienced.

**0:15** · The first is that AI always forgets, and the second is more relevant if you use more than one agent.

**0:21** · You may have felt that when chatting with one agent, it has different memories compared to others.

**0:26** · But with this second brain, everything can be synced and seamless. Let me show you right away. So, here I have a cloud desktop running cloud code, and I’m using Claude Opus 3.5, where I just chat normally.

**0:40** · I asked it to save everything from my latest video topic to something called Obsidian, which acts as the tool that creates my second brain, where it can access the memory of my second brain and record what I ask.

**0:53** · Here, Opus 3.5 scans the folder containing my latest content, records everything into my second brain, and now , if I open my Hermes agent on Telegram .

**1:03** · This is hosted on a VPS. So, it’s a separate device. If I ask about my latest topic, it instantly syncs and understands what I mean.

**1:12** · This is truly the same topic I previously asked Opus 3.5 to save to my second brain.

**1:19** · The topic name is "First 10 Million from AI Coding," and what Hermes discussed with me is the same, "First 10 Million from AI Coding," and if I want to see the specific memory, I can just open the tool called Obsidian.

**1:31** · I check here, and there is a script about my latest topic, the "First 10 Million from AI Coding."

**1:37** · It already contains what we asked Opus 3.5 to record earlier.

**1:42** · And another thing is that we can visualize our second brain.

**1:46** · This shows individual memories that are interconnected.

**1:50** · For example, here, regarding this content, I’ve uploaded all the analytics and transcripts from my short-form videos.

**1:58** · So, this is connected to the note about content.

**2:01** · Meanwhile, if you look down here, there’s information about my products, even though it’s still a bit limited. In this video, I will show you how you can set up your own second brain, 100%for free.

**2:12** · I will also show you the workflow or use cases for this second brain that I use all the time. So, make sure to watch this video until the end. Okay, let's jump straight into the discussion.

### Mengenal Obsidian

**2:22** · So, first off, the tool you'll need to create your second brain is called Obsidian.

**2:26** · Honestly, Obsidian is actually quite simple.

**2:29** · It’s basically just a note-taking app or a place where you can jot down your notes, much like Notion.

**2:35** · But the difference is, it writes everything in .md files stored directly in your file directory. This tool is 100 %free, and you can use it as much as you want without any limits.

**2:46** · It also supports a ton of plugins that you can use to support various integrations or customizations.

**2:55** · What makes Obsidian unique compared to regular note-taking apps is its system for connecting and grouping individual notes.

**3:03** · By linking these notes or memories together, it makes it easier for the agent and us to retrieve the memories we need.

**3:10** · Let me give you a quick example.

**3:13** · So, here I have a recent note about a video I just uploaded; as you can see, there are several properties here, which help in retrieving the memory.

**3:26** · And if you look at the left here, the tree structure of the files or notes is exactly the same as how you'd store folders or files on your computer.

**3:39** · Because if we look in Finder or Windows Explorer, you can see that every single note is saved as a markdown file within that folder structure.

**3:50** · If I scroll all the way to the bottom, you can see there’s a sort of link there . If I look at the graph view itself, you can see it.

**3:59** · By providing these various links and the tags at the top, it creates a kind of connection with other memories.

**4:09** · And this is definitely useful because your agent will know which references are related to that memory, using them as extra context to provide the best response.

**4:19** · I also want to mention something.

**4:24** · You can write these notes manually, but ideally, your workflow should have the agent record and save everything into Obsidian for you.

**4:34** · It will understand the formatting just fine.

### Hubungkan Obsidian ke Agent

**4:37** · Now, to connect your agent to Obsidian, you first need to enable a setting in the app.

**4:43** · Just go here to preferences, then general, and scroll all the way to the bottom.

**4:48** · There’s a command-line interface here.

**4:50** · Just enable it, then search for " Obsidian skill" on Google, and you'll find the repository.

**4:57** · You can just ask your agent to set up that skill for you.

**5:01** · It’s easy; just copy the link here. Then you just need to paste it into your cloud code or your agent of choice. Just use your prompts. Something like this.

**5:09** · After that, just restart your agent.

**5:11** · Once the skill is installed correctly and it's connected to the Obsidian CLI.

**5:18** · Later, if you prompt about the memories in your second brain, your agent should be able to access those memories and write new ones or create new notes.

**5:28** · Installing Obsidian is also quite simple .

**5:32** · Just go to the official Obsidian website and download it for your platform.

**5:36** · I'm using macOS here, so just install it .

**5:40** · Once installed, open it and you'll be asked to create a new vault.

**5:44** · The vault is the main folder that will store all your notes or memories.

### Setup Multi-Device

**5:51** · Next, I want to explain the setup I use to sync my second brain across other devices and agents.

**6:01** · More specifically, I have a laptop where I do my work, like coding or creating content.

**6:09** · For my main agent, I use a cloud desktop .

**6:13** · Meanwhile, if I'm out and about or want to brainstorm, I use Telegram, which connects to my Hermes.

**6:19** · My Hermes agent is hosted on a VPS that runs 24 hours a day.

**6:29** · Previously, the main issue I faced with this setup was that when I brainstormed on one agent and finished, if I wanted to continue working on another device or agent, I had to export it as a summary or document, save it to Google Docs, and then mention that Google Docs in the next agent, which was very annoying and messy because my notes would often get scattered.

**6:54** · Unfortunately, to get the sync feature between devices, you need to subscribe, which costs about $ 4 per month.

**7:04** · However, I found a free and real-time way to sync our second brain to more than one device using a tool called Syncthing.

**7:13** · It's not "sinting," but Syncthing.

**7:16** · Before I continue discussing Syncthing to sync my second brain from my laptop to my VPS.

### Hermes Agent di VPS

**7:22** · I want to talk about my Hermes agent setup already on my VPS.

**7:27** · The main reason I use this Hermes agent on a VPS instead of my personal laptop is because if I'm out, I certainly don't want my laptop to be on all the time.

**7:36** · And since the VPS runs 24/7, my Hermes Agent is always running and I can always access it through my phone.

**7:43** · Besides that, because it's always on, if there's any change to my second brand, it will always stay in sync.

**7:51** · And since this VPS is my own private server, I'm free to host my applications to run the Hermes agent and my apps simultaneously without any performance issues.

**8:03** · I'm using Hostinger KVM2, which is having a huge sale, and if you use my link in the description and enter my coupon code, you can get an extra 10% discount.

**8:15** · I suggest picking the KVM2 plan because it's very affordable.

**8:20** · I've tried running the Hermes Agent while hosting over 10 apps and had no issues; the VPS remained stable.

**8:28** · At the checkout page, don't forget to add my coupon code, Rafde Hermes, to get an additional 10%discount.

**8:35** · So the monthly total is around 136 thousand rupiah.

**8:42** · Then, if you don't want the hassle of setting up your Hermes agent with external API connections, you can choose the ready-to-use AI provided by Hostinger.

**8:54** · And for those who intend to do web scraping, you can enable the instant web scraping option to enhance its features .

**9:01** · Once your VPS is set up, you can go to the Hostinger hPanel.

**9:06** · Then just click on the web console, and it will open your VPS shell.

**9:10** · Next, just input the Hermes command here as follows.

**9:14** · It will then ask you to configure the Hermes agent.

### Sinkronisasi dengan Syncthing

**9:17** · But since I've already set up my Hermes agent, it directly opens the Hermes CLI .

**9:22** · Okay, back to the explanation regarding Syncthing.

**9:27** · To sync between your devices, you need to install Syncthing on each of them.

**9:34** · The installation is simple, just search for Syncthing on Google.

**9:40** · Then go to the downloads page and download it according to the platform you're using.

**9:46** · Once installed, just open the application.

**9:51** · Here, you can click open, and it will open the localhost browser like this.

**9:57** · Here we can see which folders we are syncing.

**10:01** · For example, I've synced my vault, which is named RF Vault.

**10:06** · And for the devices, I've connected it to my Hostinger VPS.

**10:11** · To connect a device, just add a new remote device here.

**10:15** · Then add or enter the device ID.

**10:19** · You can also enter the device name and device group here.

**10:23** · Then in the advanced tab, add the IP or host of your remote device.

**10:28** · Now, that was for the Syncthing desktop setup.

**10:34** · But if you're using a VPS or want to connect Syncthing on a server, like me, I've prepared a prompt that you can copy to your Hermes agent or any agent you've set up on your VPS or server.

**10:47** · Just copy it.

**10:49** · And what I did was, after copying, I also prepared my device ID, which is the one on my laptop here.

**10:57** · To see it, just click Actions, then Show ID, and the full ID will appear.

**11:03** · So besides giving this prompt to your agent on the server, for instance, I use Telegram to connect to my Hermes agent.

**11:10** · So I just paste it into Telegram.

**11:13** · After that, I enter the device ID, and it will connect once everything is running smoothly.

**11:18** · If it's successful, the status will be " Up to date" like this.

**11:23** · And to make sure your second brain is truly synchronized between devices, you can just send a prompt like this to your Hermes agent.

**11:31** · Okay, it's finished being added.

**11:34** · Now I can just open my Obsidian on my laptop.

**11:39** · Then here, the Hermes folder should be there—okay, this test connection appeared.

**11:45** · So it's truly connected between my devices.

**11:50** · Everything is synced now; my second brain can be accessed by the Hermes agent as well as my cloud desktop.

### Workflow Riset di Hermes

**11:57** · Now I want to show you the workflow I usually follow.

**12:00** · Usually, for brainstorming or conducting research, I use the Hermes agent via my Telegram. So here, I've prepared the prompt as an example.

**12:10** · I've created a prompt asking the Hermes agent to research which content would be best for me to create next.

**12:17** · I asked it to reference my previous content.

**12:21** · This also has the analytics inside my second brain.

**12:25** · So if we check here in Obsidian, everything is already there.

**12:30** · For these videos, the analytics, summaries, and transcripts are all saved in my second brain.

**12:37** · Then, at the end, I asked it to save everything to my vault once finished so I can access it later on other devices.

**12:44** · So let's try submitting it here.

**12:47** · Okay, the research is done, and it has created the report as follows.

**12:52** · It's complete and just as I wanted because it understands my preferences.

**12:58** · And now if we check in Obsidian on my laptop, it's synced, and the newest note is already there.

**13:05** · And here we can see the full details of what it looks like.

**13:09** · And here, if I open the graph, it looks like this.

**13:13** · Now, open local graph.

**13:16** · We can see where it gets its references and what videos it's related to, right?

**13:22** · Then there is also a graph view that is complete for all my memories.

**13:29** · We can see at the bottom here, those are the research results I just did in Hermes.

**13:36** · We can see, yes, it's like the graph from before.

**13:40** · But here you can see the connections between nodes or memories, which are quite complex.

**13:45** · I think it's pretty cool. We can drag it around like this.

**13:50** · Also, we can actually filter and change the colors to make each group easier to see.

**14:00** · I think this is cool, too; if we turn on tags, it’s easier to see which are scripts, which are AI designs, or which use open code, and so on.

**14:11** · So, I find this feature quite interesting.

### Lanjut ke Claude Desktop

**14:17** · After I get the full report from the Hermes agent about the research I did, I usually continue with Claude on the desktop app, either creating an outline directly or testing apps to demo in the next video.

**14:32** · I'm in the Claude desktop app now, choosing the Opus 3.5 model, and I’m asking it to create a new project folder for the video and an outline for it.

**14:44** · In the tool traces, we can see Claude searching for the notes I made in Hermes , finding them, and opening the files directly.

**14:52** · It uses these MD files as context to create the outline.

**14:56** · Okay, Claude is done creating the outline. We can see it directly in the Claude Desktop app.

**15:01** · But I see it has also saved it in Obsidian.

**15:06** · So, if I open Obsidian, in the script section, the outline for the video is already there, having been researched by Hermes and outlined by Claude.

**15:15** · That's it for the demo. Sorry it's not complete, as it would get a bit too long .

**15:20** · But more or less, after the outline is done, I will read and review it, and do a few more iterations.

**15:29** · And if the video includes an app I'm going to demo, I'll ask it to create a high-level explanation or a brief so I can do the planning on moding pakai i.com.

**15:41** · Then I build the application using Opus 3.5 or whatever model I'm featuring in the video.

### Penutup

**15:47** · So that’s it for this video.

**15:50** · I highly recommend that those of you who haven't tried a second brand, just follow this video.

**15:55** · And if you have your own workflow or setup that might be better than mine, feel free to share it in the comments below.

**16:04** · If you want to get an affordable VPS with high performance, don't forget to click my link in the description to get Hostinger KVM, and don't forget to enter my coupon code Raf Dev Hermes to get an extra 10%discount.

**16:18** · Thank you for watching until the end.