import json

path = 'archive.txt'

def write_archive() -> list:
    marketplaces : list = []

    marketplaces.append('{"name": "magalu", "category": [{"name": "eletronico", "subcategories": [{"name":"celulares"}, {"name":"televisões"}]}]}')
    marketplaces.append('{"name": "mercado livre", "category": [{"name": "quarto", "subcategories": [{"name":"armarios"}, {"name": "camas"}, {"name":"abajur"}]}]}')
    marketplaces.append('{"name": "netshoes", "category": [{"name": "sapatos", "subcategories": []}, {"name": "chinelos", "subcategories": []}]}')

    archive = open(path, 'w')
    for obj in marketplaces:
        archive.write(f'{obj}\n')
    archive.close()


def read_archive() -> list:
    marketplaces : list = []
    archive = open(path, 'r')
    
    for obj in archive:
        line_cleaned = obj.strip() #clear caracteres and clear white spaces (\n \t \r ' ')
        line_json = json.loads(line_cleaned)
        marketplaces.append(line_json)

    archive.close()
    return marketplaces