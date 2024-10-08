from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SECRET_KEY'] = 'incorrectyoualreadyknow'

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False)

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
min=4, max=20)], render_kw={"placeholder":"Username"})
    password = PasswordField(validators=[InputRequired(), Length(
min=4, max=20)], render_kw={"placeholder":"Password"})

submit = SubmitField("Register")

def validate_username(self, username):
    existing_user_username = User.query.filterby(username=username.data).first()
    if existing_user_username:
        raise ValidationError(
        "This username already exists, chagua yengine Tafadhali"
        )
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
min=4, max=20)], render_kw={"placeholder":"Username"})
    password = PasswordField(validators=[InputRequired(), Length(
min=4, max=20)], render_kw={"placeholder":"Password"})
submit = SubmitField("login")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
