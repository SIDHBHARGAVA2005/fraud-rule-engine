import pandas as pd

def load_transactions(path):
    df=pd.read_csv(path, parse_dates=["timestamp"])
    return df.to_dict("records")