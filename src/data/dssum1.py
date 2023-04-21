# %%
import numpy as np 
import pandas as pd 
from tqdm import tqdm 

# %%
max_number = 2**64 - 1

# %%
np.random.seed(42)

# %%
final_df = pd.DataFrame(dict(a=[2], b=[2]))

# %%
i = 1
progress_bar = tqdm(19)
while 2**i <= max_number:
    a = np.random.randint(2**(i-1), 2**i, size=10000, dtype='ulonglong')
    b = np.random.randint(2**(i-1), 2**i, size=10000, dtype='ulonglong')

    progress_bar.update(1)
    i += 1
    final_df = pd.concat([final_df, pd.DataFrame(dict(a = a, b=b))])

# %%
final_df['target'] = final_df['a'] + final_df['b']

# %%
final_df.to_csv('llm-sum/data/dssum1.csv')


