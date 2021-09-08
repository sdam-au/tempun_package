from scipy.stats import halfnorm
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

r = halfnorm.rvs(size=1000, scale=25)
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()