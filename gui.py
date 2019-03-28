from tkinter import *
from tkinter import ttk

import european
import america
import asian_geometric
import asian_arithmetic
import basket_geometric
import basket_arithmetic
import volatility


# function
def clear():
    ans.set("Calc...")
    entry_s.delete(0, 999)
    entry_sig.delete(0, 999)
    entry_r.delete(0, 999)
    entry_t.delete(0, 999)
    entry_k.delete(0, 999)
    entry_V.delete(0, 999)
    entry_s1.delete(0, 999)
    entry_sig1.delete(0, 999)
    entry_m.delete(0, 999)
    entry_n.delete(0, 999)
    entry_p.delete(0, 999)
    entry_q.delete(0, 999)
    # entryvariate.set(0)


def price():
    if chosen.get() == "European option":
        price = european.price(entry_s.get(), entry_sig.get(
        ), entry_r.get(), entry_t.get(), entry_k.get(), optiontype.get())
        ans.set(price)
    elif chosen.get() == "American option":
        price = america.price(entry_s.get(), entry_sig.get(), entry_r.get(
        ), entry_t.get(), entry_k.get(), entry_n.get(), optiontype.get())
        ans.set(price)
    elif chosen.get() == "Geometric Asian option":
        price = asian_geometric.price(entry_s.get(), entry_sig.get(), entry_r.get(
        ), entry_t.get(), entry_k.get(), entry_n.get(), optiontype.get())
        ans.set(price)
    elif chosen.get() == "Arithmetic Asian option":
        price = asian_arithmetic.price(entry_m.get(), entry_s.get(), entry_sig.get(), entry_r.get(
        ), entry_t.get(), entry_k.get(), entry_n.get(), optiontype.get(), entryvariate.get())
        ans.set(price)
    elif chosen.get() == "Geometric basket option":
        price = basket_geometric.price(entry_s.get(), entry_s1.get(), entry_sig.get(), entry_sig1.get(
        ), entry_p.get(), entry_r.get(), entry_t.get(), entry_k.get(), optiontype.get())
        ans.set(price)
    elif chosen.get() == "Arithmetic basket option":
        price = basket_arithmetic.price(entry_m.get(), entry_s.get(), entry_s1.get(), entry_sig.get(), entry_sig1.get(
        ), entry_p.get(), entry_r.get(), entry_t.get(), entry_k.get(), optiontype.get(), entryvariate.get())
        ans.set(price)
    elif chosen.get() == "Implied volatility calculator":
        price = volatility.price(entry_s.get(), entry_V.get(), entry_r.get(
        ), entry_t.get(), entry_k.get(), entry_q.get(), optiontype.get())
        ans.set(price)


# GUI
root = Tk()
root.title("Option Pricer")

# #
option_type = Label(root, text="Choose the Option Type")
comValue = StringVar()
chosen = ttk.Combobox(root, textvariable=comValue, width=25)
chosen["values"] = ["European option", "American option", "Geometric basket option",
                    "Arithmetic basket option", "Geometric Asian option", "Arithmetic Asian option",
                    "Implied volatility calculator"]
chosen.current(0)

ans = StringVar()
ans.set("Calc...")
answer = Label(root, textvariable=ans, bg='yellow', font='Helvetica -16 bold')
answer1 = Label(root, text="Answer:", bg='yellow', font='Helvetica -16 bold')

hint = StringVar()
hint.set("Please input the value of necessary parameters.")
tip = Label(root, textvariable=hint)

submitBtn = Button(root, text="  Submit \n  Input  ", bg="green", command=price, font='Helvetica -14 bold')
clearBtn = Button(root, text="clear input", bg="red", command=clear, font='Helvetica -14 bold')

optiontype = StringVar()
call = Radiobutton(root, text="call", variable=optiontype, value="call")
put = Radiobutton(root, text="put", variable=optiontype, value="put")

entryvariate = StringVar()
variate = Label(root, text="variate")
variate0 = Radiobutton(root, text="none (0)", variable=entryvariate, value="0")
variate1 = Radiobutton(root, text="geo- (1)", variable=entryvariate, value="1")

# input var
path = Label(root, text="Monte Carlo paths m")
entry_m = Entry(root)
S = Label(root, text="spot price S1(0) S")
entry_s = Entry(root)
S1 = Label(root, text="spot price S2(0) S")
entry_s1 = Entry(root)
sig = Label(root, text="volatility(1) σ")
entry_sig = Entry(root)
sig1 = Label(root, text="volatility(2) σ")
entry_sig1 = Entry(root)
p = Label(root, text="correlation ρ")
entry_p = Entry(root)
r = Label(root, text="risk-free rate r")
entry_r = Entry(root)
T = Label(root, text="time to maturity T")
entry_t = Entry(root)
K = Label(root, text="strike K")
entry_k = Entry(root)
n = Label(root, text="average steps N")
entry_n = Entry(root)
repo_rate = Label(root, text="repo rate q")
entry_q = Entry(root)
V = Label(root, text="option premium V")
entry_V = Entry(root)

# ============================================================
# top
answer.grid(row=0, rowspan=2, column=1, columnspan=2, pady=10)
answer1.grid(row=0, rowspan=2, column=0, pady=10, sticky=E)
option_type.grid(row=2, column=0, padx=10, pady=10, sticky=E)
chosen.grid(row=2, column=1, pady=10, padx=10, sticky=W)
call.grid(row=2, column=2)
put.grid(row=2, column=3, sticky=W)
tip.grid(row=3, columnspan=4, pady=10)

# left
S.grid(row=4, column=0, pady=2, padx=10, sticky=E)
sig.grid(row=5, column=0, pady=2, padx=10, sticky=E)
r.grid(row=6, column=0, pady=2, padx=10, sticky=E)
T.grid(row=7, column=0, pady=2, padx=10, sticky=E)
K.grid(row=8, column=0, pady=2, padx=10, sticky=E)
V.grid(row=9, column=0, pady=2, padx=10, sticky=E)
# left1
entry_s.grid(row=4, column=1, padx=10)
entry_sig.grid(row=5, column=1, padx=10)
entry_r.grid(row=6, column=1, padx=10)
entry_t.grid(row=7, column=1, padx=10)
entry_k.grid(row=8, column=1, padx=10)
entry_V.grid(row=9, column=1, padx=10)

# right
S1.grid(row=4, column=2, pady=2, padx=10, sticky=E)
sig1.grid(row=5, column=2, pady=2, padx=10, sticky=E)
path.grid(row=6, column=2, padx=10, sticky=E)
n.grid(row=7, column=2, pady=2, padx=10, sticky=E)
repo_rate.grid(row=8, column=2, pady=2, padx=10, sticky=E)
p.grid(row=9, column=2, pady=2, padx=10, sticky=E)
variate.grid(row=10, column=2, pady=2, padx=10, sticky=E)
# right1
entry_s1.grid(row=4, column=3, padx=10)
entry_sig1.grid(row=5, column=3, padx=10)
entry_m.grid(row=6, column=3, padx=10)
entry_n.grid(row=7, column=3, padx=10)
entry_q.grid(row=8, column=3, padx=10)
entry_p.grid(row=9, column=3, padx=10)
variate0.grid(row=10, column=3, padx=10, sticky=W)
variate1.grid(row=10, column=3, padx=10, sticky=E)

# bottom
clearBtn.grid(row=11, column=0, rowspan=2, columnspan=1, pady=10)
submitBtn.grid(row=11, column=1, rowspan=2, columnspan=2, pady=10)

root.mainloop()
