age_a = int(input("Enter 1st people age : "))
age_b = int(input("Enter 2nd people age : "))
age_c = int(input("Enter 3rd people age : "))
if age_a > age_b and age_a > age_c:
    oldest = age_a
elif age_b > age_a and age_b > age_c:
    oldest = age_b
else:
    oldest = age_c
    
if age_a < age_b and age_a < age_c:
    youngest = age_a
elif age_b < age_a and age_b < age_c:
    youngest = age_b
else:
    youngest = age_c
    
print("oldest person age's :", oldest)
print("youngest person age's :", youngest)