count_odd=0
count_even=0
for i in range(1,11):
    if(i%2==0):
        count_even=count_even+1
    if(i%2!=0):
        count_odd=count_odd+1
print("even : ",count_even)
print("odd : ",count_odd)
