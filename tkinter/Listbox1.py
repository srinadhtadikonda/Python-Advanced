#demo of List Widget
import tkinter as tk
root = tk.Tk()
root.title('Listbox Widget')
root.geometry('300x250+400+50')
def setsize():
    ind = lbox.curselection()
    #print(lbox.get(ind))
    text.config( font=('Times new roman', lbox.get(ind)),height=10,width=30)
    
lbox = tk.Listbox(root, height=10,width=5)
for i in range(10,31,2):
    lbox.insert(tk.END, i)

text = tk.Text(root, width=30, height=10)
btn = tk.Button(root, text='Set Size', command=setsize)

lbox.place(x=10,y=10)
text.place(x=50,y=10)
btn.place(x=10,y=180)

root.mainloop()
