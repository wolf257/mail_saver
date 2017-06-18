#!usr/bin/python3
#-*- coding : utf8 -*-

#================================
# List functions :
#	l_write_message(rawMessages, i, uid)
#================================

import imapclient
import pyzmail
import pprint
import os
import time

#====================================================================================
#TODO : 17/06/18 : l_write_message writes them all in ONE file.
#	Create One file BY message with appropriated naming.
# + Why not ask the user if he wants it in one place or separated
#====================================================================================

def l_create_message_file() :
     #create file with right name
     pass

def l_write_message(rawMessages, i, uid) :
    #open file with right name
    #write

    message = pyzmail.PyzMessage.factory(rawMessages[i][uid][b'BODY[]'])

    expediteur = message.get_address('from')
    sujet = message.get_subject()
    destinataire = message.get_addresses('to')

    content = message.text_part.get_payload().decode(message.text_part.charset)

    print("Enregistrement du mail : ", i , " de la boite. \n")

    with open("essai_write.txt", 'at') as f:
        try :
            f.write("Il a pour sujet : " + sujet + "\n")
        except :
            print("Probleme de sujet")
        try :
            f.write("Il a pour expediteur : " + expediteur[1] + "\n")
        except :
            print("Probleme expediteur")
        try :
            f.write("===============================\n\n")
        except :
            print("PRobleme fin de message")

    print("C'est bon pour lui. \n")
