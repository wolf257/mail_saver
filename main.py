#!usr/bin/python3
#-*- coding : utf8 -*-


#-------------------
# MAIN PART
#-------------------

import back_code.connections as myconnections
import back_code.cmain as mails_main
import back_code.local_directories as mylocal_directories
import back_code.server_directories as myserver_directories
import back_code.local_messages as mylocal_messages
import back_code.server_messages as myserver_messages

import interface.l0mainpage as mainpage

while 1 :

    #========================
    # 1st choice
    #========================

    a = input("How do you want me to work ? " + \
    "\n 1 - via Terminal" + \
        "\n 2 - via GUI" + \
        "\n (enter) - Exit" + \
        "\nYour choice : ")

    #==================================
    if a.strip() == '1' :

        imapObj = myconnections.connect()

        #========================
        # 2nd choice
        #========================

        b = input("What do you want me to do ? " + \
            "\n a - Basic process" + \
            "\n b - Create directories"+
            "\nYour choice : ")


        if b.strip() == 'a' :
            mails_main.basic_process(imapObj)
        elif b.strip == 'b' :
            mylocal_directories.create_directories(imapObj)
        else :
            print("I dont know what to do. (restart)")

        myconnections.disconnect(imapObj)

    #==================================
    elif a.strip() == '2' :
        print("Go see the GUI. Talk to you later.")
        mainpage.MainWindow()
            # Note : program resume without waiting until you close the GUI

    #==================================
    elif a.strip() == '' :
        print("+++++++++++++++++++++++++++++")
        print("Thank you ! Bye.")
        print("+++++++++++++++++++++++++++++")

        break

    #==================================
    else :
        print("\n-----------------------------------")
        print("I dont know what to do. (I restart).")
        print("-----------------------------------")
