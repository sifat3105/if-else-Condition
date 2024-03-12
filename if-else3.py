marks = int(input("Enter the marks : "))
if marks < 25:
    print("The Grade is 'F'")
elif marks <= 45:
    print("The Grade is 'E'")
elif marks <= 50:
    print("The Grade is 'D'")
elif marks <= 60:
    print("The Grade is 'C'")
elif  marks <= 80:
    print("The Grade is 'B'")
elif marks > 80:
    print("The Grade is 'A'")