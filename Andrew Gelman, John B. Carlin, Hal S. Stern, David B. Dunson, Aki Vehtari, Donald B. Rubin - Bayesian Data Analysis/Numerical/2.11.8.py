import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

theta_min = 140
theta_max = 190

n = np.arange(0, 100+1)
theta = np.linspace(theta_max, theta_min, 101)
b_n, b_theta = np.meshgrid(n, theta)

mean = (40**(-2)*180+20**(-2)*150*n)/(40**(-2)+20**(-2)*n)
stddev = 1/np.sqrt(40**(-2)+n*20**(-2))
b_mean = (40**(-2)*180+20**(-2)*150*b_n)/(40**(-2)+20**(-2)*b_n)
b_inv_stddev = np.sqrt(40**(-2)+b_n*20**(-2))

b_prob = st.norm.pdf((b_theta-b_mean)*b_inv_stddev)

fig, ax = plt.subplots(figsize=(6, 4))

ax.set_ylim(theta_min, theta_max)

im = ax.imshow(b_prob, extent=(0, 100, theta_min, theta_max), aspect='auto',
               interpolation='bilinear')

level_deviations = [-3, -1, 0, 1, 3]
colors = [ (0.8, 0.8, 0.8) ]*2+[ (0, 0, 0) ]+[ (0.8, 0.8, 0.8) ]*2
for dev, color in zip(level_deviations, colors):
    ax.plot(n, mean+dev*stddev, color=color, ls='--', lw=1)

fig.savefig('2.11.8.png')
