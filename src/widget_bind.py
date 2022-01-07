import tkinter as tk
from tkinter import ttk

# There are two ways to bind a function to a widget.

root = tk.Tk()


def select(option=None):
    print(option)


# The function can be bound to widget with the parameter 'command'.

# If the function has no parameters, simply write its name
ttk.Button(root, text='Rock', command=select).pack()
# If the function has parameters use the lambda construction.
ttk.Button(root, text='Paper', command=lambda: select('Paper')).pack()

# Other way to bind is using of method 'bind'. This way is more sophisticated compared with the first one.
# Different event types can be handled, and more than one handler can be used for one event.

button_scissors = ttk.Button(root, text='Scissors')
button_scissors.pack()
button_scissors.bind('<Button-1>', lambda e: select('Scissors'))
button_scissors.bind('<Button-1>', lambda e: select('Scissors-2'), add=True)
root.mainloop()
