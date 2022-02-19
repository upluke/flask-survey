from copyreg import constructor
from select import select
from unicodedata import category
from surveys import surveys
from flask import Flask,request, redirect, render_template
app = Flask(__name__)
#  initialize a variable called responses to be an empty list. As people answer questions, you should store their answers in this list.
responses = []
current_idx=1
@app.route('/')
def home():
    return render_template('home.html',   survey_types=surveys.keys())

@app.route('/survey/<surveyname>')
def render_instruction(surveyname):
    selected_survey=surveys[surveyname]
    return render_template('instruction.html', surveyname=surveyname, survey=selected_survey)

 

@app.route('/survey_question/<surveyname>/<int:question_idx>')
def render_question( surveyname,question_idx):
    global current_idx
    print(current_idx, question_idx)
    print("args: ", len(request.args))

    if current_idx==question_idx:
      selected_question_obj=surveys[surveyname]
      question_idx=question_idx-1
      question=selected_question_obj.questions[question_idx].question
      choices=selected_question_obj.questions[question_idx].choices

      if len(request.args)>0 :
        option = request.args['option']
        responses.append(option)  

      if question_idx>1 and len(request.args)==0:
        print("here")
        current_idx=1 
        return redirect(f'/survey_question/{surveyname}/1')
      
              
      if len(request.args)>=len(selected_question_obj.questions):
        return redirect('/answer')
          
      
    
      question_idx=question_idx+1
      current_idx+=1

      return render_template('survey_question.html', question=question, choices=choices, surveyname=surveyname, question_idx=question_idx)
    else: 
      print("inininininni")
      
      return redirect(f'/survey_question/{surveyname}/{current_idx}')
     
@app.route('/answer' )
def handle_question_submit():
    return render_template('answer.html')

