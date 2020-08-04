
__author__ : "@rockdevu"

import numpy as np

def distance_bet_2(A, B):
	result = np.sum([abs(a - b) for (a, b) in zip(A, B)])
	return result

if __name__ == "__main__":

	arr1 = [1, 2, 13, 5]
	arr2 = [1, 27, 3, 4]

	result = distance_bet_2(arr1, arr2)
	print("The distance between 2-coordinates is :", result)