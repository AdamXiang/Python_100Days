from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length
from wtforms import StringField, PasswordField, SubmitField
from flask_bootstrap import Bootstrap5
import email_validator
import os

SECRET_KEY = os.urandom(32)

class MyForm(FlaskForm):
    email = StringField(label='email', validators=[Email(message=('That\'s not a valid email address.'))])
    pwd = PasswordField(label='password', validators=[Length(min=8, message='Field must be at least 8 characters long.')])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.email.data
        pwd = form.pwd.data
        if pwd == '12345678' and email == 'admin@email.com':
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    