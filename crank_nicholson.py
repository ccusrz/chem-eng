"""
-Problem:
There's a metallic bar (alpha = 0.18cm) of about 120 centimetres long,
with an initial temperature distribution given by:
	U(x, 0) = 10x^2 Where U is expressed as °C and X as cm.

It's also known that:
	U(0, t) = 6(15 - t)
	U(L, t) = 2t - 3

Determine the temperature distribution after 60 seconds.

-Solution approach:
Crank-Nicholson method, according to the convergence standard.
"""

import numpy as np
import matplotlib.pyplot as plt

#Constants
alpha = 0.18
length = 120
delta_X = 24
delta_T = 10

def cramer_rule4x4(matrix, column):

	#print(matrix)
	#Determinant of the base matrix
	D = np.linalg.det(matrix)

	#Saving copy of column of independent terms
	cpy = column.copy()

	#print(cpy)
	#print(D)
	#Saving three copies of the base matrix
	Da, Db, Dc, Dd = matrix.copy(), matrix.copy(), matrix.copy(), matrix.copy()

	#Computing Da, Db and Dc
	for i in range(len(cpy)):
		Da[i,0] = cpy[i]
		Db[i,1] = cpy[i]
		Dc[i,2] = cpy[i]
		Dd[i,3] = cpy[i]

	#Determinants of Da, Db and Dc respectively
	Da, Db, Dc, Dd = np.linalg.det(Da), np.linalg.det(Db), np.linalg.det(Dc), np.linalg.det(Dd)

	#Returning list of resulting values
	return [Da/D, Db/D, Dc/D, Dd/D]

def left_temperature(T):
	return 6*(15-T)

def right_temperature(T):
	return 2*T - 3

def first_temperatures(X):
	return 10 * (X**2)

def next_temperature(lamb, prev_to_next_temp, curr_row, last_temp_to_next_temp):
	
	column = np.array([ curr_row[0] + curr_row[2] + prev_to_next_temp,
						curr_row[1] + curr_row[3],
						curr_row[2] + curr_row[4],
						curr_row[3] + curr_row[5] + last_temp_to_next_temp
						]).reshape(4, 1)

	matrix = np.array( [
						[4, -1, 0, 0], 
						[-1, 4, -1, 0],
						[0, -1, 4, -1],
						[0, 0, -1, 4] 
						])

	return cramer_rule4x4(matrix, column)

def crank_nicholson(table, alpha):

	#Setting first temperatures up
	for temp in range(2, 6):
		table[1, temp] = first_temperatures(table[0, temp])

	#Defining standard of convergence
	lamb = alpha * ((delta_T)/(delta_X)**2)

	#Doing iterations for Crank-Nicholson method
	for row in range(1, 8):
		if row < 7: 
			prev_to_next_temp = table[row + 1][1]
			table[row + 1, range(2, 6)] = next_temperature(lamb, prev_to_next_temp, table[row][1:], table[row + 1][6])		
	
def main():
	#General table for the problem
	table = np.array([0, 0, 0, 0, 0, 0, 0], dtype='float32')
	table = np.repeat(table, 8).reshape(8, 7)

	#Setting initial temperature conditions up
	table[0, 1:7] = range(0, length+1, delta_X)
	T = 0
	for i in range(1, 8): 
		table[i, 0] = T
		table[i, 1] = left_temperature(T)
		table[i, 6] = right_temperature(T)
		T += 10

	crank_nicholson(table, alpha)

if __name__ == '__main__':
	main()
