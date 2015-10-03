from flask import Flask, url_for, request, render_template
from app import app
import redis

#connect to Redis
r = redis.StrictRedis('localhost',port=6379,db=0,charset="utf-8",decode_responses=True)

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

        #Store data in database
        #Key name will be the title they type in :question
        r.set(title + ':question', question)
        r.set(title + ':answer',answer)
        return render_template('CreatedQuestion.html', question = question)
    else:
        return '<h2>Invalid request</h2>'


@app.route('/question/<title>', methods=['GET','POST'])
def question(title):
    if request.method == 'GET':
        #send the user the form        
        #Read question from Database
        question = r.get(title+':question')
        return render_template('AnswerQuestions.html',question = question)
    elif request.method == 'POST':
        #User has attempted answer. Check if they're correct
        submittedAnswer = request.form['submittedAnswer']
        #Read answer from DB
        answer = r.get(title + ':answer')
        if submittedAnswer == answer:
            return render_template('Correct.html')
        else:
            return render_template('Incorrect.html',submittedAnswer = submittedAnswer,answer = answer)
    else:
        return '<h2>Invalid request</h2>'