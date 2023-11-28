from flask import Flask, render_template
import requests


app = Flask('__name__')


response = requests.get('https://api.npoint.io/e6d991e0a3c88e6184ba')
data = response.json()


@app.route('/')
def home():
    return render_template('index.html', res=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
