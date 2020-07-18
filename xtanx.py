"""
-Problem: 
Represent graphic of function f(x) = xtanx and find its roots
within the interval [0, 20]
"""

from math import tan
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x * np.tan(x)

def main():
	
	roots = np.array([0.])
	roots = np.repeat(roots, 20).reshape(20, 1)

	#Finding roots through optimization function of SciPy
	for i in range(20):
		roots[i] = optimize.root(f, i).x[0]
		
	#Displaying graphic
	x = np.linspace(0, 20)
	plt.plot(x, f(x), 'g')
	plt.plot(roots, f(roots), 'kv', label = 'Roots')
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.legend()
	plt.show()
	
if __name__ == '__main__':
	main()
