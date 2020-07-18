"""
-Problem:
A metal chunk of mass 0.1 kg at a temperature of 743K sets up at a certain moment
within a 25°C environment. There, it's being subject to cooling by natural conventions 
and heat transfers by radiation. Under the hypothesis of uniform temperature distribution on the metal, 
the temperature equation is provided by:

	dT/ dt = A /(pcv)[E*O*(298^4 - T^4) + hc * (298 - T)]

Where:
E = 0.8
O = 5.67 * 10^(-9) W/m^2K^4
hc = 30 W / m^2K
A = 0.25m^2
p = 300Kg/m^2
c = 900 J / Kg.K
v = 0.0001m^3

-Solution approach:
T(10) Runge Kutta employing an h = 1 seconds jump.
"""

import matplotlib.pyplot as plt
import numpy as np

#Constants
E = 0.8
O = 5.67 * pow(10, -8)
hc = 30
A = 0.25
p = 300
c = 900
v = 0.001

def f(x0, y0): 
	"""
	Given function
	"""
	return (A /(p*c*v)) * ( E*O*(pow(298, 4) - pow(y0, 4)) + hc * (298 - y0) ) 

def next_step(h, x0, y0):
	"""
	Calculator of next step of
	Runge-Kutta iterations
	"""
	k1 = f(x0, y0)
	k2 = 2 * f(x0 + (1/2)*h, y0 + (1/2)*h*k1)
	k3 =  2 * f(x0 + (1/2)*h, y0 + (1/2)*h*k2)
	k4 =  f(x0 + h, y0 + h*k1)
	return y0 + (1/6)*h*(k1 + k2 + k3 + k4)
 
def runge_kutta(h, x0, y0):

	solution = np.array([0., 0.], dtype='float32')
	solution = np.repeat(solution, 10).reshape(10, 2)
	
	#Doing ten steps, since T(10)
	for i in range(10):
		y0 = next_step(h, x0, y0)
		x0 = x0 + h
		solution[i][0], solution[i][1] = x0, y0
	return solution

def main():
	
	#Runge Kutta step's size
	h = 1

	#Initial conditions 
	x0 = 0
	y0 = 743

	solution = runge_kutta(h, x0, y0)

	#Displaying solution
	print(f"\nCoordinates of solution:\n{solution}")
	print(f"\nGraphic of solution:\n")
	plt.plot(solution[:, 0], solution[:, 1], 'g')
	plt.xlabel("Time (seconds)")
	plt.ylabel("Temperature (K)")
	plt.show()	

if __name__ == '__main__':
	main()

