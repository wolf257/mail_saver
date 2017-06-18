#!usr/bin/python3
#-*- coding : utf8 -*-

#================================
# List functions :
#	s_get_all_uids(imapObj, folder), s_messages_get_topic(rawMessages, i, uid),
#	s_messages_get_generals(rawMessages, i, uid), s_get_messages(imapObj, folder, myUIDs),
#================================

import imapclient
import pyzmail
import pprint
import os
import time

#====================================================================================
#TODO :  17/06/18 : 1 - Verify in s_get_messages that i won't look in the file we don't want
#		2 - rewrite fonction to either WRITE OR PRINT
#====================================================================================

import back_code.local_messages as mylocal_messages

def s_get_all_uids(imapObj, folder): #WORKS_TO_KEEP
    """ List all uids and return them as list """
    myUIDs = imapObj.search()

    print("\n\nIl y a " , len(myUIDs) , " messages dans le dossier ", folder[2], ".") #, line[2], ".")

    return myUIDs

def s_messages_get_topic(rawMessages, i, uid):
    """ Test function : get and print topic of message """

    message = pyzmail.PyzMessage.factory(rawMessages[i][uid][b'BODY[]'])

    sujet = message.get_subject()
    #content = message.text_part.get_payload().decode(message.text_part.charset)

    print("Il a pour sujet : ", sujet)
    #print("Et contenu : ", content)

def s_messages_get_generals(rawMessages, i, uid):
    """ Get and print generalities about the message (from, subject, to) """

    message = pyzmail.PyzMessage.factory(rawMessages[i][uid][b'BODY[]'])

    expediteur = message.get_address('from')
    sujet = message.get_subject()
    destinataire = message.get_addresses('to')

    print("Il a pour sujet : ", sujet)
    print("Il a pour expediteur : ", expediteur[1])
    if destinataire != 0 :
        print("et il est destiné à : ", destinataire)

def s_get_messages(imapObj, folder, myUIDs) : #WORKS_TO_KEEP


    print("-------------- ACQUISITION DES MESSAGES DU DOSSIER " , folder[2] , " --------------")

    i = 1
    rawMessages = {}

    for uid in range(1,3,1) : #myUIDs :
        try :
            rawMessages[i] = imapObj.fetch([uid], ['BODY[]', 'FLAGS'])
            #print("\nC'est bon pour le messages ", i, "de la boite : ", folder[2])
            #TEST :
            #pprint.pprint(rawMessages[i])

            #TEST :
            #s_messages_get_topic(rawMessages, i, uid)
            mylocal_messages.l_write_message(rawMessages, i, uid)

            #message = pyzmail.PyzMessage.factory(rawMessages[i][uid][b'BODY[]'])
            # TEST :
            #print(" Il a pour sujet : ", message.get_subject())

        except :
            print("On a un probleme sur le mail ", i)

        finally :
            #TEST :
            #print("Test réussie")
            i += 1

def s_traitement_messages(arg):
    pass



#class message(object):
#    """docstring for message."""
