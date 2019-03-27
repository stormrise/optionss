import basket_geometric
import decimal
import math
from symtable import Symbol
from scipy import stats
import random
from sympy import *


def price(path, S1, S2, sigma1, sigma2, rho, r, T, K, option_type, variate):
    path_ = int(path)
    S1_ = float(S1)
    S2_ = float(S2)
    sigma1_ = float(sigma1)
    sigma2_ = float(sigma2)
    rho_ = float(rho)
    r_ = float(r)
    T_ = float(T)
    K_ = float(K)
    type_ = option_type
    variate_ = int(variate)
    arithpayoff = [0 for x in range(0, path_+1)]
    geopayoff = [0 for x in range(0, path_+1)]
    Z = [0 for x in range(0, path_+1)]
    arithsum = 0
    geosum = 0
    arithstd = 0
    geostd = 0
    xsum = 0
    zsum = 0
    zstd = 0
    bprice = basket_geometric.price(S1_, S2_, sigma1_, sigma2_, rho_, r_, T_, K_, type_)
    drift1 = math.exp((r_ - 0.5 * math.pow(sigma1_, 2)) * T_)
    drift2 = math.exp((r_ - 0.5 * math.pow(sigma2_, 2)) * T_)
    for num in range(1, path_+1):
        x = random.gauss(0, 1)
        growth1 = drift1*math.exp(sigma1_*math.sqrt(T_)*x)
        growth2 = drift2 * \
            math.exp(sigma2_*math.sqrt(T_) *
                     (rho_*x+math.sqrt(1-math.pow(rho_, 2))*random.gauss(0, 1)))
        M1 = S1_*growth1
        M2 = S2_*growth2
        M = (M1+M2)/2
        N = math.sqrt(M1*M2)
        if type_ == "call":
            if(M > K_):
                arithpayoff[num] = math.exp(-r_*T_)*(M-K_)
                arithsum += arithpayoff[num]
            else:
                arithpayoff[num] = 0
            if (N > K_):
                geopayoff[num] = math.exp(-r_*T_)*(N-K_)
                geosum += geopayoff[num]
            else:
                geopayoff[num] = 0
        else:
            if (M < K_):
                arithpayoff[num] = math.exp(-r_ * T_) * (K_-M)
                arithsum += arithpayoff[num]
            else:
                arithpayoff[num] = 0
            if (N < K_):
                geopayoff[num] = math.exp(-r_ * T_) * (K_-N)
                geosum += geopayoff[num]
            else:
                geopayoff[num] = 0
    arithmean = arithsum/path_
    geomean = geosum/path_
    for i in range(1, path_+1):
        arithstd = arithstd + math.pow((arithpayoff[i] - arithmean), 2)
        geostd = geostd + math.pow((geopayoff[i] - geomean), 2)
        xsum += arithpayoff[i] * geopayoff[i]
    arithstd = math.sqrt(arithstd/path_)
    geostd = math.sqrt(geostd/path_)
    xmean = xsum/path_
    covxy = xmean-geomean*arithmean
    theta = covxy/math.pow(geostd, 2)
    if variate_ == 1:
        for i in range(1, path_+1):
            Z[i] = arithpayoff[i]+theta*(bprice - geopayoff[i])
            zsum += Z[i]
        zmean = zsum/path_
        for j in range(1, path_+1):
            zstd += math.pow((Z[j]-zmean), 2)
        zstd = math.pow(zstd/path_, 1/2)
        a = zmean - 1.96 * zstd / math.sqrt(path_)
        c = str(a)
        b = zmean + 1.96 * zstd / math.sqrt(path_)
        d = str(b)
        return c + "---" + d
    elif variate_ == 0:
        a = arithmean - 1.96 * arithstd / math.sqrt(path_)
        c = str(a)
        b = arithmean + 1.96 * arithstd / math.sqrt(path_)
        d = str(b)
        return c+"---"+d
