import time
import threading

def cal_square(numbers):
    print("calculate square number")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n*n)

def cal_cube(numbers):
    print("calculate cube number")
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n*n*n)

arr = [2,3,7,9]

try:
    t = time.time()

    run_cal_square = threading.Thread(target=cal_square, args=(arr,))
    run_cal_square.start()

    run_cal_cube = threading.Thread(target=cal_cube, args=(arr,))
    run_cal_cube.start()

    run_cal_square.join()
    run_cal_cube.join()
    print("done in ",time.time() - t)
except:
    print("Error")