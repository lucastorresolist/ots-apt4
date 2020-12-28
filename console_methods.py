
def list_marketplaces(marketplaces: list) -> None:
    print('Marketplaces: ')
    for obj in marketplaces:
        print(obj['name'])
        # print(obj[1])


def list_marketplaces_and_categories(marketplaces: list) -> None:
    for obj in marketplaces:
        print('\nmarketplace: ')
        print(obj['name'])
        print('categories: ')
        for cat in obj['category']:
            print(cat['name'])


def list_all(marketplaces: list):
    for obj in marketplaces:
        print('\nmarketplace: ')
        print(obj['name'])
        print('categories: ')
        for cat in obj['category']:
            print(cat['name'])
            print('subcategories: ')
            for sub in cat['subcategories']:
                print(sub['name'])