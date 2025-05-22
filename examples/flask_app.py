'''
Ten kod uruchamia prosty serwer Flask, który zwraca komunikat "Hello from Flask!" pod adresem /.
'''
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello from Flask!"


if __name__ == '__main__':
    app.run(debug=True)
