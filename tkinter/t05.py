from tkinter import * 
root=Tk()

def bgr():
    lb1.config(text="You Clicked RED Button",bg="red")
    root.config(bg="red")

def bgb():
    lb1.config(text="You Clicked BLUE Button",bg="blue")
    root.config(bg="blue")    

def bgg():
    lb1.config(text="You Clicked GREEN Button",bg="green")
    root.config(bg="green")

def bgy():
    lb1.config(text="You Clicked YELLOW Button",bg="yellow")
    root.config(bg="yellow")

def qf():
    root.destroy()

btn1=Button(text="RED",command=bgr,width=10)
btn1.pack()

btn2=Button(text="BLUE",command=bgb,width=10)
btn2.pack()

btn3=Button(text="GREEN",command=bgg,width=10)
btn3.pack()

btn4=Button(text="YELLOW",command=bgy,width=10)
btn4.pack()

btn5=Button(text="QUIT",command=qf,width=10)
btn5.pack()

lb1=Label(text="",width=50)
lb1.pack()

mainloop()