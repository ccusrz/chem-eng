import numpy as np
import sys

def cramer_ruleNxN(matrix, column, N):
	"""
	Returns roots of N systems of equations
	with N independent terms through
	Cramer's Rule.

	The first two parameters are to be numpy objects.
	"""

	#Determinant of base matrix
	D = np.linalg.det(matrix)

	#Saving copy of column of independent terms
	iterms = column.copy()

	#Array of copies for base matrix
	copies = np.array([matrix.copy() for i in range(N)])

	#Arranging each copy of base matrix with column of independent terms
	for i in range(N):
		for j in range(N):
			copies[i][j][i] = iterms[j]

	#Calculating determinants of each updated copy and returning list of roots
	roots = lambda x: np.linalg.det(x) / D
	return list(map(roots, copies))

if __name__ == '__main__':
	sys.exit("Script intended to be imported to another module.")