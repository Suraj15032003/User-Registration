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



import re

def is_valid_password(password):
    if len(password) < 8:
        return False

password = input("Enter your password: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid because the length of the password is less then 8")#adding the comment why it user get invalid output


import re

def is_valid_password(password):
    if not (re.search(r'[A-Z]', password) and re.search(r'[a-z]', password)):
        return False
    return True

password = input("Enter your password: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid beacuse it did't contain uppercase ya lowercase letter so use it .")


