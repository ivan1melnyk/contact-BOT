
USERS_CONTACTS = {}


def input_error(func):
    def inner(user_input):
        user_input = user_input.split(' ')
        try:
            result = func(user_input)
        except KeyError:
            print("Give me name and phone please")
        except ValueError:
            print("Give me name and phone please")
        except IndexError:
            print("Give me name and phone please")
        return result
    return inner


def input_error_one(func):
    def inner(user_input):
        user_input = user_input.split(' ')
        try:
            result = func(user_input)
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Enter user name")
        except IndexError:
            print("Enter user name")
        return result
    return inner


@input_error
def add(user_input):
    print(user_input)
    USERS_CONTACTS[user_input[1]] = user_input[2]
    print('ADD USERS_CONTACTS:', user_input[1], 'NUMER:', user_input[2])


@input_error
def change(user_input):
    print(user_input)
    USERS_CONTACTS[user_input[1]] = user_input[2]
    print('CHANGE USERS_CONTACTS:', user_input[1], 'NUMER:', user_input[2])


@input_error_one
def phone(user_input):
    try:
        print(USERS_CONTACTS[user_input[1]])
    except:
        print('This contact doesn\'t exist')


while True:
    user_input = input()
    if user_input == "hello":
        print("How can I help you?")
    elif user_input.startswith("add"):
        add(user_input)
    elif user_input.startswith("change"):
        change(user_input)
    elif user_input.startswith("phone"):
        phone(user_input)
    elif user_input == "show all":
        print(USERS_CONTACTS)
    elif user_input == "good bye" or user_input == "close" or user_input == "exit":
        print("Good bye!")
    elif user_input == '.':
        break
