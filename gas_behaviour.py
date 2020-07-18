"""
The following data set exposes a specific volume behaviour
of some gas in regards to the change in pressure.

	P: 2 - 5 - 10 - 15 - 20
	v: 25953 - 11213 - 3473 - 483 - 33

a) By the least squares method, find the polinomial equation 
that best fits the supplied data by calculating 
the R^2 coefficient.

b) Represent the data set graphically, where 
the table's values and the curve that best fit them
are plotted.

c) Find the rough volume value (v) when pressure is of 17 units.

d) Use divided differences to find the polynomial 
that best fits the data set and find the volume value
when pressure is of 17 units. (Compare results between d, b and c)

e) The employed work to compress the gas can be expressed as:

	w = Integral from p1 to p2 of v*dP
Find w from 5 to 20 units.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def polynomial(coeff, x):
	return coeff[0]*x**4 + coeff[1]*x**3 + coeff[2]*x**2 + coeff[3]*x + coeff[4]

def to_integrate(x, v):
	return v

def divided_differences(N, table):
	"""
	Divided differences numerical method
	"""

	return 

def main():

#(a)
	P_v = np.array([[2, 5, 10, 15, 20], [25953, 11213, 3473, 483, 33]])

	#Using NumPy fuction to find the polynomial coefficients that best fits
	coeffs = np.polyfit(P_v[0], P_v[1], 4)

	#Now let's calculate the new range, so we can plot the curve
	new_range = [polynomial(coeffs, P_v[0][i]) for i in range(5)]

	#Checking out correlation coefficient R^2
	correlation_matrix = np.corrcoef(P_v[1], new_range)
	r_squared = correlation_matrix[0, 1] ** 2

#(b)
	fig, axs = plt.subplots(2, sharex = True)
	axs[0].plot(P_v[0], P_v[1], 'o')
	axs[0].set_title('Set of values')
	axs[1].plot(P_v[0], new_range, 'r')
	axs[1].set_title(f'Curve that best fits them, with R^2 = {r_squared}')
	plt.show()

#(c)
	print(f'Rough value of v when pressure is of 17 units: {abs(polynomial(coeffs, 17))}')

#(d)
	
#(e)
	
	"""
	aux = lambda v: integrate.quad(to_integrate, 5, 20, args=v)
	w = list(map(aux, P_v[1, 1:]))
	plt.plot(w, 'g')
	plt.show()
	"""
	
if __name__ == '__main__':
	main()