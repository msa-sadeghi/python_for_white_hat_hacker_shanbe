# import time
# import random
# import threading

# def port_scan(port_number):
#     time.sleep(random.randint(1,3))
#     print("scanning...", port_number)



# for i in range(5):
#     t = threading.Thread(target=port_scan, args=(i,))
#     t.start()

def login():
    correct_password = "1234"
    password = input("enter the password: ")
    if password == correct_password:
        print("login success...")
    else:
        print("login failed...")

# login()

def brute_force():
    passwords = ["123", "password", "admin", "1234", "abcd"]
    correct_password = "1234"