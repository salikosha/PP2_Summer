class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky")

v = Vehicle()
c = Car()
p = Plane()

v.move()   
c.move()   
p.move()   
