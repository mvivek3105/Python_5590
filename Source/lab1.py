import re
password = input("type the password that has 6 to 12 characters")
if len(password) >= 6 and len(password) <= 12 and re.search("[$#@!]",password) and re.search("[A-Z]",password) and re.search("[a-z]",password) and re.search("[0-9]",password):
    print("password is valid")
else:
    print("password is not valid")




