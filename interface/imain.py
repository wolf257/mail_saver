#!/usr/bin/python3
# -*- coding: utf8 -*-

import tkinter

import widgets
import functions

class interface_tk(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Mail saver")

        self.initialize()

        #self.root.minsize(width=500, height=500)
        #self.root.maxsize(width=1000, height=1000)

        self.root.resizable(width=True, height=False)
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
        # Presentation (row 0)
        #------------------------------

        widgets.create_label(self, self.frame_connexion, 0, 0, 4, \
                    name='label_invit', text='Veuillez entrer vos informations', \
                    font=('Courrier New', '18', 'bold underline'))

        #------------------------------
        # Email (row 1)
        #------------------------------

        widgets.create_label(self, self.frame_connexion, 1, 0, 2, \
                    name='label_pseudo', text='Adresse mail :')

        self.pseudo = tkinter.StringVar()
        self.pseudo.set(u'example@exemple.com')

        widgets.create_entry(self, self.frame_connexion, 1, 2, 2, \
                    name='entry_pseudo', textvariable=self.pseudo)

        #------------------------------
        # Password (row 2)
        #------------------------------

        widgets.create_label(self, self.frame_connexion, 2, 0, 2, \
                    name='label_pass', text='Mot de passe : ')

        self.password = tkinter.StringVar()
        self.password.set(u"password")

        widgets.create_entry(self, self.frame_connexion, 2, 2, 2, \
                    name='entry_password', textvariable=self.password, show = '*')

        #------------------------------
        # BUTTON <Connexion> (row 3)
        #------------------------------

        widgets.create_button(self, self.frame_connexion, 3, 3, \
            name = 'button_connexion', text = 'Connexion', \
            command = functions.showmyId(self))

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

        #------------------------------
        # TEST (row 4)
        #------------------------------

if __name__ == "__main__":
    #If the program is used by itself
    import tkinter
    f = interface_tk()
