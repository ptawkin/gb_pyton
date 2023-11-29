import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

data2 = data.copy()
data2['whoAmI_human'] = data2.whoAmI.map({'robot': 0, 'human': 1})
data2['whoAmI_robot'] = data2.whoAmI.map({'robot': 1, "human": 0})
data2.drop(data2.columns[0], axis=1, inplace=True)
