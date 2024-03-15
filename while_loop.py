startin = input("Enter starting number :",)
endin = input("Enter ending number :",)
oparetor = input("Which number you need 'even' or 'odd' :")

try:
    start = int(startin)
    end = int(endin)
    if start >= end:
        print("Starting number should be less than the ending number.")
    else:
        if oparetor == "even":
            while start < end:
                if start % 2 == 0:
                    print(start)
            start += 1
        elif oparetor == "odd":
                while start < end:
                    if start % 2 != 0:
                        print(start)
                start += 1
        else:
            print("Please enter either 'even' or 'odd' for the operator.")
except ValueError:
    print("Please enter valid integers for the starting and ending numbers.")
