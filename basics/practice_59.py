n=int(input())
rev=0
while n>0 :
    num=n%10
    rev=rev*num+num
    n=n//10
    print(rev)
