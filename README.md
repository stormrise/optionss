# options

> :+1:Contributions:
> 
> - Ran Xin
> 
> - Tian Yiping
> 
> - Li Lingxiao

## How to Run

Environment requirements:

- Environment: Python 3.6

- Packages: 
  
  - tkinter: for UI
  
  - traceback: capturing log
  
  - math: for some math function calculations such as root, square and so on
  
  - scipy: for standard normal distribution density function calculation
  
  - sympy: 
  
  - random: for generating Gaussian distribution random numbers
  
  - numpy: for matrix operations
  
  To Run our option pricer, just put all the .py files in the same directory, and run gui.py.



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

### European Option

`european.py`

### Implied volatility

`volatility.py`

### American Option

`american.py`

### Geometric Basket Option

`baskt_geometric.py`

This file defines a function to calculate the price of geometric basket call/put options.

### Arithmetic Basket Option

`basket_arithmetic.py`

This file defines a function to calculate the price of arithmetic basket call/put options.

### Geometric Asian option

`asian_geometric.py`

### Arithmetic Asian option

`asian_arithmetic.py`

---

## Test cases and analysis

how each parameter aﬀects the option price

|                      | Call option | Put option |
| -------------------- | ----------- | ---------- |
| spot price (S) ↑     |             |            |
| strike (K) ↑         | ↓↓          | ↑↑         |
| maturity (T) ↑       | ↑           | ↓          |
| risk free rate (r) ↑ | ↑           | ↓          |
| volatility (σ) ↑     | ↑           | ↓          |
|                      |             |            |

TODO
