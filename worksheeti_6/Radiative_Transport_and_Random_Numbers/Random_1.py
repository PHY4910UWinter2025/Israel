import numpy as np
import matplotlib.pyplot as plt

# Initialize random number generator
rng = np.random.default_rng()

# Number of random samples
N = 100000

# Generate random numbers
rnums = rng.random(size=N) 
rnorms = rng.normal(size=N)  

plt.figure(figsize=(12, 6))

# Plot rnums
plt.subplot(1, 2, 1)
plt.plot(rnums, ',', color='blue', alpha=0.7)
plt.title("rnums")
plt.xlabel('x')
plt.ylabel('y')

# Plot rnorms
plt.subplot(1, 2, 2)
plt.plot(rnorms, ',', color='red')
plt.title('rnorms')
plt.xlabel('x')
plt.ylabel('y')

# Show the plots
plt.tight_layout()
plt.show()

data = np.array([rnums]).flatten()
bins = np.linspace(0,1,6)
bin_indices = np.digitize(data, bins) - 1
bin_counts = np.bincount(bin_indices, minlength=len(bins) - 1)

print(rnums)
print(bin_counts)







