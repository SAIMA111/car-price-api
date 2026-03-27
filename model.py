import numpy as np
import pandas as pd

import numpy as np
import pandas as pd

w0 = 9.31769997489616

w = [
    0.00371966395,
    0.0775899393,
    -0.00324002587,
    0.0109615368,
    -0.0000463569,
    -0.0937682483
]

base = ['engine_hp', 'engine_cylinders', 'highway_mpg',
        'city_mpg', 'popularity']

def prepare_X(df):
    df = df.copy()
    
    df['age'] = 2017 - df['year']
    features = base + ['age']
    
    df_num = df[features]
    df_num = df_num.fillna(0)

    return df_num.values