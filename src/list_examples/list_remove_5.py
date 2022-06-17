def remove_item_from_list(x: object):
    """

    :param x:
    :return:
    """
    try:
        # animals list
        animals = ['cat', 'dog', 'rabbit', 'guinea pig']

        # Deleting 'fish' element
        animals.remove(x)

        # # Updated animals List
        print('Updated animals list: ', animals)
    except ValueError as ve:
        print(f'{x} {ve}')


if __name__ == "__main__":
    remove_item_from_list(2)
