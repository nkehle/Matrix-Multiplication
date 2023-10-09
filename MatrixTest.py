# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 2

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import timeit

# import algorithms
import DNCMxMultiplication
import MatrixMath
import NaiveMxMultiplication
import StrassenAlgorithm

matplotlib.use('TkAgg')

def compareTime():
    sizes = [8,16,32,64,131]
    repeats = 1
    avgNaive = []
    avgDNC = []
    avgStrassen = []

    for size in sizes:
        nCnt = 0
        dCnt = 0
        sCnt = 0
        for j in range(repeats):
            A = np.random.randint(low=0, high=100, size=(size, size))
            B = np.random.randint(low=0, high=100, size=(size, size))

            # error checking and padding of matrices
            A = MatrixMath.padMatricies(A, B)[0]
            B = MatrixMath.padMatricies(A, B)[1]

            # run the naive version and time
            naiveTime = timeit.timeit(lambda: NaiveMxMultiplication.MXMultiply(A, B), setup="pass", number=1)
            nCnt += naiveTime

            # run the DNC version and time
            dncTime = timeit.timeit(lambda: DNCMxMultiplication.MXMultiply(A, B), setup="pass", number=1)
            dCnt += dncTime

            # run the Strassen version and time
            strassenTime = timeit.timeit(lambda: StrassenAlgorithm.MXMultiply(A, B), setup="pass", number=1)
            sCnt += strassenTime

        # add the averages to their respected lists
        avgNaive.append(round(nCnt/repeats, 5))
        avgDNC.append(round(dCnt/repeats, 5))
        avgStrassen.append(round(sCnt/repeats, 5))

    return avgNaive, avgDNC, avgStrassen

# gather results
res = compareTime()

print("Naive:    ", res[0], "\nDNC:      ", res[1], "\nStrassen: ", res[2])

'''
# plot linear
plt.plot(res[0], res[1], label='findSecondLinear', color='blue', linestyle='-')

# plot dnc
plt.plot(res[0], res[2], label='findSecondDNC ', color='red', linestyle='--')

# labels
plt.xlabel('Length of the Array')
plt.ylabel('Average number of comparisons')
plt.title('Avg number of comparisons to find second largest sizes')
plt.grid = True
plt.legend()

# show plotting
plt.show()

'''


'''A = np.array([[3, 4, -2, 0, 6, -1, 4, 4],
              [2, 2, 0, 3, -3, -2, 6, -2],
              [1, 3, 8, 3, 9, 1, -2, -5],
              [4, -2, 5, -1, 0, 0, -6, 2],
              [3, 4, -1, -3, 3, 0, 8, 1],
              [5, 5, 3, -2, -1, -3, 7, 1],
              [1, -2, -3, 7, 1, 2, 0, 0],
              [0, 0, -1, 0, 2, -2, 0, -3]])

B = np.array([[6, 3, 4, 2, 2, 3, 2, 7],
              [0, 3, 2, -2, -2, 3, 3, 1],
              [0, 3, 1, 0, 0, 4, 5, -2],
              [-2, -2, 0, 5, 0, 7, -6, 0],
              [2, -2, -1, 7, 0, 1, -9, 0],
              [5, -2, -2, 2, -2, -1, 2, 3],
              [0, -2, -4, 1, 4, 0, -2, 1],
              [-1, 0, 0, 6, -5, 2, 0, -2]])'''