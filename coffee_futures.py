import math
#cost-of-carry model
def futures_price(spot_price,risk_free_rate,storage_cost,time_to_maturity,convenience_yield=0):
    futures_price = spot_price * math.exp((risk_free_rate+ storage_cost- convenience_yield)* time_to_maturity)
    return futures_price

if __name__ == "__main__": # testing function so only works in this test but cant be imported
    spot_price = 1.20
    risk_free_rate = 0.02
    storage_cost = 0.01
    time_to_maturity = 0.5

    fair_futures_price = futures_price(spot_price,risk_free_rate,storage_cost,time_to_maturity )

    print(f"Fair futures price: "f"${fair_futures_price:.4f} per pound")