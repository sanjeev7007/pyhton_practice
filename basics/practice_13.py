a = int(input("enter number a :"))
b = int(input("enter number b :"))
cal = input("say add/sub/mul/div :")
if(cal=="add"):
    print("Addition of numbers",a+b)
elif(cal=="sub"):
    print("Subtraction of numbers",a-b)
elif(cal=="mul"):
    print("multiply of two numbers",a*b)
elif(cal=="div"):
    print("division of two numbers",a/b)
else:
    print("invalid")
