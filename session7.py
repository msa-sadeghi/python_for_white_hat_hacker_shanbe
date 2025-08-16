from flask import Flask, request, render_template_string
app = Flask("myapp")
html_form = '''
<form method="POST">
username:<input type="text" name="username"><br>
password:<input type="password" name="password"><br>
<input type="submit" value="login">
</form>
'''
correct_username = "user1"
correct_password = "pass1"
@app.route("/home/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == correct_username and \
        password == correct_password:
            return "login success"
        else:
            return "login failed"    
    return render_template_string(html_form)
app.run(debug=True)