import json

people = {"employee_1": {'name': 'John', 'age': '27', 'sex': 'Male'},
          "employee_2": {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
# print(json.dumps(people, sort_keys=True, indent=4))
# json.dumps(people["employee_1"], sort_keys=True, indent=4)
people["example_3"] = {}
people["example_3"]["name"] = "Jackob"
people["example_3"]["age"] = "39"
people["example_3"]["sex"] = "Male"

people["example_4"] = {"name": "Jill", "age": 29, "sex": "Female"}

print(json.dumps(people, sort_keys=True, indent=4))
# print(f'Details of  employee_1:\n{json.dumps(people["employee_1"], sort_keys=True, indent=4)}')
