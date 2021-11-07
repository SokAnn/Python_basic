"""
классы: основы
"""


# creating class
# empty class does nothing
class MyClass:  # equal: class MyClass(object):
    def __init__(self):  # constructor
        pass


class Vehicle:
    """ documentation string (optional) """
    vehicle_count = 0  # counter of instances
    __private_attr = 1  # private attribute: attribute cannot be called outside of class

    def __init__(self, color, doors, vtype):  # constructor - basic method
        # self - pointer to an instance
        self.color = color  # attributes
        self.doors = doors
        self.vtype = vtype
        Vehicle.vehicle_count += 1
        print(f"init {self.vtype}")

    # methods drive() & stop()
    def drive(self):
        return f"I'm driving a {self.color} {self.vtype}!"

    def brake(self):
        return f"{self.vtype} braking!"

    def __repr__(self):  # programmatic representation of object - basic method
        return f"Class  = {self.__class__}"

    def __str__(self):  # string representation of object - basic method
        return f"Car: color = {self.color}, doors = {self.doors}, vtype = {self.vtype}, private = {self.__private_attr}"

    def __del__(self):  # destructor (optional) - basic method
        print(f"del {self.vtype}")


class Car(Vehicle):  # inheritance: Vehicle - superclass (parent), Car - subclass (child)
    # redefine method
    def brake(self):  # polymorphism: same interface Vehicle.brake() & Car.brake()
        return "BRAKING!!!"


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector{self.x, self.y}"

    def __add__(self, other):  # basic method
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    # creating instances
    car = Vehicle("white", 4, "car")
    print(car.drive())
    print(car.brake())
    print("-------------")
    truck = Vehicle("green", 6, "truck")
    print(truck.drive())
    print(truck.brake())
    print("-------------")
    bike = Vehicle("blue", 2, "bike")
    print(bike.drive())
    print(bike.brake())
    vector1 = Vector(3, 7)
    vector2 = Vector(10, 5)
    print("-------------")

    # creating subclass instance
    new_car = Car("black", 4, "car")
    print(new_car.drive())
    print(new_car.brake())
    print("-------------")

    # access to attributes
    print(f"number of instances = {Vehicle.vehicle_count}")
    print("color: ", car.color)
    print("number of doors: ", truck.doors)
    print("getattr() method:", getattr(new_car, "color"))  # access to attribute
    print("hasattr() method: ", hasattr(car, "vtype"))  # check attribute
    print("hasattr() method: ", hasattr(car, "bodytype"))
    setattr(car, "color", "pink")  # set value to attribute
    print("color: ", car.color)
    setattr(new_car, "bodytype", "sedan")
    print("", hasattr(new_car, "bodytype"))
    delattr(new_car, "bodytype")  # delete attribute
    print("", hasattr(new_car, "bodytype"))
    print("-------------")

    # built-in attributes
    print("dictionary: ", Vehicle.__dict__)  # dictionary with namespace of class
    print("documentation: ", Vehicle.__doc__)  # documentation string
    print("name: ", Vehicle.__name__)  # name of class
    print("module: ", Vehicle.__module__)  # name of module in which class is defined
    print("bases: ", Vehicle.__bases__)  # tuple of basic classes
    print("base: ", Vehicle.__base__)  # basic class (1st in tuple of basic classes)
    print("-------------")

    print(issubclass(Vehicle, Car))  # check subclass
    print(issubclass(Car, Vehicle))
    print(isinstance(new_car, Car))  # check instance
    print(isinstance(truck, Car))
    print("-------------")

    # basic methods
    # __init__(), __del__()
    print(repr(new_car))  # __repr__()
    # print(new_car.__class__)
    # print(new_car.__class__.__mro__)
    print(str(new_car))  # __str__()
    # print(new_car.__private_attr)  # error!!! - access to private attribute cannot directly
    print(new_car._Vehicle__private_attr)  # access to private attribute from outside
    print(vector1)
    print(vector1 + vector2)
    print("-------------")
