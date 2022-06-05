# Creating pandas series

import pandas as pd

# fruit stand Dictionary
data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}
# purchases
purchases = pd.DataFrame(data)
print(f'Fruits purchased:{purchases}')
