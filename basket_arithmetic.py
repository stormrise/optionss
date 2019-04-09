import math
import random
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

    random.seed(1234)
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
        else:
            arith_payoff.append(max(math.exp(-r_ * T_) * (K_ - M), 0))
            geo_payoff.append(max(math.exp(-r_ * T_) * (K_ - N), 0))
    # arith_mean = arith_sum/path_
    arith_mean = np.mean(np.array(arith_payoff))
    # geo_mean = geo_sum/path_
    geo_mean = np.mean(np.array(geo_payoff))
    arith_std = np.std(np.array(arith_payoff))
    # arith_std = math.sqrt(arith_std / path_)
    geo_std = np.std(np.array(geo_payoff))
    cov_xy = np.mean(np.array(arith_payoff) * np.array(geo_payoff)) - geo_mean * arith_mean
    theta = cov_xy / np.var(np.array(geo_payoff))
    if variate_ == 1:
        Z = np.array(arith_payoff) + theta * (basket_price - np.array(geo_payoff))
        z_mean = np.mean(Z)
        z_std = np.std(Z)
        # z_std = math.sqrt(z_std / path)
        return "[" + str(z_mean - 1.96 * z_std / math.sqrt(path_)) + ", " \
               + str(z_mean + 1.96 * z_std / math.sqrt(path_)) + "]"
    elif variate_ == 0:
        return "[" + str(arith_mean - 1.96 * arith_std / math.sqrt(path_)) + ", " \
               + str(arith_mean + 1.96 * arith_std / math.sqrt(path_)) + "]"
