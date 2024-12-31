# Finding factorial using for loop
def factorial(number) :
    result = 1 
    for num in range (1, number+1) :
        result *=num
    return result

print(factorial(int(input())))

# Finding factorial using recursive 
def Rfactorial (number) :
    if number==1:
        return 1 
    return number * Rfactorial(number-1)

print(Rfactorial(int(input())))


# Finding sum of first n number using recursive 
def sum (n) :
    if n == 0 :
        return 0 
    return n+sum(n-1)

print(sum(int(input())))


# m power of n number
def powerup(n, m) :
    if m == 0 :
        return 1
    else :
        return n*powerup(n, m-1)
    
print(powerup(2,5))

# Reversing string using recursive function 
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
print(reverse_string("Enguunbayar"))