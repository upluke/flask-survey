from surveys import surveys
from flask import Flask, render_template
app = Flask(__name__)
#  initialize a variable called responses to be an empty list. As people answer questions, you should store their answers in this list.
responses = []

print()

 

@app.route('/')
def home():
    return render_template('home.html',   survey_types=surveys.keys())


@app.route('/survey/satisfaction')
def handle_satisfaction_survey():
    return render_template('satisfaction_survey.html')

@app.route('/survey/personality')
def handle_personality_quiz():
    return render_template('personality_quiz.html')