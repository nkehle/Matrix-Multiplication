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

"""
    compareTime: computes the averge times for running the three algorithms
    Parameters:
        parameter1 (sizes = []): array of given sizes of matricies 
    Returns:
        res[0] -> # of rows
        res[1] -> # of cols
"""
def compareTime(sizes):
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
        avgNaive.append(round(nCnt / repeats, 5))
        avgDNC.append(round(dCnt / repeats, 5))
        avgStrassen.append(round(sCnt / repeats, 5))

    return avgNaive, avgDNC, avgStrassen

def multipleExample():
    # choose a size
    size = 4
    # creates random matrices
    A = np.random.randint(low=0, high=100, size=(size, size))
    B = np.random.randint(low=0, high=100, size=(size, size))

    # error checking and padding of matrices
    A = MatrixMath.padMatricies(A, B)[0]
    B = MatrixMath.padMatricies(A, B)[1]

    naiveRes = NaiveMxMultiplication.MXMultiply(A, B)
    dncRes = DNCMxMultiplication.MXMultiply(A, B)
    strassRes = StrassenAlgorithm.MXMultiply(A, B)

    print("Naive Product:\n", naiveRes, "\nDNC Product:\n", dncRes, "\nStrassen Product:\n", strassRes, '\n')


''' ** MULTIPLICATION DEMONSTRATION ** '''
multipleExample()


''' ** PLOTTING THE GRAPHS WITH AVERAGE TIMES ** '''
sizes = [2, 4, 8, 16, 32, 64, 128, 256]
res = compareTime(sizes)

print("Naive:    ", res[0], "\nDNC:      ", res[1], "\nStrassen: ", res[2], '\n')

# plot naive
plt.plot(sizes, res[0], label='Naive', color='red', linestyle='-')

# plot dnc
plt.plot(sizes, res[1], label='Divide n Conquer', color='blue', linestyle='--')

# plot strassen
plt.plot(sizes, res[2], label='Strassens', color='green', linestyle='-.')

# labels
plt.xlabel('Size of the Matrix NxN')
plt.ylabel('Average time to multiply (Seconds)')
plt.title('Average MXMultiply Time with Differnet Algorithms')
plt.grid = True
plt.legend()

# show plotting
plt.show()
