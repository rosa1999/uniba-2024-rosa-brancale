# importazione librerie
from flask import Flask, request, jsonify
from flask_cors import CORS

# creazione applicazione
app = Flask(__name__)
CORS(app)


# settaggio memoria
tasks = []
task_id_counter = 1


# definizione della root
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Task API"


# sezione task
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


# creazione task
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    new_task = request.json
    new_task['id'] = task_id_counter
    tasks.append(new_task)
    task_id_counter += 1
    return jsonify(new_task), 201


# aggiornamento di un task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = next((task for task in tasks if task['id'] == id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task.update(request.json)
    return jsonify(task)


# eliminazione di un task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return '', 204

# avvio dell'applicazione
if __name__ == '__main__':
    app.run(debug=True)

# app.run(host='0.0.0.0', port=5000,debug=True) # per renderlo accessibile a tutti gli indirizzi