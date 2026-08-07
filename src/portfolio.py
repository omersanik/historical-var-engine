import pandas as pd 
from returns import load_data, calculate_returns
from var import sort_returns, calculate_var, calculate_expected_shortfall
portfolio = {
    "AAPL": 0.5,
    "MSFT": 0.3,
    "GOOGL": 0.2,
}

def load_portfolio_returns(portfolio):
    portfolio_returns = pd.DataFrame()

    for stock, weight in portfolio.items():
        filepath = f"data/raw/{stock}.csv"

        data = load_data(filepath)
        data = calculate_returns(data)

        portfolio_returns[stock] = data["Returns"]

    return portfolio_returns

weights = pd.Series(portfolio)
portfolio_returns = (
    load_portfolio_returns(portfolio) *weights
).sum(axis=1)

sorted_returns = sort_returns(portfolio_returns)
portfolio_var = calculate_var(sorted_returns)
portfolio_es = calculate_expected_shortfall(sorted_returns)

print(f"Portfolio VaR: {portfolio_var:.6f}")
print(f"Portfolio ES : {portfolio_es:.6f}")

aapl = pd.read_csv("data/raw/AAPL.csv")
msft = pd.read_csv("data/raw/MSFT.csv")
googl = pd.read_csv("data/raw/GOOGL.csv")

if __name__ == "__main__":
    portfolio_returns = load_portfolio_returns(portfolio)

    sorted_returns = sort_returns(portfolio_returns)
    portfolio_var = calculate_var(sorted_returns)
    portfolio_es = calculate_expected_shortfall(sorted_returns)

    print(f"Portfolio VaR: {portfolio_var:.6f}")
    print(f"Portfolio ES : {portfolio_es:.6f}")