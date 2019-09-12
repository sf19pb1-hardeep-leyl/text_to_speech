# Converts text to speech in different accents. Requires pip3 install gTTS
from gtts import gTTS
import os

language_code = """
Language Code
-------- ----
Afrikaans       af
Albanian        sq
Arabic  ar
Belarusian      be
Bulgarian       bg
Catalan         ca
Chinese Simplified      zh-CN
Chinese Traditional     zh-TW
Croatian        hr
Czech   cs
Danish  da
Dutch   nl
English         en
Estonian        et
Filipino        tl
Finnish         fi
French  fr
Galician        gl
German  de
Greek   el
Hebrew  iw
Hindi   hi
Hungarian       hu
Icelandic       is
Indonesian      id
Irish   ga
Italian         it
Japanese        ja
Korean  ko
Latvian         lv
Lithuanian      lt
Macedonian      mk
Malay   ms
Maltese         mt
Norwegian       no
Persian         fa
Polish  pl
Portuguese      pt
Romanian        ro
Russian         ru
Serbian         sr
Slovak  sk
Slovenian       sl
Spanish         es
Swahili         sw
Swedish         sv
Thai    th
Turkish         tr
Ukrainian       uk
Vietnamese      vi
Welsh   cy
Yiddish         yi
"""

print("We're going to speak anything you type in a different accent")
mytext = input("Please enter some text: ")
print(language_code)
language = input("Please select the accent: ")

# Passing the text and language to the engine
myobj = gTTS(text=mytext, lang=language, slow=True)

# Saving the converted audio in a mp3 file named texty
myobj.save("texty.mp3")

# It does create the file but doesnt play. 
# Also, I wanted it to actually translate to a different language, but all it does is say it in a different accent!
os.system("mpg321 texty.mp3")
