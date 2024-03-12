num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
oper = input("Enter operator : ")

oper1 = num1+num2
oper2 = num1-num2
oper3 = num1*num2
oper4 = num1/num2

if oper == "+":
    print("a+b=%s"% oper1)
elif oper == "-":
    print("a-b=%s"% oper2)
elif oper == "*":
    print("a*b=%s"% oper3)
elif oper == "/":
    print("a/b=%s"% oper4)

else:
    print("Invalid operator entered")