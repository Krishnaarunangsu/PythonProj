def test_yield():
    yield "Welcome to Guru99 Python Tutorials"
    yield "TCG"


output = test_yield()
print(output.__next__())
print(output.__next__())
