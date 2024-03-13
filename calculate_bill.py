unit = int(input("Enter number of electricity Unit :"))
if unit <= 100:
    text_massege = "First 100 Unit is Free"
    total_bill = unit * 0
elif unit <= 200:
    text_massege = "After 100 unit price is 5 tk per Unit"
    total_bill = (unit -100 )* 5
elif unit > 200:
    text_massege = "After 200 unit price is 10 tk per Unit"
    total_bill = (unit - 100 )* 10
else:
    print("Type only number")
    
print(text_massege)
print( "Your Electricity bill is :", total_bill , "Taka")