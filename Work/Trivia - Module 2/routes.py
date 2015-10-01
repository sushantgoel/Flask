from flask import Flask, url_for
from app import app

#@app.route('/')
#def hello():
#    url = url_for('about');
#    link = '<a href="' + url + '">About us!</a>';
#    return link;

#@app.route('/about')
#def about():
#    return 'We are the knights who say Ni!!';

@app.route('/question/<title>')
def question(title):
    message = '<h2> You said ' + title + '</h2>';
    return message;

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

@app.route('/Create')
def create():
    return '<h2>This is the create page</h2>'