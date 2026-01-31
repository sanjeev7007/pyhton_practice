salary = int(input("Enter your salary : "))
age = int(input("Enter your age : "))
if(salary>=20000 or age<=25):
    loan=int(input("Enter required loan amount : "))
    if(loan<=50000):
        print("you are eligible for loan")
    else:
        print("maximum loan amount is 50000")
    
else:
    print("you are not eligible")
