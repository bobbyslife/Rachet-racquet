# Simple Linear Regression on the Swedish Insurance Dataset
from random import seed
from random import randrange
from csv import reader
from math import sqrt

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
 
# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			if row[0] == "tourney_name": #skip the first row of headers
				continue
			dataset.append(row)
	return dataset

def create_arrays(dataset1, dataset2, dataset3, dataset4, dataset5, dataset6):
	age_col = 5
	hand_col = 2
	height_col = 3
	country_col = 4
	rank_col = 6
	age = list() # col 5
	hand = list() # col 2
	height = list() # col 3
	country = list() # col 4
	rank = list() # col 6

	x_list = list()
	y_list = list()

	for row in dataset1:
		if row[age_col] != '' and row[hand_col] != '' and row[height_col] != '' and row[country_col] != '' and row[rank_col] != '':
			if (row[hand_col] == 'R'):
				x_list.append([int(float(row[age_col])), '0', row[height_col]])
			else:
				x_list.append([int(float(row[age_col])), '1', row[height_col]])
			rank.append([row[rank_col]])

	for row in dataset2:
		if row[age_col] != '' and row[hand_col] != '' and row[height_col] != '' and row[country_col] != '' and row[rank_col] != '':
			if (row[hand_col] == 'R'):
				x_list.append([int(float(row[age_col])), '0', row[height_col]])
			else:
				x_list.append([int(float(row[age_col])), '1', row[height_col]])
			rank.append([row[rank_col]])

	for row in dataset3:
		if row[age_col] != '' and row[hand_col] != '' and row[height_col] != '' and row[country_col] != '' and row[rank_col] != '':
			if (row[hand_col] == 'R'):
				x_list.append([int(float(row[age_col])), '0', row[height_col]])
			else:
				x_list.append([int(float(row[age_col])), '1', row[height_col]])
			rank.append([row[rank_col]])

	for row in dataset4:
		if row[age_col] != '' and row[hand_col] != '' and row[height_col] != '' and row[country_col] != '' and row[rank_col] != '':
			if (row[hand_col] == 'R'):
				x_list.append([int(float(row[age_col])), '0', row[height_col]])
			else:
				x_list.append([int(float(row[age_col])), '1', row[height_col]])
			rank.append([row[rank_col]])

	for row in dataset5:
		if row[age_col] != '' and row[hand_col] != '' and row[height_col] != '' and row[country_col] != '' and row[rank_col] != '':
			if (row[hand_col] == 'R'):
				x_list.append([int(float(row[age_col])), '0', row[height_col]])
			else:
				x_list.append([int(float(row[age_col])), '1', row[height_col]])
			rank.append([row[rank_col]])

	for row in dataset6:
		if row[age_col] != '' and row[hand_col] != '' and row[height_col] != '' and row[country_col] != '' and row[rank_col] != '':
			if (row[hand_col] == 'R'):
				x_list.append([int(float(row[age_col])), '0', row[height_col]])
			else:
				x_list.append([int(float(row[age_col])), '1', row[height_col]])
			rank.append([row[rank_col]])

	x = np.array(x_list, dtype='<U32')
	y = np.array(rank, dtype='<U32')
	return [x, y]

# load and prepare data
dataset1 = load_csv('atp_matches_2012_grand_slams.csv')
dataset2 = load_csv('atp_matches_2013_grand_slams.csv')
dataset3 = load_csv('atp_matches_2014_grand_slams.csv')
dataset4 = load_csv('atp_matches_2015_grand_slams.csv')
dataset5 = load_csv('atp_matches_2016_grand_slams.csv')
dataset6 = load_csv('atp_matches_2017_grand_slams.csv')
train_x, train_y = create_arrays(dataset1, dataset2, dataset3, dataset4, dataset5, dataset6)

#print(train_x.shape)
#print(train_x)
#print("\n")
#print(train_y.shape)
#print(train_y)

regr = linear_model.LinearRegression()
# Train the model using the training sets
regr.fit(train_x, train_y)

# The coefficients
print('Coefficients: \n', regr.coef_)

# age, right/left hand, height
bad_player = np.array([25, 0, 190])
good_player = np.array([25, 1, 190])

bad_player_rank = (-regr.coef_[0][0]*bad_player[0]) + (regr.coef_[0][1]*bad_player[1]) - (regr.coef_[0][2]*bad_player[2])
print("Bad Player:", bad_player_rank)
good_player_rank = (-regr.coef_[0][0]*good_player[0]) + (regr.coef_[0][1]*good_player[1]) - (regr.coef_[0][2]*good_player[2])
print("Good Player:", good_player_rank)
