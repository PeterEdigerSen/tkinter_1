from tkinter import Button, Frame, Tk  # Python 2


def func(_event=None):
    print("Hello, world")


root = Tk()
root.bind('f', func)

frame = Frame(root)
frame.pack()

button = Button(frame, text="Hello", command=func)
button.pack(side='left')

root.mainloop()
