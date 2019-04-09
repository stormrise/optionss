import math
from scipy import stats


def price(S1, sigma1, r1, T1, K1, type1, q1):
    S = float(S1)
    sigma = float(sigma1)
    r = float(r1)
    T = float(T1)
    K = float(K1)
    type = type1
    q = float(q1)

    d1 = (math.log(S / K) + (r - q) * T) / (sigma * math.sqrt(T)) + 0.5 * (sigma * math.sqrt(T))
    d2 = (math.log(S / K) + (r - q) * T) / (sigma * math.sqrt(T)) - 0.5 * (sigma * math.sqrt(T))

    if type == "call":
        call_price = S * math.exp(-q * T) * stats.norm.cdf(d1) - K * math.exp(-r * T) * stats.norm.cdf(d2)
        return call_price
    else:
        put_price = K * math.exp(-r * T) * stats.norm.cdf(-d2) - S * math.exp(-q * T) * stats.norm.cdf(-d1)
        return put_price
