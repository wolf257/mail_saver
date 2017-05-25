#!usr/bin/python3
#-*- coding : utf8 -*-


#-------------------
# MAIN PART
#-------------------

from myMod.connections import *
from myMod.directories import *
from myMod.mails import *

imapObj = connect()

#print_all_folders(imapObj)

#create_directories(imapObj)

#basic_process(imapObj)

#get_raw_messages(imapObj, UIDs)

disconnect(imapObj)
