a=[]
n=int(input("Enter the n terms :"))
for i in range (1,n+1):
    a.append(i)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)
