from portfolio import load_portfolio_returns, portfolio
import pandas as pd
import numpy as np
def calculate_covariance_matrix(returns):
    covariance_matrix = returns.cov()
    return covariance_matrix

portfolio_returns = load_portfolio_returns(portfolio)
covariance_matrix = calculate_covariance_matrix(portfolio_returns)
print(covariance_matrix)

def calculate_portfolio_volatility(covariance_matrix, weight):
    portfolio_volatility = np.sqrt(weight.T @ covariance_matrix @ weight)
    return portfolio_volatility

weight = pd.Series(portfolio).to_numpy()
covariance_matrix = covariance_matrix.to_numpy()

volatility = calculate_portfolio_volatility(covariance_matrix, weight)
