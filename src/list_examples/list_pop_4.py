# Pop item at the given index from the list

def pop_from_list_by_index(i: int):
    """

    :param i:
    :return:
    """
    try:
        # programming languages list
        languages = ['Python', 'Java', 'C++', 'French', 'C']

        # remove and return the 7th item
        return_value = languages.pop(i)

        print('Return Value:', return_value)

        # Updated List
        print('Updated List:', languages)
    except IndexError as ie:
        print(f'{ie}:{i}')


if __name__ == "__main__":
    pop_from_list_by_index(6)
