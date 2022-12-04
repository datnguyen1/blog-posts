from flask import *
import sqlite3

app = Flask(__name__)

#function/shortcut to connect to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#the home page basically
@app.route("/")
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template("/index.html", posts=posts)

#this run when a new post is created
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

#this function runs when edit button is pressed
@app.route("/edit/<int:id>", methods = ('GET', 'POST'))
def edit(id):
    db = sqlite3.connect('database.db')
    cursor = db.execute('SELECT * FROM posts WHERE id = ?', (id,))
    row = cursor.fetchone()
    title = row[2]
    content = row[3]
    db.close()
    return render_template("/edit.html" , title=title, content=content, id=id)

#this function is to process the data put in to edit a post
@app.route("/handle_data_edit/<int:id>/", methods = ('GET','POST'))
def handle_data_edit(id: int):
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash("Title is required!")
        elif not content:
            flash("Content is required!")
        else:
            conn = get_db_connection()
            sql = ''' UPDATE posts
              SET title = ? ,
                  content = ? 
              WHERE id = ?'''   
            cur = conn.cursor()
            data = [
                (title),
                (content),
                (id)
            ]
            cur.execute(sql, data)
            conn.commit()

            return redirect(url_for('index'))

@app.route("/delete/<int:id>/")
def delete(id: int):
    conn = get_db_connection()
    sql = ''' DELETE from posts WHERE id = ?'''   
    cur = conn.cursor()
    new_id = id
    cur.execute(sql, (new_id,))
    conn.commit()

    return redirect(url_for('index'))

