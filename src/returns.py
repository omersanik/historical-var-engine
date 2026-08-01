import pandas as pd
import os

def load_data(filepath):
    data = pd.read_csv(filepath)

    return data


def calculate_returns(data):
    data["Returns"] = (data["Close"] - data["Close"].shift(1)) / data["Close"].shift(1)
    data = data.dropna()

    return data

if __name__ == "__main__":

    data = load_data("data/raw/AAPL.csv")
    data = calculate_returns(data)
    print(data.head())
    print(data.columns)