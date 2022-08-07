import json

d = {
    'a': 10,
    'b': 20,
    'c': 30
}

print(type(d))

d['x'] = 5

d.update({'y': 7})
print(json.dumps(d, sort_keys=False, indent=4))
