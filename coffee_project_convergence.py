import matplotlib.pyplot as plt
from coffee_black76 import black76_call
from coffee_futures import futures_price
from coffee_monte_carlo import monte_carlo_futures_call

spot_price = 1.20
risk_free_rate = 0.02
storage_cost = 0.01
time_to_maturity = 0.5
strike_price = 1.25
volatility = 0.25

simulation_counts = [10, 100, 1_000, 10_000, 100_000]

fair_futures_price = futures_price(spot_price, risk_free_rate, storage_cost, time_to_maturity)
black76_price = black76_call(fair_futures_price, strike_price, risk_free_rate, volatility, time_to_maturity)

monte_carlo_prices = []
standard_errors = []

for M in simulation_counts:
    price, error = monte_carlo_futures_call(fair_futures_price, strike_price, risk_free_rate, volatility, time_to_maturity, M, seed=40)
    monte_carlo_prices.append(price)
    standard_errors.append(error)
    print(f"Simulations = {M:>6} | Monte Carlo = ${price:.4f} | Standard error = ${error:.4f}")

print(f"\nBlack-76 price = ${black76_price:.4f}")


plt.errorbar(simulation_counts, monte_carlo_prices, yerr=standard_errors, marker="o", linestyle="-", capsize=4, label="Monte Carlo")
plt.axhline(black76_price, color="red", linestyle="--", label="Black-76 price")
plt.xscale("log")
plt.xlabel("number of simulations")
plt.ylabel("coffee call option price")
plt.title("monte carlo convergence for a coffee futures option")
plt.legend()
plt.grid(True)
plt.savefig("coffee_convergence.png", dpi=300, bbox_inches="tight")
plt.show()