import math
from black_scholes import black_scholes_call

def binomial_call(S, K, r, sigma, T, N):

    #price a European call option using a Cox-Ross-Rubinstein binomial tree.
    #there will be N intervals assume so each interval has dt
    dt = T / N
    # Up and down factors, up is p going up and d is p going down
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    # Risk-neutral probability
    p = (math.exp(r * dt) - d) / (u - d)
    discount_factor = math.exp(-r * dt)

    # calculate option payoffs at maturity
    option_values = []
    # so it can be either going up ie u or down ie d.
    #so it can be N, 0 or N-1, 1 or N-2 ,2 and so on.
    # N=2 eg. so like 2 falls results in 81 quid eg, and 1 fall result in 99 quid
    #but both below 100 so payoff is 0. but 2 increaes results in 121 quid so 21 payoff
    for i in range(N + 1):
        stock_price = S * (u ** i) * (d ** (N - i))
        payoff = max(stock_price - K, 0)
        option_values.append(payoff)

    # backwards, so basically on the final date will be 3 results of payoff
    #eg N=2. two results after that so 00 results in 0 and 0 21 retuls in 10.5 .so on applies
    for step in range(N - 1, -1, -1):
        new_values = []

        for j in range(step + 1):
            expected_value = ( p * option_values[j + 1]+ (1 - p) * option_values[j])
            discounted_value = discount_factor * expected_value
            new_values.append(discounted_value)

        option_values = new_values

    return option_values[0]

if __name__ == "__main__":
    S = 100
    K = 100
    r = 0.05
    sigma = 0.20
    T = 1
    N = 100
    binomial_price = binomial_call( S, K, r, sigma, T, N )
    black_scholes_price = black_scholes_call(  S, K, r, sigma, T )
    print(f"binomial Tree price: {binomial_price:.4f}")
    print(f"black-Scholes price: {black_scholes_price:.4f}")