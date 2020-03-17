from flask import Flask, render_template, request, url_for, redirect
from forms import RegistrationForm, LoginForm
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = '031f28bc85ee8031c0d726c354171021'

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title="Register", form=form,message="Register")

@app.route('/login',methods=["GET","POST"])
def login():
    form = LoginForm()
    return render_template('login.html',title="login", form=form,message='Login')
        

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.errorhandler(404)
def notFound(e):
    return "<h1>Error 404!</h1>"

if __name__ == '__main__':
    app.debug = True
    app.run()