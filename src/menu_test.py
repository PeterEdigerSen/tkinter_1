import _curses
from tkinter import *

import click


def donothing(nothing_button="Do nothing button"):
    filewin = Toplevel(root)
    button = Button(filewin, text=nothing_button)
    button.pack()


def post():
    print('POST')


def info():
    print('INFO')


def ende():
    print('ENDE')


def popupMenu(event):
    popup.entryconfig(0, label='Coords:x=' + str(event.x) + '; y=' + str(event.y))
    popup.post(event.x_root, event.y_root)


root = Tk()
label = Label(text='Ohoho')
label.pack()
frame1 = Frame(root, width=100, height=100, bg='YELLOW')
frame1.pack(fill=BOTH, expand=YES)
frame2 = Frame(root, width=100, height=100)
frame2.pack()
# textfenster = Text(frame1,width=90)        ## Textfenster
# textfenster.pack(fill=BOTH,expand=YES)


menubar = Menu(root, tearoff=0)
root.config(menu=menubar)

newmenu = Menu(menubar)
newmenu.add_command(label="New 1", command=lambda: donothing('New 1'))
newmenu.add_command(label="New 2", command=lambda: donothing('New 2'))

filemenu = Menu(menubar, tearoff=0, postcommand=post)
filemenu.add_cascade(label="New12", menu=newmenu)
filemenu.add_command(label="New", command=lambda: donothing('NEW'))
filemenu.add_command(label="Open", command=lambda: donothing("Open"))
filemenu.add_command(label="Save", command=lambda: donothing("Save"))
filemenu.add_command(label="Save as...", command=lambda: donothing("Save as..."))
filemenu.add_command(label="Close", command=lambda: donothing("Close"))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=lambda: donothing("Undo"))
editmenu.add_cascade(label="New", menu=newmenu)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=lambda: donothing("Cut"))
editmenu.add_command(label="Copy", command=lambda: donothing("Copy"))
editmenu.add_command(label="Paste", command=lambda: donothing("Paste"))
editmenu.add_command(label="Delete", command=lambda: donothing("Delete"))
editmenu.add_command(label="Select All", command=lambda: donothing("Select All"))

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=lambda: donothing("Help Index"))
helpmenu.add_command(label="About...", command=lambda: donothing("About..."))

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Help", menu=helpmenu)
menubar.add_command(label='Extra', command=donothing)

popup = Menu(frame1, tearoff=0)  ## Popup-Menue
popup.add_command(label='Info', command=info)
popup.add_separator()
popup.add_command(label='Beenden', command=ende)

frame1.bind('<Button-2>', popupMenu)

root.mainloop()
