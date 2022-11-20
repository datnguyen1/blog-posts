from flask import *
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template("/index.html", posts=posts)

@app.route("/handle_data", methods = ('GET', 'POST'))
def handle_data():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash("Title is required!")
        elif not content:
            flash("Content is required!")
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?,?)',
                        (title, content))
            posts = conn.execute('SELECT * FROM posts').fetchall()
            conn.commit()
            conn.close()
            return render_template("/index.html", posts=posts)