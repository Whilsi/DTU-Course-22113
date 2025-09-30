import numpy as np
from scipy import stats
import pandas as pd

np.random.seed(25565)

data = pd.DataFrame()

for test_size in range(20,10001,499):
    random_data = np.random.normal(loc = 0,scale = 1,size = (test_size ,10000))
    statistic,p_value = stats.normaltest(random_data)
    data[test_size] = p_value

for key in data.keys():
    count = len(data[data[key] >= 0.05])
    print(key,count)