import functools
from tkinter import Button, Tk, PhotoImage, LEFT, RIGHT, TOP, CENTER, BOTTOM  # Python 3


def func(param, event=None):
    if event is None:
        txt = 'Mouse'
    else:
        txt = 'Key ' + event.char
    print("Hello, world " + param + ' (source: ' + txt + ')')


root1 = Tk(className='Oho 1')
root2 = Tk(className='Oho 2')
root1.geometry('200x200+500+500')
root2.geometry('200x200+800+500')

rose1 = PhotoImage(file='../files/rose_1_50x67.png')
rose2 = PhotoImage(file='../files/rose_2_100x133.png')

b1 = Button(root1, image=rose1, text='Label 2', compound=CENTER,
            width=50, height=50,
            command=functools.partial(func, '1'))
b1.pack(side=LEFT)
Button(root1, image=rose2, text='Label 1', compound=LEFT,
       width=50, height=50,
       command=functools.partial(func, '2')). \
    pack(side=RIGHT)

root1.bind('a', functools.partial(func, '1'))
root1.bind('b', functools.partial(func, '2'))
root2.bind('c', functools.partial(func, '3'))

root1.mainloop()

print('finish')
