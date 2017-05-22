#!usr/bin/python3
#-*- coding : utf8 -*-

import imapclient, pyzmail, pprint, os, time

#-----------------------------
#	TESTED
#-----------------------------


def create_directories(imapObj): #WORKS_TO_KEEP
    """ CREATES ALL THE DIRECTORIES existing IN the SERVERS """

    list = imapObj.list_folders()

    #TODO : Create folder save_date,
        # Put your self in it,
        # Create file report (a)
        # After each operation, write the content in (a)
        # Close (a)

    print("Sauvegarde effectuée le : " + time.strftime("%A") + ", " + time.strftime("%Y/%m/%d")
    + " at : " + time.strftime("%H:%M:%S") )
    print("Email concerné :" + "#email a mettre \n" )

    print("-------------- CREATION SUR VOTRE MACHINE DES DOSSIERS --------------")

    for line in list :
        if line[2] == '[Gmail]/Corbeille' :
            continue

        os.makedirs(time.strftime("%Y%m%d")+'_sauvegarde'+'/'+line[2])
        print("--- Le dossier : ", line[2] , " a été créé. ---")

    print("-------------- OPERATION 'CREATION DOSSIERS' TERMINÉE --------------")






#---------------------------------------
#	Not TESTED yet / Not NEEDED anymore
#---------------------------------------
