n=int(input("Enter the number : "))
rev=0
for i in range(len(str(n))):
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)
