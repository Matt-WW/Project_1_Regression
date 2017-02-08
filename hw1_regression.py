# -*- coding: utf-8 -*-
"""
hw1_regression.py

W_RR = (lambda*I + X^t*X)^-1*(X^t*y)

"""

import sys
import csv
import numpy as np

#   READ IN VALUE OF LAMBDA AND ASSIGN TO VARIABLE
input_lambda = float(sys.argv[1])
#print input_lambda
#print type(input_lambda)


#   READ IN VALUE OF SIGMA2 AND ASSIGN TO VARIABLE
input_sigma2 = float(sys.argv[2])
#print input_sigma2
#print type(input_sigma2)


#   READ IN X TRAINING DATA
x_training_data = open(sys.argv[3],'r')
csv_reader = csv.reader(x_training_data)
input_x_training_data = list(csv_reader)
x_training_data.close()
#print input_x_training_data
#print input_x_training_data[0][0]
#print type (input_x_training_data)


#   READ IN Y TRAINING DATA
y_training_data = open(sys.argv[4],'r')
csv_reader = csv.reader(y_training_data)
input_y_training_data = list(csv_reader)
y_training_data.close()
#print input_y_training_data
#print input_y_training_data[0][0]
#print type (input_y_training_data)


#   READ IN X TESTING DATA
x_testing_data = open(sys.argv[5],'r')
csv_reader = csv.reader(x_testing_data)
input_x_testing_data = list(csv_reader)
x_testing_data.close()
#print input_x_testing_data
#print input_x_testing_data[0][0]
#print type (input_x_testing_data)


#   READ IN DIMENSIONS OF DATA AND ASSIGN TO VARIABLE
number_of_observations = len(input_x_training_data[0])
#print number_of_observations


#   SET UP IDENTITY MATRIX
identity_matrix = np.matrix(np.identity(number_of_observations))
#print identity_matrix
print np.shape(identity_matrix)
print type(identity_matrix)


#   BEGIN MATRIX OPERATIONS. Multiply lambda by an identity matrix
sub_matrix_1 = identity_matrix * input_lambda
#print sub_matrix_1
print np.shape(sub_matrix_1)
print type(sub_matrix_1)


#   BEGIN MATRIX OPERATIONS. Transpose the x training data
sub_matrix_2 = map(list, zip(*input_x_training_data))
print sub_matrix_2
print np.shape(sub_matrix_2)


#   BEGIN MATRIX OPERATIONS. Multiply the transpose of X by X
sub_matrix_3 = np.asarray(sub_matrix_2) * np.asarray(input_x_training_data)
print sub_matrix_3
print np.shape(sub_matrix_3)


#   BEGIN MATRIX OPERATIONS. Add matrices 1 and 3 together.
sub_matrix_4 = sub_matrix_1 + sub_matrix_3
print sub_matrix_4
print np.shape(sub_matrix_4)




