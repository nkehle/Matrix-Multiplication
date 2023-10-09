# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 2

import numpy as np
import MatrixMath

def MXMultiply(A, B):

    hA = (A.shape[0])      # height of A
    wA = (A.shape[1])      # width of A
    wB = (B.shape[1])      # width of B

    # create result matrix
    C = np.zeros((A.shape[0], B.shape[1]), dtype=int)

    for i in range(hA):
        for j in range(wB):
            sum = 0
            for k in range(wA):
                sum += A[i, k] * B[k, j]
            C[i, j] = sum

    return C

