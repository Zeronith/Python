numbers = input().split()
for number in numbers:
    if int(number) < 0 :
        numbers[numbers.index(number)]='0'
print(numbers)