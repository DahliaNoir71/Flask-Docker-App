from flask import request, jsonify, render_template
from models.todo import Todo
from app import db

def create_display_routes(app):
    """
    This function creates routes for displaying a list of todos.

    Parameters:
    app (Flask): The Flask application instance.

    Returns:
    None. This function registers routes within the Flask application.
    """

    @app.route('/', methods=['GET'])
    @app.route('/todos', methods=['GET'])
    def get_todos():
        """
        This route retrieves all todos from the database and renders them in a template.

        Parameters:
        None. This function uses the Flask request context.

        Returns:
        render_template: A rendered HTML template with a list of todos.
        """
        todos = Todo.query.all()
        return render_template('todos_list.html', todos=todos)


def create_crud_routes(app):
    """
    This function creates routes for performing CRUD operations on a list of todos.

    Parameters:
    app (Flask): The Flask application instance.

    Returns:
    None. This function registers routes within the Flask application.
    """

    @app.route('/todos', methods=['POST'])
    def add_todo():
        """
        This route adds a new todo to the database.

        Parameters:
        None. This function uses the Flask request context to get JSON data.

        Returns:
        jsonify: A JSON response containing the added todo and a status code of 201 (Created).
        """
        data = request.get_json()
        title = data.get('title')
        description = data.get('description', '')

        new_todo = Todo(title=title, description=description)
        db.session.add(new_todo)
        db.session.commit()

        return jsonify(new_todo.to_dict()), 201

    @app.route('/todos/<int:id>', methods=['DELETE'])
    def delete_todo(id):
        """
        This route deletes a todo from the database.

        Parameters:
        id (int): The unique identifier of the todo to delete.

        Returns:
        jsonify: A JSON response with a success message and a status code of 200 (OK) if the todo is found and deleted.
                 A JSON response with an error message and a status code of 404 (Not Found) if the todo is not found.
        """
        todo = Todo.query.get(id)
        if todo is None:
            return jsonify({"error": "Task not found"}), 404

        db.session.delete(todo)
        db.session.commit()
        return jsonify({"message": "Task deleted"}), 200


def create_routes(app):
    """
    This function creates routes for displaying and performing CRUD operations on a list of todos.

    Parameters:
    app (Flask): The Flask application instance. This instance is used to register routes within the Flask application.

    Returns:
    None. This function does not return any value. It registers routes within the Flask application.
    """
    create_display_routes(app)
    create_crud_routes(app)

# Import and call the create_routes function from the app module
from app import app
create_routes(app)