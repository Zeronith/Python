# find sum of n digit number 
'''
# First Version
n = input()
i=0
sum = 0
while(i<len(n)) :
    sum+=int(n[i])
    i+=1
print(sum)
'''
# Second Version , Which is my best version 

n = input()
print(sum(int(n[i]) for i in range(0,len(n)))) 

# Then the actual best version comes from Taivnaa ah 

print(sum(int(i) for i in str(input("n: "))))

# Comment from Enguunbayar : Looks smooth and easy to understand , simple compared to mine . fuck