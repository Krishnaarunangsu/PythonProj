# Function defined outside the class
def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


if __name__ == "__main__":
    a=int(input('Enter the first number:'))
    b=int(input('Enter the second number:'))
    c = C()
    print(f'Minimum of two numbers {a} and {a+b}:{c.f(a, b)}')
    print(c.h())
    print(c.g())
