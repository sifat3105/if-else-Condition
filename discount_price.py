price = int(input("Enter the marketed price : "))
if price <= 7000:
    discount = round(price * 0.1)
elif price > 7000 and price < 10000:
    discount = round(price * 0.15)
else:
    discount = round(price * 0.20)
    
net_price = price - discount
print("Amount :",price)
print("Discount :",discount)
print("Net Amount :",net_price)