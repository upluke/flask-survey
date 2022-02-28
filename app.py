from copyreg import constructor
from select import select
from unicodedata import category
from surveys import surveys
from flask import Flask,request, redirect, render_template, flash, session
app = Flask(__name__)
app.config['SECRET_KEY'] = "dumbonudumb"
#  initialize a variable called responses to be an empty list. As people answer questions, you should store their answers in this list.
# responses = []
current_idx=0
RESPONSES_KEY = "responses"


@app.route('/')
def home():
    session[RESPONSES_KEY]=[]
    return render_template('home.html',   survey_types=surveys.keys())

@app.route('/survey/<surveyname>')
def render_instruction(surveyname):
    selected_survey=surveys[surveyname]
    return render_template('instruction.html', surveyname=surveyname, survey=selected_survey)

 

@app.route('/survey_question/<surveyname>/<int:question_idx>')
def render_question( surveyname,question_idx):
    global current_idx
    global responses 
 

    selected_question_obj=surveys[surveyname]
    question_idx=question_idx-1

    if question_idx<len(selected_question_obj.questions):
        question=selected_question_obj.questions[question_idx].question
        choices=selected_question_obj.questions[question_idx].choices
 

    if current_idx>=len(selected_question_obj.questions):
        return redirect('/answer') 
    elif current_idx==question_idx and len(request.args) or question_idx==0 and current_idx==0:
      if len(request.args):
        option = request.args['option']
        responses= session[RESPONSES_KEY]
        print(responses, ")))))")
        responses.append(option)
      current_idx+=1
      question_idx=question_idx+1
 
      return render_template('survey_question.html', question=question, choices=choices, surveyname=surveyname, question_idx=question_idx)
    else: 
      
      if current_idx<len(selected_question_obj.questions):
        current_idx-=1
        # responses=responses[:current_idx+1] #without gloable: UnboundLocalError: local variable 'responses' referenced before assignment
        flash("Please don't skip questions!")
        return redirect(f'/survey_question/{surveyname}/{current_idx+1}')
     
@app.route('/answer' )
def handle_question_submit():
    return render_template('answer.html')

