from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
 
pncr = tk.Tk()
pncr.title('Ugur Not Defteri')

menubar = Menu(pncr)
 
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label='Yeni',command=yeni)
filemenu.add_command(label='Aç', command=aç)
filemenu.add_command(label='Kaydet', command=kaydet)
filemenu.add_separator()
filemenu.add_command(label='Çıkış', command=çıkış)
menubar.add_cascade(label='Dosya', menu=filemenu)
menubar.add_command(label='Hakkında', command=hakkında)
 
textarea = Text(pncr, width=100,height=20)
textarea.pack() 
 
pncr.configure(background='white')
pncr.config(menu=menubar)
pncr.mainloop()
