import numpy as np
import matplotlib as plt
import pandas as pd

#Euler's Method equation
def f(x, y, z):
 	return z
def g(x, y, z):
	return -z**2 * (1/y)

h = 0.01
x = np.arange(0, 10, h)
N =len(x)
y = np.zeros(N)
z = np.zeros(N)
#set Boundary condition
y[0] = 1
z[0] = 1
X_N = 5

for i in range(N-1):
	k1 = h * f(x[i], y[i], z[i])
	ell1 = h * g(x[i], y[i], z[i])
	
	y[i+1] = y[i] + k1
	z[i+1] = z[i] + ell1
	
#x,y,z =ode_euler(0, 10, 0.01, 1, 1, f, g)
	
#np.savetxt("euler_data.txt",np.column_stack((x,y,z)))
data = pd.DataFrame({'x':x, 'f(x)': y, 'z': z})
data.to_csv("data.txt", index=False, sep="\t", float_format="%.6f", header=True)

