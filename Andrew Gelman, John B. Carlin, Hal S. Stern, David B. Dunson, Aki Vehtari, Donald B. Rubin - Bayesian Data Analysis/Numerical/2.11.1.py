import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 1, 128)
beta_unnorm = lambda y: theta**(3+y)*(1-theta)**(13-y)
beta = lambda y: beta_unnorm(y)/beta_unnorm(y).sum()
dist = beta(0)+beta(1)+beta(2)
dist = dist/3

fig, ax = plt.subplots(figsize=(6, 4))

ax.set_xlim(0, 1)
ax.set_ylim(0, dist.max()*1.05)
ax.set_ylabel(r'$p(\theta|D)$')
ax.set_xlabel(r'$\theta$')

ax.plot(theta, dist, color=(0, 0, 0))
ax.axvline(5/18, ls='--', color=(.2, .2, .2))

fig.savefig('2.11.1.png', bbox_inches='tight')
