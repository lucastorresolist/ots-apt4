from flask import Flask, render_template, request
from archive_methods import write_marketplace, read_archive
from logfile_methods import save_log


def run_web(marketplaces: list):
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    @app.route('/')
    def index():
        marketplaces = read_archive()
        return render_template('index.html')

    @app.route('/insertmarketplace')
    def insert_market():
        marketplaces = read_archive()
        return render_template('insert_marketplace.html')


    @app.route('/writearchive')
    def write_archive():
        marketplace_name = request.args.get('name_marketplace')
        write_marketplace(marketplace_name)
        return index()


    @app.route('/listmarketplaces')
    def list_marketplaces():
        marketplaces = read_archive()
        save_log('web: list_marketplaces')
        return render_template('list_marketplace.html', marketplaces = marketplaces)
    

    @app.route('/listcategories')
    def list_categories():
        marketplaces = read_archive()
        save_log('web: list_categories')
        return render_template('list_categories.html', marketplaces = marketplaces)


    @app.route('/listcategoriesandsubcategories')
    def list_categories_subcategories():
        marketplaces = read_archive()
        save_log('web: list_categories_subcategories')
        return render_template('list_categories_subcateries.html', marketplaces = marketplaces)
    
    @app.route('/listall')
    def list_all():
        marketplaces = read_archive()
        save_log('web: list_all')
        return render_template('list_all.html', marketplaces = marketplaces)


    app.run()