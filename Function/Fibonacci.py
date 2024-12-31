def FibonacciByPeace(n) :
    if n==0 :
        return 0
    elif n==1 :
        return 1
    else :
        return FibonacciByPeace(n-1) + FibonacciByPeace(n-2)
    
print(FibonacciByPeace(int(input())))

# def FibonacciByEnguunee(n) :
