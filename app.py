from flask import Flask,jsonify

app = Flask(__name__)

students = [
    {'id': 1, 'name': 'Alice', 'age': 20},
    {'id': 2, 'name': 'Bob', 'age': 20},
    {'id': 3, 'name': 'Charlie', 'age': 20}
]

@app.route('/student_list')
def students_list():
    return jsonify(students)
'''
@app.route('/student_list') : This line is a Flask route decorator. It associates the URL path /student_list with the function students_list. When a client makes an HTTP GET request to this URL, the students_list function will be executed.

def students_list() : This line defines a function named students_list. This function will handle the HTTP GET requests made to the /student_list route.

return jsonify(students) : This line returns a JSON response containing the list of students. The jsonify function is used to convert the students list (a Python list of dictionaries) into a JSON-formatted response, which is then sent back to the client. This allows clients to easily consume the data in a structured format.
'''

@app.route('/student_list/get/<int:id>')
def students_id(id):
    print(id)
    for student in students:
        if student['id'] == id:
            return jsonify(student)
    return jsonify({'error': 'Not Found'})
'''
1. @app.route('/student_list/get/<int:id>'): This is a decorator that associates the following function students_id with the specified URL route. The <int:id> part in the route indicates that the id parameter should be an integer.
2. def students_id(id): This function is defined to handle the HTTP GET request for the specified URL route. It takes an integer id as a parameter.
3. print(id): This line prints the value of the id parameter to the console for debugging purposes.
4. for student in students: This line starts a loop that iterates over each student in the students list.
5. if student['id'] == id: This line checks if the current student's id matches the provided id parameter.
6. return jsonify(student): If a matching student is found, this line returns a JSON response containing the student's details.
7. return jsonify({'error': 'Not Found'}): If no matching student is found, this line returns a JSON response with an error message indicating that the student was not found.
'''



if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )