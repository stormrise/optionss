import basket
import decimal
import math
from symtable import Symbol
from scipy import stats
import random
from sympy import *


def price(path1, S3, S4, vol3, vol4, p1, r1, T1, K1, type1, variate1):
    path = int(path1)
    S1 = float(S3)
    S2 = float(S4)
    vol1 = float(vol3)
    vol2 = float(vol4)
    p = float(p1)
    r = float(r1)
    T = float(T1)
    K = float(K1)
    type = type1
    variate = int(variate1)
    arithpayoff = [0 for x in range(0, path+1)]
    geopayoff = [0 for x in range(0, path+1)]
    Z = [0 for x in range(0, path+1)]
    arithsum = 0
    geosum = 0
    arithstd = 0
    geostd = 0
    xsum = 0
    zsum = 0
    zstd = 0
    bprice = basket.price(S1, S2, vol1, vol2, p, r, T, K, type)
    drift1 = math.exp((r - 0.5 * math.pow(vol1, 2)) * T)
    drift2 = math.exp((r - 0.5 * math.pow(vol2, 2)) * T)
    for num in range(1, path+1):
        x = random.gauss(0, 1)
        growth1 = drift1*math.exp(vol1*math.sqrt(T)*x)
        growth2 = drift2 * \
            math.exp(vol2*math.sqrt(T) *
                     (p*x+math.sqrt(1-math.pow(p, 2))*random.gauss(0, 1)))
        M1 = S1*growth1
        M2 = S2*growth2
        M = (M1+M2)/2
        N = math.sqrt(M1*M2)
        if type == "call":
            if(M > K):
                arithpayoff[num] = math.exp(-r*T)*(M-K)
                arithsum += arithpayoff[num]
            else:
                arithpayoff[num] = 0
            if (N > K):
                geopayoff[num] = math.exp(-r*T)*(N-K)
                geosum += geopayoff[num]
            else:
                geopayoff[num] = 0
        else:
            if (M < K):
                arithpayoff[num] = math.exp(-r * T) * (K-M)
                arithsum += arithpayoff[num]
            else:
                arithpayoff[num] = 0
            if (N < K):
                geopayoff[num] = math.exp(-r * T) * (K-N)
                geosum += geopayoff[num]
            else:
                geopayoff[num] = 0
    arithmean = arithsum/path
    geomean = geosum/path
    for i in range(1, path+1):
        arithstd = arithstd + math.pow((arithpayoff[i] - arithmean), 2)
        geostd = geostd + math.pow((geopayoff[i] - geomean), 2)
        xsum += arithpayoff[i] * geopayoff[i]
    arithstd = math.sqrt(arithstd/path)
    geostd = math.sqrt(geostd/path)
    xmean = xsum/path
    covxy = xmean-geomean*arithmean
    theta = covxy/math.pow(geostd, 2)
    if variate == 1:
        for i in range(1, path+1):
            Z[i] = arithpayoff[i]+theta*(bprice - geopayoff[i])
            zsum += Z[i]
        zmean = zsum/path
        for j in range(1, path+1):
            zstd += math.pow((Z[j]-zmean), 2)
        zstd = math.pow(zstd/path, 1/2)
        a = zmean - 1.96 * zstd / math.sqrt(path)
        c = str(a)
        b = zmean + 1.96 * zstd / math.sqrt(path)
        d = str(b)
        return c + "---" + d
    elif variate == 0:
        a = arithmean - 1.96 * arithstd / math.sqrt(path)
        c = str(a)
        b = arithmean + 1.96 * arithstd / math.sqrt(path)
        d = str(b)
        return c+"---"+d
