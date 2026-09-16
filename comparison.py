from ipaddress import summarize_address_range

import matplotlib.pyplot as plt
from black_scholes import black_scholes_call
from binomial_tree import binomial_call
from monte_carlo import monte_carlo_call

S = 100
K = 100
r = 0.05
sigma = 0.20
T = 1

N = 1000
M = 100000

black_scholes_price = black_scholes_call(S, K, r, sigma, T)
binomial_price = binomial_call(S, K, r, sigma, T, N)
monte_carlo_price, monte_carlo_error = monte_carlo_call(S, K, r, sigma, T, M, seed=42)

print(f"Black-Scholes price: {black_scholes_price:.4f}")
print(f"Binomial Tree price: {binomial_price:.4f}")
print(f"Monte Carlo price: {monte_carlo_price:.4f}")
print(f"Monte Carlo standard error: {monte_carlo_error:.4f}")

methods = ["Black-Scholes","Binomial Tree","Monte Carlo"] #still a list omds i forgot abt ts 1000 times
prices = [ black_scholes_price,binomial_price, monte_carlo_price]
errors = [ 0, 0, monte_carlo_error] # bs and bt have zero error!

plt.bar(methods,
    prices,
    yerr=errors,
    capsize=5,
    color=["red", "blue", "green"])
plt.ylabel("Call option price")
plt.title("Comparison of Option Pricing Methods")
plt.grid(axis="y")
plt.savefig("option_pricing_comparison.png",
    dpi=300,
    bbox_inches="tight")
plt.show()
