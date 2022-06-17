import json

nested_dictionary_1 = {1: "Geeks", 2: "For",
                       3: {"A": "Welcome", "B": "To", "C": "Geeks"}}

print(json.dumps(nested_dictionary_1, sort_keys=False, indent=4))
