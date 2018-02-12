contact_list = [{"name":'vivek', "number":9989743445, "email":"mvivek@gmail.com"},{"name":"saidu", "number":7634678057, "email":"sai@gmail.com"},{"name":"mike","number":8700009826,"email":"mike@gmail.com"}]

# Asking input from user to enter name to get contact
nm = input("Enter name to get contact: ")

# Iterating over contact_list
for i in contact_list:
# if condition for checking the name entered by the user is in the dictionary or not
    if nm in i.values():
# if true printing the contact
        print(i)

# Asking input from the user to enter number to get contact
num = int(input("Enter number to get contact: "))
# Iterating over contact_list
for j in contact_list:
# If condition for checking whether the entered number is in dictinary or not
    if num in j.values():
# Prnting the contact if condition is true
        print(j)

# Asking user to enter the name
nmer = input("Enter name to get contact and edit number: ")
# Iterating over the contact_list
for aa in contact_list:
# If the entered name in dictionary
    if nmer in aa.values():
# Prnting the contact
        print(aa)
# Asking user if he want to edit the number
        newnum = int(input("Enter number to edit: "))
# Editing the nimber for the particular user
        aa["number"] = newnum
        print(aa)