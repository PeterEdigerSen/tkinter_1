import tkinter as tk

root2 = tk.Tk()
img = tk.PhotoImage(file="../files/app_icon.ico")

# create window
root2.geometry("250x400+800+500")
#root2.tk.call('wm', 'iconphoto', root2._w, tk.PhotoImage(file="../files/download.png"))
root2.iconphoto(False,tk.PhotoImage(file="../files/app_icon.ico"))
#root2.iconbitmap("../files/app_icon.ico")
root2.title("App 2")
root2.resizable(0, 0)
root2.config(bg="blue")

root2.mainloop()
