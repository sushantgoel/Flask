"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from TriviaMVAApp import app

if __name__ == '__main__':
    import os    
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    #app.run(debug=True)
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
