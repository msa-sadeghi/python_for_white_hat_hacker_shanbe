import time
import random
import threading

def port_scan(port_number):
    time.sleep(random.randint(1,3))
    print("scanning...", port_number)



for i in range(5):
    t = threading.Thread(target=port_scan, args=(i,))
    t.start()