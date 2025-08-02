# import socket


# target_ip = input("enter the ip: ")
# ports = [445, 135]

# for port in ports:
#     sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     result = sock.connect_ex((target_ip, port))
#     sock.settimeout(0.5)
#     if result == 0:
#         print(f"port {port} is open!")
#     sock.close()


# import requests
# ip = input("enter the ip: ")
# response = requests.get(f"http://ip-api.com/json/{ip}")
# data = response.json()
# if data['status'] =="success":
#     print(f"country: {data['country']}")
#     print(f"city: {data['city']}")
#     print(f"isp: {data['isp']}")


with open("report.html", "w") as f:
    f.write("<html><head></head><body><h1>Hello</h1></html>")