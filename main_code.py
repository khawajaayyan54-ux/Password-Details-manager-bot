import json
import os
import hashlib

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()


def load_commands(filename="commands.txt"):
    try:
        with open(filename) as f:
            return [line.strip().lower() for line in f if line.strip()]
    except:
        print("Error file doesnt found, please create file first")
        return []
    
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

def say_hello():
    print("hello, i am digital Ai password manager")

def who_are_you():
    print("i am digital Ai password manager")

def show_user_name():
    print(config.get("user_name", "No user name found"))

def show_user_id():
    print(config.get("user_email", "No email found"))

def show_user_password():
    print(config.get("user_password", "No password found"))

def show_recent_project():
    print("Ai making")

def show_insta_id():
    print("xyz id")

command_action = {
    "hello" : say_hello,
"who are u" : who_are_you,
"user name" : show_user_name,
"user id" : show_user_id,
"user password" : show_user_password,
"user recent project" : show_recent_project,
"user insta id" : show_insta_id,
}

commands = load_commands()
config = load_config()

def password():
    plain_password = "3009"
    password_value = hash_password(plain_password)
    password_bypass = ["hello", "who are u"]
    return password_value, password_bypass

def help_menu():
    print()
    print("these are the keys that can continue without error:") 
    for cmd in commands:
        print(f"-{cmd}")
    print()
    print("for exiting help menu these are the keys:")
    print() 
    print("y to start again") 
    print("n to stop") 
    print("type help if u get any error")
    
def code():
    password_value, password_bypass = password()
        
    user = input("Enter ur command:  ").lower()
    if user == "help":
        help_menu()
    else:
        if user in commands:
            if user.lower() in password_bypass:
                entered_password = password_value
                # bypass password
            else:
                try:
                    entered_password_input = input("Enter password first: ")
                    entered_password = hash_password(entered_password_input)
                except ValueError:
                    print("Password must be numbers only.")
                    return

            if entered_password != password_value:
                print("wrong password")
                return
            
            command_action[user]()
        else:
            print("Please write correct command")
code()



while True:
    a = input(f"u want to continue? \nto continue type y\nto Exit type n \nif u facing any problem type help: " )
    if a.lower() == "y":
        code()

    elif a.lower() == "help":
        help_menu()

    elif a.lower() == "n":
        print("exiting program")
        break

    else:
        print("error, use help")
