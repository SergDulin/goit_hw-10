from collections import UserDict

class Field:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def __str__(self) -> str:
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone_class(self, index, phone):
        self.phones[index] = phone

    def __repr__(self) -> str:
        return ",".join([p.value for p in self.phones])


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record


contact_book = AddressBook()


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Invalid input. Please provide both name and phone number."
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please provide valid arguments."

    return wrapper


def hello_command(*args):
    return "Hello. How can I help you?"


def goodbye_command(*args):
    return "Goodbye!"


@input_error
def add_contact(*args):
    list_of_param = args[0].split()
    if len(list_of_param) < 2:
        raise IndexError
    name = Name(" ".join(list_of_param[:-1]))
    phone = Phone(list_of_param[-1])
    new_user = Record(name)
    new_user.add_phone(phone)
    contact_book.add_record(new_user)
    return "Contact added successfully"


def show_all_contacts(*args):
    if contact_book.data:
        lst_phones = [f"{k.title()}:{', '.join(str(num) for num in v.phones)}" for k, v in contact_book.data.items()]
        return "\n".join(lst_phones)
    else:
        return "No contacts found."


@input_error
def get_phone(*args):
    name = args[0]
    matching_contacts = [f"{k.title()}:{', '.join(str(num) for num in v.phones)}" for k, v in contact_book.data.items() if
                         name.lower() in k.lower()]
    if matching_contacts:
        return "\n".join(matching_contacts)
    else:
        return "No contacts found with that name."


@input_error
def change_phone(*args):
    name, phone = args[0].split(maxsplit=1)
    name = Name(name)
    phone = Phone(phone)
    if name.value not in contact_book.data:
        raise KeyError
    update_user = contact_book.data[name.value]
    update_user.change_phone_class(0, phone)
    return f"User {name.value} has changed the phone to {phone.value}"


def no_command(*args):
    return "Invalid command. Please try again."


command_handlers = {
    hello_command: 'hello',
    goodbye_command: ['exit', 'close', 'good bye'],
    add_contact: 'add',
    show_all_contacts: 'show all',
    get_phone: 'phone',
    change_phone: 'change'
}


def komand(text):
    for command, keywords in command_handlers.items():
        if isinstance(keywords, str):
            if text.startswith(keywords):
                return command, text.replace(keywords, '').strip()
        elif isinstance(keywords, list):
            for keyword in keywords:
                if text.startswith(keyword):
                    return command, text.replace(keyword, '').strip()
    return no_command, None


def main():
    while True:
        user_input = input("Enter a command: ").lower()
        command, data = komand(user_input)
        result = command(data)
        print(result)

        if result == "Goodbye!":
            break


if __name__ == '__main__':
    main()
