import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

x = np.linspace(0, 1, 512)
y = np.linspace(0, 1, 512)
b_x, b_y = np.meshgrid(x, np.flip(y))

fig, ax = plt.subplots(1, 2, figsize=(8, 4))

def plot_convergence_region(ax, a, b, title=None):
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    if title:
        ax.set_title(title)
    ax.imshow(a*b<np.abs((a*b_x+b*(1-b_x))*(a*b_y+b*(1-b_y))),
              aspect='auto', interpolation='bilinear',
              cmap=ListedColormap([(0.8, 0.4, 0.4), (0.6, 0.8, 0.8)]),
              extent=[0, 1, 0, 1])

plot_convergence_region(ax[0], 0.25, 0.5, title='a<b')
ax[0].text(0.15, 0.15, 'Convergence region')
ax[0].text(0.45, 0.85, 'Divergence region')
plot_convergence_region(ax[1], 0.5, 0.25, title='a>b')
ax[1].text(0.10, 0.15, 'Divergence region')
ax[1].text(0.30, 0.85, 'Convergence region')

fig.savefig('5.2.png', bbox_inches='tight')
