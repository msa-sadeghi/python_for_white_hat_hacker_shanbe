import requests
url = "http://127.0.0.1:5000/home/"

def test_login(username, password):
    data = {"username": username, 
            "password":password
            }
    
    response = requests.post(url, data=data)
    if "success" in response.text:
        print(f"{password} is correct")
        return True
    else:
        print(f"password is incorrect")
        return True
    

test_login("user1", "wwwww")