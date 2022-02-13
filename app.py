from surveys import surveys
from flask import Flask, render_template
app = Flask(__name__)
#  initialize a variable called responses to be an empty list. As people answer questions, you should store their answers in this list.
responses = []

print()

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# @app.route('/')
# def home():
#     return render_template('home.html',   survey_types=surveys.keys())


# @app.route('survey/satisfaction')
# def handle_satisfaction_survey():
#     return render_template('satisfaction_survey')
