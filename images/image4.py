import PIL
from tkinter import *
from PIL import Image
from PIL import ImageTk
from PIL import ImageFilter
from tkinter import filedialog
import cv2
from skimage import filters
import skimage
import mahotas
import mahotas.demos
import numpy as np

root = Tk()
root.title("IMAGE PROCESSING")


def emboss():
    kernel = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
    emboss = cv2.filter2D(image, kernel=kernel, ddepth=-1)
    emboss= cv2.cvtColor(emboss, cv2.COLOR_BGR2GRAY)
    emboss=255-emboss
    emboss1= Image.fromarray(emboss)
    
    emboss1= ImageTk.PhotoImage(emboss1)
    
    panelB = Label(image=emboss1, borderwidth=5, relief="sunken")
    panelB.image = emboss1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
    
    return emboss

def watercolor():
    watercolor = cv2.stylization(image, sigma_s=100, sigma_r=0.45)
    
    watercolor1= Image.fromarray(watercolor)
    
    watercolor1= ImageTk.PhotoImage(watercolor1)
    
    panelB = Label(image=watercolor1, borderwidth=5, relief="sunken")
    panelB.image = watercolor1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
    
    return watercolor

def cartoon():
    gray=grayscale()
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    color = cv2.bilateralFilter(image, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    cartoon1= Image.fromarray(cartoon)
    
    cartoon1= ImageTk.PhotoImage(cartoon1)
    
    panelB = Label(image=cartoon1, borderwidth=5, relief="sunken")
    panelB.image = cartoon1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
    
    return cartoon

def colpencil():
    img_invert = cv2.bitwise_not(image)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    
    colpencilimg = cv2.divide(image, 255- img_smoothing, scale=255)
    colpencilimg1= Image.fromarray(colpencilimg)
    
    colpencilimg1= ImageTk.PhotoImage(colpencilimg1)
    
    panelB = Label(image=colpencilimg1, borderwidth=5, relief="sunken")
    panelB.image = colpencilimg1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
    
    return colpencilimg

def pencil():
    img=grayscale()
    img_invert = cv2.bitwise_not(img)
    img_smoothing = cv2.GaussianBlur(img_invert, (25, 25),sigmaX=0, sigmaY=0)
    
    pencilimg = cv2.divide(img, 255 - img_smoothing, scale=255)
    pencilimg1= Image.fromarray(pencilimg)
    
    pencilimg1= ImageTk.PhotoImage(pencilimg1)
    
    panelB = Label(image=pencilimg1, borderwidth=5, relief="sunken")
    panelB.image = pencilimg1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
    
    return pencilimg


def maskimg():  
    x, y , w, h = cv2.selectROI(image)
    start = (x, y)
    end = (x + w, y + h)
    rect = (x, y , w, h)
    
    cv2.rectangle(image, start, end, (0,0,255), 3)
    mask = np.zeros(image.shape[:2], np.uint8)
        
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
        
    cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 100, cv2.GC_INIT_WITH_RECT)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
    mask1 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    maskimage = image * mask1[:, :, np.newaxis]
    
    maskimage1 = Image.fromarray(maskimage)
    
    maskimage1= ImageTk.PhotoImage(maskimage1)
    
    panelB = Label(image=maskimage1, borderwidth=5, relief="sunken")
    panelB.image = maskimage1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)

    return maskimage

def powerlawtrans():
    gammaplt = np.array(255*(image/255)**2.05,dtype='uint8')
    gammaplt1 = Image.fromarray(gammaplt)
    
    gammaplt1= ImageTk.PhotoImage(gammaplt1)
    
    panelB = Label(image=gammaplt1, borderwidth=5, relief="sunken")
    panelB.image = gammaplt1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
    
    return gammaplt

def histo():
    histogram = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    histogram [:,:,0] = cv2.equalizeHist(histogram [:,:,0])
    histogram = cv2.cvtColor(histogram, cv2.COLOR_YUV2BGR)
    histogram1 = Image.fromarray(histogram)
    
    histogram1= ImageTk.PhotoImage(histogram1)
    
    panelB = Label(image=histogram1, borderwidth=5, relief="sunken")
    panelB.image = histogram1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
    
    return histogram

