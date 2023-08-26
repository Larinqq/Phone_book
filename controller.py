from models import *
from tempates import *


def main_menu():
    print_main_menu()
    state = input('> ')
    return state


def view_phone_book():
    print_data_from_page()
    pass


def search_contact():
    search()
    input('Press any key to exit')
    clear_console()
    pass


def add_new_contact():
    User.add_new_contact()
    input('Press "Enter" to exit')
    pass


def edit_contact():
    clear_console()
    print(" \n Firts step: you MUST search a contact to edit using any parameters you like")
    print(" Second step: choose Parameter(s) and ENTER new name for them ")
    input('\nPress Enter to start')

    write_edited_contact(search())

    pass


def choose_menu(state):
    return controllers_menu_selector.get(state, main_menu)


controllers_menu_selector = {
    '0': main_menu,
    '1': view_phone_book,
    '2': search_contact,
    '3': add_new_contact,
    '4': edit_contact
}
