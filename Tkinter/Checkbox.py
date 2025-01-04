from tkinter import * 
window = Tk()
window.title("Main Window")
window.geometry("500x500")
window.resizable(True,True)
def comment() :
    print("printing comment ")



B = Checkbutton(window, text="Video", variable=IntVar, onvalue=1, offvalue=0, height=5, width=20, command=comment, justify=LEFT)
B.pack() 

window.mainloop()