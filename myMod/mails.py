#!usr/bin/python3
#-*- coding : utf8 -*-

import imapclient, pyzmail, pprint, os, time

#-----------------------------
#	TESTED
#-----------------------------

def list_all_uids(imapObj): #WORKS_TO_KEEP
    """ GIVE US ALL UIDS"""
    UIDs = imapObj.search()

    print("Il y a " , len(UIDs) , " messages dans le dossier") #, line[2], ".")

    return UIDs

def list_all_folders(imapObj): #WORKS_TO_KEEP
    """ LIST FOLDER IN SERVER AND RETURN IT AS A LIST """
    list = imapObj.list_folders()
    #pprint.pprint(list)

    return list

def list_messages(imapObj, line, UIDs) : #WORKS_TO_KEEP

    print("-------------- ACQUISITION DES MESSAGES DU DOSSIER " , line[2] , " --------------")

    i = 1
    rawMessages = {}

    for uid in UIDs :
        try :
            rawMessages[i] = imapObj.fetch([uid], ['BODY[]', 'FLAGS'])
            print("C'est bon pour le messages ", i, "de la boite : ", line[2])
            #pprint.pprint(rawMessages[i])

            message = pyzmail.PyzMessage.factory(rawMessages[i][uid][b'BODY[]'])
            # TEST :
            # print("     Il a pour sujet : ", message.get_subject())

        except :
            print("On a un probleme sur le mail ", i)

        finally :
            #print("Test réussie")
            i += 1

def basic_process(imapObj):
    """ ENTER IN ALL DIRECTORIES, GET ALL MESSAGES """

    print("-------------- ACQUISITION DES UIDs --------------")

    list = list_all_folders(imapObj)

    for line in list : ## line[2] sera un nom de dossier
        try :
            imapObj.select_folder(line[2], readonly=True)
        except :
            print("On a un probleme.")
        else :
            UIDs = list_all_uids(imapObj)

            list_messages(imapObj, line, UIDs)






#-----------------------------
#	Not TESTED yet / Not NEEDED anymore
#-----------------------------


def get_raw_messages(imapObj, list_uids):
    """ """
    #print("-------------- ACQUISITION DES MESSAGES --------------")

    #rawMessages = {}
    for uid in list_uids :
        print(uid , end = '***')
        #rawMessages[uid] = imapObj.fetch([uid], ['BODY[]', 'FLAGS'])
            #rawMessages = imapObj.fetch([uid], ['BODY[]', 'FLAGS'])


    #for message in rawMessages :
        #pprint.pprint(message)

    #return rawMessages #dict_raws plus loin
