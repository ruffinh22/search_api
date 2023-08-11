import os
from bs4 import BeautifulSoup
from flask_migrate import Migrate
os.environ['REQUESTS_CA_BUNDLE'] = '/etc/ssl/certs/ca-certificates.crt'
from flask import render_template, redirect, request, url_for, jsonify
from models import SearchResult  # Import the SearchResult model
import facebook
from googlesearch import search
import requests
from flask import render_template, Flask, request, jsonify
from bs4 import BeautifulSoup
from fabfile import db, app
from models import SearchResult, SearchResultf
from collections import namedtuple
from datetime import datetime


migrate = Migrate(app, db)


with app.app_context():
    # Run the Alembic upgrade command
    from alembic.config import Config
    from alembic import command

    alembic_cfg = Config("alembic.ini")

YOUR_FACEBOOK_ACCESS_TOKEN = "EABFF8EjW7UYBO2DrHtxZBWBNE0zXFYs6QY9KVYybG8JoCsWk9T98ZCWyFHdrrhpQeSq1V5CyUDAM4spxB9Px70ZC3BJ0CZBCxRJULA42smJPtzXaRl2Bx0dL49C7RuOiY7ZAZBmMiN11ivZAl5sZAWj5nwg1K6MaLrVIHiYrQwKDzGZA4QKaV7IVPfjGzFl2L9s0WuDNZCm9mt"
BASE_URL = "https://graph.facebook.com/v17.0"
API_KEY2 = "996698248315914|gvfccZ3PA7r-xSE1inDN31MKhu8"
API_KEY = "AIzaSyDY4Ap1KhK7ox8f1t3KrfnHuH_qd9eSYI0"
SEARCH_ENGINE_ID = "a574e952c328446ce"
SEARCH_ENGINE_ID2 = "32a9b32894f0b4a61"


SearchResult = namedtuple('SearchResult', ['text', 'images', 'post_url', 'time', 'likes', 'comments', 'shares'])


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


import os
from bs4 import BeautifulSoup
from flask_migrate import Migrate
os.environ['REQUESTS_CA_BUNDLE'] = '/etc/ssl/certs/ca-certificates.crt'
from flask import render_template, redirect, request, url_for
from models import SearchResult  # Import the SearchResult model



migrate = Migrate(app, db)

# ... (le reste du code est inchangé)


@app.route('/search', methods=['GET', 'POST'])
def search_google():
    error_message = None
    
    if request.method == 'POST':
        sector = request.form.get('sector')
        location = request.form.get('location')

        if not sector or not location:
            error_message = 'Veuillez renseigner le secteur et la localisation'
        else:
            query = f"{sector} {location}"

            url = f"https://www.googleapis.com/customsearch/v1"
            params = {
                'key': API_KEY,
                'cx': SEARCH_ENGINE_ID,
                'q': query,
                'num': 10,  # Nombre de résultats à afficher
            }

            response = requests.get(url, params=params)
            data = response.json()

            extracted_results = []  # Pour stocker les résultats extraits

            if 'items' in data:
                for item in data['items']:
                    title = item['title']
                    link = item['link']
                    description = item.get('snippet', '')
                    image_url = item.get('pagemap', {}).get('cse_image', [{}])[0].get('src', '')

                    extracted_result = {
                        'title': title,
                        'link': link,
                        'description': description,
                        'image_url': image_url,
                    }
                    extracted_results.append(extracted_result)

                    # Enregistrement dans la base de données
                    new_search_result = SearchResult(
                        title=title,
                        link=link,
                        description=description,
                        image_url=image_url
                    )
                    db.session.add(new_search_result)
                    db.session.commit()

            return render_template('search_results.html', extracted_results=extracted_results)
    
    return render_template('search_form.html', error_message=error_message)




@app.route('/facebook', methods=['GET', 'POST'])
def search_facebook():
    error_message = None
    
    if request.method == 'POST':
        sector = request.form.get('sector')
        location = request.form.get('location')

        if not sector or not location:
            error_message = 'Veuillez renseigner le secteur et la localisation'
        else:
            query = f"{sector} {location}"

            url = f"https://www.googleapis.com/customsearch/v1"
            params = {
                'key': API_KEY,
                'cx': SEARCH_ENGINE_ID2,
                'q': query,
                'num': 10,  # Nombre de résultats à afficher
            }

            response = requests.get(url, params=params)
            data = response.json()

            extracted_results = []  # Pour stocker les résultats extraits

            if 'items' in data:
                for item in data['items']:
                    title = item['title']
                    link = item['link']
                    description = item.get('snippet', '')
                    image_url = item.get('pagemap', {}).get('cse_image', [{}])[0].get('src', '')

                    extracted_result = {
                        'title': title,
                        'link': link,
                        'description': description,
                        'image_url': image_url,
                    }
                    extracted_results.append(extracted_result)

                    # Enregistrement dans la base de données
                    new_search_result = SearchResult(
                        title=title,
                        link=link,
                        description=description,
                        image_url=image_url
                    )
                    db.session.add(new_search_result)
                    db.session.commit()

            return render_template('res_faceb.html', extracted_results=extracted_results)
    
    return render_template('search.html', error_message=error_message)






@app.route('/results', methods=['GET'])
def show_results():
    # Récupérer les résultats depuis la base de données
    results = SearchResult.query.all()

    return render_template('results.html', results=results)




@app.route('/delete/<int:result_id>', methods=['POST'])
def delete_result(result_id):
    result = SearchResult.query.get(result_id)
    if result:
        db.session.delete(result)
        db.session.commit()
    
    return redirect(url_for('show_results'))

@app.route('/delete/all', methods=['POST'])
def delete_all():
    # Supprimez tous les éléments de la table SearchResult
    db.session.query(SearchResult).delete()
    db.session.commit()

    return redirect(url_for('show_results'))




if __name__ == '__main__':

    app.run(debug=True)





