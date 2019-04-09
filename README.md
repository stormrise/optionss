# options

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

- **Packages**: 

  - tkinter: for UI

  - traceback: capturing log

  - math: for some math function calculations such as root, square and so on

  - scipy: for standard normal distribution density function calculation

  - random: for generating Gaussian distribution random numbers

  - numpy: for matrix operations

:red_circle:To **Run** our option pricer, just put all the .py files in the same directory, and run `gui.py`. 

```bash
bash:~$ python3 gui.py
```

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

This file defines a function to calculate the price of European call/put options. And there is a closed formular, we can simply implement it.

### Implied volatility

`volatility.py`    *(S, S_true, r, T, K, q, type)*

This file defines a function to calculate the implied volatility of call/put options. All the inputs of this function are strings captured by GUI so the first step is type conversion. Then, just follow the formulas in "lecture 4" using Newton Method to solve the problem which converges quickly, we can figure out the implied volatility of call/put options.

### American Option

`american.py`    *(S, sigma, r, T, K, n, type)*

This file defines a function to calculate the price of American call/put options. All the inputs of this function are strings captured by GUI so the first step is type conversion. There is no closed formular, so we use bionominal tree to solve it. First step is to iterate the bionominal tree and calculate the stock price in each node. Second step is to backtrack the tree and calculate the price of call/put options.

### Geometric Basket Option

`baskt_geometric.py`    *(S1, S2, sigma1, sigma2, rho, r, T, K, option_type)*

This file defines a function to calculate the price of geometric basket call/put options. All the inputs of this function are strings captured by GUI so the first step is type conversion. Then, just follow the formulas described in mathematical background in "assignment 3", we can figure out the call or put geometric basket option.

### Arithmetic Basket Option

`basket_arithmetic.py`    *(path, S1, S2, sigma1, sigma2, rho, r, T, K, option_type, variate)*

This file defines a function to calculate the price of arithmetic basket call/put options. The first step is also type conversion of inputted varibles. For arithmetic option price, there is no closed-form formulas so we need to use Monte Carlo to simulate it. We use the method proved in assignment 2 (2.1)  to generate two random varibles with correlation coefficient σ. Then, similar to Asian option, we can calculate the basket option price (95% confidence interval) with or without control variate.

### Geometric Asian option

`asian_geometric.py`    *(S, sigma, r, T, K, n, option_type)*

This file defines a function to calculate the price of geometric asian call/put options. And there is a closed formular we can simply implement it.

### Arithmetic Asian option

`asian_arithmetic.py`   *(path, S, sigma, r, T, K, n, option_type, variate)*

This file defines a function to calculate the price of arithmetic asian call/put options. There is no closed-form formulas so we need to use Monte Carlo to simulate it.

---

## Test cases and analysis

how each parameter aﬀects the option price

| European             | Call option | Put option |
| -------------------- | ----------- | ---------- |
| spot price (S) ↑     |             |            |
| strike (K) ↑         | ↓↓          | ↑↑         |
| maturity (T) ↑       | ↑           | ↓          |
| risk free rate (r) ↑ | ↑           | ↓          |
| volatility (σ) ↑     | ↑           | ↓          |
| repo rate (q)        |             |            |

| Implied volatility   | Call option | Put option |
| -------------------- | ----------- | ---------- |
| spot price (S) ↑     |             |            |
| strike (K) ↑         | ↓↓          | ↑↑         |
| maturity (T) ↑       | ↑           | ↓          |
| risk free rate (r) ↑ | ↑           | ↓          |
| volatility (σ) ↑     | ↑           | ↓          |
| repo rate (q)        |             |            |

| American             | Call option | Put option |
| -------------------- | ----------- | ---------- |
| spot price (S) ↑     |             |            |
| strike (K) ↑         | ↓↓          | ↑↑         |
| maturity (T) ↑       | ↑           | ↓          |
| risk free rate (r) ↑ | ↑           | ↓          |
| volatility (σ) ↑     | ↑           | ↓          |
| repo rate (q)        |             |            |

| Geometric Basket     | Call option | Put option |
| -------------------- | ----------- | ---------- |
| spot price (S) ↑     |             |            |
| strike (K) ↑         | ↓↓          | ↑↑         |
| maturity (T) ↑       | ↑           | ↓          |
| risk free rate (r) ↑ | ↑           | ↓          |
| volatility (σ) ↑     | ↑           | ↓          |
| repo rate (q)        |             |            |

| Arithmetic Basket    | Call option | Put option |
| -------------------- | ----------- | ---------- |
| spot price (S) ↑     |             |            |
| strike (K) ↑         | ↓↓          | ↑↑         |
| maturity (T) ↑       | ↑           | ↓          |
| risk free rate (r) ↑ | ↑           | ↓          |
| volatility (σ) ↑     | ↑           | ↓          |
| repo rate (q)        |             |            |

| Geometric Asian      | Call option | Put option |
| -------------------- | ----------- | ---------- |
| spot price (S) ↑     |             |            |
| strike (K) ↑         | ↓↓          | ↑↑         |
| maturity (T) ↑       | ↑           | ↓          |
| risk free rate (r) ↑ | ↑           | ↓          |
| volatility (σ) ↑     | ↑           | ↓          |
| repo rate (q)        |             |            |

| Arithmetic Asian     | Call option | Put option |
| -------------------- | ----------- | ---------- |
| spot price (S) ↑     |             |            |
| strike (K) ↑         | ↓↓          | ↑↑         |
| maturity (T) ↑       | ↑           | ↓          |
| risk free rate (r) ↑ | ↑           | ↓          |
| volatility (σ) ↑     | ↑           | ↓          |
| repo rate (q)        |             |            |

TODO:floppy_disk:
