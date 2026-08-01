import pandas as pd
import os
from data_loader import save_to_csv

def load_data(filepath):
    data = pd.read_csv(filepath)

    return data


def calculate_returns(data):
    data["Returns"] = data["Close"].pct_change()
    data = data.dropna()

    return data



if __name__ == "__main__":

    data = load_data("data/raw/AAPL.csv")
    data = calculate_returns(data)
    save_to_csv(data, "data/processed/AAPL_returns.csv")

    print(data.head())
    print(data.columns)