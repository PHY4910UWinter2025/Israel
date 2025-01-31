import numpy as np
from phy4910 import move_photon
import matplotlib.pyplot as plt

rng = np.random.default_rng()
n = 1000
nr_ar = np.zeros(n)
ns_ar = np.zeros(n)

for i in range (n):
    x, y, z, theta, phi, nr, ns = move_photon(taumax = 5, log = False, rng = rng)
    nr_ar[i] = nr
    ns_ar[i] = ns

#print(nr_ar)

avg_nr = np.mean(nr_ar)
print(avg_nr / (avg_nr + 1))

avg_ns = np.mean(ns_ar)
dev_ns = np.std(ns_ar)

print(f"2B, Average number of steps is: {avg_ns} before leaving the surface and the corresponding standard deviation is {dev_ns}:.3f")
    
	  
  

