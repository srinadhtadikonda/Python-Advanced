import tkinter as tk
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def text_to_audio():
    text = entry.get()
    
    if text:
        tts = gTTS(text=text, lang='en')
        audio_file = "temp_audio.mp3"
        tts.save(audio_file)
        
        # Play the audio using pydub
        audio = AudioSegment.from_mp3(audio_file)
        play(audio)
        
        entry.delete(0, 'end')

        # Optionally remove the file after playback
        os.remove(audio_file)

# Create the main window
root = tk.Tk()
root.title("Text to Audio Converter")

# Create an Entry widget for text input
entry = tk.Entry(root, width=40)
entry.pack(pady=20)

# Create a Button to trigger the conversion
button = tk.Button(root, text="Convert to Audio", command=text_to_audio)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
