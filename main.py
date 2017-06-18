#!usr/bin/python3
#-*- coding : utf8 -*-


#-------------------
# MAIN PART
#-------------------

import time

import back_code.connections as myconnections
import back_code.cmain as mails_main
import back_code.local_directories as mylocal_directories
import back_code.server_directories as myserver_directories
import back_code.local_messages as mylocal_messages
import back_code.server_messages as myserver_messages

try:
    import interface.l0mainpage as mainpage
except:
    import l0mainpage as mainpage

while 1 :

    #========================
    # 1st choice
    #========================

    a = input("\nLevel 0 : How do you want me to work ? " + \
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
        while 1 :

            b = input("\n Level 1 : What do you want me to do ? " + \
                "\n a - Basic process" + \
                "\n b - Create directories"+ \
                "\n (enter) - Go back to the precedent options"
                "\nYour choice : ")


            if b.strip() == 'a' :
                mails_main.basic_process(imapObj)
            elif b.strip() == 'b' :
                mylocal_directories.l_create_directories(imapObj)
            elif b.strip() == '' :
                break
            else :
                print("I dont know what to do. (restart level 0)")

        myconnections.disconnect(imapObj)

    #==================================
    elif a.strip() == '2' :
        print("Go see the GUI. Talk to you later.")
        c = mainpage.MainWindow()
        c.mainloop() # Note : so the program won't resume without waiting until you close the GUI
        #the mainloop returns when the window dies.

        print("****************************")
        print("The GUI is closed.")
        print("****************************\n\n")

    #==================================
    elif a.strip() == '' :
        print("\n+++++++++++++++++++++++++++++")
        print("Thank you ! Bye.")
        print("+++++++++++++++++++++++++++++\n")

        break

    #==================================
    else :
        print("\n-----------------------------------")
        print("I dont know what to do. (Restart level 0).")
        print("-----------------------------------")
