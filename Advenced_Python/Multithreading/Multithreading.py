import time
import threading
def calc_square(numbers):
    print("calculate square numbers")
    for i in numbers:
        time.sleep(0.2)
        print("square: ",i*i)
def calc_cube(numbers):
    print("calculate cube of numbers")
    for i in numbers:
        time.sleep(0.2)
        print("qube: ", i * i)
arr = [2,3,8,9]
t = time.time()
t1 = threading.Thread(target=calc_square,args=(arr,))
t2 = threading.Thread(target=calc_cube,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
tt= time.time()
print("done in "+str(tt-t)+"sec")