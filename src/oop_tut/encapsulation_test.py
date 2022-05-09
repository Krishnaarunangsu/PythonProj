class Computer:
    def __init__(self):
        self.__maxprice = 500

    def show(self):
        print("Max Price is", self.__maxprice)

    def setMaxPrice(self, price):
        self.__maxprice = price


# Outside class
E = Computer()
# E.PrintName()
# print(E.PrintName())
E.show()
E.setMaxPrice(9000)
E.show()
