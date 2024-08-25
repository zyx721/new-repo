# class Vehicle:
#     def general_usage(self):
#         print("general use: transportation")
# class car(Vehicle):
#     def __init__(self):
#         print("i'm a car")
#         self.wheels = 4
#         self.has_roof=True
#     def specific_usage(self):
#         print("specific use: commute to work, vacation with family")
# class motorcycle(Vehicle):
#     def __init__(self):
#         print("im a moto")
#         self.wheels = 2
#         self.has_roof=False
#     def specific_usage(self):
#         self.general_usage()
#         print("specific use: road trip ,racing")
# c = car()
# m = motorcycle()
# m.specific_usage()
# print(isinstance(m,Vehicle))
# print(isinstance(m,car))
# print(isinstance(m,motorcycle))
#exercice:
class Animal:
    def __init__(self, hab):
        self.habitait = hab
        self.habitat()

    def habitat(self):
        print(self.habitait)
class dog(Animal):
    def __init__(self):
        super().__init__("where human lives")

a = Animal("somewhere")
d = dog()