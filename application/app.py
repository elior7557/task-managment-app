from flask import Flask, request, render_template, jsonify, make_response
import mongo


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Return all the tasks from the data base
@app.route('/api/tasks', methods=['GET'])
def tasks_get():
    tasks = mongo.get_Tasks()
    print(type(tasks))
    return jsonify(tasks)

# updates a task based on an id
@app.route('/api/tasks', methods=['POST'])
def tasks_post():
    data = request.get_json()
    print(f"data recived in response is: {data}")
    mongo.add_task(data)
    # Do something with the data, such as saving it to a database
    response = jsonify({'status':'success'})
    response.status_code = 201
    return response

# Deletes task on given ID
@app.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task_route(task_id):
    print(task_id)
    result = mongo.delete_task(task_id)
    if result == "Error: Task not found":
        return result, 404
    elif result == "Error: Invalid task id":
        return result, 400
    else:
        return result, 200


@app.route('/api/health', methods=['GET'])
def test():
    return 'ok'


# Gets id of a task and changes the information in the data base
@app.route('/api/tasks/<int:id>', methods=['PUT'])
def tasks_id(id):
    return 'PUT /api/tasks/<id> not implemented'

# Return all tasks with certein status
@app.route('/api/tasks/{status}', methods=['GET'])
def tasks_status(status):
    return 'GET /api/tasks/{status} not implemented'


if __name__ == '__main__':
    app.run(debug=True)