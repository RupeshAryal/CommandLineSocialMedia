class App():
    def __init__(self):
        self.user_database = {}
        self.logged_in = False

    def sign_in(self):
        username = input("enter your username")
        password = input("enter your password")

        if username in self.user_database and self.user_database[username]['password'] == password:
            logged_in = True
            display_function(logged_in)
            user_input = int(input("please provide your response"))
            match user_input:
                case 1:
                    reset_password(username)
                case 2:
                    sign_out()

    def display_function(logged_in):
        if logged_in:
            print("logged in successful \n")
            print("press 1 to reset password\n"
                  "press 2 to signout")

        else:

            print("Welcome to my brilliant website \n"
                  "press 1 to signin \n"
                  "press 2 to register to our website \n"
                  "press 3 to terminate")

    def sign_out():
        logged_in = False
        main_function()
        return

    def reset_password(username):
        phone = int(input("enter your phone number"))
        if phone == self.user_database[username]['phonenumber']:
            password = input("enter your new password")
            user_database[username]['password'] = password
            print(user_database)
        else:
            print("password didn't match, terminating the process")

    def main_function(self):
        valid_input = False
        self.display_function(self.logged_in)
        user_input = int(input("Please provide your response"))
        if user_input == 1 or user_input == 2 or user_input == 3:
            valid_input = True
        else:
            print('not a valid input, terminating')
        while True:
            if valid_input:
                match user_input:
                    case 1:
                        self.sign_in()
                    case 2:
                        self.register()
                    case 3:
                        break
        return