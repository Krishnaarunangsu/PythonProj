import json

list_1 = [1, 2]
list_2 = [3, 4]
dict_1: dict = {"A": list_1, "B": list_2}
print(json.dumps(dict_1, indent=4))
