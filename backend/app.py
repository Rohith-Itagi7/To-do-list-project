from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

# ✅ CORS setup to allow frontend (React) access
CORS(app, resources={r"/todos/*": {"origins": "*"}}, methods=["GET", "POST", "DELETE", "PATCH", "OPTIONS"])


# SQLite DB configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

# Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250))
    due_time = db.Column(db.String(100))
    reminder = db.Column(db.Boolean, default=False)
    completed = db.Column(db.Boolean, default=False)

# Initialize DB inside app context
with app.app_context():
    db.create_all()

# GET all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "due_time": t.due_time,
            "reminder": t.reminder,
            "completed": t.completed
        } for t in todos
    ])

# POST new todo
@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    todo = Todo(
        title=data['title'],
        description=data.get('description', ''),
        due_time=data.get('due_time'),
        reminder=data.get('reminder', False)
    )
    db.session.add(todo)
    db.session.commit()
    return jsonify({
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "due_time": todo.due_time,
        "reminder": todo.reminder,
        "completed": todo.completed
    }), 201

# DELETE a todo (with OPTIONS support)
@app.route('/todos/<int:todo_id>', methods=['DELETE', 'OPTIONS'])
def delete_todo(todo_id):
    if request.method == 'OPTIONS':
        return jsonify({"status": "OK"}), 200

    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo deleted"}), 200

# PATCH: Toggle completed status (with OPTIONS support)
@app.route('/todos/<int:todo_id>/toggle', methods=['PATCH', 'OPTIONS'])
def toggle_complete(todo_id):
    if request.method == 'OPTIONS':
        return jsonify({"status": "OK"}), 200

    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    todo.completed = not todo.completed
    db.session.commit()
    return jsonify({
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "due_time": todo.due_time,
        "reminder": todo.reminder,
        "completed": todo.completed
    }), 200

@app.route('/')
def home():
    return "Flask Backend is Running 🚀"
# Start server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
