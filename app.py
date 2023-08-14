from flask import render_template, redirect, request, url_for
from datetime import datetime
from collections import namedtuple
from models import SearchResult, SearchResultf
from fabfile import db, app
from flask import render_template, Flask, request, jsonify
import requests
from googlesearch import search
from logging import DEBUG
import facebook
from models import SearchResult  # Import the SearchResult model
from flask import render_template, redirect, request, url_for, jsonify
import os
from bs4 import BeautifulSoup
from flask_migrate import Migrate
os.environ['REQUESTS_CA_BUNDLE'] = '/etc/ssl/certs/ca-certificates.crt'


migrate = Migrate(app, db)


with app.app_context():
    # Run the Alembic upgrade command
    from alembic.config import Config
    from alembic import command

    alembic_cfg = Config("alembic.ini")

YOUR_FACEBOOK_ACCESS_TOKEN = "EAAw9qOJhpzkBO9SpApFr23ICON5CHj8sAyGWb8ueZBP8fgdkjufhcZAfSftesVmgBV7cYliLUhd8gxmQmtOIa456ZATfy4js8aiBBKErbVjduoqZBZBnuDQukxQnHyA0raVDtbdZBrPXeIgXT8gWZCcq04o2au237C1d3AFrUKhgVl5mRHMRHCO3GZBGnLcedGsAxxKP62FekxUmybGIZCpJ87ARJVylzkdlDM4JsGfxe8d3nPIVOSjoYddENzCaUZA4w0siIfdG1YWsAZD"
BASE_URL = "https://graph.facebook.com/v17.0"
API_KEY2 = "996698248315914|gvfccZ3PA7r-xSE1inDN31MKhu8"
API_KEY = "AIzaSyDY4Ap1KhK7ox8f1t3KrfnHuH_qd9eSYI0"
SEARCH_ENGINE_ID = "a574e952c328446ce"
SEARCH_ENGINE_ID2 = "32a9b32894f0b4a61"


SearchResult = namedtuple('SearchResult', [
                          'text', 'images', 'post_url', 'time', 'likes', 'comments', 'shares'])


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


os.environ['REQUESTS_CA_BUNDLE'] = '/etc/ssl/certs/ca-certificates.crt'


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

            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                'key': API_KEY,
                'cx': SEARCH_ENGINE_ID,
                'q': query,
                'num': 10,  # Nombre de résultats à afficher
            }

            response = requests.get(url, params=params)
            data = response.json()

            extracted_results = []  # Pour stocker les résultats extraits

            for item in data['items']:
                title = item['title']
                link = item['link']
                description = item.get('snippet', '')
                image_url = item.get('pagemap', {}).get(
                    'cse_image', [{}])[0].get('src', '')

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
                    image_url=image_url,
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

            url = "https://www.googleapis.com/customsearch/v1"
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
                    image_url = item.get('pagemap', {}).get(
                        'cse_image', [{}])[0].get('src', '')

                    # Extraire les informations de likes et commentaires de la description
                    likes = 0
                    comments = 0
                    description_parts = description.split('·')
                    for part in description_parts:
                        part_lower = part.lower()
                        if "j'aime" in part_lower or "like" in part_lower:
                            likes_text = ''.join(filter(str.isdigit, part))
                            likes = int(likes_text) if likes_text else 0
                        elif 'comment' in part_lower:
                            comments_text = ''.join(filter(str.isdigit, part))
                            comments = int(
                                comments_text) if comments_text else 0

                    if created_time_str := item.get('created_time', ''):
                        created_time = datetime.strptime(
                            created_time_str, '%Y-%m-%dT%H:%M:%S%z')  # Convertir en objet datetime
                    else:
                        created_time = None  # ou une autre valeur par défaut, si nécessaire

                    extracted_result = {
                        'title': title,
                        'link': link,
                        'description': description,
                        'image_url': image_url,
                        'created_time': created_time,  # Utiliser l'objet datetime ici
                        'likes': likes,  # Utiliser la valeur de likes
                        'comments': comments,  # Utiliser la valeur de comments
                    }
                    extracted_results.append(extracted_result)

                    # Enregistrement dans la base de données
                    new_search_result = SearchResultf(
                        title = title,
                        link= link,
                        description = description,
                        image_url = image_url,
                        created_time = created_time,  # Utiliser l'objet datetime ici
                        likes = likes,  # Utiliser la valeur de likes
                        comments = comments,  # Utiliser la valeur de comments

                    )
                    db.session.add(new_search_result)
                    db.session.commit()

            return render_template('facebook_results.html', extracted_results=extracted_results, error_message=error_message)

    return render_template('facebook_search_form.html')


@app.route('/facebook1', methods=['GET', 'POST'])
def search_facebook1():
    error_message = None
    if request.method == 'POST':
        sector = request.form.get('sector')
        location = request.form.get('location')

        extracted_results = []

        if not sector or not location:
            error_message = 'Veuillez renseigner le secteur et la localisation'
        else:
            try:
                access_token = YOUR_FACEBOOK_ACCESS_TOKEN  # Replace with the actual token
                graph = facebook.GraphAPI(access_token)

                # Fetch posts of the user associated with the token
                search_results = graph.get_object('/user/feed')

                for post in search_results['data']:
                    post_id = post.get('id')
                    post_data = graph.get_object(
                        id=post_id, fields='message,created_time,attachments,likes.summary(true),comments.summary(true),shares')

                    created_time = datetime.strptime(post_data.get(
                        'created_time', ''), '%Y-%m-%dT%H:%M:%S%z')
                    message = post_data.get('message', '')
                    image_url = ''

                    attachments = post_data.get('attachments', {})
                    if 'data' in attachments and attachments['data']:
                        media = attachments['data'][0].get('media', {})
                        if 'image' in media and 'src' in media['image']:
                            image_url = media['image']['src']

                    search_result = SearchResultf(
                        text=message,
                        images=image_url,
                        title=extracted_title,
			 link=extracted_link,
			 description=extracted_description,
                        post_url=f"https://www.facebook.com/{post_id}",
                        time=created_time,
                        likes=post_data.get('likes', {}).get(
                            'summary', {}).get('total_count', 0),
                        comments=post_data.get('comments', {}).get(
                            'summary', {}).get('total_count', 0),
                        shares=post_data.get('shares', {}).get('count', 0)
                    )
                    extracted_results.append(search_result)
            except Exception as e:
                error_message = str(e)

        return render_template('facebook_results.html', extracted_results=extracted_results, error_message=error_message)

    return render_template('facebook_search_form.html')


@app.route('/results', methods=['GET'])
def show_results():
    # Récupérer les résultats depuis la base de données
    results = SearchResult.query.all()

    return render_template('results.html', results=results)


@app.route('/delete/<int:result_id>', methods=['POST'])
def delete_result(result_id):
    if result := SearchResult.query.get(result_id):
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
    with app.app_context():

        db.create_all()
    app.run(debug=DEBUG, host='localhost', port='5000')
