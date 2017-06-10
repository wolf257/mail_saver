#!/usr/bin/python3
# -*- coding: utf8 -*-

import tkinter

class interface_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)

        self.parent = parent

        self.initialize()

    def initialize(self):
        self.grid()

    #------------------------------
    # BLOC 1
    #------------------------------

        frame_connexion = tkinter.Frame(self, bd='8', bg='yellow', \
        highlightthickness='10', highlightcolor='blue')
        frame_connexion.grid()

        #------------------------------
        # FIRST LINE (row 0)
        #------------------------------

        label_invit = tkinter.Label(frame_connexion, text="Veuillez entrer vos informations",
        anchor="center", font=('Courrier New', '18', 'bold underline'))
        label_invit.grid(row=0, column=0,columnspan=4,sticky='EW')

        #------------------------------
        # Email (row 1)
        #------------------------------

        label_pseudo = tkinter.Label(frame_connexion, text="Adresse mail : ", anchor="center")
        label_pseudo.grid(row=1, column=0,columnspan=2,sticky='EW')

        self.pseudo = tkinter.StringVar()
        self.pseudo.set(u'example@exemple.com')

        self.entry_pseudo = tkinter.Entry(frame_connexion, textvariable=self.pseudo)
        self.entry_pseudo.grid(column=2,row=1,columnspan=2,sticky='EW')
        #self.entry_pseudo.bind("<Return>", self.PressEnter)

        self.entry_pseudo.focus_set()
        self.entry_pseudo.selection_range(0, tkinter.END)

        #------------------------------
        # Password (row 2)
        #------------------------------

        label_pass = tkinter.Label(frame_connexion, text="Mot de passe : ", anchor="center")
        label_pass.grid(row=2, column=0, columnspan=2,sticky='EW')

        self.password = tkinter.StringVar()
        self.password.set(u"password")

        self.entry_password = tkinter.Entry(frame_connexion, textvariable=self.password, show='*')
        self.entry_password.grid(column=2,row=2, columnspan=2, sticky='EW')
        #self.entry_pseudo.bind("<Return>", self.PressEnter)

        self.entry_password.focus_set()
        self.entry_password.selection_range(0, tkinter.END)

        #------------------------------
        # PARTIE BUTTON (row 3)
        #------------------------------

        button_connexion = tkinter.Button(frame_connexion,text=u"Connexion") # , command=self.ButtonClick)
        button_connexion.grid(row=3, column=3)

        #------------------------------
        # RESIZING
        #------------------------------

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())


        #------------------------------
        # Essai (row 4)
        #------------------------------

    #def ButtonClick(self):
    #    self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)" )
    #    self.entry.focus_set()
    #    self.entry.selection_range(0, tkinter.END)

    #def PressEnter(self, event):
    #    self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
    #   self.entry.focus_set()
    #    self.entry.selection_range(0, tkinter.END)

if __name__ == "__main__":
    app = interface_tk(None)
    app.title('Mail saver')
    app.mainloop()
