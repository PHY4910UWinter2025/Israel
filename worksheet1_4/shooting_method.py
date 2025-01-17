import numpy as np
import matplotlib.pyplot as plt
import phy4910


def f(x, y, z):
	return z
	
def g(x, y, z):
	return -1/y * z**2

x, y, z = phy4910.ode_rk4(0, 1, 0.001, 1, 12.012, f, g)

np.savetxt('shooting_method_data.txt',np.column_stack((x, y,z)))
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
plt.savefig("shooting_method.pdf")



#plt.show()

print(y[-1])
