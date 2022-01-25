import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for ", count, "seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

answer = input("Do you wish to exit?\n")