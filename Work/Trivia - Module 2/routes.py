from flask import Flask, url_for, request, render_template
from app import app

@app.route('/')
def hello():
    return '''<html>
                <head>
                    <title>Hello, world</title>
                </head>
                <body>
                    <h1>Hello, world</h1>
                </body>
            </html>''';


@app.route('/Create', methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        #send the user the form
        return render_template('CreateQuestion.html')
    elif request.method == 'POST':
        #read the form data and save it
        title = request.form['title']
        question = request.form['question']
        answer = request.form['answer']

        #Store data in database
        return render_template('CreatedQuestion.html', question = question)
    else:
        return '<h2>Invalid request</h2>'


@app.route('/question/<title>', methods=['GET','POST'])
def question(title):
    if request.method == 'GET':
        #send the user the form
        question = 'Question here.'
        #Read question from Database
        return render_template('AnswerQuestion.html',question = question)
    elif request.method == 'POST':
        #User has attempted answer. Check if they're correct
        submittedAnswer = request.form['submittedAnswer']
        #Read answer from DB
        answer = 'Answer'
        if submittedAnswer == answer:
            return render_template('Correct.html')
        else:
            return render_template('Incorrect.html',submittedAnswer = submittedAnswer,answer=answer)
    else:
        return '<h2>Invalid request</h2>'