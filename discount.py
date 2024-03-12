total_unit = int(input("enter quantity of purchased unit : "))
total_cost1 = total_unit*100
if total_cost1 > 1000:
    discount = total_cost1*0.1
    total_cost = total_cost1-discount
    print("Total cost : %s" %total_cost)
else:
    print("Total cost : %d"%total_cost1)