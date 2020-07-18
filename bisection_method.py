"""
-Problem:
The Bernoulli equation to an open-channel fluid flow with a small protuberance is given.

Where:
Q = 1.2m^2/s (volumetric flow)
g = 9.81m/s^2 (gravity)
b = 1.8m (channel width)
ho = 0.6m (upward water level) 
hs = 0.075m (size of protuberance)
h = Water level above the protuberance

Determine value of h

-Solution approach:
Bisection method
"""

import numpy as np

#Constants after some algebraic manipulations
b = 0.5879239501
c = 0.02265262204

def f(x):
	"""
	Given Bernoulli equation
	"""
	return pow(x, 3) -b*pow(x, 2) + c

def bisection_method():

	#Setting initial conditions up
	a = -0.05
	b = 1

	#Defining initial conditions for bisection method
	xr = (a + b )/ 2
	f_a = f(a)
	f_b = f(b)
	f_xr = f(xr)
	mul = f_a * f_xr
	error = 1 

	#Doing Bisection Method iterations
	while error != 0:
		if mul > 0: a = xr
		if mul < 0: b = xr
		prev_xr = xr
		xr = (a + b)/2
		f_a = f(a)
		f_b = f(b)
		f_xr = f(xr)
		mul = f_a * f_xr
		error = abs(((xr - prev_xr )/ xr) * 100)
	return xr

def main():

	#Displaying result
	print(f"Value of h: {bisection_method()}")

if __name__ == '__main__':
	main()