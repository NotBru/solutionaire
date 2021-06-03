import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb
import scipy.stats as st

# Drawing

y = np.arange(50, 301, 1)
beta = lambda y, n, p: comb(n, y)*p**y*(1-p)**(n-y)
normal = lambda x, mu, sigma: np.exp(-0.5*(x-mu)**2/sigma**2)\
                              /np.sqrt(2*np.pi*sigma**2)

fig, ax = plt.subplots(figsize=(4, 3))

ax.set_ylabel(r'$p(y)$')
ax.set_xlabel(r'$y$')

ax.scatter(y, 0.25*beta(y, 1000, 1/12)
             +0.5*beta(y, 1000, 1/6)
             +0.25*beta(y, 1000, 1/4), color=(0, 0, 0), s=4,
             label='Actual')
ax.plot(y, 0.25*normal(y, 1000/12, np.sqrt(1000*11/12/12))
          +0.5*normal(y, 1000/6, np.sqrt(1000*5/6/6))
          +0.25*normal(y, 1000/4, np.sqrt(1000*3/4/4)),
          color=(0.5, 0.5, 0.5), lw=0.5, label='Approximate')

fig.legend(loc='upper right', bbox_to_anchor=(1, 0.95))
fig.savefig('2.11.4.png', bbox_inches='tight')

# Numerical integration

y = np.arange(0, 1001, 1)
pdf = 0.25*beta(y, 1000, 1/12)+0.5*beta(y, 1000, 1/6)+0.25*beta(y, 1000, 1/4)
cdf = np.cumsum(pdf)

print("5%, 25%, 50%, 75%, and 95% exact points: ", end='')
print(*[np.argmax(cdf>p) for p in [.05, .25, .5, .75, .95] ], sep=', ')
print("5%, 25%, 50%, 75%, and 95% approximate points: ", end='')
print(1000/12+np.sqrt(1000*11/12/12)*st.norm.ppf(0.2),
      0.5*(1000/12+1000/6),
      167,
      0.5*(1000/6+1000/4),
      1000/4+np.sqrt(1000*3/4/4)*st.norm.ppf(0.80), sep=', ')
