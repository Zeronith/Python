a = int(input())
b = int(input())

if a > b : 
    print(f"{a} is greater than {b}") # Again using f-string 
elif b > a :
    print(f"{b} is greater than {a}")
else :
    print(f"{a} and {b} are equal to each other")