import tkinter as tk
import os
import functools


def add_digit_keyboard(event):
    add_digit(event.char)


def add_digit(msg_par):
    msg.configure(text=(msg.cget('text') + str(msg_par)))


def remove_digit(event=None):
    msg.configure(text=msg.cget('text')[:-1])


master_widget = tk.Tk()
button_panel = tk.Frame(master_widget, bg='light blue')
button_panel.pack(expand=False, fill=tk.BOTH)

for i in range(1, 10):
    tk.Button(button_panel,
              text=i,
              command=functools.partial(add_digit, i),
              fg="red",
              bg='grey',
              width=5,
              height=3,
              relief=tk.GROOVE). \
        grid(row=(i - 1) // 3,
             column=(i - 1) % 3,
             padx=5,
             pady=5)
    master_widget.bind(str(i), add_digit_keyboard)

tk.Button(button_panel,
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
b = tk.Button(button_panel,
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

msg = tk.Label(button_panel,
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
