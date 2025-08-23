from flask import Flask, request, render_template_string, send_file
from PIL import Image, ImageDraw, ImageFont
import io
import random
import string
from time import sleep
app = Flask("myapp")
html_form = '''
<p style="color:red">{{message}}</p>
<form method="POST">
username:<input type="text" name="username"><br>
password:<input type="password" name="password"><br>
<input type="submit" value="login">
</form>
'''

def generate_captcha_text(length=5):
    return ''.join(random.choice(string.ascii_uppercase + string.digits , k = length))

def generate_captcha_image(text):
    img = Image.new('RGB', (150,60), color=(255,255,255))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    d.text((10,10), text, font=font, fill=(0,0,0))
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf


@app.route("/captcha.png")
def captcha_image(text):
    img = generate_captcha_image(text)
    return send_file(img, mimetype='image/png')



correct_username = "user1"
correct_password = "pass1"
attempts = 0
@app.route("/home/", methods=["GET", "POST"])
def login():
    global attempts
    attempts += 1
    sleep(1)
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if attempts > 3:
            message = "Captcha"
        elif username == correct_username and \
        password == correct_password:
            message =  "login success"
        else:
            message =  "login failed"    
    return render_template_string(html_form, message= message)
app.run(debug=True)