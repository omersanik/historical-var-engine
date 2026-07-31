import yfinance as yf
import pandas as pd
import os 

def download_stock_data(ticker, start_date, end_date):
    #Download historical prices using yahoo finance
    data = yf.download(
        ticker,
        start_date,
        end_date
    )
    return data



def save_to_csv(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    data.to_csv(filepath)

    print(f"Data saved to {filepath}")

if __name__ == '__main__':
    apple = download_stock_data(
        ticker='AAPL',
        start_date='2020-01-01',
        end_date='2020-12-31'
    )

    save_to_csv(data=apple, filepath="data/raw/AAPL.csv")
    print(apple.head())