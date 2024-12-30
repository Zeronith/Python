#Нэрсийн дарааллаас хамгийн богино нэртэй хүмүүсийн тоог ол.
name_list = input().split()
minimum_digit = len(name_list[0])
counter = 0
for name in name_list :
    if minimum_digit == len(name) :
        counter+=1
    elif len(name) < minimum_digit :
        minimum_digit = len(name)
        counter=0
print(minimum_digit)