import re
# use case 1
def firstname(first_name):
    name_len=len(first_name)
    if name_len<3:
        print("Invalid name")
    elif re.match(r'^[A-Z][a-zA-Z]*$', first_name):
        print("valid name")
    else:
        print("Invalid name")

first_name = str(input("Enter your First name "))
firstname(first_name)




def lastname(last_name):
    name_len=len(last_name)
    if name_len<3:
        print("Invalid name")
    elif re.match(r'^[A-Z][a-zA-Z]*$', last_name):
        print("valid name")
    else:
        print("Invalid name")

last_name = str(input("Enter your last name: "))
lastname(last_name)


