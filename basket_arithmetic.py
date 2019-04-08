import math
import random
from sympy import *
import numpy as np

import basket_geometric


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
    arith_payoff = []
    geo_payoff = []
    # Z = []
    # arith_sum = 0
    # geo_sum = 0
    # arith_std = 0
    # geo_std = 0
    # x_sum = 0
    # z_sum = 0
    # z_std = 0
    basket_price = basket_geometric.price(S1_, S2_, sigma1_, sigma2_, rho_, r_, T_, K_, type_)
    drift1 = math.exp((r_ - 0.5 * sigma1_ ** 2) * T_)
    drift2 = math.exp((r_ - 0.5 * sigma2_ ** 2) * T_)
    for num in range(path_):
        x = random.gauss(0, 1)
        y = random.gauss(0, 1)
        growth_factor1 = drift1 * math.exp(sigma1_ * math.sqrt(T_) * x)
        """We have improved in assignment 2 (2.1) that if X and Y are two independent standard normal random variables,\
        and Z = rho * X + sqrt(1 - rho ^ 2) * Y, then the correlation coefficient between X and Z is rho.
        """
        growth_factor2 = drift2 * \
                         math.exp(sigma2_ * math.sqrt(T_) *
                                  (rho_ * x + math.sqrt(1 - rho_ ** 2) * y))
        M1 = S1_ * growth_factor1
        M2 = S2_ * growth_factor2
        M = (M1 + M2) / 2
        N = math.sqrt(M1 * M2)
        if type_ == "call":
            arith_payoff.append(max(math.exp(-r_ * T_) * (M - K_), 0))
            geo_payoff.append(max(math.exp(-r_ * T_) * (N - K_), 0))
            """if(M > K_):
                arith_payoff.append(math.exp(-r_*T_)*(M-K_))
                arith_sum += arith_payoff[num]
            else:
                arith_payoff.append(0)
            if (N > K_):
                geo_payoff[num] = math.exp(-r_*T_)*(N-K_)
                geo_sum += geo_payoff[num]
            else:
                geo_payoff[num] = 0"""
        else:
            arith_payoff.append(max(math.exp(-r_ * T_) * (K_ - M), 0))
            geo_payoff.append(max(math.exp(-r_ * T_) * (K_ - N), 0))
            """if (M < K_):
                arith_payoff[num] = math.exp(-r_ * T_) * (K_-M)
                arith_sum += arith_payoff[num]
            else:
                arith_payoff[num] = 0
            if (N < K_):
                geo_payoff[num] = math.exp(-r_ * T_) * (K_-N)
                geo_sum += geo_payoff[num]
            else:
                geo_payoff[num] = 0"""
    # arith_mean = arith_sum/path_
    arith_mean = np.mean(np.array(arith_payoff))
    # geo_mean = geo_sum/path_
    geo_mean = np.mean(np.array(geo_payoff))
    """for i in range(1, path_+1):
        arith_std += math.pow((arith_payoff[i] - arith_mean), 2)
        geo_std += math.pow((geo_payoff[i] - geo_mean), 2)
        x_sum += arith_payoff[i] * geo_payoff[i]"""
    arith_std = np.std(np.array(arith_payoff))
    # arith_std = math.sqrt(arith_std / path_)
    geo_std = np.std(np.array(geo_payoff))
    # geo_std = math.sqrt(geo_std / path_)
    # x_mean = x_sum / path_
    cov_xy = np.mean(np.array(arith_payoff) * np.array(geo_payoff)) - geo_mean * arith_mean
    theta = cov_xy / np.var(np.array(geo_payoff))
    if variate_ == 1:
        """for i in range(1, path_+1):
            Z[i] = arith_payoff[i] + theta * (basket_price - geo_payoff[i])
            z_sum += Z[i]"""
        Z = np.array(arith_payoff) + theta * (basket_price - np.array(geo_payoff))
        z_mean = np.mean(Z)
        # z_mean = z_sum/path_
        """for i in range(1, path_+1):
            z_std += math.pow((Z[i] - z_mean), 2)"""
        z_std = np.std(Z)
        # z_std = math.sqrt(z_std / path)
        return "[" + str(z_mean - 1.96 * z_std / math.sqrt(path_)) + ", " \
               + str(z_mean + 1.96 * z_std / math.sqrt(path_)) + "]"
    elif variate_ == 0:
        """a = arith_mean - 1.96 * arith_std / math.sqrt(path_)
        c = str(a)
        b = arith_mean + 1.96 * arith_std / math.sqrt(path_)
        d = str(b)"""
        return "[" + str(arith_mean - 1.96 * arith_std / math.sqrt(path_)) + ", " \
               + str(arith_mean + 1.96 * arith_std / math.sqrt(path_)) + "]"
