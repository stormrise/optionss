# Arithmetic Asian Option
import asian_geometric  # use Geometric Asian
import decimal
import math
from symtable import Symbol
from scipy import stats
import random
from sympy import *


def price(path1, S1, sigma1, r1, T1, K1, n1, option_type1, variate1):
    path = int(path1)  # the number of paths in the Monte Carlo simulation
    S = float(S1)
    sigma = float(sigma1)
    r = float(r1)
    T = float(T1)
    K = float(K1)
    n = int(n1)  # geometric average n
    option_type = option_type1
    variate = int(variate1)
    # the control variate method
    # (no control variate, or geometric Asian option)

    # recall Geo_Asian
    geo_asian_price = asian.price(S, sigma, r, T, K, n, option_type)

    # pre-define variables and lists
    dt = T/n
    spath = [0 for x in range(0, path+1)]
    arithPayoff = [0 for x in range(0, path+1)]
    geoPayoff = [0 for x in range(0, path+1)]
    Z = [0 for x in range(0, path+1)]
    num = 1
    j = 2
    geo = 0
    geoSum = 0
    geoStd = 0
    arith = 0
    arithSum = 0
    arithStd = 0
    xSum = 0
    zSum = 0
    zStd = 0

    #
    drift = math.exp((r-0.5*math.pow(sigma, 2))*dt)
    for num in range(1, path+1):
        growth = drift * math.exp(sigma * math.sqrt(dt) * random.gauss(0, 1))
        spath[1] = S * growth
        arith = spath[1]
        geo = spath[1]
        for j in range(2, n+1):
            growth = drift * math.exp(sigma * math.sqrt(dt) * random.gauss(0, 1))
            spath[j] = spath[j-1] * growth
            arith = arith + spath[j]
            geo = geo * spath[j]
        arithaverage = arith/n
        geoaverage = math.pow(geo, 1/n)
        if option_type == "call":
            if arithaverage > K:
                arithPayoff[num] = math.exp(-r*T)*(arithaverage-K)
            else:
                arithPayoff[num] = 0
            if geoaverage > K:
                geoPayoff[num] = math.exp(-r*T)*(geoaverage-K)
            else:
                geoPayoff[num] = 0
        else:  # put
            if arithaverage < K:
                arithPayoff[num] = math.exp(-r * T) * (K - arithaverage)
            else:
                arithPayoff[num] = 0
            if geoaverage < K:
                geoPayoff[num] = math.exp(-r * T) * (K - geoaverage)
            else:
                geoPayoff[num] = 0

    # Arithmetic mean
    for i in range(1, path+1):
        arithSum += arithPayoff[i]
    arithMean = arithSum/path
    for i in range(1, path+1):
        arithStd = arithStd + math.pow((arithPayoff[i]-arithMean), 2)
    arithStd = math.pow(arithStd/path, 1/2)
    # Geometric mean
    for i in range(1, path+1):
        geoSum += geoPayoff[i]
    geoMean = geoSum/path
    for i in range(1, path+1):
        geoStd = geoStd + math.pow((geoPayoff[i]-geoMean), 2)
    geoStd = math.pow(geoStd/path, 1/2)
    # Control Variate
    for i in range(1, path+1):
        xSum += arithPayoff[i]*geoPayoff[i]
    xMean = xSum/path
    covXY = xMean - geoMean * arithMean
    theta = covXY/math.pow(geoStd, 2)

    # control variate version
    if variate == 0: # no control variate,
        a = arithMean - 1.96 * arithStd / math.sqrt(path)
        b = arithMean + 1.96 * arithStd / math.sqrt(path)
        return str(a) + "---" + str(b)
    elif variate == 1: # geometric Asian option
        for i in range(1, path + 1):
            Z[i] = arithPayoff[i] + theta * (geo_asian_price - geoPayoff[i])
            zSum += Z[i]
        zMean = zSum / path
        for j in range(1, path + 1):
            zStd += math.pow((Z[j] - zMean), 2)
        zStd = math.pow(zStd/path, 1 / 2)
        e = str(zMean)
        f = str(zStd)
        a = zMean - 1.96*zStd/math.sqrt(path)
        b = zMean + 1.96*zStd/math.sqrt(path)
        return str(a) + "---" + str(b)
