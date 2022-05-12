class Dog:
    def __init__(self):
        """

        """
        self.name = "Tom"
        self._breed = 'Normal'
        self.__color = 'Brown'
        self._country = 'India'

    @property
    def breed(self):
        return self._breed


bello = Dog()
print(f'Name is:{bello.name}')
print(f'Breed is:{bello.breed}')
print(f'Breed is:{bello._breed}')
print(f'Country is:{bello._country}')
print(f'Color is:{bello.color}')
print(f'Color is:{bello.__color}')
# print(f'Country is:{bello._country}')
