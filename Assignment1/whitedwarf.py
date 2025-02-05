import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from phy4910 import ode_rk4

# A. Let's build a nonrelativistic model of a white dwarf!

# some physical numbers, in cgs units
# we can change rho_c to make different mass white dwarfs
rho_0 = 3.789E6
k_nr = 3.166E12
G = 6.6743E-8
M_sun = 1.989E33

#
#  Part 1 - Solve Lane-Emden
#

# polytropic index of the model

# these two functions define the Lane-Emden differential equation
def A(x):
	return ((-5/9)*x**(-4/3) * (1 + x**(2/3))**(-1/2)) - ((2/3) * x**(-2/3) * (1 + x**(2/3))**(-3/2)) + ((1/3) * (1 + x**(2/3))**-(5/2))
	
def B(x):
	return ((5/3)*x**(-1/3) * (1 + x**(2/3))**(-1/2)) - ((1/3) * x**(1/3) * (1 + x**(2/3))**(-3/2)) 
	
def f(eta, varrho, z):
	return z
	
def g(eta, varrho, z):
	return ((-2/eta)*z) - (A(varrho) / B(varrho) * z**2)- ((1/B(varrho)) * varrho)

# solve the Lane-Emden equation
eta, varrho, z = ode_rk4(0.0001, 10, 0.0001, 1, 0, f, g)

# uh oh, we get some NaNs thanks to varrho going negative.  Remove them:
positivevalues = varrho > 0
eta = eta[positivevalues]
varrho = varrho[positivevalues]
z = z[positivevalues]

plt.plot(eta, varrho, color="orange", marker = 'o',linestyle='-',markersize=1)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel(r"$\eta$", fontsize = 14)
plt.ylabel(r"$\varrho$", fontsize = 14)
plt.title("Lane-Emdem",fontsize = 20)
plt.show()

# find the surface in "scaled radius"
eta_s = eta[-1]
print(f'The surface in scaled radius of the star is at: {eta_s:.3f}')

#
# Part 2 - Calculating the dimensionless mass m
#
#what is m?



m = np.trapezoid( eta**(2) * varrho, eta)

print(f"The dimensionless mass is {m:.3f}")

#
# Part 3 - Converting to real units
#

# Part a
# calculate the radial scale factor
#add lambda
lam = np.sqrt((k_nr) / (rho_0**(1/3) * 4 * np.pi * G)) 

print(f"The radial scale factor is {lam/1e5:.3f} km")

# Part b

# Create arrays for the physical radius and density
r = lam * eta
rho = rho_0 * varrho

plt.plot(r / 1e5, rho)
plt.xlabel(r"$r$ (km)")
plt.ylabel(r"$\rho$ (g/cm$^3$)")
plt.title("Density Profile of the White Dwarf")
plt.show()

print(f"The radius of the white dwarf is R = {r[-1] / 1e5:.3f} km")

# Calculate the mass of the white dwarf
m_dwarf = 4 * np.pi * rho_0 * lam ** 3 * m
print(f"The mass of the white dwarf is M = {m_dwarf / M_sun:.3f} M☉")


print(f"The mass of the white dwarf is {m_dwarf/M_sun:.3f} solar masses")

"""







# Part c

"""



