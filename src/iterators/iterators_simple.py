class IteratorSimple:
    """
    Class for Iterators
    """

    def __init__(self):
        """

        """
        self.my_list = None

    def show_iterables(self):
        """

        :return:
        """
        self.my_list = [4, 7, 0, 3]
        # get an iterator using iter()
        my_iter = iter(self.my_list)
        # iterate through it using next()

        # Output: 4
        print(next(my_iter))
        # Output: 7
        print(next(my_iter))
        # next(obj) is same as obj.__next__()

        # Output: 0
        print(my_iter.__next__())

        # Output: 3
        print(my_iter.__next__())

        # This will raise error, no items left
        next(my_iter)

    def show_iterables_1(self):
        """

        :return:
        """
        try:
            self.my_list = [4, 7, 0, 3]
            # get an iterator using iter()
            my_iter = iter(self.my_list)
            # iterate through it using next()

            # Output: 4
            print(next(my_iter))
            # Output: 7
            print(next(my_iter))
            # next(obj) is same as obj.__next__()

            # Output: 0
            print(my_iter.__next__())

            # Output: 3
            print(my_iter.__next__())

            # This will raise error, no items left
            next(my_iter)
        except StopIteration as stop_iter_err:
            print(f'Coming in Exception:{stop_iter_err}')
        finally:
            print('Iteration Completed')


if __name__ == "__main__":
    iterator_simple = IteratorSimple()
    iterator_simple.show_iterables_1()
