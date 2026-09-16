import matplotlib.pyplot as plt
from black_scholes import black_scholes_call
from binomial_tree import binomial_call
S = 100
K = 100
r = 0.05
sigma = 0.20
T = 1
number_of_steps = [5, 10, 25, 50, 100, 250, 500, 1000]
black_scholes_price = black_scholes_call( S, K, r, sigma, T)
binomial_prices = []
for N in number_of_steps:
    price = binomial_call( S, K, r, sigma, T, N )
    binomial_prices.append(price)
    print(f"N = {N:4d} | "
        f"binomial price = {price:.4f} | "
        f"difference = {price - black_scholes_price:.4f}")
plt.plot( number_of_steps,
    binomial_prices,
    marker="o",
    label="binomial tree")
plt.axhline(black_scholes_price,
    color="red",
    linestyle="--",
    label="black-scholes price")
plt.xlabel("number of time steps")
plt.ylabel("call option price")
plt.title("convergence of the Binomial Tree Price")
plt.legend()
plt.grid(True)
plt.savefig(    "binomial_convergence.png",
    dpi=300,
    bbox_inches="tight")
plt.show()