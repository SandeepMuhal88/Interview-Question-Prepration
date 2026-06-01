# import math 
# c=50
# h=30
# value = []
# items=[x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print(','.join(value))




print("The Login Page of the Website:- ")
username = input("Enter the username: ")
password = input("Enter the password: ")

username_list=[]

password_list=[]

if username is not username_list and password is not password_list:
    print("Login failed! Register first to login.")
    if input("Do you want to register? (yes/no): ").lower() == "yes":
        new_username = input("Enter a new username: ")
        new_password = input("Enter a new password: ")
        username_list.append(new_username)
        password_list.append(new_password)
        print("Registration successful! You can now log in.")

if username and password:
    username_list.append(username)
    password_list.append(password)
    print("Login successful!")
else:
    print("Login failed! Please enter both username and password.") 

