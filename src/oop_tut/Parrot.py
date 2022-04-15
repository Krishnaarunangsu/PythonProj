class Parrot:
    """
    Parrot Class
    """
    # class attribute
    species = 'Bird'

    # initialization: Constructor
    # instance attribute
    def __init__(self, name, age):
        """
        Initialization
        :param name:
        :param age:
        """
        self.name = name
        self.age = age


if __name__ == "__main__":
    blue_parrot = Parrot("Blu", 10)
    yellow_parrot = Parrot("Yellow", 15)
    print(f"Species is:{blue_parrot.species}")
    print(f"Name is:{blue_parrot.name}")
    print(f"Age is:{blue_parrot.age}")
