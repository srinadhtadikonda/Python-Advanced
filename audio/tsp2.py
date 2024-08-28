import tkinter as tk
from gtts import gTTS
import pygame
import os
import time

def text_to_audio():
    # Get the text from the Entry widget
    text = entry.get()

    if text:
        # Convert text to speech
        tts = gTTS(text=text, lang='en')
        audio_file = "temp_audio.mp3"
        tts.save(audio_file)

        # Initialize the mixer and play the audio file
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Stop the mixer and close any resources
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        entry.delete(0,'end')
        # Give a short delay to ensure the file is fully released
        time.sleep(0.1)
        
        # Remove the audio file after playback
        if os.path.exists(audio_file):
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
