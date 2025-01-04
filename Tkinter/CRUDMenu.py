from tkinter import * 
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

data =  [
    {
        "owog":"Bat",
        "ner":"Bold",
        "nas": 26,
        "huis": "er",
        "utas": "99562312"
    },
    {
        "owog":"Bat",
        "ner":"Bold",
        "nas": 26,
        "huis": "er",
        "utas": "99562312"
    },
    {
        "owog":"Bat",
        "ner":"Bold",
        "nas": 26,
        "huis": "er",
        "utas": "99562312"
    }
]

root = Tk()
root.title("Python : Simple CRUD application UI")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 565
height = 400
x = (screen_width/2)-(width/2)
y = (screen_height/2)-(height/2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0,0)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0,weight=1)

# Frames
top_frame = Frame(root, bg="white", width=450, height=30, pady=3).grid(row=0, sticky="ew")
center = Frame (root, bg = "gray" , width=50, height=40, padx=3, pady=3).grid(row =1 , sticky="nsew")


def menu_clicked() :
    print("Menu daragdsan")

menubar = Menu(root)
menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu=menu)
menu.add_command(label="Create" , command=menu_clicked)
menu.add_command(label="Read", command=menu_clicked)
menu.add_command(label="Update", command = menu_clicked)
menu.add_command(label="Delete", command=menu_clicked)
menu.add_separator()
exit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Exit",menu =exit_menu)
exit_menu.add_command(label="Are U Sure ?", command=tkMessageBox.askyesno("Geniune Question", "Are u really sure about that"))
root.config(menu=menubar) # Displaying Menu

root.mainloop()
