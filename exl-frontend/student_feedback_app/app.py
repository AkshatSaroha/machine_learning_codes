from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        feedback = request.form['feedback']

        print("Name:", name)
        print("Course:", course)
        print("Feedback:", feedback)
        return f"Thank you for your feedback, {name}!"
    return render_template('feedback_form.html')

if __name__ == '__main__':
    app.run(debug=True)