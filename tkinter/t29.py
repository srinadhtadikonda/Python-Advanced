import tkinter as tk
from PIL import Image, ImageTk

# Function to create and display the main window with an image
def display_image(image_path):
    # Create the main window
    root = tk.Tk()
    root.title("Image Display Example")

    # Load the image using Pillow
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    label = tk.Label(root, image=photo)
    label.image = photo  # Keep a reference to avoid garbage collection
    label.pack()

    # Run the application
    root.mainloop()

# Path to the image file
image_path = "path/to/your/image.jpg"  # Replace with your image file path

# Display the image
display_image(image_path)
