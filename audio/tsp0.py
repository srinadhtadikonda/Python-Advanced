from gtts import gTTS
import os
mytext = 'Welcome to the world of Joe!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=True)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")
