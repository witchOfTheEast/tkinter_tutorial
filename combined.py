from Tkinter import *
import tkMessageBox

def callback():
    print 'called the callback!'

def setStatus():
    myBar.set("%s", 'STATUS BAR INFO')   


def exitNow():
    exit()

def confirmExit():
    if tkMessageBox.askyesno('Exit dialog', 'Really exit?'):
        exitNow()

root = Tk()

# create a menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=confirmExit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)


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

# create a toolbar
toolbar = Frame(root)

b = Button(toolbar, text='new', width=6, command=setStatus)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text='open', width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)
mainloop()
