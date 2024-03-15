total_bill = 16000
total_set = 32
age1 = 13
age1_total = 2
age2 = 16
age2_total = 3
age3 = 18
age3_total = 8

par_set = 16000/32
if age1 <= 13:
    age13_fair = par_set * 0.80
if age2 <= 16:
    age16_fair = par_set * 0.90

print("under 13:",age13_fair)
print("under 16:",age16_fair)
# print(age18_fair)

age1_cost = age13_fair * age1_total
age2_cost = age16_fair * age2_total

total_cost = age1_cost + age2_cost #+ age3_cost
# print(total_cost)
total_bill = total_bill - total_cost
total_set = total_set - (age1_total+age2_total)
per_set_new = total_bill/total_set

if age3 >= 18:
    age18_fair = (per_set_new)
    
age3_cost = age18_fair * age3_total
total_set_price = age1_cost + age2_cost + age3_cost
print("uper 18:",age18_fair)
print("total filled set cost:",total_set_price)
print("total empty set cost:",total_bill-total_set_price)

