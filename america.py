import decimal
import math
from symtable import Symbol
from scipy import stats
import random
import numpy as np
from sympy import *
def price(S1,vol1,r1,T1,K1,n1,type1):
    # parameters
    S = float(S1)
    vol = float(vol1)
    r = float(r1)
    T = float(T1)
    K = float(K1)
    n = int(n1)
    type = type1

    n= n+1
    price = [[0 for i in range(0,n+1)]for j in range(0,n+1)]
    optionprice = [[0 for i in range(0,n+1)]for j in range(0,n+1)]
    dt = T/(n-1)
    df = math.exp(-r*dt)
    # choosing u and d
    u = math.exp(vol*math.sqrt(dt))
    d = 1/u
    # calculate risk neutral probability
    p = (math.exp(r*dt)-d)/(u-d) 
    
    if type == "call":
        for num in range(1,n+1):
            for j in range(1,num+1):
                price[num][j]=S*math.pow(u,num-1)*math.pow(d,(j-1)*2)
                if price[num][j] > K:
                    optionprice[num][j] = price[num][j] - K
                else:
                    optionprice[num][j] = 0

        for num in range(n-1,0,-1):
            for j in range(1,num+1):
                if num != n:
                    optionprice[num][j] = df*(p*optionprice[num+1][j]+(1-p)*optionprice[num+1][j+1])
        return optionprice[1][1]
    else:
        for num in range(1, n + 1):
            for j in range(1, num + 1):
                price[num][j] = S * math.pow(u, num - 1) * math.pow(d, (j - 1) * 2)
                if price[num][j] < K:
                    optionprice[num][j] =K - price[num][j]
                else:
                    optionprice[num][j] = 0

        for num in range(n - 1, 0, -1):
            for j in range(1, num + 1):
                if num != n:
                    optionprice[num][j] = df * (p * optionprice[num + 1][j] + (1 - p) * optionprice[num + 1][j + 1])
        return optionprice[1][1]
