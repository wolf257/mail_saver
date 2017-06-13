'''
 l1diffpages for level 1.
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

#====================================================================================
# TODO : Modify Button StartPage to reinitialize
    # create it as a Button with a function double (go_to_page AND reinitialize)
    # don't forget to copy the function show_frame to l2functions
#====================================================================================

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

    def __init__(self, parent, controller) : #,  width=400, height=300):
        tkinter.Frame.__init__(self, parent) #, width=width, height=height)
        #self.grid(sticky='we')
        #self.grid_columnconfigure(0, weight=1)

        #------------------------------
        # Titre Page : Hors FC
        #------------------------------

        self.controller = controller
        label = tkinter.Label(self, text="PageConnexion", font=controller.title_font)
        label.grid()#sticky='ne')

        #------------------------------
        # Frame CENTRAL (FC)
        #------------------------------

        parent = tkinter.Frame(self, bd='8', bg='green', \
            highlightthickness='10', highlightcolor='blue')
        parent.grid()

            #------------------------------
            # FC : Presentation (row 0)
            #------------------------------

        widgets.create_label_text(self, parent, 0, 0, 4, \
                    name='label_invit', text='Veuillez entrer vos informations', \
                    font=('Courrier New', '18', 'bold underline'))

            #------------------------------
            # FC : Email (row 1)
            #------------------------------

        widgets.create_label_text(self, parent, 1, 0, 2, \
                    name='label_pseudo', text='Adresse mail :')

        self.pseudo = tkinter.StringVar()
        self.pseudo.set(u'example@exemple.com')

        widgets.create_entry(self, parent, 1, 2, 2, \
                    name='entry_pseudo', textvariable=self.pseudo)

            #------------------------------
            # FC : Password (row 2)
            #------------------------------

        widgets.create_label_text(self, parent, 2, 0, 2, \
                    name='label_pass', text='Mot de passe : ')

        self.password = tkinter.StringVar()
        self.password.set(u"password")

        widgets.create_entry(self, parent, 2, 2, 2, \
                    name='entry_password', textvariable=self.password, show = '*')

            #------------------------------
            # FC : Label myId (row 3)
            # 	BUTTON <Connexion> (row 4)
            # 	BUTTON <Reinitialize> (row 5) (temporary)
            #------------------------------

        self.myId = tkinter.StringVar()
        widgets.create_label_textvar(self, parent, 3, 0, 4, name='label_id', textvariable = self.myId)

        self.myId.set('Click on connexion to Change me !' )

        widgets.create_button(self, parent, 4, 3, \
            name = 'button_connexion', text = 'Connexion', \
            command = lambda : functions.showmyId(self, self.myId, self.pseudo))

        widgets.create_button(self, parent, 5, 3, \
            name = 'button_reinit', text = 'Reinitialize', \
            command = lambda : functions.reinitialize(self, self.myId, self.pseudo))

        #------------------------------
        # Button <Go to Start> : Hors FC
        #------------------------------

        button = tkinter.Button(self, text="Go to the start page", \
            command=lambda: controller.show_frame("StartPage"))
        button.grid()
