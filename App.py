from controller import *
from models import check_datafile_is_exist


def main():
    state = '0'
    while state != 'q':
        clear_console()
        state = choose_menu(state)()


if __name__ == "__main__":
    main()
