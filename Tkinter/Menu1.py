from tkinter import * 

def donithing() :
    filewin = Toplevel(root) # Creates child window
    button = Button(filewin, text = "Do nothing button")
    button.pack()

root= Tk() # Making root as main window
menubar = Menu(root)  # Creating a menu bar for File , Edit , Help etc
filemenu = Menu(menubar, tearoff=0) # Creating menu bar for File's sub option
menubar.add_cascade(label="File", menu=filemenu) # Making File menu is cascadable 
filemenu.add_command(label="New", command=donithing) # Adding option for file menu
filemenu.add_command(label="Open", command=donithing)
filemenu.add_command(label="Save", command=donithing)
filemenu.add_command(label="Save As", command=donithing)
filemenu.add_command(label="Close", command=donithing)
filemenu.add_separator() # Adding separate line for Exit 
filemenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(menubar, tearoff=0) 
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo" , command=donithing)
editmenu.add_command(label="Cut", command=donithing)
editmenu.add_command(label="Copy", command=donithing)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="FAQ", command=donithing)
helpmenu.add_command(label="User Manual", command=donithing)









root.mainloop()
