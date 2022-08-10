import pandas as pd

dict = {'Name': ['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths': [87, 91, 97, 95],
        'Science': [83, 99, 84, 76]
        }

df = pd.DataFrame(dict)
print(f'Original Dataframe:\n{df}')

df.loc[len(df.index)] = ['Amy', 89, 93]

print(f'Modified Dataframe:\n{df}')
