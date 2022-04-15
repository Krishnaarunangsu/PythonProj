# Find the largest Integer
# Enter the number of integers

n = int(input("Enter the number of elements:"))
lst_int = []
largest_no: int
print(f"Length of the numbers:{n}")

# Iterating till the range
for i in range(0, n):
    element: int = int(input())
    lst_int.append(element)

print(f"The list of integers is:{lst_int}")

# Find the largest number in the list
for i in range(len(lst_int)):
    print('Hi')
    while i <= n - 1:
        print('Coming here')
        if i + 1 < n:
            if lst_int[i] <= lst_int[i + 1]:
                largest_no = lst_int[i + 1]
            else:
                largest_no = lst_int[i]
        i += 1

print(f"Largest No is:{largest_no}")
