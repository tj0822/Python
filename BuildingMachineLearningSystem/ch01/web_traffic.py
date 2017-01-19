#-*- coding:utf-8 -*-

import scipy as sp
data = sp.genfromtxt("data/web_traffic.tsv", delimiter="\t")

print(data[:10])

print(data.shape)


x = data[:,0]
y = data[:,1]

print(sp.sum(sp.isnan(y)))

print(x[sp.isnan(y)])
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]


def error(f, x, y):
    return sp.sum((f(x)-y)**2)

import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()



fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
print("Model parameters : %s" % fp1)
print(residuals)

f1 = sp.poly1d(fp1)
print(f1)
print(error(f1, x, y))

fx = sp.linspace(0, x[-1], 1000)
plt.plot(fx, f1(fx), linewidth=4)
plt.legend(["%i" % f1.order], loc="upper left")



f2p = sp.polyfit(x, y, 2)
print(f2p)
f2 = sp.poly1d(f2p)
print(f2)
print(error(f2, x, y))
plt.plot(fx, f2(fx), linewidth=4)


f3p = sp.polyfit(x, y, 3)
print(f3p)
f3 = sp.poly1d(f3p)
print(f3)
print(error(f3, x, y))
plt.plot(fx, f3(fx), linewidth=4)

f50p = sp.polyfit(x, y, 50)
f50 = sp.poly1d(f50p)
plt.plot(fx, f50(fx), linewidth=4)

plt.show()