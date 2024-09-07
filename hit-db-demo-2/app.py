import sys
from database import DBhelper
class Flipkart:
    def __init__(self):
        # connect to the database
        self.db = DBhelper()
        self.menu()

    def menu(self):

        user_input = input("""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to leave
        """)

        if user_input == '1':
            self.register()
        elif user_input == '2':
            self.login()
        else:
            sys.exit(1000)

    def login_menu(self):
        input(""" 
1. Enter 1 to view profile
2. Enter 2 to view profile
3. Enter 3 to delete profie
4. Enter 4 to logout

""")

    def register(self):
        name = input("enter the name: ")
        email = input("enter the Email: ")
        password = input("enter the password: ")


        response = self.db.register(name, email, password)

        if response == 1:
            print("user created")
        else:
            print("user not created")
        self.menu()
    def login(self):
        email = input("enter the Email: ")
        password = input("enter the password: ")

        data = self.db.search(email, password)

        if len(data) == 0:
            print("incorrect email/password")
        else:
            print("Hello ", data[0][1])

obj = Flipkart()
