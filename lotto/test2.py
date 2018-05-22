from scipy.optimize import fsolve
import numpy as np


l = []
for a in range(1, 46):
    for b in range(a+1, 46):
        for c in range(b+1, 46):
            for d in range(c+1, 46):
                for e in range(d+1, 46):
                    for f in range(e+1, 46):
                        if a+b+c+d+e+f == 200:
                            l.append([a, b, c, d, e, f])

print(l)