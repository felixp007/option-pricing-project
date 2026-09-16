import numpy as np
from black_scholes import black_scholes_call

def monte_carlo_call(
    S, K, r, sigma, T, num_simulations, seed=42
):# for seed here i acc didnt rlly used it on the first trial of writing this cuz i think its should be com random.
    # but seed can make sure its random and starting from same point every time. its is not reducing randomness but just
    #making this experiment repeatble. ie every result generatred from python is same but random. pseudo-random nums has
    #this thing with computers. so ive changed it but future i could change the seeds to do a robustness check tho. right now
    #its just making it more convenient and reduce random error.
    rng = np.random.default_rng(seed) #rng here for generaitng random nums

    Z = rng.standard_normal(num_simulations) # standard normal dis Z~N(0,1)m pos goes towards pos market and vice versa
    terminal_prices = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    payoffs = np.maximum( terminal_prices - K,0 )
    discounted_payoffs = (np.exp(-r * T) * payoffs)
    # as pay off is one yr later so future money will be more. therefore exponentially cal
    #the today's price with ir.
    #standard error=standard deviation/sqrtNum
    option_price = np.mean(discounted_payoffs)
    standard_error = (np.std(discounted_payoffs, ddof=1) / np.sqrt(num_simulations) )

    return option_price, standard_error

if __name__ == "__main__":
    S = 100
    K = 100
    r = 0.05
    sigma = 0.20
    T = 1

    black_scholes_price = black_scholes_call( S, K, r, sigma, T)
    for M in [10, 100, 1_000, 10_000, 100_000]:
        monte_carlo_price, standard_error = (monte_carlo_call(S, K, r, sigma, T, M ) )
        print(f"Simulations = {M:>6} | "
            f"Monte Carlo = {monte_carlo_price:.4f} | "
            f"Standard error = {standard_error:.4f}" )


    print( f"\nBlack-Scholes price = "
        f"{black_scholes_price:.4f}")
