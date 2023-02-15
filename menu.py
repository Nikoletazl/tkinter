from tkinter import *

root = Tk()

m = Menu(root)
root.config(menu=m)
fm = Menu(m)

m.add_cascade(label="File", menu=fm)

fm.add_command(label="Open..")
fm.add_command(label="Save..")


hm = Menu(m)
m.add_cascade(label="?", menu=hm)
hm.add_command(label="Help")


def new_win():
    win = Toplevel(root)


def close_win():
    root.destroy()


def about():
    win = Toplevel(root)
    lab = Label(win, text="My Program")
    lab.pack()


fm.add_command(label="New", command=new_win)
fm.add_command(label="Exit", command=close_win)
hm.add_command(label="About", command=about)

root.mainloop()