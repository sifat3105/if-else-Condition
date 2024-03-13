held = int(input("Enter Number of classes held : "))
attend = int(input("Enter Number of classes attended : "))
attend_per =round(attend/held*100)
print("Percentage of class attended :",attend_per)
if attend_per >=75:
    print("The Student is allowed to sit in exam")
else:
    print("The Student is not allowed to sit in exam")