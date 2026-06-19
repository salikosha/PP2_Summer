class Car:
    total_cars = 0 

    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model   
        Car.total_cars += 1  
car1 = Car("BMW", "X5")
car2 = Car("Audi", "A4")
car3 = Car("Mercedes", "C-Class")
print(f"Total number of cars created: {Car.total_cars}")


class Student:
    school_name = 'ABC School '
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

s1 = Student('Emma', 10)
print(s1.name, s1.roll_no, Student.school_name)

s2 = Student('Jessa', 20)

print(s2.name, s2.roll_no, Student.school_name)


class Student:
    school_name = 'ABC School '

    def __init__(self, name):
        self.name = name# access class variable inside constructor using self
        print(self.school_name)
       
        print(Student.school_name)

s1 = Student('Emma')


class Car:
    manufacturer = 'BMW'

    def __init__(self, model, price):
        self.model = model
        self.price = price
car = Car('x1', 2500)
print(car.model, car.price, Car.manufacturer)