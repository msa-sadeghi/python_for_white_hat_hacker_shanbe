from flask import Flask, request, render_template_string, send_file
from PIL import Image, ImageDraw, ImageFont
import io
import random
import string
from time import sleep
app = Flask("myapp")
html_form = '''
<p style="color:red">{{message}}</p>
{% if show_captcha %}

<img src="{{url_for('captcha_image', text='something')}}" alt="CAPTCHA">
<br>
captcha <input type="text" name="captcha">
<br>
{% endif %}

<form method="POST">
username:<input type="text" name="username"><br>
password:<input type="password" name="password"><br>
<input type="submit" value="login">
</form>
'''

def generate_captcha_text(length=5):
    return ''.join(random.choices(string.ascii_uppercase +\
                                   string.digits , k = length))

def generate_captcha_image(text):
    img = Image.new('RGB', (150,60), color=(255,255,255))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    d.text((10,10), text, font=font, fill=(0,0,0))
    # img = img.rotate(30, expand=1)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf


@app.route("/captcha.png")
def captcha_image():
    img = generate_captcha_image(captcha_text)
    return send_file(img, mimetype='image/png')


captcha_text = ""
correct_username = "user1"
correct_password = "pass1"
attempts = 0
@app.route("/home/", methods=["GET", "POST"])
def login():
    global attempts
    global captcha_text
    attempts += 1
    sleep(1)
    message = ""
    show_captcha = False
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if attempts > 3:
            show_captcha = True
            message = "Captcha"
            captcha_text = generate_captcha_text()
            
            user_captcha = request.form.get("captcha", "")
            print("captcha_text", captcha_text)
            print("user_captcha", user_captcha)
            if captcha_text == user_captcha:
                print("captcha ok")
        elif username == correct_username and \
        password == correct_password:
            message =  "login success"
        else:
            message =  "login failed"    
    return render_template_string(html_form, message= message, show_captcha=show_captcha)
app.run(debug=True)