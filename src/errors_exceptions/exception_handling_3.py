def divide_me(n):
    x = 1 / n


i = int(input('enter a number '))
try:
    divide_me(i)

except Exception as e:
    print(e)  # this will print the error msg but don't kill the execution of program

else:
    print('Your Code Run Successfully')  # this will execute if divide_me(i) run successfully without an error

finally:
    print('thanks')  # this will execute in every condition
