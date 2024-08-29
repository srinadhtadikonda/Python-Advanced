import PIL
from tkinter import *
from PIL import Image
from PIL import ImageTk
from PIL import ImageFilter
from tkinter import filedialog
import cv2


root = Tk()
root.title("IMAGE PROCESSING")



def upload():
    global panelA, panelB, image
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')] 
    path = filedialog.askopenfilename(filetypes=f_types)
    image = cv2.imread(path) 
    image = cv2.resize(image, (500,500))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image)

    image1 = ImageTk.PhotoImage(image1)

    panelA = Label(image=image1, borderwidth=5, relief="sunken")
    panelA.image = image1
    panelA.grid(row= 1, column=1 , rowspan= 13, columnspan= 3, padx=20, pady=20)
    
    return image



btn= Button(root, text="UPLOAD", fg="black", bg="lavender", command=upload)
btn.grid(row= 1, column= 0, padx=10, pady=10, sticky='nesw')



root.mainloop()
