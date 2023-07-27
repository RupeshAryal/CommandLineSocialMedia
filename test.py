user_database = {
    'rupesh': {
        'phonenumber': 98234982,
        'password': "rupesh123"
    }, 'kushal': {
        'phonenumber': 98234982,
        'password': "kushal123"
    }, 'bijesh': {
        'phonenumber': 98234982,
        'password': "bijesh123"
    },
}

print(user_database['rupesh'])

print(user_database)
logged_in = False

program_running = True

print(user_database)


def sign_in():
    username = input("enter your username")
    password = input("enter your password")

    if username in user_database and user_database[username]['password'] == password:
        logged_in = True
        display_function(logged_in)
        user_input = int(input("please provide your response"))
        match user_input:
            case 1:
                reset_password(username)
            case 2:
                sign_out()

    return




def register():
    username = input("provide your username")
    password = input("provide your password")
    phone_number = input("provide your phone number")
    return

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

    return


def sign_out():
    logged_in = False
    main_function()
    return


def reset_password(username):
    phone  = int(input("enter your phone number"))
    if phone == user_database[username]['phonenumber']:
        password = input("enter your new password")
        user_database[username]['password'] = password
        print(user_database)
    else:
        print("password didn't match, terminating the process")








main_function()
