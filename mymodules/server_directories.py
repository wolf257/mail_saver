#!usr/bin/python3
#-*- coding : utf8 -*-

import imapclient
import pyzmail
import pprint
import os
import time

import mymodules.server_messages as myserver_messages

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