def sharp():
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    sharpened = cv2.filter2D(image, ddepth=-1, kernel=kernel)
    
    sharpened1 = Image.fromarray(sharpened)
    
    sharpened1= ImageTk.PhotoImage(sharpened1)
    
    panelB = Label(image=sharpened1, borderwidth=5, relief="sunken")
    panelB.image = sharpened1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
    
    return sharpened

def denoise():
    denoise = cv2.fastNlMeansDenoisingColored(image,None,5,5,7,21)
    denoise1 = Image.fromarray(denoise)
    
    denoise1= ImageTk.PhotoImage(denoise1)
    
    panelB = Label(image=denoise1, borderwidth=5, relief="sunken")
    panelB.image = denoise1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
    
    return denoise

def skeleton():
    image = threshold()
    skel = np.zeros(image.shape, np.uint8)
    
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    
    while True:
        open = cv2.morphologyEx(image, cv2.MORPH_OPEN, element)
        temp = cv2.subtract(image, open)
        eroded = cv2.erode(image, element)
        skel = cv2.bitwise_or(skel,temp)
        image = eroded.copy()
        if cv2.countNonZero(image)==0:
            break
            
    skel1= Image.fromarray(skel)
    
    skel1= ImageTk.PhotoImage(skel1)
    
    panelB = Label(image=skel1, borderwidth=5, relief="sunken")
    panelB.image = skel1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)

    return skel

def edge():
    image = threshold()
    
    edged = cv2.Canny(image, 50, 100)
    edged1 = Image.fromarray(edged)
    
    edged1= ImageTk.PhotoImage(edged1)
    
    panelB = Label(image=edged1, borderwidth=5, relief="sunken")
    panelB.image = edged1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
    
    return edged



def redext():
    row,col,plane = image.shape
                
    red = np.zeros((row,col,plane),np.uint8)
    red[:,:,0] = image[:,:,0]
    
    red1 = Image.fromarray(red)
    
    red1= ImageTk.PhotoImage(red1)
    
    panelB = Label(image=red1, borderwidth=5, relief="sunken")
    panelB.image = red1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
        
    return red

def greenext():
    row,col,plane = image.shape
        
    green= np.zeros((row,col,plane),np.uint8)
    green[:,:,1] = image[:,:,1]
    
    green1 = Image.fromarray(green)
    
    green1= ImageTk.PhotoImage(green1)
    
    panelB = Label(image=green1, borderwidth=5, relief="sunken")
    panelB.image = green1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
       
    return green

def blueext():
    row,col,plane = image.shape
        
    blue = np.zeros((row,col,plane),np.uint8)
    blue[:,:,2] = image[:,:,2]
    
    blue1 = Image.fromarray(blue)
    
    blue1= ImageTk.PhotoImage(blue1)
    
    panelB = Label(image=blue1, borderwidth=5, relief="sunken")
    panelB.image = blue1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
        
    return blue 


def threshold():
    image = grayscale()
    
    ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    thresh1= Image.fromarray(thresh)
    
    thresh1= ImageTk.PhotoImage(thresh1)
    
    panelB = Label(image=thresh1, borderwidth=5, relief="sunken")
    panelB.image = thresh1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
        
    return thresh


def negative():
    neg= 255 - image
    neg1= Image.fromarray(neg)
    
    neg1= ImageTk.PhotoImage(neg1)
    
    panelB = Label(image=neg1, borderwidth=5, relief="sunken")
    panelB.image = neg1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
    
    return neg


def grayscale():
    grayimg= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayimg1= Image.fromarray(grayimg)
    
    grayimg1= ImageTk.PhotoImage(grayimg1)
    
    panelB = Label(image=grayimg1, borderwidth=5, relief="sunken")
    panelB.image = grayimg1
    panelB.grid(row= 1, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)
    
    return grayimg



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



