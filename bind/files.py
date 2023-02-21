from tkinter import *

root = Tk()

ent = Entry(root, width=20)
but = Button(root, text="Open")
tex = Text(root, width=80, height=30, font="Courier12", wrap=WORD)


def output(event):
    s = ent.get()

    try:
        txt = open(s, "r", encoding='utf-8')
        content = txt.read()
        tex.delete(1.0, END)
        tex.insert(END, content)
    except:
        tex.delete(1.0, END)
        tex.insert(END, "File not exists")


ent.grid(row=0, column=0)
but.grid(row=2, column=0)
tex.grid(row=1, column=2)

but.bind("<Button-1>", output)

root.mainloop()
