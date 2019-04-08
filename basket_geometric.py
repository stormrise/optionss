

# import decimal
import math
# from symtable import Symbol
from scipy import stats
# import random
from sympy import *


def price(S1, S2, sigma1, sigma2, rho, r, T, K, option_type):
    S1_ = float(S1)
    S2_ = float(S2)
    sigma1_ = float(sigma1)
    sigma2_ = float(sigma2)
    rho_ = float(rho)
    r_ = float(r)
    T_ = float(T)
    K_ = float(K)
    type_ = option_type

    sigma_ = math.sqrt(sigma1_*sigma1_+sigma2_*sigma2_+2 * sigma1_*sigma2_*rho_) / 2
    mean = r_ - 0.5 * (sigma1_ * sigma1_ + sigma2_ * sigma2_) / 2 + 0.5 * sigma_ * sigma_

    Bg0 = math.sqrt(S1_*S2_)
    d1 = (math.log(Bg0 / K_) + (mean + 0.5 * math.pow(sigma_, 2)) * T_) / \
        (sigma_ * math.sqrt(T_))
    d2 = d1-sigma_ * math.sqrt(T_)

    if type_ == "call":
        call_price = math.exp(-r_ * T_) * (Bg0 * math.exp(mean * T_) *
                                       stats.norm.cdf(d1) - K_ * stats.norm.cdf(d2))
        return(call_price)
    else:
        put_price = math.exp(-r_ * T_) * (K_ * stats.norm.cdf(-d2) -
                                       Bg0 * math.exp(mean * T_) * stats.norm.cdf(-d1))
        return(put_price)
