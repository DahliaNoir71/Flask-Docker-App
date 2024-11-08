from flask import request, jsonify, render_template
from db import db
from models.todo import Todo


def create_display_routes(app):
    # Route pour afficher la liste des todos
    @app.route('/')
    @app.route('/todos')
    def get_todos():
        todos = Todo.query.all()
        return render_template('todos_list.html', todos=todos)

    @app.route('/add_todo')
    def display_add_todo():
        return render_template('add_todo.html')

    @app.route('/todos/<int:todo_id>/edit')
    def display_edit_todo(id):
        todo = Todo.query.get(id)
        return render_template('edit_todo.html', todo=todo)


def create_api_routes(app):
    # Route pour ajouter un todo (POST)
    @app.route('/add_todo', methods=['POST'])
    def add_todo():
        data = request.get_json()
        title = data.get('title')
        description = data.get('description', '')

        new_todo = Todo(title=title, description=description)
        db.session.add(new_todo)
        db.session.commit()

        return jsonify(new_todo.to_dict()), 201

    # Route pour modifier un todo (PUT)
    @app.route('/todos/<int:id>', methods=['PUT'])
    def update_todo(id):
        todo = Todo.query.get(id)
        if not todo:
            return jsonify({"error": "Todo not found"}), 404

        data = request.get_json()
        todo.title = data.get('title', todo.title)
        todo.description = data.get('description', todo.description)

        db.session.commit()
        return jsonify(todo.to_dict())

    # Route pour supprimer un todo (DELETE)
    @app.route('/todos/<int:id>', methods=['DELETE'])
    def delete_todo(id):
        todo = Todo.query.get(id)
        if not todo:
            return jsonify({"error": "Todo not found"}), 404

        db.session.delete(todo)
        db.session.commit()
        return jsonify({"message": "Todo deleted"}), 200


def create_routes(app):
    create_display_routes(app)
    create_api_routes(app)