#!usr/bin/python3
#-*- coding : utf8 -*-

#================================
# List functions :
#================================

import imapclient
import pyzmail
import pprint
import os
import time

import back_code.messages as messages

#-----------------------------
#	TESTED
#-----------------------------

def s_print_all_folders(imapObj): #WORKS_TO_KEEP
    """ Print folders in server No return. """
    myFolders = imapObj.list_folders()
    pprint.pprint(myFolders)

def s_get_all_folders(imapObj): #WORKS_TO_KEEP
    """ List folders in server and return them as a list """
    myFolders = imapObj.list_folders()

    return myFolders

#================================
# List functions :
#	l_create_directories(imapObj),
#================================

import imapclient
import pyzmail
import pprint
import os
import time

def l_create_directories(imapObj): #WORKS_TO_KEEP
    #Commentaire : Si le dossier existe déjà, il y error.
    #TODO : Trouver solutions

    """ CREATES LOCALLY ALL THE DIRECTORIES existing IN the SERVERS """

    myFolders = imapObj.list_folders()

    #TODO : Create folder save_date,
        # Put your self in it,
        # Create file report (a)
        # After each operation, write the content in (a)
        # Close (a)

    print("Sauvegarde effectuée le : " + time.strftime("%A") + ", " + time.strftime("%Y/%m/%d")
    + " at : " + time.strftime("%H:%M:%S") )
    print("Email concerné :" + "#email a mettre \n" )

    print("-------------- CREATION SUR VOTRE MACHINE DES DOSSIERS --------------")

    for folder in myFolders :
        if folder[2] == '[Gmail]/Corbeille' or folder[2] == '[Gmail]/Spam' :
            continue

        os.makedirs(time.strftime("%Y%m%d")+'_sauvegarde'+'/'+folder[2])
        print("--- Le dossier : ", folder[2] , " a été créé. ---")

    print("-------------- OPERATION 'CREATION DOSSIERS' TERMINÉE --------------")
