```
import sqlite3, datetime

from flask import Flask, render_template, request, url_for, redirect, make_response, flash, get_flashed_messages
from my_library import database_worker, encrypt_password, check_password

app = Flask(__name__)

db = database_worker('social_net.db')

app.secret_key = 'app'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 3600 # 1 hour

# Create a datetime object representing today's date
today = datetime.datetime.today()
# Format the date as a string
date_string = today.strftime("%Y/%m/%d")
# Print the formatted date string
print("Today's date:", date_string)

# CREATE TABLES DATABASE
def create_db():
    db = database_worker("social_net.db")
    query_user = """Create table if not exists users(
    id INTEGER PRIMARY KEY,
    username VARCHAR (150),
    password TEXT
    )
    """


    query_posts = """Create table if not exists forum_posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_text TEXT NOT NULL,
    created_at TEXT NOT NULL,
    book TEXT NOT NULL,
    user_id TEXT NOT NULL,
    post_topic TEXT NOT NULL,
    username TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
    )
    """


    db.run_save(query_user)
    db.run_save(query_posts)
    db.close()

#ERROR PAGE FOR REGISTRATION
@app.route('/errorregister')
def errorregister():  # put application's code here
    print("error")
    return render_template('errorregister.html')


#ERROR PAGE FOR POST
@app.route('/errorpost')
def errorpost():  # put application's code here
    print("error")
    return render_template('errorpost.html')

#ERROR PAGE FOR LOGIN
@app.route('/errorlogin')
def errorlogin():  # put application's code here
    print("error")
    return render_template('errorlogin.html')

#LOGIN SCREEN
@app.route('/', methods=['GET', 'POST'])
def welcome():  # put application's code here
    print("here")
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['password']
        if len(username) > 0 and len(passwd) > 0:
            db = database_worker('social_net.db')
            user = db.search(f"SELECT * from users where username='{username}'")
            print("hello", user)
            if user:
                user = user[0]  # search returns a list, so here I select one
                id= user[0]
                username = user[1]
                hash = user[2]
                if check_password(hashed_password=hash, user_password=passwd):
                    print("sup")
                    # create cookie with logged in user
                    # 1-create the response webpage (redner template)
                    resp = make_response(render_template('main.html'))
                    resp.set_cookie('user_id', f"{id}")
                    print("password is correct")
                    return resp
                else:
                    return redirect(url_for('errorlogin'))

    return render_template('bookback.html')


# REGISTRATION PAGE
@app.route('/register', methods=['POST', 'GET'])
def register():  # put application's code here
    message = ""
    if request.method == 'POST':  # register button pressed®
        db = database_worker('social_net.db')
        username = request.form['username']
        passwd = request.form['passwd']
        passwd_check = request.form['passwd_check']

        print("variables received.R")
        if passwd_check != passwd or len(passwd_check) < 8:
            return redirect(url_for('errorregister'))
        else:
            db = database_worker('social_net.db')
            existing_user = db.search(f"SELECT * from users where username='{username}'")
            if existing_user:
                return redirect(url_for('errorregister'))
            else:
                new_user = f"INSERT into users (username, password) values ('{username}', '{encrypt_password(passwd)}')"
                db.run_save(new_user)
                db.close()
                flash("Registration successful!")
                return redirect(url_for('welcome'))

    return render_template("register.html", messages=message)

#MAIN PAGE
@app.route('/main')
def lobby():
    return render_template("main.html")

#POST DISPLAY OF IN PRAISE OF SHADOWS
@app.route('/postsdisplay')
def display():

    db = database_worker('social_net.db')
    # Retrieve all posts from the forum
    query_posts = "SELECT username, created_at, post_topic, book, post_text FROM forum_posts where book = 'In Praise of Shadows'"
    posts = db.search(query=query_posts)
    print(posts)

    return render_template('displaypost.html', forum_posts=posts)

#POST DISPLAY OF THE AWAKENING
@app.route('/postsdisplay2')
def display2():
    db = database_worker('social_net.db')
    # Retrieve all posts from the forum
    query_posts = "SELECT username, created_at, post_topic, book, post_text FROM forum_posts where book = 'The Awakening'"
    posts = db.search(query=query_posts)
    print(posts)

    return render_template('displaypost2.html', forum_posts=posts)

#POST DISPLAY OF ORYX AND CRAKE
@app.route('/postsdisplay3')
def display3():
    db = database_worker('social_net.db')
    #Retrieve all posts from the forum
    query_posts = "SELECT username, created_at, post_topic, book, post_text FROM forum_posts where book = 'Oryx and Crake'"
    posts = db.search(query=query_posts)
    print(posts)

    return render_template('displaypost3.html', forum_posts=posts)

#POST DISPLAY OF EARNEST
@app.route('/postsdisplay4')
def display4():
    db = database_worker('social_net.db')
    #Retrieve all posts from the forum
    query_posts = "SELECT username, created_at, post_topic, book, post_text FROM forum_posts where book = 'The Importance of being earnest'"
    posts = db.search(query=query_posts)
    print(posts)
    
    return render_template('displaypost4.html', forum_posts=posts)


#CREATE A NEW POST PAGE
@app.route('/new_post', methods=['POST', 'GET'])
def add_topic():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        book = request.form['books']
        post_topic = request.form['post_topic']
        post_text = request.form['post_text']

        # Create a datetime object representing today's date
        today = datetime.datetime.today()
        # Format the date as a string
        created_at = today.strftime("%Y/%m/%d")

        if request.cookies.get('user_id'):
            if len(username) > 0 and len(post_topic) > 0 and len(post_text) > 0:
                print("The cookie was found in creating posts")
                user_id = request.cookies.get('user_id')
                print('cookie requested, ', user_id)
                # DO SOMETHING WITH THE POSTS
                db = database_worker("social_net.db")
                new_post = f"INSERT into forum_posts (username, post_topic, post_text, user_id, created_at, book) values ('{username}','{post_topic}','{post_text}','{user_id}', '{created_at}', '{book}')"
                db.run_save(new_post)
                db.close()
            else:
                return redirect(url_for('errorpost'))

    return render_template('new_post_page.html')

#LEADERBOARD/STATS
@app.route('/profile')
def profile():

    id = request.cookies.get('user_id')
    db = database_worker('social_net.db')

    #GET USERNAME
    query_username= f"SELECT username FROM forum_posts where user_id = '{id}'"
    user = db.search(query=query_username)
    print(user)

    #GET NUMBER OF POSTS
    query_noposts= f"SELECT username, COUNT(*) as num_posts FROM forum_posts where user_id = '{id}'"
    noposts = db.search(query=query_noposts)
    print(noposts)

    #GET MOST COMMENTED BOOK
    query_book= f"SELECT book, COUNT(*) as num_comments FROM forum_posts GROUP BY book ORDER BY num_comments DESC LIMIT 1"
    book = db.search(query=query_book)
    print(book)

    return render_template('profile.html', user=user, noposts=noposts, book=book)

#PROFILE PAGE
@app.route('/myposts')
def myposts():

    id = request.cookies.get('user_id')
    db = database_worker('social_net.db')
    query_posts= f"SELECT username, created_at, post_topic, book, post_text FROM forum_posts where user_id = '{id}'"
    posts = db.search(query=query_posts)
    print(posts)

    return render_template('myposts.html', forum_posts=posts)

#STATS
@app.route('/stats')
def stats():
    db = database_worker('social_net.db')
    query_posts = "SELECT username, COUNT(*) as num_posts FROM forum_posts GROUP BY user_id ORDER BY num_posts DESC LIMIT 3"
    top_users = db.search(query=query_posts)
    print(top_users)
    return render_template('stats.html', top_users=top_users)
  
#CREATE DATABASE
create_db()
print("creating database")

#RUN PROGRAM
if __name__ == '__main__':
    app.run()


```.py
