import functools
import tkinter as tk


class Key(tk.Button):
    def white(self):
        self.configure(fg='white')

    def red(self):
        self.configure(fg='red')


def add_digit(digit, event=None):
    msg.configure(text=(msg.cget('text') + str(digit)))
    current_key = keys[digit]
    for i in range(0, 1000, 100):
        current_key.after(i, current_key.white)
        current_key.after(i + 50, current_key.red)


def remove_digit(event=None):
    msg.configure(text=msg.cget('text')[:-1])


def destroy_master(event=None):
    master_widget.destroy()


master_widget = tk.Tk()
frame = tk.Frame(master_widget, bg='light blue')
frame.pack()


def grid_place(digit):
    if digit == 0:
        return 3, 0, 2
    else:
        return (digit - 1) // 3, (digit - 1) % 3, 1


keys = []
for i in range(0, 10):
    r, c, cs = grid_place(i)
    keys.append(
        Key(frame,
            text=i,
            command=functools.partial(add_digit, i),
            fg="red",
            bg='grey',
            width=5,
            height=3,
            relief=tk.GROOVE))
    keys[i].grid(row=r,
                 column=c,
                 columnspan=cs,
                 sticky=tk.E + tk.W,
                 padx=5,
                 pady=5)
    master_widget.bind(str(i), functools.partial(add_digit, i))

tk.Button(frame,
          text='DEL',
          command=remove_digit,
          fg="red",
          width=5,
          height=3). \
    grid(row=3,
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

tk.Button(frame,
          text='QUIT',
          command=destroy_master,
          fg="red",
          width=5,
          height=3). \
    grid(row=5,
         column=0,
         columnspan=3,
         sticky=tk.E + tk.W,
         padx=5,
         pady=5)
master_widget.bind('q', destroy_master)

master_widget.mainloop()
