# Get Current date and time
import datetime

datetime_object = datetime.datetime.now()
print(f'Current Date and Time is:{datetime_object}')

current_date = datetime.date.today()
print(f'Current Date is:{current_date}')
print(f'Current year:{current_date.year}')
print(f"Current month:{current_date.month}")
print(f"Current day:{current_date.day}")

print(dir(datetime))

# Date object to represent date
d = datetime.date(2019, 4, 13)
print(d)

# Get date from a timestamp
timestamp = datetime.date.fromtimestamp(1326244364)
print(f'Date:{timestamp}')
