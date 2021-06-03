import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def simul(docs=3, tau=10, min_time=5, max_time=20, opn=9*60, clse=16*60):
    total_time = clse-opn
    queue = np.random.exponential(scale=tau, size=int(1.5*total_time/tau))
    queue = np.cumsum(queue)
    queue = queue[queue<total_time]
    docs = np.zeros(3)
    sooner = 0
    wait_times = []
    for arrival in queue:
        taken = max(docs[sooner], arrival)
        wait_times.append(taken-docs[sooner])
        docs[sooner] = taken+np.random.uniform(min_time, max_time)
        sooner = np.argmin(docs)
    wait_times = np.array(wait_times)
    close = (opn+np.max(docs))
    close_hour = int(close/60)
    close_minute = int(close-close_hour*60)
    return {'patients': queue.shape[0],
            'in_wait': (wait_times>0).sum(),
            'average_wait': wait_times.mean(),
            'close_time': '{:d}:{:02d}:00'.format(close_hour, close_minute),
            'excess_close_min': np.max(docs)}

np.random.seed(42)
first = simul()
outf = open('1.12.9.out', 'w')
outf.write(
     "\\begin{{itemize}}\n"
     "    \\item[] ${:d}$ patients came to the office.\n"
     "    \\item[] ${:d}$ patients had to wait for a doctor.\n"
     "    \\item[] Average wait time was ${:.02f}$ minutes.\n"
     "    \\item[] Office closed at ${}$.\n"
     "\\end{{itemize}}".format(first['patients'],
                              first['in_wait'],
                              first['average_wait'],
                              first['close_time']))

runs = []
for i in range(100000):
    runs.append(simul())
results = pd.DataFrame(runs)

fig, ax = plt.subplots(2, 2, figsize=(12, 8))
ax[0, 0].set_xlim(20, 60)
ax[0, 0].hist(results['patients'],
                    bins=range(results['patients'].min(),
                               results['patients'].max()), color=(0, 0, 0))
ax[0, 0].axvspan(results['patients'].quantile(.25),
                 results['patients'].quantile(.75),
                 alpha=0.3, color=(0, 0.8, 0.8))
ax[0, 0].axvline(results['patients'].quantile(.5), c=(0, 0.5, 0.5))
ax[0, 0].set_title('Total patients received')
ax[0, 1].set_xlim(20, 50)
ax[0, 1].hist(results['in_wait'],
                    bins=range(results['in_wait'].min(),
                               results['in_wait'].max()), color=(0, 0, 0))
ax[0, 1].axvspan(results['in_wait'].quantile(.25),
                 results['in_wait'].quantile(.75),
                 alpha=0.3, color=(0, 0.8, 0.8))
ax[0, 1].axvline(results['in_wait'].quantile(.5), c=(0, 0.5, 0.5))
ax[0, 1].set_title('Patients that had to wait')
ax[1, 0].set_xlim(5, 40)
ax[1, 0].hist(results['average_wait'], bins=100, color=(0, 0, 0))
ax[1, 0].axvspan(results['average_wait'].quantile(.25),
                 results['average_wait'].quantile(.75),
                 alpha=0.3, color=(0, 0.8, 0.8))
ax[1, 0].axvline(results['average_wait'].quantile(.5), c=(0, 0.5, 0.5))
ax[1, 0].set_title('Average waiting time')
ax[1, 1].hist(results['excess_close_min'], bins=100, color=(0, 0, 0))
ax[1, 1].axvspan(results['excess_close_min'].quantile(.25),
                 results['excess_close_min'].quantile(.75),
                 alpha=0.3, color=(0, 0.8, 0.8))
ax[1, 1].axvline(results['excess_close_min'].quantile(.5), c=(0, 0.5, 0.5))
ax[1, 1].set_title('Average closing excess minutes')

fig.savefig('1.12.9.png', bbox_inches='tight')
