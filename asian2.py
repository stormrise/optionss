
import asian
import decimal
import math
from symtable import Symbol
from scipy import stats
import random
from sympy import *


def price(path1, S1, vol1, r1, T1, K1, n1, type1, variate1):
    path = int(path1)
    S = float(S1)
    vol = float(vol1)
    r = float(r1)
    T = float(T1)
    K = float(K1)
    n = int(n1)
    type = type1
    variate = int(variate1)
    aprice = asian.price(S, vol, r, T, K, n, type)
    dt = T/n
    spath = [0 for x in range(0, path+1)]
    arithpayoff = [0 for x in range(0, path+1)]
    geopayoff = [0 for x in range(0, path+1)]
    Z = [0 for x in range(0, path+1)]
    num = 1
    j = 2
    geo = 0
    arith = 0
    arithsum = 0
    arithstd = 0
    geosum = 0
    geostd = 0
    xsum = 0
    zsum = 0
    zstd = 0
    drift = math.exp((r-0.5*math.pow(vol, 2))*dt)
    for num in range(1, path+1):
        growth = drift*math.exp(vol*math.sqrt(dt)*random.gauss(0, 1))
        spath[1] = S*growth
        arith = spath[1]
        geo = spath[1]
        for j in range(2, n+1):
            growth = drift * math.exp(vol * math.sqrt(dt) * random.gauss(0, 1))
            spath[j] = spath[j-1]*growth
            arith = arith+spath[j]
            geo = geo*spath[j]
        arithaverage = arith/n
        geoaverage = math.pow(geo, 1/n)
        if type == "call":
            if arithaverage > K:
                arithpayoff[num] = math.exp(-r*T)*(arithaverage-K)
            else:
                arithpayoff[num] = 0
            if geoaverage > K:
                geopayoff[num] = math.exp(-r*T)*(geoaverage-K)
            else:
                geopayoff[num] = 0
        else:
            if arithaverage < K:
                arithpayoff[num] = math.exp(-r * T) * (K - arithaverage)
            else:
                arithpayoff[num] = 0
            if geoaverage < K:
                geopayoff[num] = math.exp(-r * T) * (K - geoaverage)
            else:
                geopayoff[num] = 0

    for i in range(1, path+1):
        arithsum += arithpayoff[i]
    arithmean = arithsum/path
    for i in range(1, path+1):
        arithstd = arithstd + math.pow((arithpayoff[i]-arithmean), 2)
    arithstd = math.pow(arithstd/path, 1/2)
    for i in range(1, path+1):
        geosum += geopayoff[i]
    geomean = geosum/path
    for i in range(1, path+1):
        geostd = geostd + math.pow((geopayoff[i]-geomean), 2)
    geostd = math.pow(geostd/path, 1/2)
    for i in range(1, path+1):
        xsum += arithpayoff[i]*geopayoff[i]
    xmean = xsum/path
    covxy = xmean-geomean*arithmean
    theta = covxy/math.pow(geostd, 2)

    if variate == 0:
        a = arithmean - 1.96 * arithstd / math.sqrt(path)
        c = str(a)
        b = arithmean + 1.96 * arithstd / math.sqrt(path)
        d = str(b)
        return c + "---" + d
    elif variate == 1:
        for i in range(1, path + 1):
            Z[i] = arithpayoff[i] + theta * (aprice - geopayoff[i])
            zsum += Z[i]
        zmean = zsum / path
        for j in range(1, path + 1):
            zstd += math.pow((Z[j] - zmean), 2)
        zstd = math.pow(zstd/path, 1 / 2)
        e = str(zmean)
        f = str(zstd)
        a = zmean - 1.96*zstd/math.sqrt(path)
        c = str(a)
        b = zmean + 1.96*zstd/math.sqrt(path)
        d = str(b)
        return c + "---" + d
