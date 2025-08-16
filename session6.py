# import time
# import random
# import threading

# def port_scan(port_number):
#     time.sleep(random.randint(1,3))
#     print("scanning...", port_number)



# for i in range(5):
#     t = threading.Thread(target=port_scan, args=(i,))
#     t.start()

# password = input("enter the password: ")
def login(password):
    correct_password = "1234"
    if password == correct_password:
        return "login success..."
    return "login failed..."

# login()

def brute_force():
    passwords = ["123", "password", "admin", "1234", "abcd"]
    for p  in passwords:
        if "success" in login(p):
            print(f" password is {p}")
            break

brute_force()
    