from copyreg import constructor
from select import select
from unicodedata import category
from surveys import Question, surveys
from flask import Flask, redirect, render_template
app = Flask(__name__)
#  initialize a variable called responses to be an empty list. As people answer questions, you should store their answers in this list.
responses = []

print()
 
 

@app.route('/')
def home():
    return render_template('home.html',   survey_types=surveys.keys())

@app.route('/survey/<surveyname>')
def render_instruction(surveyname):
    selected_survey=surveys[surveyname]
    return render_template('instruction.html', surveyname=surveyname, survey=selected_survey)

 

@app.route('/survey_question/<surveyname>/<int:question_idx>')
def render_question(surveyname,question_idx):
    question=surveys[surveyname].questions[question_idx].question
    return render_template('survey_question.html', question=question)

