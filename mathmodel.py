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
from cramer_rule import cramer_ruleNxN

def analysis(results, equations):
	
	#Building matrixes
	results = np.array([results[0], results[1], results[2]]).reshape(3,1)
	equations = np.array([equations[0], equations[1], equations[2]])

	#Trying to apply the Cramer's Rule
	try:
		return cramer_ruleNxN(equations, results, 3)
	except ZeroDivisionError:
		return None

#Doing analysis of each linear combination
constants = analysis([23.4, 41.5, 52.4], [[1, 2.3, 3.1], [2, 4.5, 5.2], [3, 5.3, 6.7]])
print(f"Solution for linear combination of (1), (2) and (3): {list(map(round, constants))}", end = "\n" * 2)

constants = analysis([23.4, 41.5, 57.8], [[1, 2.3, 3.1], [2, 4.5, 5.2], [4, 6.1, 7.1]])
print(f"Solution for linear combination of (1), (2) and (4): {list(map(round, constants))}", end = "\n" * 2)

constants = analysis([23.4, 41.5, 63.9], [[1, 2.3, 3.1], [2, 4.5, 5.2], [5, 6.8, 7.7]])
print(f"Solution for linear combination of (1), (2) and (5): {list(map(round, constants))}", end = "\n" * 2)

constants = analysis([52.4, 57.8, 63.9], [[3, 5.3, 6.7], [4, 6.1, 7.1], [5, 6.8, 7.7]])
print(f"Solution for linear combination of (3), (4) and (5): {list(map(round, constants))}", end = "\n" * 2)

constants = analysis([52.4, 57.8, 23.4], [[3, 5.3, 6.7], [4, 6.1, 7.1], [1, 2.3, 3.1]])
print(f"Solution for linear combination of (3), (4) and (1): {list(map(round, constants))}", end = "\n" * 2)

constants = analysis([52.4, 57.8, 41.5], [[3, 5.3, 6.7], [4, 6.1, 7.1], [2, 4.5, 5.2]])
print(f"Solution for linear combination of (3), (4) and (2): {list(map(round, constants))}", end = "\n" * 2)

#Printing out the conclusion
print("General solution to the system: a = 1, b = 3, c = 5")