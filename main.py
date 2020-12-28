from textwrap import dedent
from flask import Flask, render_template
from flask.helpers import make_response
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
        
        option_selected = int(input('Select an option'))

        if option_selected == 1:
            list_marketplaces(marketplaces)
        
        elif option_selected == 2:
            list_marketplaces_and_categories(marketplaces)
        
        elif option_selected == 3:
            list_all(marketplaces)

    else:
        app = Flask(__name__)
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

        @app.route('/')
        def index():
            return render_template('index.html')


        @app.route('/listmarketplaces')
        def list_marketplaces():
            return render_template('list_marketplace.html', marketplaces = marketplaces)
        

        @app.route('/listcategories')
        def list_categories():
            return render_template('list_categories.html', marketplaces = marketplaces)
    

        @app.route('/listcategoriesandsubcategories')
        def list_categories_subcategories():
            return render_template('list_categories_subcateries.html', marketplaces = marketplaces)
        
        @app.route('/listall')
        def list_all():
            return render_template('list_all.html', marketplaces = marketplaces)


        app.run()