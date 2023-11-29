from flask import Flask, render_template, request
import requests
import smtplib


MY_EMAIL = 'YOUR OWN EMAIL ADDRESS'
MY_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"
TO_EMAIL = "YOUR OWN EMAIL ADDRESS"

app = Flask('__name__')


response = requests.get('https://api.npoint.io/80456ff696773734af38')
data = response.json()


@app.route('/')
def home():
    return render_template('index.html', res=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        message = request.form['message']
        with smtplib.SMTP('SMTP.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL,
                                msg=f'Subject:this is new req \n\n name: {name}\n email: {email}\n number: {number}\n message: {message}')
        return render_template('contact.html', msg=True)
    else:
        return render_template('contact.html', msg=False)


@app.route('/post/<int:id_>')
def post(id_):
    return render_template('post.html', res=data, id=id_)


if __name__ == '__main__':
    app.run(debug=True)
