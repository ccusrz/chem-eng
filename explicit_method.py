"""
Problem:
There is a 4cm bar at room temperature of 25°C. 
One of its ends is subjected to a 120°c temperature,
and the other end to a 50°c temperature. 
Calculate temperature distribution for each 0.4 cm after 5 seconds,
for the following material: steel, pottery and copper.

The given alpha coefficients are:
0.167cm^3 / seg
0.1515cm^3 / seg
0.1350cm^3 / seg

According to the obtained results, indicate which material 
corresponds to each given alpha value and say why.

Solution approach:
Utilize the explicit method according to the convergence standard.
"""

import numpy as np
import matplotlib.pyplot as plt

#Constants
length = 4
a1 = 0.167
a2 = 0.1515
a3 = 0.1350
left_t = 120
right_t = 50

def next_temperature(prev_temp, prev_next_temp, prev_to_prev_temp, lamb):
	"""
	Calculator of the next temperature
	to be computed with the explicit
	method
	"""
	return prev_temp + lamb * (prev_next_temp - 2*prev_temp + prev_to_prev_temp)

def explicit_method(table, alpha):

	#Setting up post-initial conditions, according to the convergence standard
	delta_x = 0.004
	delta_t = 1/2*(pow(delta_x, 2)/alpha)

	#Calculating lambda of next temperature formula
	lamb = alpha * (delta_t/pow(delta_x, 2))
	
	#Doing the explicit method iterations until make it to 5 seconds
	step = 1
	i = 1
	while delta_t <= 5:
		
		delta_t += delta_t

		#Saving increments to table
		table[i,0] = step		
		if delta_t > 5: table[i,1] = 5.
		else: table[i,1] = delta_t

		#Calculating each temperature
		prev_to_prev_temp = left_t
		for temp in range(3, 11):
			copy = table.copy()
			prev_temp = copy[i-1, temp]
			if temp < 11: prev_next_temp = copy[i-1, temp + 1]
			if temp > 3: prev_to_prev_temp = copy[i-1, temp - 1]
			table[i, temp] = next_temperature(prev_temp, prev_next_temp, prev_to_prev_temp, lamb)
		
		#Iterating
		step += 1
		i += 1
		
	return table

#General table for the problem
table = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype='float32')
table = np.repeat(table, 18).reshape(18, 12)

#Setting initial temperature conditions up
table[0, range(2, 11)] = 25
table[:, 2] = left_t
table[:, 11] = right_t

#Explicit method for alpha 1, 2, and 3 respectively
table1, table2, table3 = explicit_method(table, a1), explicit_method(table, a2), explicit_method(table, a3)

#Displaying temperature distributions
fig, axs = plt.subplots(3, sharex = True, sharey = True)

axs[0].plot(table1[:, 1], table1[:, range(2, 12)], 'green')
axs[0].set_title('alpha = 0.167')

axs[1].plot(table2[:, 1], table2[:, range(2, 12)], 'red')
axs[1].set_title('alpha = 0.1515')
axs[1].set(ylabel = 'Temperature (°C) ')

axs[2].plot(table3[:, 1], table3[:, range(2, 12)], 'blue')
axs[2].set_title('alpha = 0.1350')
axs[2].set(xlabel = 'Time (seconds)')

plt.show()
