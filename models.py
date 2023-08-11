from fabfile import db  # Assurez-vous d'importer correctement votre instance de la base de données
import sqlalchemy as sa

from fabfile import db  # Import your database instance here
import sqlalchemy as sa

class SearchResult(db.Model):
    __tablename__ = 'search_result'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(575))
    link = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(555))

    def __init__(self, title, link, description, image_url):
        self.title = title
        self.link = link
        self.description = description
        self.image_url = image_url







class SearchResultf(db.Model):
    __tablename__ = 'search_resultf'
    # Other column definitions

    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(2000))  # Spécifiez la longueur ici, par exemple 255
    images = db.Column(db.String(2000))
    post_url = db.Column(db.String(2000))
    time = db.Column(db.String(2000))
    likes = db.Column(db.Integer)
    comments = db.Column(db.Integer)
    shares = db.Column(db.Integer)

    def __init__(self, text, images, post_url, time, likes, comments, shares):
        self.text = text
        self.images = images
        self.post_url = post_url
        self.time = time
        self.likes = likes
        self.comments = comments
        self.shares = shares
