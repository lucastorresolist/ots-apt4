from logfile_methods import save_log

def list_marketplaces(marketplaces: list) -> None:
    save_log('console: list_marketplaces')
    print('Marketplaces: ')
    for obj in marketplaces:
        print(obj['name'])


def list_marketplaces_and_categories(marketplaces: list) -> None:
    save_log('console: list_marketplaces_and_categories')
    for obj in marketplaces:
        print('\nmarketplace: ')
        print(obj['name'])
        print('categories: ')
        for cat in obj['category']:
            print(cat['name'])


def list_all(marketplaces: list):
    save_log('console: list_all')
    for obj in marketplaces:
        print('\nmarketplace: ')
        print(obj['name'])
        print('categories: ')
        for cat in obj['category']:
            print(cat['name'])
            print('subcategories: ')
            for sub in cat['subcategories']:
                print(sub['name'])