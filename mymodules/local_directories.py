#!usr/bin/python3
#-*- coding : utf8 -*-

import imapclient, pyzmail, pprint, os, time


def create_directories(imapObj): #WORKS_TO_KEEP
    #Commentaire : Si le dossier existe déjà, il y error.
    #TODO : Trouver solutions

    """ CREATES ALL THE DIRECTORIES existing IN the SERVERS """

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
        if folder[2] == '[Gmail]/Corbeille' :
            continue

        os.makedirs(time.strftime("%Y%m%d")+'_sauvegarde'+'/'+folder[2])
        print("--- Le dossier : ", folder[2] , " a été créé. ---")

    print("-------------- OPERATION 'CREATION DOSSIERS' TERMINÉE --------------")
