# w = Button (master, option = value , .....)
# master -> Эцэг цонх
# Option -> Тохиргоо болон утгуудын өгнө


from tkinter import *
window = Tk()
window.title("Main window")  # Set the window title to "Main window"
window.geometry("290x392")   # Set the initial window size to 290px in width and 392px in height
window.resizable(1000, 1000)  # Allow resizing the window, with the maximum size being 1000px by 1000px


def helloB() :
    print("Hello everyone, i am B")

def helloC() :
    print("Hello everyone, i am C")

def helloD() :
    print("Hello everyone, i am D")
B = Button(window, text = "Tap one me. I am B", command=helloB)
B.pack()
C = Button(window, text = "Tap one me. I am C", activebackground="red", command= helloC, state=DISABLED) # Using state=Disabled to disable functionality of buttons
C.pack()
D = Button(window, text = "Tap one me. I am D", activeforeground="red", command= helloD)
D.pack()
E = Button(window, text= "This is E and bd ", bd=5)
E.pack()
F = Button(window, text = "This is F and bg ", bg="red")
F.pack()
G = Button(window, text = "This is G button and fg", fg= "red")
G.pack()
H = Button(window, text = "This is H button and heigh", height=10)
H.pack()
I = Button(window, text = "This is I button and highlightcolor", highlightcolor="red")
I.pack()
photo = PhotoImage(file="C:\\Users\\Dell\\Downloads\\Desktop\\Isagi Yoichi wallpaper.png")
image = Button(window, text = "Darah um bol goy zurag garj irne" , image=photo, height=100, width=100, justify=CENTER)
image.pack()
window.mainloop()