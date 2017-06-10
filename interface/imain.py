#!/usr/bin/python3
# -*- coding: utf8 -*-

import tkinter

class interface_tk(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Mail saver")

        self.initialize()

        self.root.resizable(True, False)
        self.root.update()
        self.root.geometry(self.root.geometry())

        self.root.mainloop()

    def initialize(self):
        #------------------------------
        # Frame
        #------------------------------

        self.frame_connexion = tkinter.Frame(self.root, bd='8', bg='yellow', \
            highlightthickness='10', highlightcolor='blue')
        self.frame_connexion.grid()

        #------------------------------
        # FIRST LINE (row 0)
        #------------------------------

        self.label_invit = tkinter.Label(self.frame_connexion, text="Veuillez entrer vos informations", \
               anchor="center", font=('Courrier New', '18', 'bold underline'))
        self.label_invit.grid(row=0, column=0,columnspan=4,sticky='EW')

        #------------------------------
        # Email (row 1)
        #------------------------------

        self.label_pseudo = tkinter.Label(self.frame_connexion, text="Adresse mail : ", anchor="center")
        self.label_pseudo.grid(row=1, column=0,columnspan=2,sticky='EW')

        self.pseudo = tkinter.StringVar()
        self.pseudo.set(u'example@exemple.com')

        self.entry_pseudo = tkinter.Entry(self.frame_connexion, textvariable=self.pseudo)
        self.entry_pseudo.grid(column=2,row=1,columnspan=2,sticky='EW')
        #self.entry_pseudo.bind("<Return>", self.PressEnter)

        self.entry_pseudo.focus_set()
        self.entry_pseudo.selection_range(0, tkinter.END)

        #------------------------------
        # Password (row 2)
        #------------------------------

        self.label_pass = tkinter.Label(self.frame_connexion, text="Mot de passe : ", anchor="center")
        self.label_pass.grid(row=2, column=0, columnspan=2, sticky='EW')

        self.password = tkinter.StringVar()
        self.password.set(u"password")

        self.entry_password = tkinter.Entry(self.frame_connexion, textvariable=self.password, show='*')
        self.entry_password.grid(column=2,row=2, columnspan=2, sticky='EW')
        #self.entry_pseudo.bind("<Return>", self.PressEnter)

        self.entry_password.focus_set()
        self.entry_password.selection_range(0, tkinter.END)

        #------------------------------
        # BUTTON <Connexion> (row 3)
        #------------------------------

        self.button_connexion = tkinter.Button(self.frame_connexion,text=u"Connexion", \
            command=self.showmyId)
        self.button_connexion.grid(row=3, column=3)

        #==============> TEST
        self.myId = tkinter.StringVar()
        self.label_show = tkinter.Label(self.frame_connexion, textvariable=self.myId, \
               anchor="center",) #font=('Courrier New', '16', 'bold underline'))
        self.label_show.grid(row=4, column=0,columnspan=4,sticky='EW')
        self.myId.set('Click on Connexion to change me !')
        #==============>

        #------------------------------
        # RESIZING
        #------------------------------

        self.frame_connexion.grid_columnconfigure(0, weight=1)
        self.frame_connexion.grid_rowconfigure(0, weight=1)

        #------------------------------
        # TEST (row 4)
        #------------------------------

    def showmyId(self):
        self.myId.set('Your email is : ' + self.pseudo.get() + "\nThat\'s the only thing I can do by now!")
        #print(self.pseudo.get())

if __name__ == "__main__":
    #If the program is used by itself
    import tkinter
    f = interface_tk()
