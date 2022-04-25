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
       print("Welcom back",username_main, "You have successfully logged in")
    else:
       print("Invalid password, Try again")
else:
    print("Invalid Username,")

    # lets create User Class

class User:
   """
   Class that generates new instancse of passwords and usernames
   """
def _init_(self,user_name,pass_word,app_name):
    self.user_name = user_name
    self.pass_word = pass_word
    self.app_name = app_name

user_list= [
    {
        "username":"Mitch2",
        "password":"23Mitch",
        "appname":"Twitter"
    },

     {
        "username":"Mitch678",
        "password":"678Mitch",
        "appname":"Chrome"
    },

     {
        "username":"Mitch20",
        "password":"2389M",
        "appname":"Snapchat"
    },
     {
        "username":"Mitch",
        "password":"2388Mitch",
        "appname":"Netflix"
    },
     {
        "username":"Mitchell21",
        "password":"44000",
        "appname":"Spotify"
    },
     {
        "username":"Mitch12",
        "password":"12789",
        "appname":"HackerRank"
    },
     {
        "username":"Mitchell29",
        "password":"29666",
        "appname":"TikTok"
    },
]

