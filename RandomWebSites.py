import webbrowser
import random
import time
while True:
    video = "https://www.youtube.com/watch?v=47023304723243"
    video2 = "https://www.youtube.com/watch?v=vlklshvsofvs"
    dictionnary = ["Youtube.com", video, "Techno World",
                   "DJ Solarstone", "DJ Manta", "Motherfucker", "How to download MEMZ.exe",
                   "Sheeeeeeeesh", "How to destroy a computer", "Amogus meme", "Full Storm - Discogs",
                   "Reverse88 - Minecraft Wiki", "Discord", "Toxic", "How to remove MEMZ.exe", "How to fuck your computer",
                   "FUCK", "Lange Artist", "Jan Johnston", "Fakten Records Germany", "FullStormsOfficial", "Trance Classics Official",
                   "FullStormOfficial - Discogs", "DJ Tiësto", "Trance Forever Classics - Youtube", "Techno World", "Hard Trance 2022"
		   "Hardcore Techno", "Jumpstyle", "Techno Music 2022", "Hard House Mix 2022", "Tech Trance",  "Assorted Trance, Techno & Acid",
		   "Trance 2000", "Delerium", "Club System Series", "International Tunning Sounds", "B-Tronixx - Feel Y Mind",
    		   "Hardstyle Music", "V-GAZ - Jump On My Beat", "The Game - Crash Test", "Techno 2003", 
		   "Bitch Project - M-Dry", "Housefucker", "All The Fuckers" "Hardcore Techno Mix 2022",
		   "DJ Sven Lanvin", "Full Storm Music 2022", "Hard Style Generation Mix 2022",
		   "Hard Techno 2005", "Panorama - Dark Age (Misteriser Mix)", "Mike Dust - Sawtooth Massacre (Boris S. Remix)", video2]
    choose = random.choice(dictionnary)
    go_to_web = webbrowser.open_new(choose)
    time.sleep(20)
