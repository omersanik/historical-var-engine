from portfolio import load_portfolio_returns, portfolio
import pandas as pd

def calculate_expected_returns(returns):
   return returns.mean()

portfolio_returns = load_portfolio_returns(portfolio)

def calculate_portfolio_return(expected_returns, weights):
   return expected_returns @ weights

expected_return = calculate_expected_returns(portfolio_returns)

weights = pd.Series(portfolio)

portfolio_return = calculate_portfolio_return(expected_return, weights)

