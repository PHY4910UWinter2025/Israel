import numpy as np
import pandas as pd

def f(x):
	return x*np.exp(-x**2)
	
x = np.linspace(0,1.0,100)

calculation = f(x)

data = pd.DataFrame({'x':x, 'f(x)': calculation})
data.to_csv("data.txt", index=False, sep="\t", float_format="%.6f", header=True)
print("data.txt created succesfully")

