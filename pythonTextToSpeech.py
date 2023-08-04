from gtts import gTTS
from playsound import playsound
from os import system, remove
texts = input("enter text to play:")
cnvrt = gTTS(texts)
cnvrt.save(f"sample.mp3")
playsound(f"sample.mp3")
remove(f"sample.mp3")

# for palying items from a given list
# for a in text:
#     cnvrt=gTTS(text=a)
#     # print(dir(cnvrt))
#     cnvrt.save(f"{a}.mp3")
#     playsound(f"{a}.mp3")
#     # system("sample.mp3")
#     remove(f"{a}.mp3")
