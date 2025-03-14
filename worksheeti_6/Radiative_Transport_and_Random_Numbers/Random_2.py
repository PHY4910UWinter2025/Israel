import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng() # random number generator

N = 10000000

rnums = rng.random(size = N)
rnorms = rng.normal(size = N)

Nbin = 50
bins = np.zeros(Nbin)

data_max = np.max(rnums) + 1e-10
data_min = np.min(rnums)


for i in range(N):
	 b = int((rnums[i] - data_min)/(data_max - data_min) * Nbin)
	 bins[b] +=1.0
plt.bar(range(Nbin), bins)
plt.show()



