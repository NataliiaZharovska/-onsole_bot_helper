from typing import Callable, Dict
from contacts import contact_book


def command_handler(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)
        except Exception as e:
            raise SystemExit("Good bye!")

    return wrapper


@command_handler

def hello_handler(*args):
    return "How can I help you?"

@command_handler

def add_handler(username: str, number: str):
    if contact_book.get(username) is None:
        contact_book[username] = number
        return "Number was added!!!"
    raise ValueError("Number already in contact book")

@command_handler

def change_handler(username: str, number: str):
    if contact_book.get(username) is not None:
        contact_book[username] = number
        return "Number was changed!!!"
    raise KeyError("Number does not exists!")

@command_handler

def phone_handler(username: str):
    phone = contact_book.get(username)
    if phone is not None:
        return f"User number is {phone}"
    raise ValueError

@command_handler

def show_all_handler(*args):
    all_response = "Contact book\n"
    contacts = "\n".join(
        f"{username} number is {number}" for (username, number) in contact_book.items()
    )
    formatted_contacts = "Number does not exists, yet!" if contacts == '' else contacts
    return all_response + formatted_contacts
   
@command_handler

def exit_handler(*args):
    raise SystemExit("Good bye!!!")

@command_handler

def unknown_handler(*args):
    raise ValueError("Command is not valid!")

handlers: Dict[str, Callable] = {
    "hello": hello_handler,
    "add": add_handler,
    "change": change_handler,
    "phone": phone_handler,
    "show all": show_all_handler,
    "good bye": exit_handler,
    "close": exit_handler,
    "exit": exit_handler,
}


