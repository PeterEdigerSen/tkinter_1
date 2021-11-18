import tkinter as tk

counter = 0


def counter_label(label):
    def count():
        global counter
        #if counter > 10:
        #    return
        label.config(text=str(counter))
        counter += 1
        label.after(1000, count)

    count()


root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, bg='yellow', fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()
