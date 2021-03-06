# Group 17's Option Pricer

> :thumbsup:Contributions:
> 
> - Ran Xin
> 
> - Tian Yiping
> 
> - Li Lingxiao

## How to Run

Environment requirements:

- **Environment**: Python 3.6

- **Packages**: **tkinter** : for UI, **traceback**: for capturing log, **math**: for some math calculations (root, square), **scipy**: for standard normal distribution density function, **random**: for generating Gaussian distribution random, **numpy**: for matrix operations

:red_circle:To **Run** our option pricer, just put all the .py files in the same directory, and run `gui.py`. 

## GUI

Using a simple python [tkinter]([https://wiki.python.org/moin/TkInter]) GUI libray to build a simple GUI Option Pricer:

![5ca998a16e750](https://i.loli.net/2019/04/07/5ca998a16e750.png)

- Just like a Calculator the **result answer** shows in the above, highlight in yellow;

- The second line is **Option Type**, it's a combo box, list all avaliable option types: European, American, Asian, Basket; Also you can click the radio button to choose call or put option.

- The third line is **alert information** that informs you about which missing value you forget to input in order to make the calculation. We simply extract the error traceback message to achieve this.

- In the middle area is input value field, all the **input parameters** should be input here, left-hand side is most commonly input one, right-hand side is less common and also symmetric.

- In the bottom center (green) its a **submit** button, and the bottom left (red) is **clear** all input button.

#### How to calc?

Choose option type, here we select "Arithmetic basket option", call, input all the needed parameter, with variate:

if we forget input the correlation ρ , click submit will be informed,

![5ca99ef09541a](https://i.loli.net/2019/04/07/5ca99ef09541a.png)

after all correct, the answer will be calculated and display in above.

![5ca99f671a2cc](https://i.loli.net/2019/04/07/5ca99f671a2cc.png)

---

## Functionalities

> **parameter in code**
> 
> spot price  **S**, volatility **sigma**, risk-free rate **r**, time to maturity **T**, strike **K**, option premium **V**, Monte Carlo paths **path**, average steps **n**, repo rate **q**, correlation **rho**

### European Option

`european.py`    *(S, sigma, r, T, K, type, q)*

Using Lecture 3 **Black-Scholes Formulas**: with BS-PDE & Call-Put Parity

$$
C(S,t)=Se^{-qT}N(d_1)-Ke^{-rT}N(d_2) \qquad P(S,t)=Ke^{-rT}N(-d_2)-Se^{-qT}N(-d_1)
$$

$$
in\ which:\qquad d_1={{ln(S/k)+(r-q)T}\over{\sigma \sqrt{T}}}+{1\over2}\sigma \sqrt{T} \qquad d_2={{ln(S/k)+(r-q)T}\over{\sigma \sqrt{T}}}-{1\over2}\sigma \sqrt{T}
$$

### Implied volatility

`volatility.py`    *(S, S_true, r, T, K, q, type)*

Follow the formulas in "lecture 4" using **Newton Method** to solve the problem which converges quickly:

$$
\hat{\sigma}=\sqrt{2 \mid {{lnS_0/K+(r-q)T}\over T}\mid} \qquad vega={{Se^{-qT}\sqrt{T} \times e^{-0.5(d1^2)}}\over{\sqrt{2\pi}}}
$$

### American Option

`american.py`    *(S, sigma, r, T, K, n, type)*

There is no closed formular, so we use **bionominal tree** in "lecture 6" to solve it. First step is to iterate the bionominal tree and calculate the stock price in each node. Second step is to backtrack the tree and calculate the price of call/put options.

$$
Se^{r\Delta t}=pS_u+(1-p)S_d \qquad p={{e^{r\Delta t}-d}\over{u-d}} \qquad u=e^{\sigma \sqrt{\Delta t}} \qquad d={1\over u} =e^{-\sigma \sqrt{\Delta t}}
$$

### Geometric Basket Option

`baskt_geometric.py`    *(S1, S2, sigma1, sigma2, rho, r, T, K, option_type)*

Follow the formulas described in mathematical background in "assignment 3" **geometric Brownian motion**, we can figure out the call or put geometric basket option. 

$$
B_g(t)=(\prod_{i=1}^n)^{1/n} \qquad \sigma_{B_g}={\sqrt{\sum_{i=1}^{n=2} \sum_{j=1}^{n=2} \sigma_i \sigma_j \rho_{i,j}}\over 2} \qquad \mu_{B_g}=r-{1\over 2}{\sum_{i=1}^{n=2} \sigma_i^2\over n}+{1\over 2}\sigma_{B_g}^2 \qquad n=2
$$

$$
C_{B_g}=e^{-rT}(B_g(0)e^{\mu T}N(\hat{d_1})-KN(\hat{d_2})) \qquad P_{B_g}=e^{-rT}(KN(-\hat{d_2})-B_g(0)e^{\mu T}N(-\hat{d_1}))
$$

### Arithmetic Basket Option

`basket_arithmetic.py`    *(path, S1, S2, sigma1, sigma2, rho, r, T, K, option_type, variate)*

For arithmetic option price, there is no closed-form formulas so we need to use **Monte Carlo** to simulate the stock price. We use the method proved in assignment 2 (2.1)  to generate two random varibles with correlation coefficient σ. Then, similar to Asian option, we can calculate the basket option price (95% confidence interval) with or without control variate. 

$$
B_a(t)={1\over n}\sum_{i=1}^nSi(t) \qquad n=2
$$

Rest is similar to Asian-Arithmetic, 2 drift, 2 growthFactor. simulate multiple times output the 95% conﬁdence interval.

### Geometric Asian option

`asian_geometric.py`    *(S, sigma, r, T, K, n, option_type)*

There is a closed formular in "lecture 5" we can simply implement it.

$$
\hat{\sigma}=\sigma \sqrt{{(n+1)(2n+1)}\over 6n^2} \qquad \hat{\mu}=(r-{1\over 2}\sigma^2){(n+1)\over 2n}+{1\over 2}\hat{\sigma}^2
$$

$$
C_{A_g}=e^{-rT}(S_0e^{\hat{\mu} T}N(\hat{d_1})-KN(\hat{d_2})) \qquad P_{A_g}=e^{-rT}(KN(-\hat{d_2})-S_0e^{\hat{\mu} T}N(-\hat{d_1}))
$$

### Arithmetic Asian option

`asian_arithmetic.py`   *(path, S, sigma, r, T, K, n, option_type, variate)*

There is no closed-form formulas so we need to use **Monte Carlo** to simulate it.

$$
drift=e^{(r-0.5\sigma^2)\Delta t} \qquad growthFactor=drift \times e^{\sigma \sqrt{\Delta t}\times gaussRandom}
$$

Then calculate the mean, std, cov of the payoff, simulate multiple times output the 95% conﬁdence interval.

---

## Test cases and analysis

how each parameter aﬀects the option price

r = 0.05, T = 3, and S(0) = 100. paths in Monte Carlo simulation is m = 100, 000. RandomSeed(1234)

#### Asian option:

| σ   | K   | n   | Type | Geometric | Arithmetic    | Arithmetic(variate) |
| --- | --- | --- | ---- | --------- | ------------- | ------------------- |
| 0.3 | 100 | 50  | Put  | 8.482     | 7.681~7.818   | 7.799~7.807         |
| 0.3 | 100 | 100 | Put  | 8.431     | 7.667~7.804   | 7.747~7.756         |
| 0.4 | 100 | 50  | Put  | 12.558    | 11.125~11.304 | 11.277~11.292       |
|     |     |     |      |           |               |                     |
| 0.3 | 100 | 50  | Call | 13.259    | 14.639~14.927 | 14.714~14.736       |
| 0.3 | 100 | 100 | Call | 13.138    | 14.482~14.768 | 14.598~14.620       |
| 0.4 | 100 | 50  | Call | 15.759    | 18.072~18.476 | 18.181~18.222       |

| Geometric Asian     | Call option | Put option |
| ------------------- | ----------- | ---------- |
| volatility (σ) ↑    | ↑↑          | ↑↑         |
| average steps (n) ↑ | ↓           | ↓          |

| Arithmetic Asian    | Call option | Put option |
| ------------------- | ----------- | ---------- |
| volatility (σ) ↑    | ↑↑          | ↑↑         |
| average steps (n) ↑ | ↓           | ↓          |

#### Basket options:

| S1(0) | S2(0) | K   | σ1  | σ2  | ρ   | Type       | Geometric | Arithmetic    | Arithmetic(variate) |
| ----- | ----- | --- | --- | --- | --- | ---------- | --------- | ------------- | ------------------- |
| 100   | 100   | 100 | 0.3 | 0.3 | 0.5 | Put        | 11.491    | 10.469~10.658 | 10.563~10.587       |
| 100   | 100   | 100 | 0.3 | 0.3 | 0.9 | Put        | 12.622    | 12.281~12.492 | 12.426~12.431       |
| 100   | 100   | 100 | 0.1 | 0.3 | 0.5 | Put        | 6.586     | 5.479~5.593   | 5.508~5.525         |
| 100   | 100   | 80  | 0.3 | 0.3 | 0.5 | Put        | 4.711     | 4.214~4.325   | 4.247~4.262         |
| 100   | 100   | 120 | 0.3 | 0.3 | 0.5 | Put        | 21.289    | 19.712~19.980 | 19.867~19.900       |
| 100   | 100   | 100 | 0.5 | 0.5 | 0.5 | Put        | 23.469    | 20.885~21.178 | 21.054~21.110       |
| 120   | 100   | 100 | 0.3 | 0.3 | 0.5 | Put        | 8.915     | 7.975~8.144   | 8.043~8.068         |
| 120   | 120   | 100 | 0.3 | 0.3 | 0.5 | Put        | 6.736     | 6.047~6.195   | 6.095~6.115         |
| 100   | 100   | 100 | 0.3 | 0.3 | 0.5 | Put r=0.1  | 6.423     | 5.782~5.915   | 5.828~5.846         |
| 100   | 100   | 100 | 0.3 | 0.3 | 0.5 | Put T=1    | 8.257     | 7.774~7.914   | 7.845~7.856         |
|       |       |     |     |     |     |            |           |               |                     |
| 100   | 100   | 100 | 0.3 | 0.3 | 0.5 | Call       | 22.102    | 24.334~24.818 | 24.461~24.523       |
| 100   | 100   | 100 | 0.3 | 0.3 | 0.9 | Call       | 25.878    | 26.223~26.775 | 26.351~26.364       |
| 100   | 100   | 100 | 0.1 | 0.3 | 0.5 | Call       | 17.924    | 19.296~19.641 | 19.414~19.451       |
| 100   | 100   | 80  | 0.3 | 0.3 | 0.5 | Call       | 32.536    | 35.227~35.765 | 35.352~35.415       |
| 100   | 100   | 120 | 0.3 | 0.3 | 0.5 | Call       | 14.685    | 16.434~16.854 | 16.559~16.617       |
| 100   | 100   | 100 | 0.5 | 0.5 | 0.5 | Call       | 28.449    | 34.598~35.537 | 34.865~35.071       |
| 120   | 100   | 100 | 0.3 | 0.3 | 0.5 | Call       | 28.753    | 31.815~32.377 | 31.946~32.024       |
| 120   | 120   | 100 | 0.3 | 0.3 | 0.5 | Call       | 36.683    | 39.832~40.468 | 39.979~40.055       |
| 100   | 100   | 100 | 0.3 | 0.3 | 0.5 | Call r=0.1 | 29.023    | 31.588~32.112 | 31.710~31.773       |
| 100   | 100   | 100 | 0.3 | 0.3 | 0.5 | Call T=1   | 12.015    | 12.649~12.889 | 12.715~12.733       |

| Geometric Basket                    | Call option | Put option |
| ----------------------------------- | ----------- | ---------- |
| spot price (S1) ↑                   | ↑           | ↓          |
| spot price (S1) ↑ (S1)↑             | ↑↑          | ↓↓         |
| strike (K) ↓                        | ↑           | ↓          |
| maturity (T) ↓                      | ↓           | ↓          |
| risk free rate (r) ↑                | ↑           | ↓          |
| volatility (σ1) ↓                   | ↓           | ↓          |
| volatility (σ1) ↑ volatility (σ2) ↑ | ↑           | ↑          |
| correlation coefficient (ρ) ↑       | ↑           | ↑          |

| Arithmetic Basket                   | Call option | Put option |
| ----------------------------------- | ----------- | ---------- |
| spot price (S) ↑                    | ↑           | ↓          |
| spot price (S1) ↑ (S1)↑             | ↑↑          | ↓↓         |
| strike (K) ↓                        | ↑           | ↓          |
| maturity (T) ↓                      | ↓           | ↓          |
| risk free rate (r) ↑                | ↑           | ↓          |
| volatility (σ) ↓                    | ↓           | ↓          |
| volatility (σ1) ↑ volatility (σ2) ↑ | ↑           | ↑          |
| correlation coefficient (ρ) ↑       | ↑           | ↑          |

#### European:

| S1(0) | K   | σ1  | r    | T   | Type | European |
| ----- | --- | --- | ---- | --- | ---- | -------- |
| 100   | 100 | 0.2 | 0.01 | 0.5 | call | 5.876024 |
| 100   | 120 | 0.2 | 0.01 | 0.5 | call | 0.774138 |
| 100   | 120 | 0.2 | 0.01 | 1   | call | 8.433318 |
| 100   | 100 | 0.3 | 0.01 | 0.5 | call | 8.677645 |
| 100   | 100 | 0.2 | 0.02 | 0.5 | call | 6.120654 |
|       |     |     |      |     |      |          |
| 100   | 100 | 0.2 | 0.01 | 0.5 | put  | 5.377272 |
| 100   | 120 | 0.2 | 0.01 | 0.5 | put  | 20.17563 |
| 100   | 120 | 0.2 | 0.01 | 1   | put  | 7.438302 |
| 100   | 100 | 0.3 | 0.01 | 0.5 | put  | 8.178893 |
| 100   | 100 | 0.2 | 0.02 | 0.5 | put  | 5.125637 |

| European             | Call option | Put option |
| -------------------- | ----------- | ---------- |
| strike (K) ↑         | ↓↓          | ↑↑         |
| maturity (T) ↑       | ↑           | ↓          |
| risk free rate (r) ↑ | ↑           | ↓          |
| volatility (σ) ↑     | ↑           | ↓          |

#### American:

| S1(0) | K   | σ1  | r    | T   | Type | European |
| ----- | --- | --- | ---- | --- | ---- | -------- |
| 100   | 100 | 0.2 | 0.01 | 0.5 | call | 5.861975 |
| 100   | 120 | 0.2 | 0.01 | 0.5 | call | 0.776743 |
| 100   | 100 | 0.2 | 0.01 | 1   | call | 8.413504 |
| 100   | 100 | 0.3 | 0.01 | 0.5 | call | 8.656601 |
| 100   | 100 | 0.2 | 0.02 | 0.5 | call | 6.106614 |
|       |     |     |      |     |      |          |
| 100   | 100 | 0.2 | 0.01 | 0.5 | put  | 5.363223 |
| 100   | 120 | 0.2 | 0.01 | 0.5 | put  | 20.17824 |
| 100   | 100 | 0.2 | 0.01 | 1   | put  | 7.418488 |
| 100   | 100 | 0.3 | 0.01 | 0.5 | put  | 8.157849 |
| 100   | 100 | 0.2 | 0.02 | 0.5 | put  | 5.111597 |

| American             | Call option | Put option |
| -------------------- | ----------- | ---------- |
| strike (K) ↑         | ↓↓          | ↑↑         |
| maturity (T) ↑       | ↑           | ↓          |
| risk free rate (r) ↑ | ↑           | ↓          |
| volatility (σ) ↑     | ↑           | ↓          |
