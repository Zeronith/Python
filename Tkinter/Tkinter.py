''' 
Tkinter нь энгийн график интерфайстэй програмыг зохион байгуулах боломжтой болгодог .
Tkinter сан нь цонхны элементүүдийг байрлуулан тэдгээрийг Tkinter үндсэн давталтад оруулдаг .
Ингэснээр программ нь үзэгдэл (Event)-ээр жолоодогддог болох ба хэрэглэгч 
цонхны элементүүдтэй харилцахад үзэгдэл үүсдэг . Үзэгдэл боловсруулахад зориулсан функцуудын тусламжтай ажилладаг .
'''


# There is 2 way to import library 
# import tkinter  -> We need to use prefix . EX : window = tkinter.Tk()
# from tkinter import * -> We dont need to use that . EX : window = Tk()



# Creating window using Tkinter

from tkinter import * 

window = Tk()
window.title("Title")
window.geometry("290x392")
window.resizable(0,0)

window.mainloop()