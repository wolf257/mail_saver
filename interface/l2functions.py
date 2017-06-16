'''
 L2FUNCTIONS for level 2.
 Easier to visualize the tree view.
'''

import tkinter
try:
    import interface.l1diffpages
except :
    import l1diffpages 

def showmyId(self, vartoset, vartoget) :
    #print("Kalanakha")
    vartoset.set('Your email is : ' + vartoget.get() + "\nThat\'s the only thing I can do by now!")
    #print(self.pseudo.get()