l1= Label(root, text="CLICK THE BUTTONS TO PERFORM THE FUNCTIONALITIES MENTIONED",
           fg="white", bg="purple", width= 98, borderwidth=5, relief="groove",  font =('Verdana', 15))
l1.grid(row= 0, column= 1, columnspan= 6, padx=20, pady=20, sticky='nesw')

btn= Button(root, text="UPLOAD", fg="black", bg="lavender", command=upload)
btn.grid(row= 1, column= 0, padx=10, pady=10, sticky='nesw')

btn1= Button(root, text="GRAYSCALE", fg="white", bg="snow4", command=grayscale)
btn1.grid(row= 2, column= 0, padx=10, pady=10, sticky='nesw')

btn2= Button(root, text="INVERT COLOR", fg="white", bg="black", command=negative)
btn2.grid(row= 3, column= 0, padx=10, pady=10, sticky='nesw')

btn3= Button(root, text="RED ATTRIBUTES", fg="white", bg="red", command=redext)
btn3.grid(row= 4, column= 0, padx=10, pady=10, sticky='nesw')

btn4= Button(root, text="GREEN ATTRIBUTES", fg="white", bg="green", command=greenext)
btn4.grid(row= 5, column= 0, padx=10, pady=10, sticky='nesw')

btn5= Button(root, text="BLUE ATTRIBUTES", fg="white", bg="blue", command=blueext)
btn5.grid(row= 6, column= 0, padx=10, pady=10, sticky='nesw')

btn6= Button(root, text="BINARY", fg="white", bg="black", command=threshold)
btn6.grid(row= 7, column= 0, padx=10, pady=10, sticky='nesw')

btn7= Button(root, text="EDGE DETECTION", fg="white", bg="black", command=edge)
btn7.grid(row= 8, column= 0, padx=10, pady=10, sticky='nesw')

btn8= Button(root, text="SKELETON", fg="white", bg="black", command=skeleton)
btn8.grid(row= 9, column= 0, padx=10, pady=10, sticky='nesw')

btn9= Button(root, text="POWER LAW TRANSFORMATION", fg="white", bg="purple", command=powerlawtrans)
btn9.grid(row= 10, column= 0, padx=10, pady=10, sticky='nesw')

btn10= Button(root, text="CONTRAST ENHANCEMENT", fg="white", bg="purple", command=histo)
btn10.grid(row= 11, column= 0, padx=10, pady=10, sticky='nesw')

btn11= Button(root, text="SHARPENING", fg="white", bg="purple", command=sharp)
btn11.grid(row= 12, column= 0, padx=10, pady=10, sticky='nesw')

btn12= Button(root, text="SMOOTHENING", fg="white", bg="purple", command=denoise)
btn12.grid(row= 13, column= 0, padx=10, pady=10, sticky='nesw')

btn13= Button(root, text="REMOVE BACKGROUND", fg="white", bg="purple", command=maskimg)
btn13.grid(row= 14, column= 0, padx=10, pady=10, sticky='nesw')

btn14= Button(root, text="PENCIL SKETCH", fg="white", bg="purple", command=pencil)
btn14.grid(row= 15, column= 1, padx=10, pady=10, sticky='nesw')

btn15= Button(root, text="COLOR PENCIL SKETCH", fg="white", bg="purple", command=colpencil)
btn15.grid(row= 15, column= 2, padx=10, pady=10, sticky='nesw')

btn16= Button(root, text="CARTOONIFY", fg="white", bg="purple", command=cartoon)
btn16.grid(row= 15, column= 3, padx=10, pady=10, sticky='nesw')

btn17= Button(root, text="WATERCOLOR", fg="white", bg="purple", command=watercolor)
btn17.grid(row= 15, column= 4, padx=10, pady=10, sticky='nesw')

btn18= Button(root, text="EMBOSS", fg="white", bg="purple", command=emboss)
btn18.grid(row= 15, column= 5, padx=10, pady=10, sticky='nesw')

btn19= Button(root, text="EMBOSS image", fg="white", bg="purple", command=emboss)
btn19.grid(row= 15, column= 6, padx=10, pady=10, sticky='nesw')

root.mainloop()
