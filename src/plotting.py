import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt



def plot_return_distribution(returns, var, expected_shortfall):
    plt.figure(figsize=(10, 6))
    plt.hist(returns, bins=30, alpha=0.7, edgecolor="black")
    plt.axvline(
        x=var,
        color="red",
        linestyle="--",
        label="VaR"
    )
    plt.axvline(
        x=expected_shortfall,
        color="orange",
        linestyle="--",
        label="Expected Shortfall"
    )
    plt.title("Distribution of Daily Returns")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.show()

def plot_rolling_var(rolling_var):
    plt.figure(figsize=(12, 6))
    plt.plot(rolling_var)
    plt.title("20-DAy rolling historical VaR")
    plt.xlabel("Window")
    plt.ylabel("VaR")
    plt.grid(True)
    plt.show()