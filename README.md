# Votre Application de Recherche

Bienvenue dans votre application de recherche personnalisée. Cette application vous permet de rechercher des informations sur diverses plateformes en ligne.

## Fonctionnalités

- Recherche Google : Effectuez des recherches sur Google en entrant un secteur d'activité et une localisation.
- Recherche Facebook : Recherchez des publications sur Facebook en utilisant un secteur d'activité et une localisation.

## Installation

1. Clonez ce dépôt vers votre machine locale.
 ```sh
   git clone https://github.com/yourusername/your-search-app.git
   ```
2. Accéder au dossier de l'application
`cd search_app`
3. Créer un environnement virtuel(optionel)

```sh


virtualenv venv
source venv/bin/activate

```
4. Installez les dépendances en exécutant :

 `pip install -r requirements.txt`



5. Configurez la Base de Données MySQL :

Assurez-vous d'avoir MySQL Server installé et en cours d'exécution sur votre machine.
Dans fabfile.py, configurez les paramètres de connexion à la base de données.

6. Effectuez les migrations de la base de données :

```sh
Copy code
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

```

7. Exécutez l'application : 


`python app.py`

## Utilisation

1. Accédez à l'application en visitant http://localhost:5000 dans votre navigateur.
2. Utilisez les liens de navigation pour effectuer des recherches sur différentes plateformes.

## Auteur

Ruffin HOUNSOUNNON

## Licence

Ce projet est sous licence [MIT](LICENSE).

---

**Note :** Assurez-vous d'avoir une connexion Internet active lors de l'utilisation de l'application, car elle dépend des services en ligne pour les recherches.
