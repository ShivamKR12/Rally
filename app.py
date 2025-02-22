from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Rally Game</title>
        </head>
        <body>
            <h1>Welcome to the Rally Game!</h1>
            <p>Use the links below to navigate:</p>
            <ul>
                <li><a href="/start">Start Game</a></li>
                <li><a href="/multiplayer">Multiplayer</a></li>
                <li><a href="/achievements">Achievements</a></li>
            </ul>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
