import math
from scipy import stats


def price_call(S, K, T, vol, r, q):
    d1 = (math.log(S / K) + (r - q) * T) / \
         (vol * math.sqrt(T)) + 0.5 * (vol * math.sqrt(T))
    d2 = (math.log(S / K) + (r - q) * T) / \
         (vol * math.sqrt(T)) - 0.5 * (vol * math.sqrt(T))
    # C(σ)
    C = S * math.exp(-q * T) * stats.norm.cdf(d1) - K * \
        math.exp(-r * T) * stats.norm.cdf(d2)
    return C


def price_put(S, K, T, vol, r, q):
    d1 = (math.log(S / K) + (r - q) * T) / \
         (vol * math.sqrt(T)) + 0.5 * (vol * math.sqrt(T))
    d2 = (math.log(S / K) + (r - q) * T) / \
         (vol * math.sqrt(T)) - 0.5 * (vol * math.sqrt(T))
    P = K * math.exp(-r * T) * stats.norm.cdf(-d2) - S * \
        math.exp(-q * T) * stats.norm.cdf(-d1)
    return P


def vega_call(S, K, T, vol, r, q):
    d1 = (math.log(S / K) + (r - q) * T) / \
         (vol * math.sqrt(T)) + 0.5 * (vol * math.sqrt(T))
    # b = stats.norm.pdf(d1)
    vega = S * math.exp(-q * T) * math.sqrt(T) / \
           math.sqrt(2 * math.pi) * math.exp(-(d1 ** 2) * 0.5)
    return vega


def price(S1, Strue, r1, T1, K1, q1, type1):
    S = float(S1)
    r = float(r1)
    T = float(T1)
    K = float(K1)
    q = float(q1)
    type = type1
    cbidtrue = float(Strue)
    sigmahat = math.sqrt(2 * abs((math.log(S / K) + (r - q) * T) / T))
    sigma = sigmahat
    tol = 10 ** (-8)
    n = 1
    nmax = 10000
    sigmadiff = 1

    while n < nmax and sigmadiff >= tol:
        vega = vega_call(S, K, T, sigma, r, q)
        if type == "call":
            C = price_call(S, K, T, sigma, r, q)
        else:
            C = price_put(S, K, T, sigma, r, q)
        increment = (C - cbidtrue) / vega
        sigma = sigma - increment
        n = n + 1
        sigmadiff = abs(increment)

    if sigmadiff > 1 or sigmadiff is None:
        return "no convergence"
    else:
        return sigma
