import tkinter as tk

root = tk.Tk()
img = tk.PhotoImage(file="Documents-icon.png")
## Labels and pack

## create window
root.geometry("250x400")
root.iconbitmap(bitmap=img)
root.title("App")
root.resizable(0, 0)
root.config(bg="blue")