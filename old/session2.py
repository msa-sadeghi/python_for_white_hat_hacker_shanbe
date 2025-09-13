# from fpdf import FPDF

# report = FPDF()

# report.add_page()
# report.set_font("arial", size=14)

# password = input("enter the password: ")
# report.cell(200, 10, txt="english", ln=True)
# report.cell(200, 10, txt= password, ln=True)

# report.output("password_report.pdf")

# pip install cryptography
# from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# print(key)

# key = b'2gdQ32p397cgJGJALeV8zBOXLP-Sw_cMbS7mjMoc2as='

# f = Fernet(key)

# pw = input("enter the password: ")

# ramz = f.encrypt(pw.encode())

# with open("secret.txt", "wb") as my_file:
#     my_file.write(ramz)
# asli = f.decrypt(ramz)
# print(ramz)
# print(asli)

import requests #pip install requests
import hashlib


pw = input("enter the password: ")
hashed = hashlib.sha1(pw.encode()).hexdigest().upper()
first = hashed[:5]
last = hashed[5:]
response = requests.get(f"https://api.pwnedpasswords.com/range/{first}")

if last in response.text:
    print("your password is hacked")

else:
    print("password is not hacked")