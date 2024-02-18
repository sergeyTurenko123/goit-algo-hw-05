def parse_input(user_input):
    name, *args = user_input.split()
    name = name.strip().lower()
    return name, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
       
    return inner

@input_error
def add_contact(args):
    name, phone = args
    if len(phone) == 10:
        phone = f"+38{phone}"
    elif len(phone) == 11:
        phone = f"+3{phone}"
    elif len(phone) == 12:
        phone = f"+{phone}"
    elif len(phone) < 10:
        return("enter phone number")
    else:
        phone = phone
    with open('name_phone.txt', "r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        match = re.sub(pattern = r"[\s\D]", repl = r"", string = list_line[1])
        lists.update({list_line[0]: f"+{match.strip()}"})
    if name in lists:
        return("Contact exists. Re-record?")
    else:
        lists[name] = phone
        with open("name_phone.txt","w", encoding = "utf-8") as fh:
            for key, value in lists.items():
                fh.write(f'{key},{value}\n')
        return "Contact added."

@input_error
def change_contact(args):
    name, phone = args
    if len(phone) == 10:
        phone = f"+38{phone}"
    elif len(phone) == 11:
        phone = f"+3{phone}"
    elif len(phone) == 12:
        phone = f"+{phone}"
    elif len(phone) < 10:
        return("enter phone number")
    else:
        phone = phone
    with open('name_phone.txt', "r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        match = re.sub(pattern = r"[\s\D]", repl = r"", string = list_line[1])
        lists.update({list_line[0]: f"+{match.strip()}"})
    if name in lists:
        lists[name] = phone
        with open("name_phone.txt","w", encoding = "utf-8") as fh:
            for key, value in lists.items():
                fh.write(f'{key},{value}\n')
        return "Contact updated."
    else:
        print("Contact does not exist. Will you write it down?")
    
@input_error
def show_phone(args):
    [name] = args
    with open('name_phone.txt', "r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        match = re.sub(pattern = r"[\s\D]", repl = r"", string = list_line[1])
        lists.update({list_line[0]: f"+{match.strip()}"})
    if name in lists:
        return(f"{name},{lists[name]}")
    else:
        return("Contact does not exist. Will you write it down?")
    
import re

def show_all():
    with open('name_phone.txt', "r", encoding = "utf-8") as fh:
        lines = fh.readlines()
    lists = {}
    for line in lines:
        list_line = line.split(",")
        pattern = r"[\s\D]"
        repl = r""
        match = re.sub(pattern, repl, list_line[1])
        match = re.sub(pattern = r"[\s\D]", repl = r"", string = list_line[1])
        lists.update({list_line[0]: f"+{match.strip()}"})
    return lists



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()