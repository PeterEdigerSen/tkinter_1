import tkinter as tk

root = tk.Tk()
root.title('RooT')
pixelVirtual = tk.PhotoImage(width=1, height=1)
rose = tk.PhotoImage(file='../files/download.png')
fr = tk.Frame(root)
fr.pack()
butt = tk.Label(fr, image=rose)
butt.pack()

root.mainloop()
