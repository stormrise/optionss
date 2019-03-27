from tkinter import *
from tkinter import ttk

import european
import america
import asian_geometric
import asian_arithmetic
import basket_geometric
import basket_arithmetic
import volatility


def price():
    if chosen.get() == "European call/put option":
        price = european.price(entrys.get(), entryvol.get(
        ), entryr.get(), entryt.get(), entryk.get(), entrytype.get())
        text.set(price)
    elif chosen.get() == "American call/put option":
        price = america.price(entrys.get(), entryvol.get(), entryr.get(
        ), entryt.get(), entryk.get(), entryn.get(), entrytype.get())
        text.set(price)
    elif chosen.get() == "Geometric Asian option":
        price = asian.price(entrys.get(), entryvol.get(), entryr.get(
        ), entryt.get(), entryk.get(), entryn.get(), entrytype.get())
        text.set(price)
    elif chosen.get() == "Arithmetic Asian option":
        price = asian2.price(entrypath.get(), entrys.get(), entryvol.get(), entryr.get(
        ), entryt.get(), entryk.get(), entryn.get(), entrytype.get(), entryvariate.get())
        text.set(price)
    elif chosen.get() == "Geometric basket option":
        price = basket_geometric.price(entrys.get(), entrys1.get(), entryvol.get(), entryvol1.get(
        ), entryp.get(), entryr.get(), entryt.get(), entryk.get(), entrytype.get())
        text.set(price)
    elif chosen.get() == "Arithmetic basket option":
        price = basket_arithmetic.price(entrypath.get(), entrys.get(), entrys1.get(), entryvol.get(), entryvol1.get(
        ), entryp.get(), entryr.get(), entryt.get(), entryk.get(), entrytype.get(), entryvariate.get())
        text.set(price)
    elif chosen.get() == "Implied volatility calculator":
        price = volatility.price(entrys.get(), entrypremium.get(), entryr.get(
        ), entryt.get(), entryk.get(), entryrepo.get(), entrytype.get())
        text.set(price)


#
root = Tk()
root.title("Option Pricer")

option_type = Label(root, text="Choose the Option Type")
comvalue = StringVar()
chosen = ttk.Combobox(root, textvariable=comvalue, width=25)
chosen["values"] = ["European option", "American option", "Geometric basket option",
                    "Arithmetic basket option", "Geometric Asian option", "Arithmetic Asian option", "Implied volatility calculator"]
chosen.current(0)

ans = StringVar()
ans.set("Calc...")
answer = Label(root, textvariable=ans)
answer1 = Label(root, text="Answer:",bg="green")

hint = StringVar()
hint.set("Please input the value of necessary parameters.")
tip = Label(root, textvariable=hint)

button = Button(root, text="  Submit \n  Input  ", bg="green", command=price)


path = Label(root, text="Monte Carlo paths m")
entrypath = Entry(root)
S = Label(root, text="spot price S1(0) S")
entrys = Entry(root)
S1 = Label(root, text="spot price S2(0) S")
entrys1 = Entry(root)
vol = Label(root, text="volatility(1) σ")
entryvol = Entry(root)
vol1 = Label(root, text="volatility(2) σ")
entryvol1 = Entry(root)
p = Label(root, text="correlation ρ")
entryp = Entry(root)
r = Label(root, text="risk-free rate r")
entryr = Entry(root)
T = Label(root, text="time to maturity T")
entryt = Entry(root)
K = Label(root, text="strike K")
entryk = Entry(root)
n = Label(root, text="geometric average steps N")
entryn = Entry(root)
type = Label(root, text="option type")
optiontype = StringVar()
call = Radiobutton(root, text="call", variable=optiontype, value="call")
put = Radiobutton(root, text="put", variable=optiontype, value="put")
entrytype = Entry(root)
variate = Label(root, text="variate (0 or 1)")
entryvariate = Entry(root)
repo_rate = Label(root, text="repo rate q")
entryrepo = Entry(root)
premium = Label(root, text="option premium V")
entrypremium = Entry(root)


answer.grid(row=0, rowspan=2, column=1, columnspan=2, pady=10)
answer1.grid(row=0, rowspan=2, column=0, pady=10, sticky=E)
option_type.grid(row=2, column=0, padx=10, pady=10, sticky=E)
chosen.grid(row=2, column=1, pady=10, padx=10, sticky=W)
call.grid(row=2, column=2)
put.grid(row=2, column=3, sticky=W)

tip.grid(row=3, columnspan=4, pady=10)
# left
S.grid(row=4, column=0, pady=2, padx=10,  sticky=E)
vol.grid(row=5, column=0, pady=2, padx=10, sticky=E)
r.grid(row=6, column=0, pady=2, padx=10, sticky=E)
T.grid(row=7, column=0, pady=2, padx=10, sticky=E)
K.grid(row=8, column=0, pady=2, padx=10, sticky=E)
premium.grid(row=9, column=0, pady=2, padx=10, sticky=E)
# left1
entrys.grid(row=4, column=1, padx=10)
entryvol.grid(row=5, column=1, padx=10)
entryr.grid(row=6, column=1, padx=10)
entryt.grid(row=7, column=1, padx=10)
entryk.grid(row=8, column=1, padx=10)
entrypremium.grid(row=9, column=1, padx=10)

# right
S1.grid(row=4, column=2, pady=2, padx=10,  sticky=E)
vol1.grid(row=5, column=2, pady=2, padx=10, sticky=E)
path.grid(row=6, column=2, padx=10, sticky=E)
n.grid(row=7, column=2, pady=2, padx=10, sticky=E)
repo_rate.grid(row=8, column=2, pady=2, padx=10,  sticky=E)
p.grid(row=9, column=2, pady=2, padx=10,  sticky=E)
variate.grid(row=10, column=2, pady=2, padx=10, sticky=E)
# right1
entrys1.grid(row=4, column=3, padx=10)
entryvol1.grid(row=5, column=3, padx=10)
entrypath.grid(row=6, column=3, padx=10)
entryn.grid(row=7, column=3, padx=10)
entryrepo.grid(row=8, column=3, padx=10)
entryp.grid(row=9, column=3, padx=10)
entryvariate.grid(row=10, column=3, padx=10)


button.grid(row=11, column=1,rowspan=2, columnspan=2, pady=10)


root.mainloop()
