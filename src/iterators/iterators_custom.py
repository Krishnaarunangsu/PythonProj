class CustomIterator:

    def __init__(self, max_value=0):
        """
        Constructor
        :param max_value:
        """
        self.max_value = max_value

    def __iter__(self):
        """
        Custom Iterator
        :return:
        """
        self.n = 0
        return self

    def __next__(self):
        """
        Custom Next
        :return:
        """
        # Check Limit. If limit is reached then stop iteration
        if self.n <= self.max_value:
            # Check odd or even
            if self.n % 2 == 0:
                result = self.n
                self.n += 1
                return result
            else:
                self.n += 1
                return 1
        else:
            raise StopIteration


# create an object
numbers = CustomIterator(10)

for i in numbers:
    print(i)
