from collections import defaultdict
from src.handlers import *

def main():
    # storage for contacts
    contacts = {}

    # command handlers

    def default_handler():
        def inner(*args, **kwargs):
            return "Invalid command."
        return inner

    # all handlers should take 2 arguments - args list and contacts dictionary
    handlers = defaultdict(default_handler)
    handlers["hello"] = lambda x,y: "How can I help you?"
    handlers["close"] = lambda x,y: "Good bye!"
    handlers["exit"] = lambda x,y: "Good bye!"
    handlers["add"] = add_contact
    handlers["change"] = change_contact
    handlers["phone"] = show_phone
    handlers["all"] = show_all

    print("Welcome to the assistant bot!")

    # main loop
    command = ""
    while command not in ["close", "exit"]:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        print(handlers[command](args, contacts))
