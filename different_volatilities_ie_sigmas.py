import numpy as np
import matplotlib.pyplot as plt
from black_scholes import black_scholes_call
K = 100
r = 0.05
T = 1

stock_prices = np.linspace(50, 150, 100)

volatilities = [0.10, 0.20, 0.30, 0.40]

for sigma in volatilities:
    call_prices = []
    for S in stock_prices:
        price = black_scholes_call(S, K, r, sigma, T)
        call_prices.append(price)

    plt.plot( stock_prices,
        call_prices,
        label=f"Volatility = {sigma:.0%}")

plt.axvline(K,
    color="black",
    linestyle="--",
    label="Strike price")

plt.xlabel("Stock price")
plt.ylabel("Call option price")
plt.title("Effect of Volatility on Call Option Prices")
plt.legend()
plt.grid(True)
plt.savefig("call_price_volatility_analysis.png",
    dpi=300,
    bbox_inches="tight")
plt.show()

#therefore conlusion: higher volatility generally increases the value of a European call option.