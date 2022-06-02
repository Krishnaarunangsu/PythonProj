def get_list_intersection():
    """

    :return:
    """

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    [c.append(x) for x in a if x in b]
    d = [x for x in a if x in b]
    print(c)
    print(d)


def get_list_intersection_set():
    """

    :return:
    """
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(set(set(a).intersection(b)))
    print(set(a).intersection(b))


if __name__ == "__main__":
    """
    """
    get_list_intersection()
    get_list_intersection_set()
