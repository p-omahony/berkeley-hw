# HW2 - O'MAHONY Paul

import numpy as np
import random as rd

def multiply_vectors(mat1, mat2) :
    return mat1.dot(mat2)

if __name__ == '__main__' :

    # Create matrix A with size (3,5) containing random numbers
    A = np.matrix(np.random.random([3,5]))
    print('Matrix 3x5 A containing random numbers: \n', A)
    print('\n')

    # Find the size and length of matrix A
    shape = A.shape
    w, h = shape[0], shape[1]
    print('Number of rows of A: %s / Number of columns of A: %s' % (w,h))
    print('\n')

    # Resize (crop/slice) matrix A to size (3,4)
    A = np.resize(A, (3,4))
    print('Resized A (3x4): \n %s' % A)
    print('\n')

    # Find the transpose of matrix A and assign it to B
    B = A.T
    print('A transposed (B): \n %s' % B)
    print('\n')

    # Find the minimum value in column 1 of matrix B
    min1 = np.min(A[0])
    print('Minimum value in the first column of B: %s' % min1)
    print('\n')

    # Find the minimum and maximum values for the entire matrix A
    min_A, max_A = np.min(A), np.max(A)
    print('Minimum value of A: %s / Maximum value of A: %s' % (min_A,max_A))
    print('\n')

    # Create vector X (an array) with 4 random numbers
    X = np.array(np.random.random([4]))
    print('X matrix: \n %s' % X)
    print('\n')

    # Create a function and pass vector X and matrix A in it
    # In the new function multiply vector X with matrix A and assign the result to D
    D = multiply_vectors(A, X)
    print('D = A.X = \n %s' % D)
    print('\n')

    # Create a complex number Z with absolute and real parts != 0
    Z = 2 + 6j
    print('Complex number Z: %s' % Z)
    print('\n')

    # Show its real and imaginary parts as well as it’s absolute value
    real, imag, abs = Z.real, Z.imag, abs(Z)
    print('Real part: %s \ Imaginary part: %s \ Absolute value: %s' % (real, imag, abs))
    print('\n')

    # Multiply result D with the absolute value of Z and record it to C
    C = D*abs
    print('C = D*abs(Z) = \n %s' % C)
    print('\n')

    # Convert matrix B from a matrix to a string and overwrite B
    name = "Paul O'MAHONY"
    B = name + ' is done with HW2!'
    print(B)
