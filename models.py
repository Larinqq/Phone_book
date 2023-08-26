import csv
import os.path

from tempates import *

HEADERS: list[str] = ['id', 'Last name', 'First name', 'Middle name',
                      'Company', 'Work phone number', 'Private phone']
DATA_FILE_NAME: str = 'phone_book_data.csv'


class User:
    def __init__(self, last_name: str, first_name: str, middle_name: str, company_name: str) -> None:
        """Includes all user data

        Args:
            last_name (str): 
            first_name (str): 
            middle_name (str): 
            company_name (str): 
        """
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.company_name = company_name

    @staticmethod
    def add_new_contact() -> None:
        """Asks user to enter contact's data and phone numbers. Writes the data file.
        """
        write_contact_to_file(User.get_user_info(), Phone.get_phone_number())

    @staticmethod
    def get_user_info() -> 'User':
        """gets user's info

        Returns:
        User: user's info such as names and company
        """
        return User(
            last_name=input('Enter Last name: ',),
            first_name=input('Enter first name: ',),
            middle_name=input('Enter middle name: ',),
            company_name=input('Enter company name: ',)
        )


class Phone:
    def __init__(self, work_phone, private_phone) -> None:
        self.work_phone = work_phone
        self.private_phone = private_phone

    @staticmethod
    def get_phone_number() -> 'Phone':
        """gets user's work and private phone numbers

        Returns:
        Phone: work,private phone numbers
        """
        return Phone(input('Enter work phone: '),
                     input('Enter private_phone: '))


def write_contact_to_file(user_data: User, phone_data: Phone) -> None:
    """Opens data file. Takes user's data and phone numbers and writes them to the csv file

    Args:
        user_data (User): class "User" with user's info
        phone_data (Phone): class "Phone" with user's phone numbers
    """
    with open(DATA_FILE_NAME, 'a', newline='') as phone_book_data:
        writer = csv.writer(phone_book_data)
        writer.writerow([
            user_data.last_name,
            user_data.first_name,
            user_data.middle_name,
            user_data.company_name,
            phone_data.work_phone,
            phone_data.private_phone
        ])
    print("New contact was added successfully! ")


def check_datafile_is_exist() -> None:
    """Checks if data file is exists and creates it if it's not
    """
    if not os.path.isfile(DATA_FILE_NAME):
        create_new_datafile()


def create_new_datafile() -> None:
    """Opens data file and writes coloum's name to the csv file
    """
    with open(DATA_FILE_NAME, 'w', newline='') as phone_book_data:
        writer = csv.writer(phone_book_data)
        writer.writerow(HEADERS)


def print_data_from_page(page_number: int = 1, rows_on_page: int = 3) -> None:
    """Opens data file and gets rows from the specified page.

    Args:
        page_number (int, optional): Page number to display. Defaults to 1.
        rows_on_page (int, optional): Number of rows to display per page. Defaults to 3.
    """
    rows = []
    with open(DATA_FILE_NAME, 'r') as phone_book_data:
        file_reader = csv.reader(phone_book_data, delimiter=",")
        rows = list(file_reader)

    total_rows = len(rows)
    total_pages = (total_rows + rows_on_page - 1) // rows_on_page

    page_number = max(1, min(page_number, total_pages))

    start_index = (page_number - 1) * rows_on_page
    end_index = min(start_index + rows_on_page, total_rows)

    clear_console()
    print(
        f'\n{total_rows} contact(s) found! Showing page {page_number}/{total_pages}\n')

    for row_number, row in enumerate(rows[start_index:end_index], start=start_index + 1):
        print_row_data(row)

    print("\nNavigation:")
    if page_number > 1:
        print("p: Previous Page")
    if page_number < total_pages:
        print("n: Next Page")

    user_choice = input(
        "Enter 'n' for next page, 'p' for previous page, or any other key to quit: ").lower()

    while user_choice not in ['n', 'p']:
        print("Invalid choice. Please enter 'n', 'p', or any other key to quit.")
        user_choice = input(
            "Enter 'n' for next page, 'p' for previous page, or any other key to quit: ").lower()

    if user_choice == 'n' and page_number < total_pages:
        print_data_from_page(page_number + 1, rows_on_page)
    elif user_choice == 'p' and page_number > 1:
        print_data_from_page(page_number - 1, rows_on_page)


def search() -> list:
    """Gets seaching parametrs from get_search_and_edit_param function and implements them like a reach requst.
    Search and prints row you are looking for

    Returns:
        list: a row's number for editing
    """
    parameters = get_search_and_edit_param('search')
    search_results_row_numbers = []

    if all(param == 0 for param in parameters):
        print_data_from_page()
        return search_results_row_numbers

    search_results = []

    with open(DATA_FILE_NAME, 'r') as phone_book_data:
        file_reader = csv.reader(phone_book_data, delimiter=",")
        for row_number, row in enumerate(file_reader):
            if all(param == 0 or row[param_number] == param for param_number, param in enumerate(parameters)):
                search_results.append(row)
                search_results_row_numbers.append(row_number)

    clear_console()
    print(f'**********\n{len(search_results)} contact(s) was found! \n ')

    for row in search_results:
        print_row_data(row)

    return search_results_row_numbers


def get_search_and_edit_param(text):
    print_search_and_edit_menu(text)
    parameters_list = [0, 0, 0, 0, 0, 0]
    param_dict = {
        '0': 'Last name',
        '1': 'First name',
        '2': 'Middle name',
        '3': 'Company name',
        '4': 'Work phone',
        '5': 'Private phone',
    }
    while True:
        print("Enter parameter's number (q to quit)")
        user_response = input('> ').lower()

        if user_response == 'q':
            break
        elif user_response.isdigit() and int(user_response) < len(param_dict):
            parameters_list[int(user_response)] = input(
                f'Enter "{param_dict[user_response]}" for {text} : ')

            if input('Continue entering parameters? (y/n): ').lower() != 'y':
                break
        else:
            print("Invalid input. Please enter a valid parameter number.")

    return parameters_list


def clear_console() -> None:
    """clears terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def write_edited_contact(list_of_row_numbers_to_edit) -> None:
    """Gets a row's number for editing from search func, asks user to enter new data and rewrite the row to the data file

    Args:
        list_of_row_numbers_to_edit (_type_): a row's number for editing
    """
    editing_parameters = get_search_and_edit_param('editing')

    with open(DATA_FILE_NAME, 'r') as phone_book_data:
        file_reader = csv.reader(phone_book_data)
        rows = [row for row in file_reader]

    for row_number_to_edit in list_of_row_numbers_to_edit:
        if row_number_to_edit < 0 or row_number_to_edit >= len(rows):
            print(f"Invalid row number {row_number_to_edit} to edit.")
            continue

        edited_row = rows[row_number_to_edit]
        for param_num, new_param in enumerate(editing_parameters):
            if new_param != 0:
                edited_row[param_num] = new_param

    with open(DATA_FILE_NAME, 'w', newline='') as phone_book_data:
        file_writer = csv.writer(phone_book_data)
        file_writer.writerows(rows)

    print("\n Contact was edited successfully!")
