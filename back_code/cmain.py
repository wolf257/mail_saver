#!usr/bin/python3
#-*- coding : utf8 -*-

#================================
# List functions :
#	basic_process(imapObj),
#================================

import imapclient
import pyzmail
import pprint
import os
import time

import back_code.connections as myconnections

import back_code.directories as directories

import back_code.messages as messages

#-----------------------------
#	TESTED
#-----------------------------

#TODO : Encapsuler en créant un objet

def basic_process(imapObj):
    """ Entre in each directory, get all his message """

    print("-------------- ACQUISITION DES UIDs --------------")
    myFolders = directories.s_get_all_folders(imapObj)

    for folder in myFolders : ## folder[2] sera un nom de dossier
        try :
            imapObj.select_folder(folder[2], readonly=True)
        except :
            print("On a un probleme sur le dossier : ", folder[2], ".")
        else :
            myUIDs = messages.s_get_all_uids(imapObj, folder)

            if len(myUIDs) > 0 :
                messages.s_get_messages(imapObj, folder, myUIDs)
            else :
                print("Le dossier est vide.")
