from tkinter import *
top = Tk()

mb = Menubutton(top, text="condiments", relief=SOLID)
# Relief defines outline of button
mb.grid()
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)
mb.pack()
top.mainloop()