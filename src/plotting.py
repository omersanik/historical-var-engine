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

def plot_monte_carlo(results, best_portfolio):
    plt.figure(figsize=(10, 6))

    # All simulated portfolios
    scatter = plt.scatter(
        results["Volatility"],
        results["Return"],
        c=results["Sharpe"],
        cmap="viridis",
        alpha=0.6,
        s=15,
    )

    # Approximate efficient frontier
    efficient = results.sort_values("Volatility")
    efficient["MaxReturn"] = efficient["Return"].cummax()

    frontier = efficient[
        efficient["Return"] == efficient["MaxReturn"]
    ]

    plt.plot(
        frontier["Volatility"],
        frontier["Return"],
        linewidth=2,
        label="Efficient Frontier"
    )

    # Best Sharpe portfolio
    plt.scatter(
        best_portfolio["Volatility"],
        best_portfolio["Return"],
        color="red",
        s=250,
        marker="*",
        label="Best Portfolio",
    )

    plt.title("Monte Carlo Portfolio Optimization")
    plt.xlabel("Portfolio Volatility")
    plt.ylabel("Expected Portfolio Return")
    plt.colorbar(scatter, label="Sharpe Ratio")
    plt.grid(alpha=0.3)
    plt.legend()

    plt.savefig(
        "results/monte_carlo.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()