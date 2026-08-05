from portfolio import load_portfolio_returns, portfolio


def calculate_correlation_matrix(returns):
    correlation_matrix = returns.corr()
    return correlation_matrix

portfolio_returns = load_portfolio_returns(portfolio)
correlation_matrix = calculate_correlation_matrix(portfolio_returns)
print(correlation_matrix)
