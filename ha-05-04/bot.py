def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
    return inner

def parse_input(user_input):
    if not user_input.strip():
        return "unknown", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    # Если аргументов нет, name, phone = args вызовет ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    # Если аргументов нет, name, phone = args вызовет ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    # Если ключа нет, генерируем KeyError для декоратора
    raise KeyError

@input_error
def show_phone(args, contacts):
    # Если args пустой, args[0] вызовет IndexError
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    raise KeyError

def show_all(contacts):
    if not contacts:
        return "Your contact list is empty."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
