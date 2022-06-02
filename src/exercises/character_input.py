def calculate_age():
    """

    :return:
    """
    name: str = input('Enter your name: ')
    age: int = int(input('Enter Your age: '))
    year_of_birth = 2014 - age
    print(year_of_birth)
    year_100: int = year_of_birth + 100
    print(f'{name} will be 100 years old in the year:{year_100}')


if __name__ == "__main__":
    calculate_age()
