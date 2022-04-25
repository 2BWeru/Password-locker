start= input(f''"Hello there, welcome to Password locker")

input(f''"please Input your user name and password to log in:")


# password locker details
username_main = "Susans"
password_main = "234567"

# Validation
login = input("Username :")


if (login == username_main):
    password_login = input("Password :")
    if (password_login == password_main):
       print("Welcom back",username_main)
    else:
       print("Invalid password, Try again")
else:
    print("Invalid username")
# print(login)
