def main():
    """

    """
    range_test = RangeTest(1, 20, 3)
    range_test.check_range_stop_only()
    print('********************************')
    range_test.check_range_start_stop()
    print('********************************')
    range_test.check_range_start_stop_step()


class RangeTest:
    """
    For Testing Range Functionality
    """

    def __init__(self, start, stop, step):
        """
        Initialization
        :param start:
        :param stop:
        :param step:
        """
        self.start = start
        self.stop = stop
        self.step = step

    def check_range_stop_only(self):
        """
        Check Range  with Start & Stop Values
        :return:
        """
        for x in range(self.stop):
            print(f"The Numbers are:{x}")

    def check_range_start_stop(self):
        """
        Check Range  with Stop Value Only
        :return:
        """
        for x in range(self.start, self.stop):
            print(f"The Numbers are:{x}")

    def check_range_start_stop_step(self):
        """
        Check Range  with Stop Value Only
        :return:
        """
        for x in range(self.start, self.stop, self.step):
            print(f"The Numbers are:{x}")


if __name__ == "__main__":
    main()
