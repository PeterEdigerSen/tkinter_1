import tkinter as tk

root = tk.Tk()
pixelVirtual = tk.PhotoImage(width=1, height=1)
fr = tk.Frame(root)
fr.pack()
butt = tk.Label(fr, image=pixelVirtual, bg='blue', width='5i',height='5i')
butt.pack()

root.mainloop()
