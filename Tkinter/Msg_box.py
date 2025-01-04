import tkinter.messagebox as tkMessageBox
import tkinter

top = tkinter.Tk()

def hello():
    tkMessageBox.showinfo("Say Hello", "Hello World")
    # Say Hello is msgBox's title 
    # Hello World is content of msgBox
B1 = tkinter.Button(top, text ="Say Hello", command=hello)
B1.pack()
top.mainloop()
