from tkinter import *


root = Tk()
root.geometry("150x200")

w = Label(root, text='HelloHello', font="50")
w.pack()

scroll_bar = Scrollbar(root)

scroll_bar.pack(side=RIGHT, fill=Y)


mylist = Listbox(root, yscrollcommand=scroll_bar.set)

for line in range(1,26):
    mylist.insert(END, "HI" + str(line))


mylist.pack(side=LEFT, fill=BOTH)

scroll_bar.config(command=mylist.yview)

root.mainloop()
