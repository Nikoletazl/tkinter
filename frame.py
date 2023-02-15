from tkinter import *

root = Tk()

fra1 = Frame(root, width=500, height=100, bg="darkred")
fra2 = Frame(root, width=300, height=200, bg="green", bd=20)
fra3 = Frame(root, width=500, height=150, bg="darkblue")

# ent1 = Entry(fra2, width=20)
#
# ent1.pack()
fra1.pack()
fra2.pack()
fra3.pack()

root.mainloop()
