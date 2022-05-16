class Vehicle:
    """
    parent class
    """

    def __init__(self, top_speed):
        """
        Constructor
        """
        self.top_speed = top_speed

    def set_top_speed(self):  # defining the set
        print("Top speed is set to", self.top_speed)


class Car(Vehicle):  # child class of Vehicle
    pass


class Truck(Vehicle):  # child class of Vehicle
    pass


def main():
    """
    Coordinating activities
    :return:
    """
    corolla = Car(200)  # creating an object of the Car class
    corolla.set_top_speed()  # accessing methods from the parent class

    volvo = Truck(180)  # creating an object of the Truck class
    volvo.set_top_speed()  # accessing methods from the parent class


if __name__ == "__main__":
    main()
