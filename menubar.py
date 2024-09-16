from tkinter import*
from tkinter.ttk import*
from time import strftime

root =Tk()
root.title('menu demontration')

menubar= Menu(root)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label= 'New File', command=None)
file.add_command(label= 'Open...', commadn=None)
file.add_command(label='Save', command= None)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)



edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label= 'Edit', menu=edit)
edit.add_command(label= 'Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Save', command=None)
edit.add_command(label='Paste all', command=None)



help = Menu(menubar, tearoff=0)
menubar.add_cascade(label = 'Help', menu=help)
help.add_command(label = 'Tk.help', command=None)
help.add_command(label = 'Demo', command=None)
help.add_command(label = 'About Tk', command=None)

root.config = (Menu=menubar)

mainloop()
