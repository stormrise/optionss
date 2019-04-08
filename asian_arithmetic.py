# Arithmetic Asian Option
import asian_geometric  # use Geometric Asian
# import decimal
import math
# from symtable import Symbol
# from scipy import stats
import random
from sympy import *
import numpy as np


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
    geo_asian_price = asian_geometric.price(S, sigma, r, T, K, n, option_type)

    # pre-define variables and lists
    dt = T / n
    spath = [0 for x in range(0, path)]
    arith_payoff = []
    geo_payoff = []
    # Z = [0 for x in range(0, path + 1)]
    # num = 1
    # j = 2
    # geo = 0
    # geo_sum = 0
    # geo_std = 0
    # arith = 0
    # arith_sum = 0
    # arith_std = 0
    # xSum = 0
    # z_sum = 0
    # z_std = 0

    #
    drift = math.exp((r - 0.5 * math.pow(sigma, 2)) * dt)
    for num in range(path):
        growth = drift * math.exp(sigma * math.sqrt(dt) * random.gauss(0, 1))
        spath[0] = S * growth
        arith = spath[0]
        geo = spath[0]
        for j in range(1, n):
            growth = drift * math.exp(sigma * math.sqrt(dt) * random.gauss(0, 1))
            spath[j] = spath[j - 1] * growth
            arith = arith + spath[j]
            geo = geo * spath[j]
        arith_average = arith / n
        geo_average = math.pow(geo, 1 / n)
        if option_type == "call":
            arith_payoff.append(max(math.exp(-r * T) * (arith_average - K), 0))
            geo_payoff.append(max(math.exp(-r * T) * (geo_average - K), 0))
            """if arith_average > K:
                arith_payoff[num] = math.exp(-r*T)*(arith_average-K)
            else:
                arith_payoff[num] = 0
            if geo_average > K:
                geo_payoff[num] = math.exp(-r*T)*(geo_average-K)
            else:
                geo_payoff[num] = 0"""
        else:  # put
            arith_payoff.append(max(math.exp(-r * T) * (K - arith_average), 0))
            geo_payoff.append(max(math.exp(-r * T) * (K - geo_average), 0))
            """if arith_average < K:
                arith_payoff[num] = math.exp(-r * T) * (K - arith_average)
            else:
                arith_payoff[num] = 0
            if geo_average < K:
                geo_payoff[num] = math.exp(-r * T) * (K - geo_average)
            else:
                geo_payoff[num] = 0"""

    # Arithmetic mean
    arith_mean = np.mean(np.array(arith_payoff))
    arith_std = np.std(np.array(arith_payoff))
    """for i in range(1, path + 1):
        arith_sum += arith_payoff[i]
    arith_mean = arith_sum / path
    for i in range(1, path + 1):
        arith_std = arith_std + math.pow((arith_payoff[i] - arith_mean), 2)
    arith_std = math.pow(arith_std / path, 1 / 2)"""
    # Geometric mean
    geo_mean = np.mean(np.array(geo_payoff))
    geo_std = np.std(np.array(geo_payoff))
    """for i in range(1, path + 1):
        geo_sum += geo_payoff[i]
    geo_mean = geo_sum / path
    for i in range(1, path + 1):
        geo_std = geo_std + math.pow((geo_payoff[i] - geo_mean), 2)
    geo_std = math.pow(geo_std / path, 1 / 2)"""
    # Control Variate
    """for i in range(1, path + 1):
        xSum += arith_payoff[i] * geo_payoff[i]
    xMean = xSum / path"""
    cov_xy = np.mean(np.array(arith_payoff) * np.array(geo_payoff)) - geo_mean * arith_mean
    theta = cov_xy / math.pow(geo_std, 2)

    # control variate version
    if variate == 0:  # no control variate,
        a = arith_mean - 1.96 * arith_std / math.sqrt(path)
        b = arith_mean + 1.96 * arith_std / math.sqrt(path)
        return "[" + str(a) + "," + str(b) + "]"
    elif variate == 1:  # geometric Asian option
        """for i in range(1, path + 1):
            Z[i] = arith_payoff[i] + theta * (geo_asian_price - geo_payoff[i])
            zSum += Z[i]"""
        z_sum = np.array(arith_payoff) + theta * (geo_asian_price - np.array(geo_payoff))
        z_mean = np.mean(z_sum)
        """for j in range(1, path + 1):
            z_std += math.pow((Z[j] - z_mean), 2)"""
        z_std = np.std(z_sum)
        a = z_mean - 1.96 * z_std / math.sqrt(path)
        b = z_mean + 1.96 * z_std / math.sqrt(path)
        return "[" + str(a) + "," + str(b) + "]"
