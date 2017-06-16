'''
 l2functions for level 2.
 Easier to visualize the tree view.
'''

import tkinter

try :
    import interface.l1diffpages
except:
    import l1diffpages

def showmyId(self, vartoset, vartoget) :
    #print("...")
    vartoset.set('Your email is : ' + vartoget.get() + "\nThat\'s the only thing I can do by now!")

# to use it with l2functions as functions
    # functions.showmyId(self, vartoset, vartoget)

def reinitialize(self, vartoset, vartoget) :
    #print("...")
    vartoget.set("example@example.com")
    vartoset.set("Reinitialization. \nMail cleared.")

# to use it with l2functions as functions
    # functions.reinitialize(self, vartoset, vartoget)

#====================================================================================
#TODO : For each function, add :
    #Print with the operation AND the time of the click
    #Will serve in the report
#====================================================================================
