#!usr/bin/python3
#-*- coding : utf8 -*-


#-------------------
# MAIN PART
#-------------------

from myMod.connections import *
from myMod.directories import *
from myMod.positions import *
from myMod.mails import *

imapObj = connect()

#create_directories(imapObj)

#UIDs =
#basic_process(imapObj)

#get_raw_messages(imapObj, UIDs)

disconnect(imapObj)
