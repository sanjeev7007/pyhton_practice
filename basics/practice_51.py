n=int(input())
largest=0
for i in range(len(str(n))):
    digit=n%10
    if digit>largest:
        largest=digit
    n//=10
print("Largest number : ",largest)
