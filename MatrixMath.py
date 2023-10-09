# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 2

import numpy as np

# TODO
def sum(A, B):
    n1, n2 = A.shape
    C = np.zeros_like(A)

    for i in range(n1):
        for j in range(n2):
            C[i, j] = A[i, j] + B[i, j]

    return C
def diff(A, B):
    n1, n2 = A.shape
    C = np.zeros_like(A)

    for i in range(n1):
        for j in range(n2):
            C[i, j] = A[i, j] - B[i, j]

    return C

def powerof2(n):
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0

def nextpowerof2(n):
    while not powerof2(n):
        n += 1
    return n

def resultDims(A, B):
    resRows = A.shape[0]
    resCols = B.shape[1]

    return resRows, resCols

def padMatricies(A, B):
    if not (nextpowerof2(A.shape[0]) == nextpowerof2(A.shape[1])
            == nextpowerof2(B.shape[0]) == nextpowerof2(B.shape[1])):

        # error checking / padding -> find the power of 2
        hA = (A.shape[0])  # height of A
        wA = (A.shape[1])  # width of A
        hB = (B.shape[0])  # height of B
        wB = (B.shape[1])  # width of B

        # desired n that is the next power of 2 for the largest of the 4 possibilities
        n = nextpowerof2(max(hA, wA, hB, wB))

        # pad matrix A
        padRow = n - hA
        padCol = n - wA
        A = np.pad(A, ((0, padRow), (0, padCol)), mode='constant', constant_values=0)

        # pad matrix B
        padRow = n - hB
        padCol = n - wB
        B = np.pad(B, ((0, padRow), (0, padCol)), mode='constant', constant_values=0)