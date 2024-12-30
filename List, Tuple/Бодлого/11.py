#Тоон дарааллаас хамгийн бага элементийг устга.
numbers = input().split()
minimum = numbers[0]
for number in numbers :
    if minimum > number :
        minimum = number 
numbers.remove(minimum)
print(numbers)