#!usr/bin/python3
#-*- coding : utf8 -*-

import imapclient, pyzmail, pprint, os, time

#-----------------------------
#	TESTED
#-----------------------------

def create_directories(imapObj): #WORKS_TO_KEEP
    """ CREATES ALL THE DIRECTORIES existing IN the SERVERS """

    list = imapObj.list_folders()

    print("-------------- CREATION SUR VOTRE MACHINE DES DOSSIERS --------------")

    for line in list :
        if line[2] == '[Gmail]/Corbeille' :
            continue

        os.makedirs(time.strftime("%Y%m%d")+'/'+line[2])
        print("--- Le dossier : ", line[2] , " a été créé. ---")

    print("-------------- OPERATION 'CREATION DOSSIERS' TERMINÉE --------------")






#---------------------------------------
#	Not TESTED yet / Not NEEDED anymore
#---------------------------------------
