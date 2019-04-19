# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 02:38:59 2019

@author: TUNATECH
"""

import numpy as np

"""Get the number of variables"""
N = int(input("How many variables: "))
"""Set iteration limit"""
ITERATION_LIMIT = int(input("Iteration Limit: "))
"""initialize the matrix """
A = np.zeros((N, N))
B = np.zeros((N))
for i in range(0, N):
    for j in range(0, N):
        A[i, j] = int(input("Enter "+"A"+"["+str(i)+","+str(j)+"] :"))
print(A)
"""Check for errors in the matrix and correct them if any"""
QUES_1 = int(input("How many mistake is in your matrix A: "))
for i in range(QUES_1):
    i, j = eval(input("Enter the position (i,j): "))
    val = int(input("Enter the correct value: "))
    A[i, j] = val
print(A)
for i in range(N):
    B[i] =int(input("Enter "+"B"+"["+str(i)+"] :"))      
print(B)
QUES_2 = int(input("How many mistake is in your matrix B: "))
for i in range(QUES_2):
    pos = int(input("Enter the position (i): "))
    val = int(input("Enter the correct value: "))
    B[0] = val
print(B)        
print("System of equations:")
for i in range(A.shape[0]):
    row = ["{0:3g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print("[{0}] = [{1:3g}]".format(" + ".join(row), B[i]))

X = np.zeros_like(B)
for it_count in range(1, ITERATION_LIMIT):
    X_new = np.zeros_like(X)
    print("Iteration {0}: {1}".format(it_count, X))
    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], X_new[:i])
        s2 = np.dot(A[i, i + 1:], X[i + 1:])
        X_new[i] = (B[i] - s1 - s2) / A[i, i]
    if np.allclose(X, X_new, rtol=1e-8):
        break
    X = X_new

print("Solution: {0}".format(X))
ERROR = np.dot(A, X) - B
print("ERROR: {0}".format(ERROR))
