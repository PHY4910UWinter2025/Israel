import numpy as np
import matplotlib.pyplot as plt
from phy4910 import ode_euler, ode_rk4

# solve the ode via euler

def f(x, y, z):
	return z
	
def g(x, y, z):
	return -z + 6*y

x, y, z = ode_euler(0, 1, 0.001, 1, -2, f, g)


np.savetxt("euler_data.txt", np.column_stack((x,y,z)))
print("File created successfully")

plt.plot(x, y, color="green", label="values", linewidth=2.5, linestyle='-', marker='o', markersize=5, markerfacecolor='#F8B400')
    
plt.grid(True, linestyle='--', linewidth=2.5, alpha=0.8, color= '#C0C0C0')
    
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
    
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#000000')
ax.spines['bottom'].set_color('#000000')

# Add labels for x and y axes
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.savefig("quiz1.pdf")

