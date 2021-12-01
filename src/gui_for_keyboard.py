import functools
from tkinter import Button, Tk  # Python 3


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

Button(root1, text="Hello 1", command=functools.partial(func, '1')).pack()
Button(root2, text="Hello 2", command=functools.partial(func, '2')).pack()

root1.bind('a', functools.partial(func, '1'))
root2.bind('b', functools.partial(func, '2'))
root2.bind('c', functools.partial(func, '3'))

root1.mainloop()

print('finish')
