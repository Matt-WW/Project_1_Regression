# -*- coding: utf-8 -*-
"""
hw1_regression.py

W_RR = (lambda*I + X^t*X)^-1*(X^t*y)

W_RR = (sub_matrix_1 + sub_matrix_2)^-1*(sub_matrix_3)

W_RR = (sub_matrix_4)^-1*(sub_matrix_3)

W_RR = (sub_matrix_5)*(sub_matrix_3)

W_RR = sub_matrix_6

"""

import sys
import csv
import numpy as np

#   READ IN VALUE OF LAMBDA AND ASSIGN TO VARIABLE
input_lambda = float(sys.argv[1])

#   READ IN VALUE OF SIGMA2 AND ASSIGN TO VARIABLE
input_sigma2 = float(sys.argv[2])


#   READ IN X TRAINING DATA
x_training_data = open(sys.argv[3],'r')
csv_reader = csv.reader(x_training_data)
input_x_training_data = list(csv_reader)
x_training_data.close()
X = np.array(input_x_training_data, dtype=np.float64)


#   READ IN Y TRAINING DATA
y_training_data = open(sys.argv[4],'r')
csv_reader = csv.reader(y_training_data)
input_y_training_data = list(csv_reader)
y_training_data.close()
Y = np.array(input_y_training_data, dtype=np.float64)


#   READ IN X TESTING DATA
x_testing_data = open(sys.argv[5],'r')
csv_reader = csv.reader(x_testing_data)
input_x_testing_data = list(csv_reader)
x_testing_data.close()
X0 = np.array(input_x_testing_data, dtype=np.float64)


#   READ IN DIMENSIONS OF DATA AND ASSIGN TO VARIABLE
number_of_observations = len(input_x_training_data[0])


#   SET UP IDENTITY MATRIX
I = np.array(np.identity(number_of_observations), dtype=np.float64)


#   BEGIN MATRIX OPERATIONS. Multiply lambda by an identity matrix
sub_matrix_1 = np.multiply(I, input_lambda)


#   BEGIN MATRIX OPERATIONS. Multiply the transpose of X by X
sub_matrix_2 = np.dot(np.transpose(X), X)


#   BEGIN MATRIX OPERATIONS. Multiply the transpose of X by Y
sub_matrix_3 = np.dot(np.transpose(X), Y)


#   BEGIN MATRIX OPERATIONS. Add matrices 1 and 2 together.
sub_matrix_4 = np.add(sub_matrix_1, sub_matrix_2)


#   BEGIN MATRIX OPERATIONS. Invert matrix 4
sub_matrix_5 = np.linalg.inv(sub_matrix_4)

#   BEGIN MATRIX OPERATIONS. Multiply matrix 5 by matrix 3
W_RR = np.dot(sub_matrix_5, sub_matrix_3)

print W_RR

