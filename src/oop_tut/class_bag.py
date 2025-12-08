class Bag:
    """
    Bag class to append data
    """

    def __init__(self):
        self.data = []

    def add(self, x):
        """

        :param x:
        :return:
        """
        self.data.append(x)

    def add_twice(self, x: str) -> object:
        """

      :param x:
      :return:
      """

        self.add(x)
        self.add(x)
        return self.data


if __name__ == "__main__":
    bag = Bag()
    y = bag.add_twice(9)
    print(f'The final array/list is:{y}')
