# Arithmetic Asian Option
import math
import random
import numpy as np

import asian_geometric  # use Geometric Asian


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

        else:  # put
            arith_payoff.append(max(math.exp(-r * T) * (K - arith_average), 0))
            geo_payoff.append(max(math.exp(-r * T) * (K - geo_average), 0))

    # Arithmetic mean
    arith_mean = np.mean(np.array(arith_payoff))
    arith_std = np.std(np.array(arith_payoff))

    # Geometric mean
    geo_mean = np.mean(np.array(geo_payoff))
    geo_std = np.std(np.array(geo_payoff))

    # Control Variate
    cov_xy = np.mean(np.array(arith_payoff) * np.array(geo_payoff)) - geo_mean * arith_mean
    theta = cov_xy / math.pow(geo_std, 2)

    # control variate version
    if variate == 0:  # no control variate,
        a = arith_mean - 1.96 * arith_std / math.sqrt(path)
        b = arith_mean + 1.96 * arith_std / math.sqrt(path)
        return "[" + str(a) + "," + str(b) + "]"
    elif variate == 1:  # geometric Asian option
        z_sum = np.array(arith_payoff) + theta * (geo_asian_price - np.array(geo_payoff))
        z_mean = np.mean(z_sum)
        z_std = np.std(z_sum)
        a = z_mean - 1.96 * z_std / math.sqrt(path)
        b = z_mean + 1.96 * z_std / math.sqrt(path)
        return "[" + str(a) + "," + str(b) + "]"
