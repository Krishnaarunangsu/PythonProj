class IteratorSimple:
    """
    Iterator Example class
    """

    def __init__(self):
        """
        Constructor
        """
        self.iterable_value = None
        self.iterable_obj = None

    def show_iterations(self):
        """

        :return:
        """
        # Here is an example of a python inbuilt iterator
        # value can be anything which can be iterate
        self.iterable_value = 1
        self.iterable_obj = iter(self.iterable_value)

        while True:
            try:
                # Iterate by calling next
                item = next(self.iterable_obj)
                print(item)
            except StopIteration:

                # exception will happen when iteration will over
                break
            finally:
                print('Iteration is completed')


if __name__ == "__main__":
    iterator_simple = IteratorSimple()
    iterator_simple.show_iterations()
