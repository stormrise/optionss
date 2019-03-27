import decimal
import math
from symtable import Symbol
from scipy import stats
from sympy import *


def price(S1, vol1, r1, T1, K1, n1, type1):
    S = float(S1)
    vol = float(vol1)
    r = float(r1)
    T = float(T1)
    K = float(K1)
    n = int(n1)
    type = type1

    volhat = vol*math.sqrt((n+1)*(2*n+1)/(6*math.pow(n, 2)))
    volmean = (r-0.5*math.pow(vol, 2))*(n+1)/(2*n)+0.5*math.pow(volhat, 2)
    d1 = (math.log(S / K) + (volmean+0.5*math.pow(volhat, 2)) * T) / \
        (volhat * math.sqrt(T))
    d2 = d1 - volhat*math.sqrt(T)
    cprice = math.exp(-r * T) * (S*math.exp(volmean*T) *
                                 stats.norm.cdf(d1) - K * stats.norm.cdf(d2))
    pprice = math.exp(-r * T) * (K * stats.norm.cdf(-d2)-S *
                                 math.exp(volmean*T)*stats.norm.cdf(-d1))
    if type == "call":
        return cprice
    else:
        return pprice
