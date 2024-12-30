# Find all prime number in between n to m 
n=int(input())
m=int(input())
c=0 # counter
for i in range(n, m):
    for j in range(2 , i//2+1) :
        if i%j==0 :
            c+=1
    if c==0 :
        print(i)
    c=0