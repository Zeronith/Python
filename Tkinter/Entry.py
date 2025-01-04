# Entry - Бичвэр оруулах хэсэг 
from tkinter import * 
window = Tk()
window.title("Main Window")
window.geometry("500x500")
window.resizable(True, True)

result_string = StringVar()


def hello() :
    print(result_string.get())
    result_string.set('')


L1 = Label(window,text = "UserName")
L1.pack(side=LEFT)
E1 = Entry(window, bd=5, textvariable=result_string)
E1.pack(side=RIGHT)

B = Button(window , text = "Help", command=hello)
B.pack()



window.mainloop()