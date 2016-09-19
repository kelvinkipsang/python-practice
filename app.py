from flask import Flask, render_template,request,redirect,session,url_for,flash, g
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import sqlite3




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db' #database directory
app.secret_key = "im batman"  #encryption key to access session data on server side

db=SQLAlchemy(app)


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
    posts=[]
    try:                     #g is a object specific to flask that stores temporary object during a request like db connection or currently logged in user
        g.db = connect_db()  # establish connection using the g object
        cur = g.db.execute('select * from posts') #value of g is reset after each request# query db/ fetch data

        for row in cur.fetchall():
            posts.append(dict(title=row[0], description=row[1]) )
        g.db.close()
    except sqlite3.OperationalError:
        flash("you shall not pass(db not there)")
    return render_template("index.html", posts=posts)


   # posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]      #add data to dictionary-fetchall return a list of tuples of each row
   # g.db.close()                                                                    #close db
    #return render_template("index.html", posts = posts)             #pass posts data fetched from db

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
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged in', None) #pop out true replacing it with None
    flash("you logged out")
    return redirect(url_for('welcome')) #redirect to login page

# funtion that creates a db object that interacts with our db or
# in simple terms connect to our db
def connect_db():
    return sqlite3.connect(app.database)


if __name__ == '__main__':
    app.run(debug=True)