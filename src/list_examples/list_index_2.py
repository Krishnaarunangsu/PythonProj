def search_letter(letter: str):
    """
    Search the letter in the given list
    :param letter:
    :return:
    """
    # vowels list
    vowels = ['a', 'e', 'i', 'o', 'u']
    try:
        # index of 'p' in vowels
        index = vowels.index(letter)
        print('The index of the letter:', index)
    except ValueError as ie:
        print(ie)


if __name__ == "__main__":
    search_letter('p')
