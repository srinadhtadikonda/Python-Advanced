
import tkinter as tk
from tkinter import Label, filedialog
from PIL import Image, ImageTk

# Image uploader function
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=fileTypes)

    # If a file is selected
    if len(path):
        img = Image.open(path)
        img = img.resize((200, 200))
        pic = ImageTk.PhotoImage(img)

        # Re-sizing the app window to fit the picture and button
        app.geometry("560x300")
        label.config(image=pic)
        label.image = pic

    # If no file is selected, display a message
    else:
        print("No file chosen! Please choose a file.")

# Main method
if __name__ == "__main__":

    # Defining the tkinter object
    app = tk.Tk()

    # Setting title and basic size of the app
    app.title("Image Viewer")
    app.geometry("560x270")

    # Adding a background image
    img = ImageTk.PhotoImage(file='gfglogo1.png')
    imgLabel = Label(app, image=img)
    imgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    # Adding a label to display the uploaded image
    label = tk.Label(app)
    label.pack(pady=10)

    # Defining the upload button
    uploadButton = tk.Button(app, text="Locate Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM, pady=20)

    app.mainloop()
