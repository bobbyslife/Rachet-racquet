from math import sqrt
from random import seed
from random import randrange
from csv import read

#root mean squared error
def rsme_metric(actual, predicted):
	sum_error =0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error**2)
	mean error = sum_error / float(len(actual))
	return sqrt(mean_error)

def evaluate_algorithm(dataset, algorithm):
	test_set = list()
	for row in dataset:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)
	predicted = algorithm(dataset, test_set)
	print(predicted)
	actual = [row[-1] for row in dataset]
	rmse = rmse_metric(actual, predicted)
	return rmse

def mean(values):
	return sum(values) / float(len(values))

def variance(values, mean):
	return sum([x-mean)**2 for x in values])

def covariance(x, mean_x, y, mean_y):
	covar =0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x)* (y[i] - mean_y)
	return covar

def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean, y_mean = mean(x), mean(y)
	b1 = covariance(x, x_mean,y,y_mean) / variance(x,x_mean)
	b0 = y_mean - b1 * x_mean
	return[b0,b1]

def simple_linear_regression(train, test):
	predictions = list()
	b0, b1 = coefficients(train)
	for row in test:
		yhat = b0 + b1*row[0]
		predictions.append(yhat)
	return predictions
