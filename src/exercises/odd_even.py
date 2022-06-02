def check_odd_even():
    """

    :return:
    """
    try:
        number: int = int(input('Enter the number:'))
        if number % 2 == 0:
            print('The number is even')
        else:
            print('The number is odd')
    except:
        raise ZeroDivisionError
    finally:
        print('Operation Completed')


if __name__ == "__main__":
    check_odd_even()
