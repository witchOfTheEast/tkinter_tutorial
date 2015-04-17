from Tkinter import *
import tkMessageBox

root = Tk()

def callback():
    print 'called the callback!'

# code here
filename = 'x'

try: 
    fp = open(filename)
except:
    tkMessageBox.showwarning(
        'Open file',
        'Cannot open this file\n(%s)' % filename
        )
#        return

if tkMessageBox.askyesno('print', 'Print this fake report?'):
    #report.print()
    callback()

mainloop()
