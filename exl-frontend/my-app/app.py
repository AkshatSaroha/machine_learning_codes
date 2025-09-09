from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def employee_form():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        salary = request.form['salary']
        
        print("Name:", name)
        print("Age:", department)
        print("Position:", salary)
        return f"Form submitted successfully! Name: {name}, Age: {department}, Position: {salary}"
    return render_template('form.html')
if __name__ == '__main__':
    app.run(debug=True)