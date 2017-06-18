#!usr/bin/python3
#-*- coding : utf8 -*-

#================================
# List functions :
#	s_print_all_folders(imapObj), s_get_all_folders(imapObj)
#================================

import imapclient
import pyzmail
import pprint
import os
import time

import back_code.server_messages as myserver_messages

#-----------------------------
#	TESTED
#-----------------------------

def s_print_all_folders(imapObj): #WORKS_TO_KEEP
    """ Print folders in server No return. """
    myFolders = imapObj.list_folders()
    pprint.pprint(myFolders)

def s_get_all_folders(imapObj): #WORKS_TO_KEEP
    """ List folders in server and return them as a list """
    myFolders = imapObj.list_folders()

    return myFolders

#---------------------------------------
#	Not TESTED yet / Not NEEDED anymore
#---------------------------------------
