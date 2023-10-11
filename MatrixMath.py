# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 2

import numpy as np

"""
    sum: adds two matricies together 
    Parameters:
        parameter1 (A = matrix): operand 1
        parameter2 (B = matrix): operand 2
    Returns:
        (C = matrix): result of added matricies 
"""
def sum(A, B):
    n1, n2 = A.shape
    C = np.zeros_like(A)

    for i in range(n1):
        for j in range(n2):
            C[i, j] = A[i, j] + B[i, j]

    return C

"""
    diff: subtracts two matricies  
    Parameters:
        parameter1 (A = matrix): operand 1
        parameter2 (B = matrix): operand 2
    Returns:
        (C = matrix): result of subtracted matricies 
"""
def diff(A, B):
    n1, n2 = A.shape
    C = np.zeros_like(A)

    for i in range(n1):
        for j in range(n2):
            C[i, j] = A[i, j] - B[i, j]

    return C

"""
    powerof2: determines if a number is a power of 2
    Parameters:
        parameter1 (int = n) = size
    Returns:
        true or false
"""
def powerof2(n):
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0

"""
    nextpowerof2: returns the next power of 2 from a number or returns the number if its already a power of 2
    Parameters:
        parameter1 (int = n) = size
    Returns:
        n = the next power of two or the original n
"""
def nextpowerof2(n):
    while not powerof2(n):
        n += 1
    return n
"""
    resultdims: returns the dimentions of the product matricie
    Parameters:
        parameter1 (A = matrix): operand 1
        parameter2 (B = matrix): operand 2
    Returns:
        res[0] -> # of rows
        res[1] -> # of cols
"""
def resultDims(A, B):
    resRows = A.shape[0]
    resCols = B.shape[1]

    return resRows, resCols

"""
    padMatricies: pads the matricies with zeros if either of the matricies A or B has a size that is not to the power of 2
    Parameters:
        parameter1 (A = matrix): operand 1
        parameter2 (B = matrix): operand 2
    Returns:
        res[0] -> padded matrix A
        res[1] -> padded matrix B
"""
def padMatricies(A, B):
    if not ((powerof2(A.shape[0])) & (powerof2(A.shape[1])) &
            (powerof2(B.shape[0])) & (powerof2(B.shape[1]))):

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

        A2 = np.pad(A, ((0, padRow), (0, padCol)), mode='constant', constant_values=0)

        # pad matrix B
        padRow = n - hB
        padCol = n - wB
        B2 = np.pad(B, ((0, padRow), (0, padCol)), mode='constant', constant_values=0)
        return A2, B2
    else:
        return A, B

