from flask import Flask, render_template
from logfile_methods import save_log


def run_web(marketplaces: list):
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/listmarketplaces')
    def list_marketplaces():
        save_log('web: list_marketplaces')
        return render_template('list_marketplace.html', marketplaces = marketplaces)
    

    @app.route('/listcategories')
    def list_categories():
        save_log('web: list_categories')
        return render_template('list_categories.html', marketplaces = marketplaces)


    @app.route('/listcategoriesandsubcategories')
    def list_categories_subcategories():
        save_log('web: list_categories_subcategories')
        return render_template('list_categories_subcateries.html', marketplaces = marketplaces)
    
    @app.route('/listall')
    def list_all():
        save_log('web: list_all')
        return render_template('list_all.html', marketplaces = marketplaces)


    app.run()