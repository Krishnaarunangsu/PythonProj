# List are represented by square brackets
# List is ordered
# List items are indexed
# List is changeable/mutable
# List allow duplicate values
# List can have values of any data types


def my_func(n):
    return abs(n - 50)


class ListClass:
    """
    Class with List Items
    """
    list_1 = ["apple", "banana", "cherry"]
    list_2 = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
    list_3 = [1, 5, 7, 9, 3]
    list_4 = [True, False, False]
    list_5 = ["abc", 34, True, 40, "male"]

    def __init__(self, item, start_index, end_index):
        """
        Initialization
        """
        self.end_index = end_index
        self.start_index = start_index
        self.item = item

    def check_list_item(self):
        """
        Check If an item exists in the list
        :return:message
        """
        if self.item in self.list_3:
            return f"Item Exists in the list"
        else:
            return f"Item does not exist in the list"

    def insert_item_in_list(self):
        """
        Insert item in the list in the specified position
        :return:
        """
        list_updated_1 = self.list_3
        print(list_updated_1)
        list_updated_1[self.start_index] = 6
        print(list_updated_1)
        # list_updated_1[self.start_index, self.end_index] = [2, 4]
        list_updated_1[self.start_index:self.end_index] = [4, 6]
        print(list_updated_1)
        list_updated_1[self.start_index:self.end_index] = [8]
        print(list_updated_1)
        list_updated_1.insert(4, True)
        print(list_updated_1)
        list_updated_1.append("Krishna")
        print(list_updated_1)
        list_updated_1.insert(1, "Jagannath")
        print(list_updated_1)
        list_7 = [2, 9, 0]
        list_updated_1.extend(list_7)
        print(list_updated_1)
        tuple_1 = (7, 6, 5)
        list_updated_1.extend(tuple_1)
        print(list_updated_1)

    def remove_from_list(self):
        """

        :return:
        """
        # Remove from a specified index
        list_8 = self.list_3
        print(self.list_3)
        list_8.remove(self.start_index)
        print(list_8)
        list_8.remove(0)
        print(list_8)
        list_8.pop(self.start_index)
        print(list_8)
        list_8.pop()
        print(list_8)
        del list_8[1]
        print(list_8)
        list_8.clear()
        print(list_8)
        del list_8
        # print(list_8)

    @classmethod
    def print_list(cls):
        """
        main method
        :return:
        """
        print(cls.list_1)
        print(len(cls.list_1))
        print(type(cls.list_1))
        # Access by Index
        print(cls.list_1[1])
        # Access by negative index
        print(cls.list_1[-1])
        print(cls.list_2)
        print(len(cls.list_2))
        print(cls.list_3)
        print(len(cls.list_3))
        print(cls.list_4)
        print(len(cls.list_4))
        print(cls.list_5)
        print(len(cls.list_5))
        print(type(cls.list_5))

        # Range of Indexes
        # You can specify a range of indexes by specifying where to start and where to end the range.
        # When specifying a range, the return value will be a new list with the specified items.
        print(cls.list_3[2:5])

        # By leaving out the start value, the range will start at the first item
        # but will leave out the item in tn the index mentioned
        print(cls.list_3[:5])

        # By leaving out the end value, the range will go on to the end of the list:
        print(cls.list_3[2:])

        print(cls.list_3[-4:])
        print(cls.list_3[-4:-1])
        print(cls.list_3[:])
        print(cls.list_3[::])  # equivalent to startIndex=0
        print(cls.list_3[1::])
        print(cls.list_3[:2:])
        print(cls.list_3[:5:])
        print(cls.list_3[::-1])
        print(cls.list_3[-1::])
        print(cls.list_3[:-1:])


class ListSpecialClass:
    """
    Sorting List
    """

    def __init__(self, list_tobe_sorted: list):
        """
         Initialization
        """
        self.list_tobe_sorted: list = list_tobe_sorted
        print(list_tobe_sorted)
        print(self.list_tobe_sorted)

    def sort_list(self):
        """

        :return:
        """
        self.list_tobe_sorted.sort()
        print(self.list_tobe_sorted)

    def sort_list_descending(self):
        """

        :return:
        """
        self.list_tobe_sorted.sort(reverse=True)
        print(self.list_tobe_sorted)

    def custom_sort_list(self):
        """

        :return:
        """
        self.list_tobe_sorted.sort(key=my_func)
        print(self.list_tobe_sorted)


def main():
    list_class = ListClass
    list_class.print_list()

    list_class_1 = ListClass(3, 1, 3)
    item_exist: str = list_class_1.check_list_item()
    print(item_exist)
    # https://www.geeksforgeeks.org/python-using-variable-outside-and-inside-the-class-and-method/

    list_class_1.insert_item_in_list()
    list_class_1.remove_from_list()

    this_list = [100, 50, 65, 82, 23]
    list_class_2 = ListSpecialClass(this_list)
    print(list_class_2)

    # print()
    list_class_2.sort_list()
    list_class_2.sort_list_descending()
    list_class_2.custom_sort_list()


if __name__ == "__main__":
    main()
