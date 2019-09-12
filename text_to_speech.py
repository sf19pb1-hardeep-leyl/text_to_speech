# Converts text to speech in different languages. Requires pip3 install gTTS
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

print("We're going to translate anything you type into another language")
mytext = input("Please enter some text in English: ")
print(language_code)
language = input("Please select the language code: ")

# Passing the text and language to the engine
myobj = gTTS(text=mytext, lang=language, slow=True)

# Saving the converted audio in a mp3 file named texty
myobj.save("texty.mp3")

# Playing the converted file.  It does create the file but doesnt play.  It also doesn't translate, just says it in a different accent!
os.system("mpg321 texty.mp3")
