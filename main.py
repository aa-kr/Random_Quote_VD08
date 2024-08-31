#импортируем Flask и библиотеку Request
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        data = response.json()
        quote = data['content']
        author = data['author']
    else:
        quote = "Не удалось получить цитату. Попробуйте позже."
        author = ""

    return render_template('index.html', quote=quote, author=author)



if __name__ == '__main__':
   app.run(debug=True)