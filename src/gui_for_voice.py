import functools
from tkinter import *
import os

count = 0


def peep(text):
    os.system('say ' + str(text))
    global count
    count += 1
    return count


root = Tk("qq", "pp", "rr")
label_texts = (
    "How are you?",
    "Hello Peter Junior!",
    "Hallo Peter Senior",
    "Привет Ольга")

for label_text in label_texts:
    w1 = Button(root, text=label_text,
                command=functools.partial(peep, label_text),
                width=15, height=5,
                fg="blue", bg="yellow",
                activebackground="yellow", activeforeground="red",
                highlightcolor="black",
                relief=RIDGE,
                bd=10,
                pady=10,
                state=NORMAL,
                underline=0
                )
    w1.pack(fill=Y)
#    i = w1.invoke()
#    print(i)

root.mainloop()
