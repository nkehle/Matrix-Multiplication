# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 2

import numpy as np
import NaiveMxMultiplication

A = np.array([[3, 4, -2, 0, 6, -1, 4, 4],
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
              [-1, 0, 0, 6, -5, 2, 0, -2]])

C = np.array([[6, 2],
              [5, 10]])

D = np.array([[2, 0, 5],
              [8, 8, 7],
              [4, 1, 6],
              [2, 2, 4],
              [7, 4, 7]])

NaiveRes = NaiveMxMultiplication.matmul(C, D)
DNCRes = NaiveMxMultiplication.matmul(C, D)
StrassenRes = NaiveMxMultiplication.matmul(C, D)


# compare the resulted numpy arrays for all three methods
comp1 = NaiveRes == DNCRes
comp2 = DNCRes == StrassenRes

eq1 = comp1.all()
eq2 = comp2.all()

print(eq1 & eq2)

print(NaiveRes, '\n', DNCRes, '\n', StrassenRes)

