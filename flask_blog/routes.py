from flask import  render_template, url_for, flash, redirect
from flask_blog.form import RegistrationForm, LoginForm
from flask_blog import app
from flask_blog.models import User, Post

posts = [
    {
        'author':'Jon Don',
        'title':'Good morning',
        'content':'Love story',
        'date_posted':'April 3, 2024'
    },
    {
        'author': 'Jane Aryer',
        'title': 'Good Night',
        'content': 'Love story',
        'date_posted': 'April 3, 2024'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html',posts = posts)


@app.route('/about')
def about():
    return render_template('about.html', title = "About")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
       flash(f"Account created for {form.username.data}.", 'success')
       return redirect(url_for('home'))
    return render_template('register.html', title = "Register", form = form)

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@blog.com' and form.password.data=='password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title = "Login", form = form)

