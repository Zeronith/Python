#Тоон дарааллын хамгийн их болон багын байрыг соль.
numbers = input().split()
maximum = numbers[0]
minimum = numbers[0]
for number in numbers :
    if int(maximum) < int(number) :
        maximum = number
    if int(minimum) > int(number) :
        minimum = number 
max_ind = numbers.index(maximum)
min_ind = numbers.index(minimum)
temp = numbers[max_ind]
numbers[max_ind]= numbers[min_ind]
numbers[min_ind]=temp
print(numbers)

    