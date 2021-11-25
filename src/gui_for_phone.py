import tkinter as tk
import os
import functools


def add_digit(msg_par, event=None):
    msg.configure(text=(msg.cget('text') + str(msg_par)))


def remove_digit(event=None):
    msg.configure(text=msg.cget('text')[:-1])


master_widget = tk.Tk()
frame = tk.Frame(master_widget, bg='light blue')
frame.pack()


def grid_place(digit):
    if digit == 0:
        return 3, 0, 2
    else:
        return (digit - 1) // 3, (digit - 1) % 3, 1


for i in range(1, 10):
    r, c, cs = grid_place(i)
    tk.Button(frame,
              text=i,
              command=functools.partial(add_digit, i),
              fg="red",
              bg='grey',
              width=5,
              height=3,
              relief=tk.GROOVE). \
        grid(row=r,
             column=c,
             columnspan=cs,
             sticky=tk.E + tk.W,
             padx=5,
             pady=5)
    master_widget.bind(str(i), functools.partial(add_digit, i))

tk.Button(frame,
          text=0,
          command=functools.partial(add_digit, 0),
          fg="red",
          width=5,
          height=3). \
    grid(row=3,
         column=0,
         columnspan=2,
         sticky=tk.E + tk.W,
         padx=5,
         pady=5)

b = tk.Button(frame,
              text='DEL',
              command=remove_digit,
              fg="red",
              width=5,
              height=3)
b.grid(row=3,
       column=2,
       columnspan=2,
       sticky=tk.E + tk.W,
       padx=5,
       pady=5)
master_widget.bind('d', remove_digit)

msg = tk.Label(frame,
               bg='light green',
               anchor=tk.W,
               font=('times', 24, 'italic'))
msg.grid(row=4,
         column=0,
         columnspan=3,
         sticky=tk.E + tk.W,
         padx=5,
         pady=5)

master_widget.mainloop()
