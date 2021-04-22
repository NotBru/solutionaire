import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.xkcd()

fig, ax = plt.subplots(figsize=(6, 4))

sigma=2
x = np.linspace(2-3*sigma, 2+3*sigma, 256)
N = lambda x: 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-0.5*((x-2)/sigma)**2)

ax.add_line(mpl.lines.Line2D(
    [2, 2], [0, N(2)], ls='--', c=(0, 0, 0)))
ax.plot(x, N(x), c=(0, 0, 0))
ax.add_line(mpl.lines.Line2D(
    [2-sigma]*4+[2+sigma]*4,
    [N(2-sigma), N(2-sigma)*0.9, N(2-sigma)*1.1, N(2-sigma)]*2,
    c=(0, 0, 0)))
ax.text(2+sigma*0.1, 0, r'$\theta=2$')
ax.text(2+sigma*0.5, N(2+sigma)*0.85, r'$2\sigma$')

fig.savefig('1.12.1.png', bbox_inches='tight')
