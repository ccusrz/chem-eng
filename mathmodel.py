"""
-Problem:
Some mathematical model answers to this equation:
 w = ax + by + cz
The following represents this model behaviour:
  a + 2.3b + 3.1c = 23.4 (1)
 2a + 4.5b + 5.2z = 41.5 (2)
 3a + 5.3b + 6.7z = 52.4 (3)
 4a + 6.1b + 7.1z = 57.8 (4)
 5a + 6.8b + 7.7z = 63.9 (5)
 
Find the value of constants a, b and c.

-Solution approach: 
This may be a nonlinear behaviour and it's considered to be an overdetermined system of equations. 
Let's cluster some of them in linear combinations to examine consistent values in the behaviour exposed.

I'll use Cramer's rule for this purpose.
"""

import numpy as np

def cramer_rule3x3(matrix, column):

	#Determinant of the base matrix
	D = np.linalg.det(matrix)

	#Saving copy of column of independent terms
	cpy = column.copy()

	#Saving three copies of the base matrix
	Da, Db, Dc = matrix.copy(), matrix.copy(), matrix.copy()

	#Computing Da, Db and Dc
	for i in range(len(cpy)):
		Da[i,0] = cpy[i]
		Db[i,1] = cpy[i]
		Dc[i,2] = cpy[i]

	#Determinants of Da, Db and Dc respectively
	Da, Db, Dc = np.linalg.det(Da), np.linalg.det(Db), np.linalg.det(Dc)

	#Returning list of constants values
	return [Da/D, Db/D, Dc/D]

def analysis(results, equations):
	
	#Building matrixes
	results = np.array([results[0], results[1], results[2]]).reshape(3,1)
	equations = np.array([equations[0], equations[1], equations[2]])

	#Trying to apply the Cramer's Rule
	try:
		return cramer_rule3x3(equations, results)
	except ZeroDivisionError:
		return None

#By clustering equations (1), (2) and (3) respectively we've got a consistent behaviour, given a = 1, b = 3 and c = 5.
constants = analysis([23.4, 41.5, 52.4], [[1, 2.3, 3.1], [2, 4.5, 5.2], [3, 5.3, 6.7]])
print(f"Solution for linear combination of (1), (2) and (3): {list(map(round, constants))}", end = "\n" * 2)

#By clustering equations (1), (2) and (4) respectively we've got a consistent behaviour, given a = 1, b = 3 and c = 5.
constants = analysis([23.4, 41.5, 57.8], [[1, 2.3, 3.1], [2, 4.5, 5.2], [4, 6.1, 7.1]])
print(f"Solution for linear combination of (1), (2) and (4): {list(map(round, constants))}", end = "\n" * 2)

#By clustering equations (1), (2) and (5) respectively we've got a consistent behaviour, given a = 1, b = 3 and c = 5.
constants = analysis([23.4, 41.5, 63.9], [[1, 2.3, 3.1], [2, 4.5, 5.2], [5, 6.8, 7.7]])
print(f"Solution for linear combination of (1), (2) and (5): {list(map(round, constants))}", end = "\n" * 2)

#By clustering equations (3), (4) and (5) respectively we've got a consistent behaviour, given a = 1, b = 3 and c = 5.
constants = analysis([52.4, 57.8, 63.9], [[3, 5.3, 6.7], [4, 6.1, 7.1], [5, 6.8, 7.7]])
print(f"Solution for linear combination of (3), (4) and (5): {list(map(round, constants))}", end = "\n" * 2)

#By clustering equations (3), (4) and (1) respectively we've got a consistent behaviour, given a = 1, b = 3 and c = 5.
constants = analysis([52.4, 57.8, 23.4], [[3, 5.3, 6.7], [4, 6.1, 7.1], [1, 2.3, 3.1]])
print(f"Solution for linear combination of (3), (4) and (1): {list(map(round, constants))}", end = "\n" * 2)

#By clustering equations (3), (4) and (2) respectively we've got a consistent behaviour, given a = 1, b = 3 and c = 5.
constants = analysis([52.4, 57.8, 41.5], [[3, 5.3, 6.7], [4, 6.1, 7.1], [2, 4.5, 5.2]])
print(f"Solution for linear combination of (3), (4) and (2): {list(map(round, constants))}", end = "\n" * 2)

#Printing out the conclusion
print("General solution to the system: a = 1, b = 3, c = 5")