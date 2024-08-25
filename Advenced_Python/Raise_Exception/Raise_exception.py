
class accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exeption(self):
        print("user defined execptiom",self.msg)


try:
    f=open("Raise_exception.py")
    x=1/0

except FileNotFoundError as e:
    print("inside except")

finally:
    print("cleaning up file")
    f.close()