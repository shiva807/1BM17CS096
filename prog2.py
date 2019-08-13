

def fib(n):
 if n<=1:
   return n
 else:
   return fib(n-1)+fib(n-2)

nterms=int(input("Enter the count of fibonacci numbers: "))
for i in range(nterms):
 print(fib(i))
 
 
