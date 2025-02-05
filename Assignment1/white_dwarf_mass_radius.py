import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from phy4910 import ode_rk4

# A. Let's build a nonrelativistic model of a white dwarf!

#
#  Part 1 - Solve Lane-Emden
#

# we can change rho_c to make different mass white dwarfs
rho_0 = 3.789E6
k_nr = 3.166E12
G = 6.6743E-8
M_sun = 1.989E33
R_sun = 6.955E10

# these two functions define the Lane-Emden differential equation
def A(x):
	return ((-5/9)*x**(-4/3) * (1 + x**(2/3))**(-1/2)) - ((2/3) * x**(-2/3) * (1 + x**(2/3))**(-3/2)) + ((1/3) * (1 + x**(2/3))**-(5/2))
	

def B(x):
	return ((5/3)*x**(-1/3) * (1 + x**(2/3))**(-1/2)) - ((1/3) * x**(1/3) * (1 + x**(2/3))**(-3/2))
	

def f(eta, varrho, z):
	return z
	

def g(eta, varrho, z):
	return ((-2/eta)*z) - (A(varrho) / B(varrho) * z**2)- ((1/B(varrho)) * varrho)

#rho_c_values = np.logspace(5, 8, 25)
rho_c_values = 10**np.random.uniform(5,8,25)
masses = []
radiuses = []

for rho_c in rho_c_values:
	# solve the Lane-Emden equation
	eta, varrho, z = ode_rk4(0.0001, 10, 0.0001, 1, 0, f, g)
	
	# uh oh, we get some NaNs thanks to varrho going negative.  Remove them:
	positivevalues = varrho > 0
	eta = eta[positivevalues]
	varrho = varrho[positivevalues]
	z = z[positivevalues]
	
	# find the surface in "scaled radius"
	eta_s = eta[-1]
	
	#dimensional mass
	m = np.trapz(eta**(2) * varrho, eta)
	
	#add lambda
	lam = np.sqrt((k_nr) / (rho_c**(1/3) * 4 * np.pi * G))
	
	# Create arrays for the physical radius and density
	r = lam * eta_s
	m_dwarf = 4 * np.pi * rho_c * lam ** 3 * m
	print(f"The radial scale factor is {lam/1e5:.3f} km")
	print(f"The mass of the white dwarf is M = {m_dwarf / M_sun:.3f} M☉")
	
	# Convert to solar units
	r /= R_sun
	m_dwarf /= M_sun
	
	masses.append(m_dwarf)
	radiuses.append(r)

plt.figure(figsize=(8,6))
plt.scatter(radiuses, masses, label="White Dwarf Models", color='orange')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Radius (R_sun)", fontsize=14)
plt.ylabel("Mass (M_sun)", fontsize=14)
plt.title("White Dwarf Mass-Radius Relationship", fontsize=20)
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("white_dwarf_mass_radius.png")

