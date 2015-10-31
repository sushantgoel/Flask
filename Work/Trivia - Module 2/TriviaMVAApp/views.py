from flask import Flask, url_for, request, render_template
from TriviaMVAApp import app
from TriviaMVAApp.models.redisclient import Client



@app.route('/')
def hello():
    return '<a href="/create">Create a question</a>';


@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        #send the user the form
        return render_template('CreateQuestion.html')
    elif request.method == 'POST':
        #read the form data and save it
        title = request.form['title']
        question = request.form['question']
        answer = request.form['answer']

        client = Client()
        client.saveQuestion(title,question,answer)
        
        return render_template('CreatedQuestion.html', question = question)
    else:
        return '<h2>Invalid request</h2>'


@app.route('/question/<title>', methods=['GET','POST'])
def question(title):
    if request.method == 'GET':
        client = Client()
        question = client.getQuestion(title);
        
        return render_template('AnswerQuestions.html',question = question)
    elif request.method == 'POST':
        #User has attempted answer. Check if they're correct
        submittedAnswer = request.form['submittedAnswer']
        client = Client()
        answer = client.getAnswer(title)
        
        if submittedAnswer == answer:
            return render_template('Correct.html')
        else:
            return render_template('Incorrect.html',submittedAnswer = submittedAnswer,answer = answer)
    else:
        return '<h2>Invalid request</h2>'