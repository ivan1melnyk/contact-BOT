
USERS_CONTACTS = {}


def input_error(func):
    def inner(user_input):
        user_input = user_input.split(' ')
        try:
            return func(user_input)
        except KeyError:
            print("Give me name and phone please")
        except ValueError:
            print("Give me name and phone please")
        except IndexError:
            print("Give me name and phone please")
    return inner


def hello():
    print("How can I help you?")


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


@input_error
def phone(user_input):
    try:
        print(USERS_CONTACTS[user_input[1]])
    except IndexError:
        print('Enter user name')
    except KeyError:
        print('This contact doesn\'t exist')


def show_all():
    if USERS_CONTACTS == {}:
        print('Your contacts list is empty')
    for name, number in USERS_CONTACTS.items():
        # print(f'Name:{contact[0]}','Number:'{contact[1]})
        print('{:^5} {:^10} {:^7} {:^10}'.format(
            'Name:', name, 'Number:', number))


def bye_bye():
    print("Good bye!")


while True:
    user_input = input()
    if user_input == "hello":
        hello()
    elif user_input.startswith("add"):
        add(user_input)
    elif user_input.startswith("change"):
        change(user_input)
    elif user_input.startswith("phone"):
        phone(user_input)
    elif user_input == "show all":
        show_all()
    elif user_input == "good bye" or user_input == "close" or user_input == "exit":
        bye_bye()
    elif user_input == '.':
        break
    else:
        print('//Error')
        print('//Unknown comand')


# print мають бути в функції main, тільки в ній
