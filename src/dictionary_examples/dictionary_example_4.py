def get_element_by_key(key):
    """
    Get Element By Key
    :param key:
    :return:
    """
    try:
        # get vs [] for retrieving elements
        my_dict = {'name': 'Jack', 'age': 26}

        # Output: Jack
        print(my_dict['name'])

        # Use get method Output: 26
        print(my_dict.get('age'))

        # Trying to access keys which doesn't exist throws error
        # Output None
        print(my_dict.get('address'))

        # KeyError
        print(my_dict['address'])
    except KeyError as ke:
        print(f'{key}:{ke} is not present')


if __name__ == "__main__":
    get_element_by_key('address')
