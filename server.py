from flask import Flask, render_template
import requests


app = Flask('__name__')


response = requests.get('https://api.npoint.io/80456ff696773734af38')
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


@app.route('/post/<int:id_>')
def post(id_):
    return render_template('post.html', res=data, id=id_)


if __name__ == '__main__':
    app.run(debug=True)
