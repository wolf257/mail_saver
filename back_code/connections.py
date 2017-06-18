#!usr/bin/python3
#-*- coding : utf8 -*-

#================================
# List functions :
#	select_servers(identifiant), connect(), disconnect()
#================================

import imapclient
import pyzmail
import pprint
import os
import time
import getpass

IMAPServers = {'gmail' : 'imap.gmail.com', 'yahoo' : 'imap.mail.yahoo.com',
'outlook' : 'imap-mail.outlook.com', 'hotmail' : 'imap-mail.outlook.com', }

#====================================================================================
#TODO :
#====================================================================================


#----------------------------------------------------
def select_servers(identifiant) : #WORKS
    """ Select the right server according to the ending of the mail """

    if identifiant.endswith('gmail.com') :
        server = IMAPServers['gmail']
    elif identifiant.endswith('yahoo.com') or identifiant.endswith('yahoo.fr') :
        server = IMAPServers['yahoo']
    elif identifiant.endswith('outlook.com') or identifiant.endswith('outlook.fr') or identifiant.endswith('hotmail.com') or identifiant.endswith('hotmail.fr') :
        server = IMAPServers['outlook']
    else :
        print("Désolé, je ne peux pas encore traiter votre boîte.")
        quit()

    return server

#----------------------------------------------------
def connect(): #WORKS
    """ Connection to the imap-server """

    identifiant = input("Quelle est votre adresse mail ? ").strip()
    server = select_servers(identifiant)

    password = getpass.getpass("Enter your password: ")

    try:
        imapObj = imapclient.IMAPClient(server, ssl=True)
        imapObj.login(identifiant, password)
    except :
        print("The connection did not work.")
        quit()
    else :
        print("-----------------------------------")
        print("Connexion reussie")
        print("-----------------------------------")

        return imapObj

#----------------------------------------------------
def disconnect(imapObj): #WORKS
    """ Disconnect from the imap-server """
    imapObj.logout()

    print("-----------------------------------")
    print("Déconnection reussie !")
    print("-----------------------------------")
