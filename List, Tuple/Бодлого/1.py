#1. Тоон дарааллын элементүүдын нийлбэрийг ол.
print(sum(int(x) for x in input().split()))


# Traditional without sum function 
niilber=0
list1 = input().split()
for i in list1 :
    niilber+=int(i)
print(niilber)