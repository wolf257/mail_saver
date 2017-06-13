'''
 l2functions for level 2.
 Easier to visualize the tree view.
'''

import tkinter
import interface.l1diffpages

def showmyId(self, vartoset, vartoget) :
    #print("...")
    vartoset.set('Your email is : ' + vartoget.get() + "\nThat\'s the only thing I can do by now!")

# to use it with l2functions as functions
    # functions.showmyId(self, vartoset, vartoget)
