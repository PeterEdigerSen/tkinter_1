import tkinter as tk
import os
import functools

message = ''


def read_aloud(msg_par):
    msg_par_as_str = str(msg_par)
    # os.system('say ' + msg_par_as_str)
    global message
    global msg
    message = message + msg_par_as_str
    msg.configure(bg='light green', text=message, font=('times', 24, 'italic'))


master_widget = tk.Tk()
button_panel = tk.Frame(master_widget, bg='light blue')
button_panel.pack()
info_panel = tk.Frame(master_widget, bg='blue')
info_panel.pack()

for i in range(1, 10):
    button = tk.Button(button_panel,
                       text=i, command=functools.partial(read_aloud, i),
                       fg="red", bg='grey', width=5, height=3,
                       relief=tk.GROOVE)
    button.grid(row=(i - 1) // 3, column=(i - 1) % 3, padx=5, pady=5)
button = tk.Button(button_panel,
                   text=0, command=functools.partial(read_aloud, 0),
                   fg="red", width=5, height=3)
button.grid(row=3, column=1)

msg = tk.Label(info_panel)
msg.pack()

master_widget.mainloop()
