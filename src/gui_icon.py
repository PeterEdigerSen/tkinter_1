import tkinter as tk

root = tk.Tk()
img = tk.PhotoImage(file="../files/rose_1.png")
## Labels and pack

## create window
root.geometry("250x400")
root.iconbitmap("../files/download.png")
root.title("App")
root.resizable(0, 0)
root.config(bg="blue")
root.mainloop()