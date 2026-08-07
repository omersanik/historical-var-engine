import numpy as np
import pandas as pd
from plotting import plot_monte_carlo


from portfolio import load_portfolio_returns, portfolio
from covariance import calculate_portfolio_volatility, calculate_covariance_matrix
from optimization import calculate_portfolio_return, calculate_expected_returns

portfolio_returns = load_portfolio_returns(portfolio)

expected_returns = calculate_expected_returns(portfolio_returns)

covariance_matrix = calculate_covariance_matrix(portfolio_returns)


def generate_random_weights(n_assets, max_weight, min_weight):
    while True:
        weights = np.random.random(n_assets)
        weights /= weights.sum()

        if not np.any(weights > max_weight) and not np.any(weights < min_weight):
            return weights

    
def monte_carlo_portfolios(n_portfolios):
    returns = []
    volatilities = []
    sharpes = []
    weights_list = []

    for i in range(n_portfolios):
        weights = generate_random_weights(len(portfolio), 0.9, 0.05)
        weights_list.append(weights)
        portfolio_return = calculate_portfolio_return(expected_returns, weights)

        portfolio_volatility = calculate_portfolio_volatility( covariance_matrix, weights)

        sharpe_ratio = portfolio_return / portfolio_volatility

        returns.append(portfolio_return)
        volatilities.append(portfolio_volatility)
        sharpes.append(sharpe_ratio)

    results = pd.DataFrame({
        "Return": returns,
        "Volatility": volatilities,
        "Sharpe": sharpes
        })

    efficient = results.sort_values("Volatility")
    efficient["MaxReturn"] = efficient["Return"].cummax()

    frontier = efficient["Return"] == efficient["MaxReturn"]
    
    best_index = results["Sharpe"].idxmax()
    best_portfolio = results.loc[best_index]
    best_weights = weights_list[best_index]

    
    return results, best_portfolio, best_weights




results, best_portfolio, best_weights = monte_carlo_portfolios(100000)

print("Best Portfolio")
print(f"Return:      {best_portfolio['Return']:.6f}")
print(f"Volatility:  {best_portfolio['Volatility']:.6f}")
print(f"Sharpe:      {best_portfolio['Sharpe']:.6f}")

print("\nWeights:")
for stock, weight in zip(portfolio.keys(), best_weights):
    print(f"{stock}: {weight:.2%}")

plot_monte_carlo(results, best_portfolio)