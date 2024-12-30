#Тоон дарааллын элементүүдын хамгийн бага элементийг ол.
print(min(int(i) for i in input().split()))

#Traditional way without using min function
list1= input().split()
minimum = int(list1[0])
for i in list1 :
    if int(minimum) > int(i) :
        minimum = i
print(minimum)