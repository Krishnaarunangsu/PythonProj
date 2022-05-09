from src.errors_exceptions.my_custom_exceptions import FahrenheitError


class FahrenheitCelsiusConversion:
    """
    Fahrenheit to Celsius Conversion
    """

    def __init__(self, fahrenheit: float):
        """
        Initialization
        :param fahrenheit:
        """

        self.fahrenheit = fahrenheit

    def fahrenheit_to_celsius(self) -> float:
        """
        Fahrenheit to Celsius Conversion
        :param self:
        :return:float
        """
        min_f: float = 32
        max_f: float = 212
        if self.fahrenheit < min_f or self.fahrenheit > max_f:
            raise FahrenheitError(self.fahrenheit)
        return (self.fahrenheit - 32) * 5 / 9

    def main(self):
        """

        :return:
        """
        # self.fahrenheit_to_celsius()
        try:
            celsius = self.fahrenheit_to_celsius()
            print(f'Celsius:{celsius}')
        except FahrenheitError as ex:
            print(ex)
        else:
            print(f'{self.fahrenheit} Fahrenheit= {celsius:.4f} Celsius')


if __name__ == "__main__":
    fah = input('Enter a temperature in Fahrenheit:')
    try:
        fahrenheit = float(fah)
    except ValueError as ex:
        print(ex)
    else:
        fah_to_cel = FahrenheitCelsiusConversion(fahrenheit)
        fah_to_cel.main()
