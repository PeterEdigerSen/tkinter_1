from tkinter import *



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

filemenu = Menu(menubar, tearoff=1, activeforeground='red', postcommand=post)
filemenu.add_cascade(label="New12", menu=newmenu)
filemenu.add_command(label="New", command=lambda: donothing('NEW'))
filemenu.add_command(label="Open", command=lambda: donothing("Open"))
filemenu.add_command(label="Save", command=lambda: donothing("Save"))
filemenu.add_command(label="Save as...", command=lambda: donothing("Save as..."))
filemenu.add_command(label="Close", command=lambda: donothing("Close"))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(menubar, tearoff=1)
editmenu.add_command(label="Undo", command=lambda: donothing("Undo"))
editmenu.add_cascade(label="New", menu=newmenu)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=lambda: donothing("Cut"))
editmenu.add_command(label="Copy", command=lambda: donothing("Copy"))
editmenu.add_command(label="Paste", command=lambda: donothing("Paste"))
editmenu.add_command(label="Delete", command=lambda: donothing("Delete"))
editmenu.add_command(label="Select All", command=lambda: donothing("Select All"))


def pv1v2():
    print(v1.get(), v2.get())


v1 = IntVar(value=1)
v2 = IntVar(value=100)

dfn = BooleanVar(value=False)
dsn = BooleanVar(value=True)
dph = BooleanVar(value=False)

game_menu = Menu(menubar)
game_menu.add_radiobutton(label='Game1', variable=v1, value=1, command=pv1v2)
game_menu.add_radiobutton(label='Game2', variable=v1, value=2, command=pv1v2)
game_menu.add_radiobutton(label='Game3', variable=v1, value=3, command=pv1v2)
game_menu.add_separator()
game_menu.add_radiobutton(label='Two players', variable=v2, value=100, command=pv1v2)
game_menu.add_radiobutton(label='Three players', variable=v2, value=101, command=pv1v2)

game_menu2 = Menu(menubar)
game_menu2.add_radiobutton(label='Game3', variable=v1, value=4, command=pv1v2)
game_menu2.add_radiobutton(label='Game4', variable=v1, value=5, command=pv1v2)

option_menu = Menu(menubar)
option_menu.add_checkbutton(label='Display first names', variable=dfn, offvalue=False, onvalue=True)
option_menu.add_checkbutton(label='Display second names', variable=dsn, offvalue=False, onvalue=True)
option_menu.add_checkbutton(label='Display phone', variable=dph, offvalue=False, onvalue=True)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=lambda: donothing("Help Index"))
helpmenu.add_command(label="About...", command=lambda: donothing("About..."))

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label='Game', menu=game_menu)
menubar.add_cascade(label='Game 2', menu=game_menu2)
menubar.add_cascade(label="Options", menu=option_menu)
menubar.add_cascade(label="Help", menu=helpmenu)
menubar.add_command(label='Extra', command=donothing)

popup = Menu(frame1, tearoff=0)  ## Popup-Menue
popup.add_command(label='Info', command=info)
popup.add_separator()
popup.add_command(label='Beenden', command=ende)

frame1.bind('<Button-3>', popupMenu)

root.mainloop()
