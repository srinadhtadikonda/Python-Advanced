#demo of adding Button widget

import tkinter as tk
root = tk.Tk()
root.title('Brilliant')
root.minsize(300,200)

def abc():
    print('Button is clicked')
    
btn = tk.Button(root, text='Click Me', command=abc)

btn.pack()
root.mainloop()
