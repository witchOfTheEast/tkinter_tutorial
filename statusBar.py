from Tkinter import *

root = Tk()

def callback():
    print 'called the callback!'

# code here
status = Label(root, text="STATUS BAR TEXT", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

mainloop()
