def print_row_data(row: str) -> None:
    """Prints contact's info nicely to the terminal

    Args:
        row (str): user data
    """
    print(f'Last name: {row[0]} ')
    print(f'First name: {row[1]} ')
    print(f'Middle name: {row[2]} ')
    print(f'Company: {row[3]} ')
    print(f'Work phone: {row[4]} ')
    print(f'Private phone: {row[5]} ')
    print('=========================\n')


def print_main_menu():
    """prints main menu
    """
    print('\nWelcome to the Phone book')
    print('Choose what would you like to do:\n')
    print('View phone book - 1')
    print('Search for a contact - 2')
    print('Add new contact - 3')
    print('Seach and Edit contact - 4\n')


def print_search_and_edit_menu(text):
    """Prints menu for search and edit

    Args:
        text (str): search or edit  str
    """
    print('=========================\n')
    print(f'Choose one or few parametres for {text}(one by one)\n')
    print(f'Last name -  0 ')
    print(f'First name - 1 ')
    print(f'Middle name - 2 ')
    print(f'Company - 3 ')
    print(f'Work phone - 4')
    print(f'Private phone - 5 \n')
    print('=========================\n')
