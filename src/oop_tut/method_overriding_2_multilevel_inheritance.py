# Python program to demonstrate
# overriding in multilevel inheritance


class Parent:

    # Parent's show method
    def display(self):
        print(f"Inside Parent:{self}")


# Inherited or Sub class (Note Parent in bracket)
class Child(Parent):

    # Child's show method
    def show(self):
        print(f"Inside Child:{self}")


# Inherited or Sub class (Note Child in bracket)
class GrandChild(Child):

    # Child's show method
    def show(self):
        print(f"Inside GrandChild:{self}")


# Driver code
g = GrandChild()
g.show()
g.display()
