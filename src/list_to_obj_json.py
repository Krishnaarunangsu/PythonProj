import json
from pprint import pprint

data = {

    'title': ['Seven days', 'Not Today', 'Bad Moms'],
    'date': ['July 17', 'Aug 18', 'Jan 19']

}
new_data = [{"title": i, "date": b} for i, b in zip(data["title"], data["date"])]
final_data = json.dumps(new_data)

# data = dict(title=['Seven days', 'Not Today', 'Bad Moms'], date=['July 17', 'Aug 18', 'Jan 19'])
# new_data = [{"title": i, "date": b} for i, b in zip(data["title"], data["date"])]
# final_data = json.dumps(new_data)

pprint(final_data, indent=4)

new_data = [dict(zip(data.keys(), i)) for i in zip(*data.values())]
pprint(new_data)

# Long Version

titles = data['title']
dates = data['date']

lst = list()

for i in range(len(titles)):
    a = dict()
    a["title"] = titles[i]
    a["date"] = dates[i]
    lst.append(a)

print(json.dumps(lst))

