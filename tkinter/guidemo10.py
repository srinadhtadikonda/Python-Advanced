# demo of enbale and disable
import tkinter as tk
root = tk.Tk()
root.title('Enable/Disable')

def toggle(event):
    if cbvar.get():
        entry.config(state='disabled')
    else:
        entry.config(state='normal')
        
cbvar = tk.BooleanVar()
cbox = tk.Checkbutton(root, text='Disable', variable=cbvar,
                      onvalue=True, offvalue=False)
#evar = tk.StringVar()
entry = tk.Entry(root, width=30)

cbox.pack()
entry.pack(padx=20, pady=10)

cbox.bind('<Button-1>',toggle)
root.mainloop()
