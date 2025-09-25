from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

conn = psycopg2.connect(os.environ['DATABASE_URL'])

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/addToGuestbook', methods=['POST'])
def add_to_guestbook():
    name = request.form['name']
    message = request.form['message']
    print(name, message)
    with conn.cursor() as cur:
        cur.execute("INSERT INTO guestbook_entry (name, message) VALUES (%s, %s)", (name, message))
        conn.commit()
    json_entries = []
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, message, created_at FROM guestbook_entry ORDER BY created_at DESC")
        rows = cur.fetchall()
        for row in rows:
            json_entries.append({
                'id': row[0],
                'name': row[1],
                'message': row[2],
                'created_at': row[3].isoformat()
            })
    print(json_entries)
    return render_template('thank_you.html', entries=json_entries)

@app.route('/guestbook')
def view_guestbook():
    json_entries = []
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, message, created_at FROM guestbook_entry ORDER BY created_at DESC")
        rows = cur.fetchall()
        for row in rows:
            json_entries.append({
                'id': row[0],
                'name': row[1],
                'message': row[2],
                'created_at': row[3].isoformat()
            })
    return render_template('thank_you.html', entries=json_entries)