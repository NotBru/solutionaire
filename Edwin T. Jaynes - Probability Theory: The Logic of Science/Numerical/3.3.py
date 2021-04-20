from math import comb
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import iqr

k = range(3, 34)

P = [ k_*(k_-1)*(k_-2)*sum((47-N_rem)*(46-N_rem)
                           *np.prod([(50-m-N_rem)/(50-m) for m in range(20)])
                        for N_rem in range(k_-3, 48))
                        for k_ in k ]
P = np.array(P)
P = P/np.sum(P)
F = np.cumsum(P)

cuartiles = [ np.argmax(F>0.25*i) for i in range(1, 4) ]
cuartiles = [ k+(F[k]-0.25*i)/(F[k]-F[k-1])+3
                for (i, k) in zip(range(1, 4), cuartiles) ]

fig, ax = plt.subplots(figsize=(6, 4))

ax.set_xlim(3, 15)
ax.set_xticks(range(3, 16))
ax.set_ylim(0, P.max()*1.1)

x = np.linspace(cuartiles[0], cuartiles[-1], 128)
ax.fill_between(x, 0, np.interp(x, k, P), color=(0.7, 0.95, 0.95))
ax.plot([cuartiles[1], cuartiles[1]], [0, np.interp(cuartiles[1], k, P)],
        color=(0.5, 0.2, 0.2))

ax.scatter(k, P, color=(0, .4, .4), label=r'$P(H_k|D)$')
ax.plot(k, P, color=(0, .4, .4), ls='--')

plt.legend()
plt.savefig('3.3.png', bbox_inches='tight')
