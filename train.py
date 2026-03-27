import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv"
df = pd.read_csv(url)

df.columns = df.columns.str.lower().str.replace(' ', '_')

base = ['engine_hp', 'engine_cylinders', 'highway_mpg',
        'city_mpg', 'popularity']

def prepare_X(df):
    df = df.copy()
    df['age'] = 2017 - df['year']
    features = base + ['age']
    df_num = df[features]
    df_num = df_num.fillna(0)
    return df_num.values

def train_linear_regression_reg(X, y, r=0.001):
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])
    XTX = X.T.dot(X)
    XTX = XTX + r * np.eye(XTX.shape[0])
    XTX_inv = np.linalg.inv(XTX)
    w_full = XTX_inv.dot(X.T).dot(y)
    return w_full[0], w_full[1:]

y = np.log1p(df.msrp.values)
del df['msrp']

X = prepare_X(df)

w0, w = train_linear_regression_reg(X, y, r=0.001)

print(w0)
print(w)
print(len(w))