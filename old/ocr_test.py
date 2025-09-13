# https://sourceforge.net/projects/tesseract-ocr.mirror/
# pip install pytesseract

from PIL import Image
import pytesseract
from io import BytesIO
import requests

def solve_captcha():
    r = requests.get("http://127.0.0.1:5000/captcha.png")
    img = Image.open(BytesIO(r.content))
    text = pytesseract.image_to_string(img)
    return text

print(solve_captcha())
