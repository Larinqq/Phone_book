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
    print('1 - View phone book')
    print('2 - Search for a contact')
    print('3 - Add new contact')
    print('4 - Seach and Edit contact\n')
    print('"q" for quit \n')


def print_search_and_edit_menu(text):
    """Prints menu for search and edit

    Args:
        text (str): search or edit  str
    """
    print('=========================\n')
    print(f'Choose one or few parametres for {text}(one by one)\n')
    print(f'0 - Last name ')
    print(f'1 - First name ')
    print(f'2 - Middle name ')
    print(f'3 - Company ')
    print(f'4 - Work phone')
    print(f'5 - Private phone \n')
    print('=========================\n')
