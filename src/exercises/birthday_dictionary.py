from KeyErrorDescription import KeyErrorDesc


def get_birthday(name):
    """

    :return:
    """
    birthday = {
        "B": '19/12/21',
        "A": '18/12/21',
        "C": '20/12/21'
    }
    try:
        print(birthday[name])
    except:
        raise KeyErrorDesc(name)
    finally:
        print('Search Completed')


if __name__ == "__main__":
    get_birthday("D")
