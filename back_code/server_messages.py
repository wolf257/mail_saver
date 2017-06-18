#!usr/bin/python3
#-*- coding : utf8 -*-

#================================
# List functions :
#	get_all_uids(imapObj, folder), messages_get_topic(rawMessages, i, uid),
#	messages_get_generals(rawMessages, i, uid), get_messages(imapObj, folder, myUIDs),
#================================

import imapclient
import pyzmail
import pprint
import os
import time

def get_all_uids(imapObj, folder): #WORKS_TO_KEEP
    """ List all uids and return them as list """
    myUIDs = imapObj.search()

    print("\n\nIl y a " , len(myUIDs) , " messages dans le dossier ", folder[2], ".") #, line[2], ".")

    return myUIDs

def messages_get_topic(rawMessages, i, uid):
    """ Test function : get and print topic of message """

    message = pyzmail.PyzMessage.factory(rawMessages[i][uid][b'BODY[]'])

    sujet = message.get_subject()

    print("Il a pour sujet : ", sujet)

def messages_get_generals(rawMessages, i, uid):
    """ Get and print generalities about the message (from, subject, to) """

    message = pyzmail.PyzMessage.factory(rawMessages[i][uid][b'BODY[]'])

    expediteur = message.get_address('from')
    sujet = message.get_subject()
    destinataire = message.get_addresses('to')

    print("Il a pour sujet : ", sujet)
    print("Il a pour expediteur : ", expediteur[1])
    if destinataire != 0 :
        print("et il est destiné à : ", destinataire)

def get_messages(imapObj, folder, myUIDs) : #WORKS_TO_KEEP

    print("-------------- ACQUISITION DES MESSAGES DU DOSSIER " , folder[2] , " --------------")

    i = 1
    rawMessages = {}

    for uid in range(1,3,1) : #myUIDs :
        try :
            rawMessages[i] = imapObj.fetch([uid], ['BODY[]', 'FLAGS'])
            print("\nC'est bon pour le messages ", i, "de la boite : ", folder[2])
            #TEST :
            #pprint.pprint(rawMessages[i])

            #TEST :
            messages_get_topic(rawMessages, i, uid)

            #message = pyzmail.PyzMessage.factory(rawMessages[i][uid][b'BODY[]'])
            # TEST :
            #print(" Il a pour sujet : ", message.get_subject())

        except :
            print("On a un probleme sur le mail ", i)

        finally :
            #TEST :
            #print("Test réussie")
            i += 1

    '''
    for uid in myUIDs :
        try :
            rawMessages[i] = imapObj.fetch([uid], ['BODY[]', 'FLAGS'])
            print("C'est bon pour le messages ", i, "de la boite : ", folder[2])
            #TEST :
            #pprint.pprint(rawMessages[i])

            #messages_topic(i, uid)
            #message = pyzmail.PyzMessage.factory(rawMessages[i][uid][b'BODY[]'])
            # TEST :
            #print(" Il a pour sujet : ", message.get_subject())

        except :
            print("On a un probleme sur le mail ", i)

        finally :
            #TEST :
            #print("Test réussie")
            i += 1
    '''

def traitement_messages(arg):
    pass



#class message(object):
#    """docstring for message."""
