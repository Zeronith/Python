from tkinter import *
import tkinter 
top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(1, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4,"JSP")
Lb1.insert(5, "Lebron")
Lb1.pack()
top.mainloop()