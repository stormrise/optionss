

import decimal
import math
from symtable import Symbol
from scipy import stats
from sympy import *


def price(S1, vol1, r1, T1, K1, type1):
    S = float(S1)
    vol = float(vol1)
    r = float(r1)
    T = float(T1)
    K = float(K1)
    type = type1

    d1 = (math.log(S / K) + r * T) / \
        (vol * math.sqrt(T)) + 0.5 * (vol * math.sqrt(T))
    d2 = (math.log(S / K) + r * T) / \
        (vol * math.sqrt(T)) - 0.5 * (vol * math.sqrt(T))
    cprice = S * stats.norm.cdf(d1) - K*math.exp(-r*T) * stats.norm.cdf(d2)
    pprice = K*math.exp(-r*T) * stats.norm.cdf(-d2) - S * stats.norm.cdf(-d1)
    if type == "call":
        return cprice
    else:
        return pprice
