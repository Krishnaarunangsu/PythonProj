class Vehicle:
    """
    parent class
    """

    def __init__(self):
        """
        Constructor
        """
        self.top_speed = None

    def set_top_speed(self, speed):
        """
        defining the top set top speed function
        :param speed:
        :return:
        """
        self.top_speed = speed
        print("Top speed is set to", self.top_speed)


class Car(Vehicle):
    """
    child class
    """

    def __init__(self, car_type: str):
        """

        """
        self.car_type = car_type

    def open_trunk(self):
        """

        :return:
        """
        self
        print("Trunk is now open.")
        print(f'The Car Type is:{self.car_type}')


def main():
    """
    Coordinate the other activities
    :return:
    """
    corolla = Car('Corolla')  # creating an object of the Car class
    corolla.set_top_speed(220)  # accessing methods from the parent class
    corolla.open_trunk()  # accessing method from its own class


if __name__ == "__main__":
    main()
