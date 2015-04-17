from Tkinter import *

root = Tk()

def callback():
    print 'called the callback!'

class StatusBar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, text="STATUS BAR START", bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

myBar = StatusBar(root)
myBar.pack(side=BOTTOM, fill=X)
#myBar.set("%s", 'STATUS BAR INFO')
mainloop()
