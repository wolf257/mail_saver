#!usr/bin/python3
#-*- coding : utf8 -*-

import imapclient, pyzmail, pprint, os, time, getpass


IMAPServers = {'gmail' : 'imap.gmail.com', 'yahoo' : 'imap.mail.yahoo.com',
'outlook' : 'imap-mail.outlook.com', 'hotmail' : 'imap-mail.outlook.com', }


#----------------------------------------------------
def select_servers(pseudo) :
    if pseudo.endswith('gmail.com') :
        server = IMAPServers['gmail']
    elif pseudo.endswith('yahoo.com') or pseudo.endswith('yahoo.fr') :
        server = IMAPServers['yahoo']
    elif pseudo.endswith('outlook.com') or pseudo.endswith('outlook.fr') or pseudo.endswith('hotmail.com') or pseudo.endswith('hotmail.fr') :
        server = IMAPServers['outlook']
    #elif pseudo.endswith('hotmail.com') or pseudo.endswith('hotmail.fr') :
    #    server = IMAPServers['hotmail']
    else :
        print("Désolé, je ne peux pas encore traiter votre boîte.")
        quit()

    return server

#----------------------------------------------------
def connect(): #WORKS

    nom = input("Quelle est votre adresse mail (gmail pour le moment) ? ")
    server = select_servers(nom)

    password = getpass.getpass("Enter your password: ")

    try:
        imapObj = imapclient.IMAPClient(server, ssl=True)
        imapObj.login(nom, password)
    except :
        print("The connection did not work.")
        quit()
    else :
        print("-----------------------------------")
        print("Connexion reussie")
        print("-----------------------------------")

        return imapObj

#----------------------------------------------------
def disconnect(obj): #WORKS
    obj.logout()
    print("-----------------------------------")
    print("Déconnection reussie !")
    print("-----------------------------------")

#---------------------------------------
#	Not TESTED yet / Not NEEDED anymore
#---------------------------------------
