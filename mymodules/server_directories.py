#!usr/bin/python3
#-*- coding : utf8 -*-

import imapclient, pyzmail, pprint, os, time

#-----------------------------
#	TESTED
#-----------------------------

def print_all_folders(imapObj): #WORKS_TO_KEEP
    """ Print folders in server No return. """
    myFolders = imapObj.list_folders()
    pprint.pprint(myFolders)

def get_all_folders(imapObj): #WORKS_TO_KEEP
    """ List folders in server and return them as a list """
    myFolders = imapObj.list_folders()

    return myFolders

#---------------------------------------
#	Not TESTED yet / Not NEEDED anymore
#---------------------------------------
