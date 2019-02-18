#Please use python3 to check the code

import re
n=int(input())
for i in range(n):
    cardnumbers = input()
    check1 = re.search(r"^[456]",cardnumbers) #Validate whether value starts with 4,5,6
    check2 = re.match(r"(-?\d{4}){4}$",cardnumbers) #Validate that value has only digits, seperated by -
    check3 = re.search(r"(.)(-?\1){3,}",cardnumbers) #validate consecutive numbers
    if ( check1 and check2  and not check3):
        print("Valid")
    else:
        print("Invalid")
