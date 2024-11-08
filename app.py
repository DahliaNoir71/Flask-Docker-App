from flask import Flask, request, jsonify, render_template
from db import db
from routes.routes import create_routes

app = Flask(__name__)

# Configuration de la base de données SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de SQLAlchemy
db.init_app(app)

# Créer la base de données
with app.app_context():
    db.create_all()

create_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
