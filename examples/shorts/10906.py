from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to simulate a database
tasks = [
    {'id': 1, 'title': 'Learn Python', 'done': False},
    {'id': 2, 'title': 'Build a REST API', 'done': False}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Return all tasks as JSON
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Return a specific task by ID
    task = next((task for task in tasks if task['id'] == task_id), None)
    return jsonify(task) if task else ('', 404)

@app.route('/tasks', methods=['POST'])
def add_task():
    # Add a new task from JSON data
    new_task = request.get_json()
    new_task['id'] = len(tasks) + 1
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # Update a specific task
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        updates = request.get_json()
        task.update(updates)
        return jsonify(task)
    return ('', 404)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Delete a specific task
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)