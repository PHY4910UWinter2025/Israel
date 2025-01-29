import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from phy4910 import ode_rk4, pick_direction, pick_optical_depth


def move_photon(t_max, zmax, rng):
    	x, y, z = [0], [0], [0]
    	n = 0
    	while z[-1] < zmax:
        	theta, phi = pick_direction(rng)
        	optical_depth = pick_optical_depth(rng)
        	s = optical_depth / t_max

        	x_i = x[-1] + s * np.sin(theta) * np.cos(phi)
        	y_i = y[-1] + s * np.sin(theta) * np.sin(phi)
        	z_i = z[-1] + s * np.cos(theta)

        	n += 1
        	print(f"Scatter {n}: Photon at {x_i:.3f}, {y_i:.3f}, {z_i:.3f}")

        	if z_i < 0:
            		x, y, z = [0], [0], [0]
        	else:
            		x.append(x_i)
            		y.append(y_i)
            		z.append(z_i)

    	return np.array(x), np.array(y), np.array(z), theta, phi
    
        
        
  
def  test_move_photon():

	t_max = 1
	z_max = 10
	
	rng = np.random.default_rng()
	x, y,z, theta, phi = move_photon(t_max,z_max,rng)
	
    

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1, projection="3d")
	    
	ax.plot(x,y,z, linestyle= '-')
	#ax.set_aspect('equal')
	ax.set_xlabel("X")
	ax.set_ylabel("Y")
	ax.set_zlabel("Z")
	plt.title("Random walks to the surface of my sphere")
	plt.show()
	
if __name__ == "__main__":
	test_move_photon()
	  
  

