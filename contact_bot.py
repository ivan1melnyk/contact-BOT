
USERS_CONTACTS = {
    'Ivan': '0962053326',
    'Myron': '0631389599'
}


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
    return "How can I help you?"


@input_error
def add(user_input):
    # print(user_input)
    USERS_CONTACTS[user_input[1]] = user_input[2]
    return '{:<22} {:^10} {:>4} {:<7} {:^10}'.format('ADD USERS_CONTACTS:', user_input[1], '|', 'NUMER:', user_input[2])


@input_error
def change(user_input):
    # print(user_input)
    USERS_CONTACTS[user_input[1]] = user_input[2]
    return '{:<22} {:^10} {:>4} {:<7} {:^10}'.format('CHANGE USERS_CONTACTS:', user_input[1], '|', 'NUMER:', user_input[2])


@input_error
def phone(user_input):
    try:
        name = user_input[1]
        number = USERS_CONTACTS[user_input[1]]
        return '{:^5} {:^10} {:^7} {:^10}'.format('Name:', name, 'Number:', number)
    except IndexError:
        return 'Enter user name'
    except KeyError:
        return 'This contact doesn\'t exist'


def show_all():
    if USERS_CONTACTS == {}:
        return 'Your contacts list is empty'
    users_list = list()
    for name, number in USERS_CONTACTS.items():
        users_list.append('{:^5} {:^10} {:^7} {:^10}'.format(
            'Name:', name, 'Number:', number))
    return users_list


def bye_bye():
    return "Good bye!"


def main(result):
    if isinstance(result, list):
        for str_user in result:
            print(str_user)
    else:
        print(result)


while True:
    user_input = input()
    if user_input == "hello":
        result = hello()
    elif user_input.startswith("add"):
        result = add(user_input)
    elif user_input.startswith("change"):
        result = change(user_input)
    elif user_input.startswith("phone"):
        result = phone(user_input)
    elif user_input == "show all":
        result = show_all()
    elif user_input == "good bye" or user_input == "close" or user_input == "exit":
        result = bye_bye()
    elif user_input == '.':
        break
    else:
        print('//Error')
        print('//Unknown comand')
    main(result)


# print мають бути в функції main, тільки в ній
