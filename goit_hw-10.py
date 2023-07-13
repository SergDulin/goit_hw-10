def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please provide valid arguments."
        except IndexError:
            return "Invalid input. Please provide both name and phone number."
    return inner

contacts = {}

@input_error
def add_contact(*args):
    if len(args) < 2:
        raise IndexError
    name = " ".join(args[:-1]).lower()
    phone = args[-1]
    contacts[name] = phone
    return "Contact added successfully."

@input_error
def change_phone(*args):
    if len(args) < 2:
        raise IndexError
    name = " ".join(args[:-1]).lower()
    phone = args[-1]
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Phone number updated successfully."

@input_error
def get_phone(name):
    matching_contacts = [f"{contact_name.title()} is {phone}" for contact_name, phone in contacts.items() if name.lower() in contact_name.lower()]
    if matching_contacts:
        return "\n".join(matching_contacts)
    else:
        return "No contacts found with that name."

@input_error
def show_all_contacts():
    if contacts:
        all_contacts = "\n".join([f"{contact_name.title()}: {phone}" for contact_name, phone in contacts.items()])
        return all_contacts
    else:
        return "No contacts found."

def hello_command():
    return "How can I help you?"

def goodbye_command():
    return "Goodbye!"

def komand(command_parts):
    command_key = command_parts[0]
    command_arguments = command_parts[1:]

    if command_key == "show" and command_arguments == ["all"]:
        return show_all_contacts()
    elif command_key == "good" and command_arguments == ["bye"]:
        return goodbye_command()
    elif command_key in command_handlers:
        handler = command_handlers[command_key]
        return handler(*command_arguments)
    else:
        return "Invalid command. Please try again."

command_handlers = {
    "hello": hello_command,
    "exit": goodbye_command,
    "close": goodbye_command,
    "add": add_contact,
    "change": change_phone,
    "phone": get_phone
}

def main():
    while True:
        command = input("Enter a command: ").lower()
        command_parts = command.split()
        
        result = komand(command_parts)
        print(result)

        if result == "Goodbye!":
            break

if __name__ == "__main__":
    main()