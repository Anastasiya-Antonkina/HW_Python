def greetings():
    print("Приветствую!")
    print("Телефонный справочник")
    
def menu():
    print("Меню")
    print("1. Добавить контакт")
    print("2. Просмотр контактов")
    print("3. Найти контакт")
    print("4. Изменить контакт")
    print("5. Удалить контакт")
    print("6. Выйти")
    command = int(input('Выберите пункт Меню: '))
    return command

def show_contact_form():
    last_name = input('Введите фамилию: ').capitalize()
    name = input('Введите имя: ').capitalize()
    phone = input('Введите номер телефона: ')
    contact = {'last_name': last_name, 'name': name, 'phone': phone}
    return contact

def show_phonebook(book):
    for i in book:
        print(i)

def show_message(message):
    print(message)

def get_search_query():
    search_name = input("Введите данные для поиска: ").capitalize()
    return 