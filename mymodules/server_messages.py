#!usr/bin/python3
#-*- coding : utf8 -*-

import imapclient, pyzmail, pprint, os, time
#from mails.py import *

def get_all_uids(imapObj): #WORKS_TO_KEEP
    """ List all uids and return them as list """
    myUIDs = imapObj.search()

    print("Il y a " , len(myUIDs) , " messages dans le dossier.") #, line[2], ".")

    return myUIDs

def get_messages(imapObj, folder, myUIDs) : #WORKS_TO_KEEP

    print("-------------- ACQUISITION DES MESSAGES DU DOSSIER " , folder[2] , " --------------")

    i = 1
    rawMessages = {}

    for uid in myUIDs :
        try :
            rawMessages[i] = imapObj.fetch([uid], ['BODY[]', 'FLAGS'])
            print("C'est bon pour le messages ", i, "de la boite : ", folder[2])
            #TEST :
            #pprint.pprint(rawMessages[i])

            message = pyzmail.PyzMessage.factory(rawMessages[i][uid][b'BODY[]'])
            # TEST :
            # print(" Il a pour sujet : ", message.get_subject())

        except :
            print("On a un probleme sur le mail ", i)

        finally :
            #TEST :
            #print("Test réussie")
            i += 1

#class message(object):
#    """docstring for message."""
