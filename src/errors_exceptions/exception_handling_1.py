# something more about try except
# basic syntax
"""
try:
    code1
except:
    some code that will execute if code 1 fails or raise some error
else:
    this code is executed only if try was successful i.e no error in code1
finally:
    this code will execute in every situation if try fails or not
"""

filename = 'exception_data.txt'
# Outer try block catches file name or file doesn't exist errors.
try:
    with open(filename) as fin:
        for line in fin:
            # print(line)
            items = line.split(',')
            total = 0

            # Inner try bock catches integer conversion errors.
            try:
                for item in items:
                    num = int(item)
                    total += num
                print('Total = ' + str(total))
            except:
                print('Error converting to integer. ', items)
except:
    print('Error opening file. ' + filename)

finally:
    print('This is our optional finally block. Code here will execute no matter what.')
