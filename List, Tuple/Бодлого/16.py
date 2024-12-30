# Нэрсийн дарааллаас хамгийн урт нэртэй хүмүүсийг ол.
name_list = input().split()
maximum_list = []
maximum_digit = len(name_list[0])
for name in name_list :
    if maximum_digit < len(name) :
        maximum_digit = len(name)
for name in name_list :
    if len(name) ==maximum_digit :
        maximum_list.append(name)
print(maximum_list)
    