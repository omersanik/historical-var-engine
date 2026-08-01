import numpy as np 



def sort_returns(returns):
   sorted_returns = returns.sort_values()
   return sorted_returns

def calculate_cutoff_index(returns, confidence_level):
    number_of_returns = len(returns)

    cutoff_index = int(number_of_returns * (1 - confidence_level))
    return cutoff_index
def calculate_var(returns, confidence_level=0.95):
    cutoff_index = calculate_cutoff_index(returns, confidence_level)
    var = returns.iloc[cutoff_index]
    return var


def calculate_expected_shortfall(returns, confidence_level=0.95):
    cutoff_index = calculate_cutoff_index(returns, confidence_level)
    tail_losses = returns.iloc[:cutoff_index + 1]
    expected_shortfall = tail_losses.mean()
    return expected_shortfall

from plotting import plot_return_distribution
from returns import load_data, calculate_returns

if __name__ == "__main__":
    data = load_data("data/raw/AAPL.csv")

    data = calculate_returns(data)

    sorted_returns = sort_returns(data["Returns"])
    my_var = calculate_var(sorted_returns)

    print(sorted_returns.head())

    numpy_var = np.percentile(data["Returns"], 5)
    print(f"NumPy VaR: {numpy_var:.6f}")

    my_es = calculate_expected_shortfall(sorted_returns)

    print(f"My VaR: {my_var:.6f}")
    print(f"My ES : {my_es:.6f}")

    plot_return_distribution(
        returns=data["Returns"],
        var=my_var,
        expected_shortfall=my_es,
    )