# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 2

import numpy as np
import MatrixMath

def MXMultiply(A, B):
    # base case
    if len(A) == 1:
        return A * B
    else:
        midIndex = len(A) // 2  # middle of the matrix used for submatricies

        # split A into 4
        A11 = A[:midIndex, :midIndex]
        A12 = A[:midIndex, midIndex:]
        A21 = A[midIndex:, :midIndex]
        A22 = A[midIndex:, midIndex:]

        # split B into 4
        B11 = B[:midIndex, :midIndex]
        B12 = B[:midIndex, midIndex:]
        B21 = B[midIndex:, :midIndex]
        B22 = B[midIndex:, midIndex:]

        # recursive calls for the resulting matrix
        C11 = MatrixMath.sum(MXMultiply(A11, B11), MXMultiply(A12, B21))
        C12 = MatrixMath.sum(MXMultiply(A11, B12), MXMultiply(A12, B22))
        C21 = MatrixMath.sum(MXMultiply(A21, B11), MXMultiply(A22, B21))
        C22 = MatrixMath.sum(MXMultiply(A21, B12), MXMultiply(A22, B22))

    return np.block([[C11, C12], [C21, C22]])
