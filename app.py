from flask import Flask, render_template,request,redirect,session,url_for,flash
from functools import wraps

app = Flask(__name__)

app.secret_key = "im batman"  #encryption key to access session data on server side


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged in' in session:
            return f(*args, **kwargs)
        else:
            flash('Log in first')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    return render_template("index.html")

@app.route('/welcome')

def welcome():
    return render_template("welcome.html")

@app.route('/login',methods = ['GET','POST'])
def login():
    error = None
    if request.method =='POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin' :
            error = 'Invalid credentials. Please enter correct details'
            return render_template('login.html', error=error)

        else:
            session['logged in'] = True
            flash("you logged in")
            return redirect(url_for('home'))
    return render_template('login.html',error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged in', None) #pop out true replacing it with None
    flash("you logged out")
    return redirect(url_for('welcome')) #redirect to login page


if __name__ == '__main__':
    app.run(debug=True)