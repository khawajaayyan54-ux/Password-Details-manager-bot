def load_config():
    config = {}
    try:
        with open("config.text") as f:
            for line in f:
                if "=" in line:
                    key, val = line.strip().split("=", 1)  # split only at first '='
                    config[key] = val
    except FileNotFoundError:
        print("config.text file not found. Using empty config.")
    return config

config = load_config()


def code():
    user = input("Enter ur command:  ")
    password_bypass = ["hello", "who are u"]

    if user.lower() in password_bypass:
        # bypass password
        password = 3009
    else:
        try:
            password = int(input("Enter password first: "))
        except ValueError:
            print("Password must be numbers only.")
            return

    if password == 3009:
        if user.lower() == "hello":
            print("hello, i am digital Ai password manager")

        elif user.lower() == "who are u":
            print("i am digital Ai password manager")

        elif user.lower() == "user name":
            print(config.get("user_name", "No user name found"))

        elif user.lower() == "user id":
            print(config.get("user_email", "No email found"))

        elif user.lower() == "user password":
            print(config.get("user_password", "No password found"))

        elif user.lower() == "user recent project":
            print("Ai making")

        elif user.lower() == "user insta id":
            print("xyz id")

        else:
            print("sorry code cant continue due to unexpected error")
    else:
        print("wrong password")
code()

def help_menu():
    print("these are the keys that can continue without error:") 
    print("hello") 
    print("user insta id") 
    print("user recent project") 
    print("user password") 
    print("user id") 
    print("user name") 
    print("who are u") 
    print("for exiting help menu these are the keys:") 
    print("yes to start again") 
    print("no to stop") 
    print("type help if u get any error")


while True:
    a = input("u want to continue? ")
    if a.lower() == "yes":
        code()

    elif a.lower() == "help":
        help_menu()

    elif a.lower() == "no":
        print("exiting program")
        break

    else:
        print("error, use help")
