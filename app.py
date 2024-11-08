import os
from db import db

from flask import Flask
from routes.routes import create_routes

app = Flask(__name__)

db_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db')
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(db_directory, "todo.db")}'
# Désactiver le tracking des modifications pour éviter des warning SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de SQLAlchemy
db.init_app(app)

# Créer la base de données
with app.app_context():
    db.create_all()

create_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)