import numpy as np
import matplotlib.pyplot as plt

from black_scholes import black_scholes_call

K = 100
r = 0.05
sigma = 0.20
T = 1

stock_prices = np.linspace(50, 150, 100)

call_prices = []

for S in stock_prices:
    price = black_scholes_call(S, K, r, sigma, T)
    call_prices.append(price)


plt.plot(stock_prices, call_prices)

plt.axvline( K,
    color="red",
    linestyle="--",
    label="Strike price")

plt.xlabel("Stock price")
plt.ylabel("Call option price")
plt.title("Call Option Price Against Stock Price")
plt.legend()
plt.grid(True)

plt.show()