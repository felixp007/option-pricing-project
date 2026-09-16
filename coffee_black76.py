import math
from scipy.stats import norm
from coffee_futures import futures_price

#spec for this project as the subject is the FUTURE p of the coffees so traditional Black Scholes model cant be used
#anymore as it is for current price of a stock. therefore black-76 is used here to predict the future price of a stock
#considering all factors such as ir, cost of storing and convenience yield. 
def black76_call(futures_price_value,strike_price,risk_free_rate,volatility,time_to_maturity):
    d1 = (math.log(futures_price_value / strike_price)+ 0.5 * volatility**2 * time_to_maturity ) / (volatility * math.sqrt(time_to_maturity))
    d2 = d1 - volatility * math.sqrt(time_to_maturity)
    discount_factor = math.exp(-risk_free_rate * time_to_maturity)
    call_price = discount_factor * (futures_price_value * norm.cdf(d1)- strike_price * norm.cdf(d2))
    return call_price


if __name__ == "__main__":
    spot_price = 1.20
    risk_free_rate = 0.02
    storage_cost = 0.01
    time_to_maturity = 0.5
    strike_price = 1.25
    volatility = 0.25
    fair_futures_price = futures_price(spot_price, risk_free_rate,storage_cost,time_to_maturity)
    coffee_option_price = black76_call(fair_futures_price,strike_price,risk_free_rate,volatility,time_to_maturity)

    print( f"Fair futures price: "
        f"${fair_futures_price:.4f} per pound")

    print(f"Coffee call option price: "
        f"${coffee_option_price:.4f} per pound")