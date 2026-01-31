mark1 =int(input("mark 1 : "))
mark2=int(input("mark 2 : "))
mark3=int(input("mark 3 : "))
mark4=int(input("mark 4 : "))
total = mark1+mark2+mark3+mark4
average=total/4

if(average<=35):
    print("Additional class required")
else:
    print("you are good to go")
