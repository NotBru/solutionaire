import numpy as np

def normalized(arr):
    return arr/arr.sum()

m = 2**12 # This is unnecessarily big I guess

y = np.array([43, 44, 45, 46.5, 47.5])
theta = np.linspace(0, 100, m+1)
b_y, b_theta = np.meshgrid(y, theta) # "Big y, big theta"

theta_updf = 1
y_gvn_theta_updf = 1/np.prod(1+(b_y-b_theta)**2, axis=1)
# item a:
theta_gvn_y_pdf = normalized(theta_updf*y_gvn_theta_updf)

np.random.seed(42)

# item b:

def draw_samples(vals, pdf, size=1):
    cdf = np.cumsum(pdf)
    udraws = np.random.uniform(size=size)
    b_cdf, b_udraws = np.meshgrid(cdf, udraws)
    ids = np.argmax(b_cdf > b_udraws, axis=1)
    return vals[ids]

theta_gvn_y_samples = draw_samples(theta, theta_gvn_y_pdf, size=1000)

# item c:
y_pred_samples = np.random.standard_cauchy(size=1000)+theta_gvn_y_samples

import matplotlib as mpl
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 3, figsize=(15, 4))

ax[0].set_xlim(40, 50)
ax[0].set_ylim(0, theta_gvn_y_pdf.max()*1.05)
ax[0].set_ylabel(r'$p(\theta|y)$')
ax[0].set_xlabel(r'$\theta$')
ax[0].plot(theta, theta_gvn_y_pdf, color=(0, 0, 0))
ax[1].set_xlim(40, 50)
ax[1].set_ylabel(r'$H(\theta|y)$')
ax[1].set_xlabel(r'$\theta$')
ax[1].hist(theta_gvn_y_samples, color=(0, 0, 0), histtype='step',
           facecolor=(0.5, 0.5, 0.5), fill=True, bins=np.arange(40, 50, 0.5))
ax[2].set_xlim(20, 80)
ax[2].set_ylabel(r'$H(\tilde{y}|y)$')
ax[2].set_xlabel(r'$\tilde{y}$')
ax[2].hist(y_pred_samples, color=(0, 0, 0), histtype='step',
           facecolor=(0.5, 0.5, 0.5), fill=True, bins=np.arange(20, 80, 2))

fig.savefig('2.11.11.png', bbox_inches='tight')
plt.close(fig)
