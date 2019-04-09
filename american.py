import math


def price(S1, sigma1, r1, T1, K1, n1, type1):
    # parameters
    S = float(S1)
    sigma = float(sigma1)
    r = float(r1)
    T = float(T1)
    K = float(K1)
    n = int(n1)
    type = type1
    # time steps
    n = n + 1
    price = [[0 for i in range(0, n + 1)] for j in range(0, n + 1)]
    optionprice = [[0 for i in range(0, n + 1)] for j in range(0, n + 1)]
    # length of time interval
    dt = T / (n - 1)
    df = math.exp(-r * dt)
    # choosing u and d
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    # calculate risk neutral probability
    p = (math.exp(r * dt) - d) / (u - d)

    if type == "call":
        # value at node n
        for num in range(1, n + 1):
            for j in range(1, num + 1):
                price[num][j] = S * math.pow(u, num - 1) * math.pow(d, (j - 1) * 2)
                if price[num][j] > K:
                    optionprice[num][j] = price[num][j] - K
                else:
                    optionprice[num][j] = 0

        # call price
        for num in range(n - 1, 0, -1):
            for j in range(1, num + 1):
                if num != n:
                    optionprice[num][j] = df * (p * optionprice[num + 1][j] + (1 - p) * optionprice[num + 1][j + 1])
        return optionprice[1][1]

    else:
        # value at node n
        for num in range(1, n + 1):
            for j in range(1, num + 1):
                price[num][j] = S * math.pow(u, num - 1) * math.pow(d, (j - 1) * 2)
                if price[num][j] < K:
                    optionprice[num][j] = K - price[num][j]
                else:
                    optionprice[num][j] = 0

        # put price
        for num in range(n - 1, 0, -1):
            for j in range(1, num + 1):
                if num != n:
                    optionprice[num][j] = df * (p * optionprice[num + 1][j] + (1 - p) * optionprice[num + 1][j + 1])
        return optionprice[1][1]
