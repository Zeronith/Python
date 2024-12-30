#Өгөгдсөн тоон дарааллыг буурахаар эрэмбэл.
list1=input().split()
list1.sort() # Өсөхөөр эрэмбэлсэн
list1.reverse()  # Урвуу болгохоор буурахаар хэвлэчихэж байгаа юм 
print(list1)


# What a heck is this ?
print(sorted(input().split(), key=int , reverse = True))

#Traditional way
list1 = input().split()
temp = None
for i in range(len(list1)) :
    for j in range (len(list1)) :
        if int(list1[i]) > int(list1[j]) :
            temp = list1[i]
            list1[i]= list1[j]
            list1[j]=temp
            print(list1)