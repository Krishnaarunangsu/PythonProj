import random

customers = ["Alex", "Bob", "Carol", "Dave", "Flow", "Katie", "Nate"]
discount_dict = {customer: random.randint(1, 100) for customer in customers}
print(discount_dict)

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp_C = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]
print(temp_C)

# Creating a dictionary of weekly temperatures from the list of temperatures and days
weekly_temp = {day: temp for (day, temp) in zip(days, temp_C)}
print(weekly_temp)
