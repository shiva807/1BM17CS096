def divisors(n):
    lis=[]
    for i in range(1, n+1):
       if n%i==0:
          lis.append(i)
    return lis
     
     
l2=[]
     
n=int(input("Enter a number"))
print("The list of divisors are:")
l2=divisors(n)
print(l2)
