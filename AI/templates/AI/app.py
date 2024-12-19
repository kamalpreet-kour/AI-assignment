
from flask import Flask, render_template, request, redirect, url_for
from models.color_logic import get_color_question, check_answer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answer = request.form['color']
        correct, feedback = check_answer(user_answer)
        return render_template('results.html', feedback=feedback, correct=correct)
    
    question = get_color_question()
    return render_template('quiz.html', question=question)

if __name__ == '__main__':
    app.run(debug=True)
        