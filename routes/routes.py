from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.todo import Todo


def create_routes(app):
    @app.route('/todos', methods=['POST'])
    def add_todo():
        data = request.get_json()
        title = data.get('title')
        description = data.get('description', '')

        db = SQLAlchemy()
        new_todo = Todo(title=title, description=description)
        db.session.add(new_todo)
        db.session.commit()

        return jsonify(new_todo.to_dict()), 201

    @app.route('/todos', methods=['GET'])
    def get_todos():
        todos = Todo.query.all()
        return jsonify([todo.to_dict() for todo in todos])

    @app.route('/todos/<int:id>', methods=['DELETE'])
    def delete_todo(id):
        todo = Todo.query.get(id)
        if todo is None:
            return jsonify({"error": "Task not found"}), 404

        db = SQLAlchemy()
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"message": "Task deleted"}), 200