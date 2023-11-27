from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass
    # реалізація класу


class Phone(Field):
    @property
    def phone(self):
        return self.__value

    @phone.setter
    def phone(self, phone):
        if len(phone) == 10:
            self.__value = self.__phone = phone
        else:
            print('Error phonenumber\'s lenght must be 10 symbols')

    # def __setitem__(self, key, value):
    #     if value not in user.phones:
    #         user.phones.append(value)


class Birthday(Field):
    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday


class Record:
    def __init__(self, name, birthday):
        self.name = Name(name)
        self.phones = []
        self.birthday = datetime.strptime(birthday, '%Y-%m-%d').date()

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones = [number for number in self.phones if number != phone]

    def edit_phone(self, old_number, new_number):
        # print('/// Chnage number', old_number, 'on', new_number)
        for i in range(len(self.phones)):
            the_number = self.phones[i]
            if str(the_number) == old_number:
                self.phones[i] = Phone(new_number)

    def find_phone(self, number):
        for phone in self.phones:
            if str(phone) == number:
                return number

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def days_to_birthday(self):
        today = datetime.now().date()
        birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
        birthday = birthday.replace(year=today.year)
        delta = birthday - today
        if delta.days < 0:
            birthday = birthday.replace(year=today.year+1)
            delta = birthday - today
        return delta


class AddressBook(UserDict):
    def add_record(self, record):
        # print(record.name)
        self.data[record.name.value] = record

    def find(self, name):
        for record_name, record in self.data.items():
            if str(record_name) == name:
                return record
        print('There is not {name} in address book')

    def delete(self, name):
        print(f'DELETE {name}')
        # del self.data[name]
        self.data = {r_name: record for r_name,
                     record in self.data.items() if str(r_name) != name}

    def iterator(self, N):
        dates = list(self.data.values())
        print(dates)
        iterations = [dates[i:i + N] for i in range(0, len(dates), N)]
        for iter in iterations:
            yield iter  # iter - one iteration return N(к-сть) записів
    # реалізація класу


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John", '2000-10-11')
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane", '2000-12-31')
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
jane_record = Record("Jams", '2000-12-31')
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print('____________________MAIN___________________________')
for iter in book.iterator(2):
    print(iter)
print('__________________________________________________')

# Знаходження та редагування телефону для John
john = book.find("John")
print(john)
john.edit_phone("1234567890", "1112223333")

# Виведення: Contact name: John, phones: 1112223333; 5555555555
print(john)

# # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
book.delete("Jane")

# Виведення всіх записів у книзі
print('__________________________________________________')
for name, record in book.data.items():
    print(record)
