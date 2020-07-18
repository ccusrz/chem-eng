"""
-Problem:
The concentration-time profile of some Liquid A dissemination in a bowl
along with some Liquid B, which apart from disseminating it also 
reacts with B to form AB, is given by the following equation:

	B* (d^2Ca/dZ^2) + Kv + Ca = 0

Where:
B = 2E-9m^2/seg
Kv = 1.389E-3seg^-1
L = 0.001m

Given Ca(0) = 5Kmol/m^3 and Ca'(0) = - 10 Kmol/m^2.
Calculate Ca(L/2), Ca(L/4), Ca(3L/4) and Ca(L) using
the Euler Method with delta_z = 0.00005m
"""

#Constants
delta_z = 0.00005
B = 2E-9
Kv = 1.389E-3
L = 0.001

def f(Ui, Cai):
	"""
	Function that represents the second derivative of
	function Ca, after a variable change and
	some algebraic manipulations

	Ui: value of Ca first derivative
	Cai: value of Ca
	"""
	return Ui + delta_z * ((-Kv * Cai)/B)

def euler_method(end):
	
	#Setting initial conditions up
	step = 0
	Cai = 5
	Ui = -10
	i = 1

	#Doing Euler method's iterations
	while step <= end:

		Cai = Cai + delta_z * Ui
		Ui = f(Ui, Cai)
		step += delta_z
		i += 1
	
	return Cai

def main():

	#Showing results
	print(f"Ca(L/2) = {euler_method(L/2)}")
	print(f"Ca(L/4) = {euler_method(L/4)}")
	print(f"Ca(3*L/4) = {euler_method((3*L)/4)}")
	print(f"Ca(L) = {euler_method(L)}")

if __name__ == '__main__':
	main()