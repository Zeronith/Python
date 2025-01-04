from tkinter import * 
root = Tk()
root.geometry("500x500")
root.resizable(True, True)
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill=Y) # Assigning position and fill coordination for scrollbar

mylist=Listbox(root, yscrollcommand=scrollbar.set) 
for line in range(100) :
    mylist.insert(END,"This is line number" +str(line) )
mylist.pack(side=LEFT, fill=Y) 
scrollbar.config(command=mylist.yview) # Linking scrollbar to list
root.mainloop()
