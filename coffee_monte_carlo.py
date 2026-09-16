import numpy as np

from coffee_black76 import black76_call
from coffee_futures import futures_price


def monte_carlo_futures_call(futures_price_value,strike_price,risk_free_rate,volatility
    ,time_to_maturity,num_simulations,seed=42):
    rng = np.random.default_rng(seed)
    Z = rng.standard_normal(num_simulations)
    #one thing here is just the monte carlo formula is different!!! cuz theres no extra rT term.
    terminal_futures_prices = futures_price_value * np.exp(-0.5 * volatility**2 * time_to_maturity + volatility
    * np.sqrt(time_to_maturity) * Z)
    payoffs = np.maximum(terminal_futures_prices - strike_price,0)
    discounted_payoffs = np.exp(-risk_free_rate * time_to_maturity) * payoffs
    option_price = np.mean(discounted_payoffs)
    standard_error = np.std(discounted_payoffs,ddof=1) / np.sqrt(num_simulations)
    return option_price, standard_error


if __name__ == "__main__":
    spot_price = 1.20
    risk_free_rate = 0.02
    storage_cost = 0.01
    time_to_maturity = 0.5
    strike_price = 1.25
    volatility = 0.25

    fair_futures_price = futures_price(spot_price, risk_free_rate, storage_cost, time_to_maturity)
    black76_price = black76_call(fair_futures_price, strike_price, risk_free_rate, volatility, time_to_maturity)

    for M in [1_000, 10_000, 100_000]:
        #here for the result is easier to read define the result from monte_carlo_futrue_calls lioke the results respetively
        #price and error, which correspodns to the results retured above ie option_price and standard_error. so it is
        #perfectly matched with the results from above, ie the order is right.
        monte_carlo_price, monte_carlo_error = monte_carlo_futures_call(fair_futures_price,
        strike_price, risk_free_rate, volatility, time_to_maturity, M, seed=42)
    print(f"Simulations = {M:>6} | Monte Carlo = ${monte_carlo_price:.4f} | Standard error = ${monte_carlo_error:.4f}")

    print(f"\nBlack-76 price = ${black76_price:.4f}")