import tkinter
from tkinter import messagebox

# Hide main window
root = tkinter.Tk()
root.withdraw()


# message box display
messagebox.showerror("Error","Something is wrong")
messagebox.showinfo("Info", "Showing Info Chill2")
messagebox.showwarning("Warning", "I have warned you ")


answer = messagebox.askokcancel("Question", "Do you want to open ?") # Returns True or False
answer = messagebox.askretrycancel("Question", "Are u okey ?")
answer = messagebox.askyesno("Question", "Do u have girlfriend ?")
answer = messagebox.askyesnocancel("Question", "Do u want to live forever ?")