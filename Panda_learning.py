
import pandas as pd
import numpy as np
import torch.cuda

s = pd.Series([1,3,6, np.nan, 44,1])



dates = pd.date_range('20160101', periods = 6)

# print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates, columns=['a','b','b','d'])

# print(df)

