from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from routes.routes import create_routes

app = Flask(__name__)

# Configuration de la base de données SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialiser la base de données avec l'application Flask
db = SQLAlchemy(app)


# Créer la base de données
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
