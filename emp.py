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


import re

def check_email(email):
  regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  if re.match(regex, email):
    print(f"{email} is a Valid Email Address.")
  else:
    print(f"{email} is an Invalid Email Address.")


email = input("Enter an email address: ")
is_valid = check_email(email)

import re

def valid_mobileno(number):
    pattern = r"^91\s\d{10}$" 
    return bool(re.match(pattern, number)) 

mob_numb = input("Enter your mobile number: ")
valid_num = valid_mobileno(mob_numb)

if valid_num:  
    print("Your mobile number is valid:", mob_numb)
else:
    print("Invalid mobile number. Please enter again.")
    mob_numb = input("Enter your mobile number: ")


