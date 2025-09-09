from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# ====> HTTP METHODS <====
    # GET --> READ DATA
    # POST --> CREATE DATA
    # PUT --> UPDATE DATA
    # DELETE --> DELETE DATA

students = [
    {"id": 1, "name": "Aman", "age": 20},
    {"id": 2, "name": "Babit", "age": 22},
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify(new_student), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    updated_data = request.get_json()
    for student in students:
        if student['id'] == student_id:
            student.update(updated_data)
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            return jsonify({"message": "Student deleted"}), 200
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__': 
    app.run(debug=True)