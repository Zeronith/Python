#2. Тоон дарааллын элементүүдын хамгийн их элементийг ол.
print(max(int(x) for x in input().split()))

#Traditional without max function
list1=input().split()
maximum = 0
for i in list1 :
    if int(i)>int(maximum) :
        maximum=i
print(maximum)