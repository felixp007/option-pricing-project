import matplotlib.pyplot as plt
from black_scholes import black_scholes_call
from monte_carlo import monte_carlo_call
S = 100
K = 100
r = 0.05
sigma = 0.20
T = 1

simulation_counts = [10, 100, 1_000, 10_000, 100_000]

monte_carlo_prices = [] #lists
standard_errors = []

black_scholes_price = black_scholes_call(S, K, r, sigma, T)

for M in simulation_counts:
    price, error = monte_carlo_call(S, K, r, sigma, T, M, seed=42)
    monte_carlo_prices.append(price)
    standard_errors.append(error)

    print(f"Simulations = {M:>6} | "
        f"Monte Carlo = {price:.4f} | "
        f"Standard error = {error:.4f}")
plt.errorbar(simulation_counts,
    monte_carlo_prices,
    yerr=standard_errors,
    marker="o",
    linestyle="-",
    capsize=4,
    label="Monte Carlo")

plt.axhline(black_scholes_price,
    color="red",
    linestyle="--",
    label="Black-Scholes price")

plt.xscale("log")# mkaes big nums smaller and more evenly and precisely shown on the digram. alevel stats trick lmfao u all know
plt.xlabel("Number of simulations")
plt.ylabel("Call option price")
plt.title("Monte Carlo Convergence")
plt.legend()
plt.grid(True)
plt.savefig("monte_carlo_convergence.png",
    dpi=300,
    bbox_inches="tight")

plt.show()