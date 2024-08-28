import tkinter as tk
from PIL import Image, ImageTk

def display_image():
    # Create the root window
    root = tk.Tk()
    root.title("Display JPG Image")

    # Load the image using Pillow
    image = Image.open("your_image.jpg")  # Replace with your image path
    photo = ImageTk.PhotoImage(image)

    # Create a Label widget to display the image
    label = tk.Label(root, image=photo)
    label.image = photo  # Keep a reference, to prevent garbage collection
    label.pack()

    # Start the Tkinter event loop
    root.mainloop()

# Call the function to display the image
display_image()
