class DogScopeIssue:
    """
    Documentation about Dog
    """
    # class variable
    tricks = []

    def __init__(self, name: str):
        """

        :param name:
        """
        self.name = name

    def add_trick(self, trick):
        """

        :param trick:
        :return:
        """
        self.tricks.append(trick)


if __name__ == "__main__":
    d = DogScopeIssue('Fido')
    e = DogScopeIssue('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    print(f"Fido's Tricks:{d.tricks}") # Wrong Tricks for Fido
