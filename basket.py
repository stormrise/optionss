

import decimal
import math
from symtable import Symbol
from scipy import stats
import random
from sympy import *


def price(S3, S4, vol3, vol4, p1, r1, T1, K1, type1):
    S1 = float(S3)
    S2 = float(S4)
    vol1 = float(vol3)
    vol2 = float(vol4)
    p = float(p1)
    r = float(r1)
    T = float(T1)
    K = float(K1)
    type = type1

    vol = math.sqrt(vol1*vol1+vol2*vol2+vol1*vol2*p+vol2*vol1*p)/2
    mean = r-0.5*(vol1*vol1+vol2*vol2)/2+0.5*vol*vol

    S = math.sqrt(S1*S2)
    d1 = (math.log(S / K) + (mean + 0.5 * math.pow(vol, 2)) * T) / \
        (vol * math.sqrt(T))
    d2 = d1-vol * math.sqrt(T)
    cprice = math.exp(-r * T) * (S*math.exp(mean*T) *
                                 stats.norm.cdf(d1) - K * stats.norm.cdf(d2))
    pprice = math.exp(-r * T) * (K * stats.norm.cdf(-d2) -
                                 S*math.exp(mean*T)*stats.norm.cdf(-d1))
    if type == "call":
        return(cprice)
    else:
        return(pprice)
