'''
 L0INTERFACEMAINPAGE for level 0.
 Easier to visualize the tree view.
'''

import tkinter
from tkinter import font  as tkfont

#Depending on where you call mainpage, you need to import differently
try :
    import l1diffpages as pages
except :
    import interface.l1diffpages as pages

class MainWindow(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.title('Mail Saver')
        self.geometry("700x400") # set size of the main window to 300x300 pixels

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tkinter.Frame(self, bd='8', bg='red', width='500', height="300", \
            highlightthickness='10', highlightcolor='yellow')
        container.grid_propagate(0)
        container.grid()

        # Fulfill (if disable) (or not) the space between
        # the container and the frame inside it
        #container.grid_rowconfigure(0, weight=1)
        #container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (pages.StartPage, pages.PageTest, pages.PageConnexion):
            page_name = F.__name__
            frame = F(parent=container, controller=self) #, width=200, height=200)
            self.frames[page_name] = frame

            # all of the pages in same location;
            # one on the top of the stack is the one visible
            frame.grid(row=0, column=0, sticky="nsew")

        # The first page to be shown
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
