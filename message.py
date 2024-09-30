from tkinter import *
from tkinter import ttk


from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry('200x150')

def save():
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('text Document', '*.txt')]
    file= asksaveasfile(filetypes = files, defaultextension = files)

    btn = ttk.Button(root, text = 'Save', command = lambda : save())
    btn.pack(side = TOP, pady = 20)
    mainloop()
