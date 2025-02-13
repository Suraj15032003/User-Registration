import re
<<<<<<< HEAD

def lastname(Last_name):
    name_len=len(last_name)
=======
# use case 1
def firstname(first_name):
    name_len=len(first_name)
>>>>>>> user_case_valid_firstname
    if name_len<3:
        print("Invalid name")
    elif re.match(r'^[A-Z][a-zA-Z]*$', last_name):
        print("Valid Lastname")
    else:
        print("Invalid Lastname")

last_name = str(input("Enter your Lastname : "))
lastname(last_name)