"""
классы: основы
"""


# creating class
# empty class does nothing
class MyClass:  # equal: class MyClass(object):
    def __init__(self):  # constructor
        pass


class Vehicle:
    def __init__(self, color, doors, vtype):  # constructor
        # self - pointer to an instance
        self.color = color  # attributes
        self.doors = doors
        self.vtype = vtype
        print(f"init {self.vtype}")

    # methods drive() & stop()
    def drive(self):
        return f"I'm driving a {self.color} {self.vtype}!"

    def brake(self):
        return f"{self.vtype} braking!"

    def __del__(self):  # destructor (optional)
        print(f"del {self.vtype}")


class Car(Vehicle):  # inheritance: Vehicle - superclass (parent), Car - subclass (child)
    def brake(self):  # polymorphism
        return "BRAKING!!!"


if __name__ == "__main__":
    # creating instances
    car = Vehicle("white", 4, "car")
    print(car.drive())
    print(car.brake())

    truck = Vehicle("green", 6, "truck")
    print(truck.drive())
    print(truck.brake())

    bike = Vehicle("blue", 2, "bike")
    print(bike.drive())
    print(bike.brake())

    # creating subclass instance
    new_car = Car("black", 4, "car")
    print(new_car.drive())
    print(new_car.brake())

