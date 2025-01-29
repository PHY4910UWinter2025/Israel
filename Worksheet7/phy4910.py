import numpy as np
import matplotlib
#matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def ode_euler(x_start, x_end, h, y0, z0, f, g):
	
	x = np.arange(x_start, x_end, h)
	N = len(x)
	y = np.zeros(N)
	z = np.zeros(N)
	
	y[0] = y0
	z[0] = z0
	
	for i in range(N-1):
		k1 = h * f(x[i], y[i], z[i])
		ell1 = h * g(x[i], y[i], z[i])
	
		y[i+1] = y[i] + k1
		z[i+1] = z[i] + ell1

	return x, y, z
	
	
def ode_rk4(x_start, x_end, h, y0, z0, f, g):
	
	x = np.arange(x_start, x_end, h)
	N = len(x)
	y = np.zeros(N)
	z = np.zeros(N)
	
	y[0] = y0
	z[0] = z0
	
	for i in range(N-1):
		k1 = h * f(x[i], y[i], z[i])
		ell1 = h * g(x[i], y[i], z[i])
		
		k2 = h * f(x[i] + 0.5*h, y[i] + 0.5*k1, z[i] + 0.5*ell1)
		ell2 = h * g(x[i] + 0.5*h, y[i] + 0.5*k1, z[i] + 0.5*ell1)

		k3 = h * f(x[i] + 0.5*h, y[i] + 0.5*k2, z[i] + 0.5*ell2)
		ell3 = h * g(x[i] + 0.5*h, y[i] + 0.5*k2, z[i] + 0.5*ell2)
		
		k4 = h * f(x[i] + h, y[i] + k3, z[i] + ell3)
		ell4 = h * g(x[i] + h, y[i] + k3, z[i] + ell3)
			
		y[i+1] = y[i] + k1/6 + k2/3 + k3/3 + k4/6
		z[i+1] = z[i] + ell1/6 + ell2/3 + ell3/3 + ell4/6

	return x, y, z
	
def pick_direction(rng):
	"""
	Picks a random Direction, Returns theta and phi"""
	theta = np.arccos(1-2* rng.random())
	phi = 2 * np.pi * rng.random()
	return theta, phi

def test_pick_direction():
    rng = np.random.default_rng()
    
    N = 1000
    theta = np.zeros(N)
    phi = np.zeros(N)
    
    for i in range(N):
        theta[i], phi[i] = pick_direction(rng)
        
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')  

    ax.plot(np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta), marker='.', color='blue')
    ax.set_aspect('equal')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Y")
    plt.title("Random walks for my sphere")
    plt.show()
 	
def pick_optical_depth(rng):
	"""returns a random optical depth fromdistribution e^tau"""
	x = rng.random()
	return -np.log(1-x) 

def test_optical_depth():
	rng = np.random.default_rng()
	optical_depths = [pick_optical_depth(rng) for _ in range(1000)]
	
	#plot
	plt.hist(optical_depths, bins = 50, density=True, color='blue')
	plt.xlabel('Optical Depth')
	plt.ylabel('Y')
	plt.title('Hist')
	plt.grid(True)
	plt.show()

 
#test your file
if __name__ == "__main__":
    #test
    test_pick_direction()
    test_optical_depth()
    
    
    
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
   
    
"""def ode_rk4(x_start, x_end, h, y0, z0, f, g, threshold=0.001):
    x = np.arange(x_start, x_end, h)
    N = len(x)
    y = np.zeros(N)
    z = np.zeros(N)

    y[0] = y0
    z[0] = z0

    for i in range(N-1):
        # Runge-Kutta method
        k1 = h * f(x[i], y[i], z[i])
        ell1 = h * g(x[i], y[i], z[i])

        k2 = h * f(x[i] + 0.5*h, y[i] + 0.5*k1, z[i] + 0.5*ell1)
        ell2 = h * g(x[i] + 0.5*h, y[i] + 0.5*k1, z[i] + 0.5*ell1)

        k3 = h * f(x[i] + 0.5*h, y[i] + 0.5*k2, z[i] + 0.5*ell2)
        ell3 = h * g(x[i] + 0.5*h, y[i] + 0.5*k2, z[i] + 0.5*ell2)

        k4 = h * f(x[i] + h, y[i] + k3, z[i] + ell3)
        ell4 = h * g(x[i] + h, y[i] + k3, z[i] + ell3)

        # Update values
        y[i+1] = y[i] + k1/6 + k2/3 + k3/3 + k4/6
        z[i+1] = z[i] + ell1/6 + ell2/3 + ell3/3 + ell4/6

        # Stop if the density drops below the threshold
        if y[i+1] < threshold * y0:
            x = x[:i+2]  # Crop arrays to current size
            y = y[:i+2]
            z = z[:i+2]
            break

    return x, y, z"""

