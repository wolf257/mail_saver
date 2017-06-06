#!usr/bin/python3
#-*- coding : utf8 -*-

import imapclient, pyzmail, pprint, os, time
#import folders, messages
#-----------------------------
#	TESTED
#-----------------------------

#TODO : Encapsuler en créant un objet

def basic_process(imapObj):
    """ Entre in each directory, get all his message """

    print("-------------- ACQUISITION DES UIDs --------------")
    myFolders = get_all_folders(imapObj)

    for folder in myFolders : ## folder[2] sera un nom de dossier
        try :
            imapObj.select_folder(folder[2], readonly=True)
        except :
            print("On a un probleme sur le dossier : ", folder[2], ".")
        else :
            myUIDs = get_all_uids(imapObj)

            get_messages(imapObj, folder, myUIDs)
