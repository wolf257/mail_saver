#!usr/bin/python3
#-*- coding : utf8 -*-


#-------------------
# MAIN PART
#-------------------

import mymodules.connections as myconnections
import mymodules.mails as mymails
import mymodules.local_directories as mylocal_directories
import mymodules.server_directories as myserver_directories
import mymodules.local_messages as mylocal_messages
import mymodules.server_messages as myserver_messages

imapObj = myconnections.connect()

#myserver_directories.print_all_folders(imapObj)

#mylocal_directories.create_directories(imapObj)

#mymails.basic_process(imapObj)

myconnections.disconnect(imapObj)
