from tkinter import *


def ffff():
    print('Message')


root = Tk()
top_yellow_frame = Frame(root, bg='yellow')
top_yellow_frame.pack()

bottom_magenta_frame = Frame(root, bg='magenta')
bottom_magenta_frame.pack(side=BOTTOM)

left_slate_blue_frame = Frame(root, bg='slate blue')
left_slate_blue_frame.pack(side=LEFT)

right_dark_sea_green_frame = Frame(root, bg='dark sea green')
right_dark_sea_green_frame.pack(side=RIGHT)

redbutton = Button(top_yellow_frame, text="Red", anchor=SW, fg="red", width=15, height=3, command=ffff())
redbutton.pack(side=RIGHT, fill=X)
greenbutton = Button(top_yellow_frame, text="green", fg="green")
greenbutton.pack(side=RIGHT)
bluebutton = Button(top_yellow_frame, text="Blue", fg="blue")
bluebutton.pack(side=RIGHT)

blackbutton = Button(bottom_magenta_frame, text="Black", bg='yellow', fg="black", width=15)
blackbutton.pack(side=BOTTOM)
blackbutton_2 = Button(bottom_magenta_frame, text="Black", bg='yellow', fg="black")
blackbutton_2.pack(side=BOTTOM)

blackbutton_3 = Button(left_slate_blue_frame, text="Black", bg='yellow', fg="black", height=6)
blackbutton_3.pack(side=LEFT)
blackbutton_4 = Button(left_slate_blue_frame, text="Black", bg='yellow', fg="black")
blackbutton_4.pack(side=LEFT)

blackbutton_5 = Button(right_dark_sea_green_frame, text="Black", bg='yellow', fg="black", height=6)
blackbutton_5.pack(side=LEFT)
blackbutton_6 = Button(right_dark_sea_green_frame, text="Black", bg='yellow', fg="black")
blackbutton_6.pack(side=LEFT)

root.mainloop()
