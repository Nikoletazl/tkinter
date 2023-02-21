from tkinter import *

root = Tk()

tx = Text(font=('times', 12), width=50, height=15, wrap=WORD)
tx.pack(expand=YES, fill=BOTH)
tx.insert(1.0, 'Line 1\nLine 2\nLine 3\n')

tx.tag_add('title', '1.0', '1.end')
tx.tag_add('special', '6.0', '8.end')
tx.tag_add('special', '3.0', '3.11')

tx.tag_config('title', foreground='red', font=('Arial', 14, 'underline'), justify=CENTER)
tx.tag_config('special', background='grey85', font=('times', 10, 'bold'))


def erase():
    tx.delete('1.0', END)


def smiley(event):
    cv = Canvas(height=30, width=30)
    cv.create_oval(1, 1, 29, 29, fill="yellow")
    cv.create_oval(9, 10, 12, 12)
    cv.create_oval(19, 10, 22, 12)
    cv.create_polygon(9, 20, 15, 24, 22, 20)
    tx.window_create(CURRENT, window=cv)

tx.bind('<Button-1>', smiley)

bt = Button(tx, text='Clear', command=erase)
tx.window_create(END, window=bt)

root.mainloop()