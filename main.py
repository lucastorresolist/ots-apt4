from textwrap import dedent
from web import run_web
from archive_methods import read_archive, write_archive
from console_methods import list_all, list_marketplaces, list_marketplaces_and_categories

if __name__ == "__main__":

    write_archive()
    marketplaces = read_archive()

    print(dedent("""
        ------Select an option------
        1 - Use console
        2 - Use Web flask
    """
    ))

    option_selected = int(input('Insert an option: '))

    if option_selected == 1:
        print(dedent('''
            1 - list marketplaces
            2 - list categories and marketplaces
            3 - list all
        '''))
        
        option_selected = int(input('Select an option: '))

        if option_selected == 1:
            list_marketplaces(marketplaces)
        
        elif option_selected == 2:
            list_marketplaces_and_categories(marketplaces)
        
        elif option_selected == 3:
            list_all(marketplaces)

    else:
        run_web(marketplaces)