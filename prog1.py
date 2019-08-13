lst= []
n= int(input("Enter the size of list: "))
for _ in range(0,n):
 x=int(input())
 lst.append(x)

new=[]
for i in lst :
  if i%2==0:
     new.append(i)
print("New list:")
print(new)



