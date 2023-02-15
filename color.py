from tkinter import *


def colorR():
    fra.config(bg="Red")


def colorG():
    fra.config(bg="Green")


def colorB():
    fra.config(bg="Blue")


def square():
    fra.config(width=640)
    fra.config(height=480)


def rectangle():
    fra.config(width=800)
    fra.config(height=600)


root = Tk()
fra = Frame(root, width=300, height=100, bg="Black")
fra.pack()

m = Menu(root)
root.config(menu=m)

cm = Menu(m)

m.add_cascade(label="Color", menu=cm)
cm.add_command(label="Red", command=colorR)
cm.add_command(label="Green", command=colorG)
cm.add_command(label="Blue", command=colorB)

root.mainloop()



