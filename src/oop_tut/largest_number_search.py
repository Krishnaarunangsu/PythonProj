class LargestNumberSearch:
    def __init__(self, list_length):
        self.list_length = list_length

    def generate_list_integer(self) -> object:
        """

        :return:
        """
        lst_int = []
        # Iterating till the range
        for i in range(0, self.list_length):
            element: int = int(input())
            lst_int.append(element)

    def search_largest_number(self):
        """

        :return:
        """
        largest_no: int
        lst_int = self.generate_list_integer()
        lst_int_length=len(lst_int)
        # Find the largest number in the list
        for i in range(lst_int_length):
            print('Hi')
            while i <= lst_int_length - 1:
                print('Coming here')
                if i + 1 < lst_int_length:
                    if lst_int[i] <= lst_int[i + 1]:
                        largest_no = lst_int[i + 1]
                    else:
                        largest_no = lst_int[i]
                i += 1
