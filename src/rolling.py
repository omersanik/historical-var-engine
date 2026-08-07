from var import calculate_var, sort_returns
from plotting import plot_rolling_var

def calculate_rolling_var(returns, window=252, confidence_level=0.95):
    rolling_var = []

    for i in range(len(returns) - window + 1):
        window_returns = returns.iloc[i: i + window]
        sorted_returns = sort_returns(window_returns)
        window_var = calculate_var(sorted_returns, confidence_level)

        rolling_var.append(window_var)


    return rolling_var

from returns import load_data, calculate_returns

data = load_data("data/raw/AAPL.csv")
data = calculate_returns(data)

rolling = calculate_rolling_var(
    data["Returns"],
    window=20
)
plot_rolling_var(rolling)


