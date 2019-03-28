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
    ans.set("")
    entrys.delete(0, 999)
    entryvol.delete(0, 999)
    entryr.delete(0, 999)
    entryt.delete(0, 999)
    entryV.delete(0, 999)
    entrys1.delete(0, 999)
    entryvol1.delete(0, 999)
    entrym.delete(0, 999)
    entryn.delete(0, 999)
    entryp.delete(0, 999)
    entryq.delete(0, 999)
    # entryvariate.set(0)


def price():
    if chosen.get() == "European option":
        price = european.price(entrys.get(), entryvol.get(
        ), entryr.get(), entryt.get(), entryk.get(), optiontype.get())
        ans.set(price)
    elif chosen.get() == "American option":
        price = america.price(entrys.get(), entryvol.get(), entryr.get(
        ), entryt.get(), entryk.get(), entryn.get(), optiontype.get())
        ans.set(price)
    elif chosen.get() == "Geometric Asian option":
        price = asian_geometric.price(entrys.get(), entryvol.get(), entryr.get(
        ), entryt.get(), entryk.get(), entryn.get(), optiontype.get())
        ans.set(price)
    elif chosen.get() == "Arithmetic Asian option":
        price = asian_arithmetic.price(entrym.get(), entrys.get(), entryvol.get(), entryr.get(
        ), entryt.get(), entryk.get(), entryn.get(), optiontype.get(), entryvariate.get())
        ans.set(price)
    elif chosen.get() == "Geometric basket option":
        price = basket_geometric.price(entrys.get(), entrys1.get(), entryvol.get(), entryvol1.get(
        ), entryp.get(), entryr.get(), entryt.get(), entryk.get(), optiontype.get())
        ans.set(price)
    elif chosen.get() == "Arithmetic basket option":
        price = basket_arithmetic.price(entrym.get(), entrys.get(), entrys1.get(), entryvol.get(), entryvol1.get(
        ), entryp.get(), entryr.get(), entryt.get(), entryk.get(), optiontype.get(), entryvariate.get())
        ans.set(price)
    elif chosen.get() == "Implied volatility calculator":
        price = volatility.price(entrys.get(), entryV.get(), entryr.get(
        ), entryt.get(), entryk.get(), entryq.get(), optiontype.get())
        ans.set(price)


# GUI
root = Tk()
root.title("Option Pricer")

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

Submitbutton = Button(root, text="  Submit \n  Input  ", bg="green", command=price, font='Helvetica -14 bold')
Clearbutton = Button(root, text="clear input", bg="red", command=clear, font='Helvetica -14 bold')

optiontype = StringVar()
call = Radiobutton(root, text="call", variable=optiontype, value="call")
put = Radiobutton(root, text="put", variable=optiontype, value="put")

entryvariate = StringVar()
variate = Label(root, text="variate")
variate0 = Radiobutton(root, text="none (0)", variable=entryvariate, value="0")
variate1 = Radiobutton(root, text="geo- (1)", variable=entryvariate, value="1")

path = Label(root, text="Monte Carlo paths m")
entrym = Entry(root)
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
n = Label(root, text="average steps N")
entryn = Entry(root)
repo_rate = Label(root, text="repo rate q")
entryq = Entry(root)
premium = Label(root, text="option premium V")
entryV = Entry(root)

answer.grid(row=0, rowspan=2, column=1, columnspan=2, pady=10)
answer1.grid(row=0, rowspan=2, column=0, pady=10, sticky=E)
option_type.grid(row=2, column=0, padx=10, pady=10, sticky=E)
chosen.grid(row=2, column=1, pady=10, padx=10, sticky=W)
call.grid(row=2, column=2)
put.grid(row=2, column=3, sticky=W)

tip.grid(row=3, columnspan=4, pady=10)
# left
S.grid(row=4, column=0, pady=2, padx=10, sticky=E)
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
entryV.grid(row=9, column=1, padx=10)

# right
S1.grid(row=4, column=2, pady=2, padx=10, sticky=E)
vol1.grid(row=5, column=2, pady=2, padx=10, sticky=E)
path.grid(row=6, column=2, padx=10, sticky=E)
n.grid(row=7, column=2, pady=2, padx=10, sticky=E)
repo_rate.grid(row=8, column=2, pady=2, padx=10, sticky=E)
p.grid(row=9, column=2, pady=2, padx=10, sticky=E)
variate.grid(row=10, column=2, pady=2, padx=10, sticky=E)
# right1
entrys1.grid(row=4, column=3, padx=10)
entryvol1.grid(row=5, column=3, padx=10)
entrym.grid(row=6, column=3, padx=10)
entryn.grid(row=7, column=3, padx=10)
entryq.grid(row=8, column=3, padx=10)
entryp.grid(row=9, column=3, padx=10)
variate0.grid(row=10, column=3, padx=10, sticky=W)
variate1.grid(row=10, column=3, padx=10, sticky=E)

Clearbutton.grid(row=11, column=0, rowspan=2, columnspan=1, pady=10)
Submitbutton.grid(row=11, column=1, rowspan=2, columnspan=2, pady=10)

root.mainloop()
