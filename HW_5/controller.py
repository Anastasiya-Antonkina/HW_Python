import model
import view

def run():
    view.greetings()

    while True:
        
        command = view.menu()
        if command == 1:
            data = view.show_contact_form()
            model.add_contact(data)
        if command == 2:
            data = model.read_phonebook()
            view.show_phonebook(data)

        if command == 3:
            search = view.get_search_query()
            data = model.find(search)
            view.show_phonebook(data)
        if command == 4:
            search = view.get_search_query()
            data = model.find_first(search)

            view.show_phonebook(data)
            view.show_message('Введите новые данные')
            data = view.show_contact_form()
            model.find_and_change(search, data)
            view.show_message('Контакт изменен')

        if command == 5:
            view.show_message('Введите данные для поиска')
            search = view.get_search_query()
            found = model.find_and_del_first(search)
            if found == False:
                view.show_message('Контакт не найден')
            else:
                view.show_message('Контакт удалён')

        if command == 6:
            break