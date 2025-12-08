class DogScopeIssue:
    """
    Documentation about Dog
    """

    def __init__(self, name: str):
        """

        :param name:
        """
        self.name = name
        self.tricks = []  # creates a new empty list for each dog

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
    print(f"Fido's Tricks:{d.tricks}")  # Correct Tricks for Fido
    print(f"Buddy's Tricks:{e.tricks}")  # Correct Tricks for Buddy
