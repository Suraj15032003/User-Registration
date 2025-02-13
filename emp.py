import re

# use case 1
def firstname(first_name):
    name_len=len(first_name)
    if name_len<3:
        print("Invalid name")
    elif re.match(r'^[A-Z][a-zA-Z]*$', first_name):
        print("Valid firsttname")
    else:
        print("Invalid Lastname")

first_name = str(input("Enter your firsttname : "))
firstname(first_name)