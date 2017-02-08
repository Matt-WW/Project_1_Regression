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

#   COMPUTE W_RR
W_RR = np.dot(np.linalg.inv(np.add(np.multiply(I, input_lambda), np.dot(np.transpose(X), X))), np.dot(np.transpose(X), Y))

print W_RR

