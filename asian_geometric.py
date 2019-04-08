# Geometric Asian Option
import math
from scipy import stats
from sympy import *


def price(S1, sigma1, r1, T1, K1, n1, option_type1):
    S = float(S1)
    sigma = float(sigma1)
    r = float(r1)
    T = float(T1)
    K = float(K1)
    n = int(n1)  # geometric average n
    option_type = option_type1

    sigmahat = sigma * math.sqrt((n + 1) * (2 * n + 1) / (6 * math.pow(n, 2)))
    mu = (r - 0.5 * math.pow(sigma, 2)) * (n + 1) / \
         (2 * n) + 0.5 * math.pow(sigmahat, 2)
    d1 = (math.log(S / K) + (mu + 0.5 * math.pow(sigmahat, 2)) * T) / \
         (sigmahat * math.sqrt(T))
    d2 = d1 - sigmahat * math.sqrt(T)

    if option_type == "call":
        call_price = math.exp(-r * T) * (S * math.exp(mu * T) * stats.norm.cdf(d1) - K * stats.norm.cdf(d2))
        return call_price
    else:  # put
        put_price = math.exp(-r * T) * (K * stats.norm.cdf(-d2) - S * math.exp(mu * T) * stats.norm.cdf(-d1))
        return put_price
