from tkinter import *


def hello(event):
    print("Hello World!")


root = Tk()
root.title("My Title")
root.geometry("300x250")
btn = Button(root)
btn["text"] = "Hello"
btn.bind("<Button-1>", hello)

btn.pack()
root.mainloop()
