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

        P1 = MXMultiply(A11, (MatrixMath.diff(B12, B22)))
        P2 = MXMultiply(MatrixMath.sum(A11, A12), B22)
        P3 = MXMultiply(MatrixMath.sum(A21, A22), B11)
        P4 = MXMultiply(A22, MatrixMath.diff(B21, B11))
        P5 = MXMultiply(MatrixMath.sum(A11, A22), MatrixMath.sum(B11, B22))
        P6 = MXMultiply(MatrixMath.diff(A12, A22), MatrixMath.sum(B21, B22))
        P7 = MXMultiply(MatrixMath.diff(A11, A21), MatrixMath.sum(B11, B12))

        # recursive calls for the resulting matrix
        C11 = P5 + P4 - P2 + P6
        C12 = P1 + P2
        C21 = P3 + P4
        C22 = P5 + P1 - P3 - P7

    return np.block([[C11, C12], [C21, C22]])

