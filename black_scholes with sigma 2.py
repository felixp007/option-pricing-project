import math
from scipy.stats import norm

def black_scholes_call(S, K, r, sigma, T):
    #calculate the price of a European call option. all formula from bs
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    call_price = ( S * norm.cdf(d1)
        - K * math.exp(-r * T) * norm.cdf(d2))
    return call_price

def black_scholes_put(S, K, r, sigma, T):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    put_price = (  K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1) )
    return put_price

if __name__ == "__main__":
    S = 100
    K = 100
    r = 0.05
    sigma = 0.40  # volatility: 40 per
    T = 1

    call_price = black_scholes_call(S, K, r, sigma, T)
    put_price = black_scholes_put(S, K, r, sigma, T)

    print(f"Call option price: {call_price:.4f}")
    print(f"Put option price: {put_price:.4f}")