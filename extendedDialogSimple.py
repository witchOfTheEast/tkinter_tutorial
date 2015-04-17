from Tkinter import *
import os

class Dialog(Toplevel):
    
    def __init__(self, parent, title=None):
        
        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        self.buttonbox()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOOW", self.cancel)

        self.geometry('+%d+%d'% (parent.winfo_rootx()+50,
                                parent.winfo.rooty()+50))

        self.initial_focus.focus_set()

        self.wait_window(self)

    #
    # construction hooks

    def body(self, master):
        # create dialog body. return widget that should have
        # initial focus. this method should be overridden
        
        pass

    def buttonbox(self):
        # add standard button box. override if you don't want the 
        # standard buttons

        box = Frame(self)

        w = Button(box, text='OK', width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text='Cancel', width=10
