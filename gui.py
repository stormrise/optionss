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
comvalue = StringVar()
chosen = ttk.Combobox(root, textvariable=comvalue, width=25)
chosen["values"] = ["European call/put option", "American call/put option", "Geometric basket option",
                    "Arithmetic basket option", "Geometric Asian option", "Arithmetic Asian option", "Implied volatility calculator"]
text = StringVar()
text.set("answer")
hint = StringVar()
hint.set("Please input the value of necessary parameters.")
chosen.current(0)
button = Button(root, text="Submit Input", command=price)
answer = Label(root, textvariable=text)
tip = Label(root, textvariable=hint)
option_type = Label(root, text="Choose the Option Type")
confirm = Button(root, text="Confirm")
path = Label(root, text="number of paths m")
entrypath = Entry(root)
S = Label(root, text="spot price S1(0)")
entrys = Entry(root)
S1 = Label(root, text="spot price S2(0)")
entrys1 = Entry(root)
vol = Label(root, text="volatility(1) σ")
entryvol = Entry(root)
vol1 = Label(root, text="volatility(2) σ")
entryvol1 = Entry(root)
p = Label(root, text="correlation p")
entryp = Entry(root)
r = Label(root, text="risk-free rate r")
entryr = Entry(root)
T = Label(root, text="time to maturity T")
entryt = Entry(root)
K = Label(root, text="strike K")
entryk = Entry(root)
n = Label(root, text="number of steps N")
entryn = Entry(root)
type = Label(root, text="option type")
entrytype = Entry(root)
variate = Label(root, text="variate (0 or 1)")
entryvariate = Entry(root)
repo_rate = Label(root, text="repo rate q")
entryrepo = Entry(root)
premium = Label(root, text="option premium V")

entrypremium = Entry(root)
option_type.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky=E)
chosen.grid(row=0, column=2, columnspan=2, pady=10, padx=20, sticky=W)
confirm.grid(row=1, columnspan=4, pady=2)
tip.grid(row=2, columnspan=4, pady=10)
# button1.pack()
path.grid(padx=20, row=3, column=0, sticky=E)
S.grid(padx=20, row=4, column=0, pady=2, sticky=E)
S1.grid(padx=20, row=5, column=0, pady=2, sticky=E)
vol.grid(padx=20, row=6, column=0, pady=2, sticky=E)
vol1.grid(padx=20, row=7, column=0, pady=2, sticky=E)
p.grid(padx=20, row=8, column=0, pady=2, sticky=E)
repo_rate.grid(padx=20, row=9, column=0, pady=2, sticky=E)

entrypath.grid(row=3, column=1, padx=10)
entrys.grid(row=4, column=1)
entrys1.grid(row=5, column=1)
entryvol.grid(row=6, column=1)
entryvol1.grid(row=7, column=1)
entryp.grid(row=8, column=1)
entryrepo.grid(row=9, column=1)


r.grid(row=3, column=2, pady=2, padx=10, sticky=E)
T.grid(row=4, column=2, pady=2, padx=10, sticky=E)
K.grid(row=5, column=2, pady=2, padx=10, sticky=E)
n.grid(row=6, column=2, pady=2, padx=10, sticky=E)
type.grid(row=7, column=2, pady=2, padx=10, sticky=E)
variate.grid(row=8, column=2, pady=2, padx=10, sticky=E)
premium.grid(row=9, column=2, pady=2, padx=10, sticky=E)

entryr.grid(row=3, column=3, padx=20)
entryt.grid(row=4, column=3, padx=20)
entryk.grid(row=5, column=3, padx=20)
entryn.grid(row=6, column=3, padx=20)
entrytype.grid(row=7, column=3, padx=20)
entryvariate.grid(row=8, column=3, padx=20)
entrypremium.grid(row=9, column=3, padx=20)
button.grid(row=10, columnspan=4, pady=10)
answer.grid(row=11, columnspan=4, pady=10)

root.mainloop()
