#!usr/bin/python3
#-*- coding : utf8 -*-


#-------------------
# MAIN PART
#-------------------

import mymodules.connections as myconnections
import mymodules.mails as mymails
import mymodules.local_directories as mylocaldirectories
import mymodules.server_directories as myserverdirectories
import mymodules. local_messages as mylocalmessages
import mymodules.server_messages as myservermessages

imapObj = myconnections.connect()

#myserverdirectories.print_all_folders(imapObj)

#mylocaldirectories.create_directories(imapObj)

#basic_process(imapObj)

#get_raw_messages(imapObj, UIDs)

myconnections.disconnect(imapObj)
