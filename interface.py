#usr/bin/python3
#-*- coding : utf8 -*-

import tkinter as tk
import tkinter.messagebox as mbox
import tkinter.filedialog as fdialog

import mymodules.connections as myconnections
import mymodules.mails as mymails
import mymodules.local_directories as mylocal_directories
import mymodules.server_directories as myserver_directories
import mymodules.local_messages as mylocal_messages
import mymodules.server_messages as myserver_messages

#Fenetre principale
root = tk.Tk()
root.title('Fenetre principale')

box = tk.LabelFrame(root, text='go')
box.grid(padx=40)

#Message intro
intro = tk.Label(box, text='Bienvenue sur ce programme\n Faites vous plaisir.')
intro.grid(row=0, column=0)


#Bouton Quitter
quit = tk.Button(box, text='Quitter', command=root.quit)
quit.grid(row=2, column=3)

root.mainloop()


#imapObj = myconnections.connect()

#myconnections.disconnect(imapObj)
