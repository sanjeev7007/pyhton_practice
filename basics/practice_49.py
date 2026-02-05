n=int(input())
rev = 0
for i in range(len(str(n))):
    rev=rev*10+n%10
    n//=10
if n==rev:
    print("Palindrome")
else:
    print("Not a palindrome")
