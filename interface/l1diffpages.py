'''
 L1DIFFPAGES for level 1.
 Easier to visualize the tree view.
'''

import tkinter
from tkinter import font

#Depending on where you call mainpage, you need to import differently
try :
    import l2widgets as widgets
    import l2functions as functions
except :
    import interface.l2widgets as widgets
    import interface.l2functions as functions

class StartPage(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.controller = controller

        label = tkinter.Label(self, text="This is the start page", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)
        label.grid()

        button1 = tkinter.Button(self, text="Go to PageTest", \
            command=lambda: controller.show_frame("PageTest"))
        button2 = tkinter.Button(self, text="Go to PageConnexion", \
            command=lambda: controller.show_frame("PageConnexion"))
        button1.grid()
        button2.grid()


class PageTest(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.controller = controller

        label = tkinter.Label(self, text="This is PageTest", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)
        label.grid()

        button = tkinter.Button(self, text="Go to the start page", \
            command=lambda: controller.show_frame("StartPage"))
        button.grid()


class PageConnexion(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.controller = controller
        label = tkinter.Label(self, text="PageConnexion", font=controller.title_font)
        label.grid()

        #label.pack(side="top", fill="x", pady=10)

        #------------------------------
        # Frame
        #------------------------------

        parent = tkinter.Frame(self, bd='8', bg='yellow', \
            highlightthickness='10', highlightcolor='blue')
        parent.grid()
        #parent.grid_columnconfigure(0, weight=4)

        #------------------------------
        # Presentation (row 0)
        #------------------------------

        widgets.create_label(self, parent, 0, 0, 4, \
                    name='label_invit', text='Veuillez entrer vos informations', \
                    font=('Courrier New', '18', 'bold underline'))

        #------------------------------
        # Email (row 1)
        #------------------------------

        widgets.create_label(self, parent, 1, 0, 2, \
                    name='label_pseudo', text='Adresse mail :')

        self.pseudo = tkinter.StringVar()
        self.pseudo.set(u'example@exemple.com')

        widgets.create_entry(self, parent, 1, 2, 2, \
                    name='entry_pseudo', textvariable=self.pseudo)

        #------------------------------
        # Password (row 2)
        #------------------------------

        widgets.create_label(self, parent, 2, 0, 2, \
                    name='label_pass', text='Mot de passe : ')

        self.password = tkinter.StringVar()
        self.password.set(u"password")

        widgets.create_entry(self, parent, 2, 2, 2, \
                    name='entry_password', textvariable=self.password, show = '*')

        #------------------------------
        # BUTTON <Connexion> (row 3)
        #------------------------------

        widgets.create_button(self, parent, 3, 3, \
            name = 'button_connexion', text = 'Connexion', \
            command = functions.showmyId(self))

        #==============> TEST
        self.myId = tkinter.StringVar()
        self.label_show = tkinter.Label(parent, textvariable=self.myId, \
               anchor="center",) #font=('Courrier New', '16', 'bold underline'))
        self.label_show.grid(row=4, column=0,columnspan=4,sticky='EW')
        self.myId.set('Click on Connexion to change me !')
        #==============>

        #------------------------------
        # RESIZING
        #------------------------------

        #parent.grid_columnconfigure(0, weight=4)

        button = tkinter.Button(self, text="Go to the start page", \
            command=lambda: controller.show_frame("StartPage"))
        button.grid()

        #parent.grid_columnconfigure(0, weight=1)
