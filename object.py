# create a class for cars
# attributes of a car brand
# should be able to start and stop
# when you start the car print "the car has started
# when start should print has start

# bonus point being able to see the car is driving
# Task 1.Create a variable when the car is driving



class Car:
    def __init__(self, brand):
        self.brand = brand
        self.is_driving = False

    def start(self):
        if self.is_driving:
            print(f"The {self.brand} is already driving.")
        else:
            self.is_driving = True
            print(f"The {self.brand} is driving.")

    def stop(self):
        if not self.is_driving:
            print(f"The {self.brand} is already stopped.")
        else:
            self.is_driving = False
            print(f"The {self.brand} has stopped driving.")


if __name__ == "__main__":
    # create objects
    car = Car("BMW")

    car.start()
    car.stop()




