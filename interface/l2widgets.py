'''
 L2WIDGETS for level 2.
 Easier to visualize the tree view.
'''

import tkinter

def create_label_text(self, parent, row, column, columnspan, name ='a', text='b', font=None) :
    self.name = tkinter.Label(parent, text=text, anchor="center", font=font)
    self.name.grid(row=row, column=column,columnspan=columnspan,sticky='EW')

# to use it with l2wigets as widgets
    # widgets.create_label_text(self, parent, row, column, columnspan, name, text, font)

def create_label_textvar(self, parent, row, column, columnspan, name ='a', textvariable = 'b', font=None) :
    self.name = tkinter.Label(parent, textvariable = textvariable, anchor="center", font=font)
    self.name.grid(row=row, column=column,columnspan=columnspan,sticky='EW')

# to use it with l2wigets as widgets
    # widgets.create_label_textvar(self, parent, row, column, columnspan, name, text, font)


def create_entry(self, parent, row, column, columnspan, name ='a', textvariable = 'b', show=None) :
    self.name = tkinter.Entry(parent, textvariable = textvariable, show = show)
    self.name.grid(row=row, column=column, columnspan=columnspan,sticky='EW')
    #self.entry_pseudo.bind("<Return>", self.PressEnter)

    self.name.focus_set()
    self.name.selection_range(0, tkinter.END)

# to use it with l2wigets as widgets
    # widgets.reate_entry(self, parent, row, column, columnspan, name, textvariable, show=None)

def create_button(self, parent, row, column, name = 'a', text = 'b', command=None) :
    self.name = tkinter.Button(parent, text = text, \
        command = command)
    self.name.grid(row=row, column=column)

# to use it with l2wigets as widgets
    # widgets.create_button(self, parent, row, column, name, text, command=None)
