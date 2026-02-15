a=list(map(int,input().split()))
largest=a[0]
smallest=a[0]
for i in a:
    if i>largest:
        largest = i
    if i < smallest:
        smallest = i
print(largest)
print(smallest)
