#Нэрсийн бүртгэл өгөгдсөн бол нэрэнд нь 2-аас олон а үсэг орсон хүмүүсийг ол
list_name = input().split()
for name in list_name :
    if (name.count("a")>2) :
        print(name)