import time
import multiprocessing
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
if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square,args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube,args=(arr,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("done")