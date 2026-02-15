a=list(map(int,input().split()))
odd=0
even=0
for i in a:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("Even : ", even)
print("Odd : ", odd)






























