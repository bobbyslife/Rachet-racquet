import math
import csv
import pandas
import random

#put csv data into pandas dataframe, use atp_matches_20--_grand_slams
atp_data = pandas.read_csv('tennis_data.csv')
atp_data.fillna('x', inplace = True)

#the list of data
playerStats = []
hold1 = []
hold2 = []
#to normalize, hold max & min I FREAKING HAXXORED IT WHY EVEN USE PANDAS I AM *ASHAMED* OF MYSELF OMG
#BUT THERE ISN'T EVEN TIME TO FIX IT SHOOT ME IN THE EAR I DON'T DESERVE TO HEAR
heightMax =0
heightMin = 100000
ageMax=0
ageMin=1000000
rankMax=0
rankMin=1000000
rankPtsMax=0
rankPtsMin=10000
aceMax=0
aceMin=100000
dfMax=0
dfMin=1000000
svptMax=0
svptMin=100000
in1Max=0
in1Min=1000000
won1Max=0
won1Min=1000000
won2Max=0
won2Min=1000000
svGmsMax=0
svGmsMin=1000000
bpSavedMax=0
bpSavedMin=1000000
bpFacedMax=0
bpFacedMin=100000

#hand r=0, l=1, height, age, win/loss (1/0)
for index, row in atp_data.iterrows():
	hold1 = []
	hold2 = []
	#win hand
	if row[2] == 'x':
		continue
	if row[2] == 'R':
		hold1.append(0)
	elif row[2] == 'L':
		hold1.append(1)
	#sometimes there isn't a value for height
	if row[3] == 'x':
		continue
	row3 = float(row[3])
	hold1.append(row3) #win height
	if row3 > heightMax:
		heightMax = row3
	if row3 < heightMin:
		heightMin = row3
	if row[5] == 'x':
		continue
	hold1.append(row[5]) #win age
	if row[5] > ageMax:
		ageMax = row[5]
	if row[5] < ageMin:
		ageMin = row[5]
	if row[6] == 'x':
		continue
	hold1.append(row[6]) #win rank
	if row[6] > rankMax:
		rankMax = row[6]
	if row[6] < rankMin:
		rankMin = row[6]
	if row[7] == 'x':
		continue
	hold1.append(row[7]) #win rank pts
	if row[7] > rankPtsMax:
		rankPtsMax = row[7]
	if row[7] < rankPtsMin:
		rankPtsMin = row[7]
	if row[18] == 'x':
		continue
	hold1.append(row[18]) #win ace
	if row[18] > aceMax:
		aceMax = row[18]
	if row[18] < aceMin:
		aceMin = row[18]
	if row[19] == 'x':
		continue
	hold1.append(row[19]) #win df
	if row[19] > dfMax:
		dfMax = row[19]
	if row[19] < dfMin:
		dfMin = row[19]
	if row[20] == 'x':
		continue
	hold1.append(row[20]) #win svpt
	if row[20] > svptMax:
		svptMax = row[20]
	if row[20] < svptMin:
		svptMin = row[20]
	if row[21] == 'x':
		continue
	hold1.append(row[21]) #win 1stIn
	if row[21] > in1Max:
		in1Max = row[21]
	if row[21] < in1Min:
		in1Min = row[21]
	if row[22] == 'x':
		continue
	hold1.append(row[22]) #win 1stWon
	if row[22] > won1Max:
		won1Max = row[22]
	if row[22] < won1Min:
		won1Min = row[22]
	if row[23] == 'x':
		continue
	hold1.append(row[23]) #win 2ndWon
	if row[23] > won2Max:
		won2Max = row[23]
	if row[23] < won2Min:
		won2Min = row[23]
	if row[24] == 'x':
		continue
	hold1.append(row[24]) #win SvGms
	if row[24] > svGmsMax:
		svGmsMax = row[24]
	if row[24] < svGmsMin:
		svGmsMin = row[24]
	if row[25] == 'x':
		continue
	hold1.append(row[25]) #win bpSaved
	if row[25] > bpSavedMax:
		bpSavedMax = row[25]
	if row[25] < bpSavedMin:
		bpSavedMin = row[25]
	if row[26] == 'x':
		continue
	hold1.append(row[26]) #win bpFaced
	if row[26] > bpFacedMax:
		bpFacedMax = row[26]
	if row[26] < bpFacedMin:
		bpFacedMin = row[26]
	#lose hand
	if row[9] == 'x':
		continue
	if row[9] == 'R':
		hold2.append(0)
	elif row[9] == 'L':
		hold2.append(1)
	#sometimes there isn't a value for height
	if row[10] == 'x':
		continue
	hold2.append(row[10]) #lose height
	if row[10] > heightMax:
		heightMax = row[10]
	if row[10] < heightMin:
		heightMin = row[10]
	if row[12] == 'x':
		continue
	hold2.append(row[12]) #lose age
	if row[12] > ageMax:
		ageMax = row[12]
	if row[12] < ageMin:
		ageMin = row[12]
	if row[13] == 'x':
		continue
	hold2.append(row[13]) #lose rank
	if row[13] > rankMax:
		rankMax = row[13]
	if row[13] < rankMin:
		rankMin = row[13]
	if row[14] == 'x':
		continue
	hold2.append(row[14]) #lose rank pts
	if row[14] > rankPtsMax:
		rankPtsMax = row[14]
	if row[14] < rankPtsMin:
		rankPtsMin = row[14]
	if row[27] == 'x':
		continue
	hold2.append(row[27]) #lose ace
	if row[27] > aceMax:
		aceMax = row[27]
	if row[27] < aceMin:
		aceMin = row[27]
	if row[28] == 'x':
		continue
	hold2.append(row[28]) #lose df
	if row[28] > dfMax:
		dfMax = row[28]
	if row[28] < dfMin:
		dfMin = row[28]
	if row[29] == 'x':
		continue
	hold2.append(row[29]) #lose svpt
	if row[29] > svptMax:
		svptMax = row[29]
	if row[29] < svptMin:
		svptMin = row[29]
	if row[30] == 'x':
		continue
	hold2.append(row[30]) #lose 1stIn
	if row[30] > in1Max:
		in1Max = row[30]
	if row[30] < in1Min:
		in1Min = row[30]
	if row[31] == 'x':
		continue
	hold2.append(row[31]) #lose 1stWon
	if row[31] > won1Max:
		won1Max = row[31]
	if row[31] < won1Min:
		won1Min = row[31]
	if row[32] == 'x':
		continue
	hold2.append(row[32]) #lose 2ndWon
	if row[32] > won2Max:
		won2Max = row[32]
	if row[32] < won2Min:
		won2Min = row[32]
	if row[33] == 'x':
		continue
	hold2.append(row[33]) #lose SvGms
	if row[33] > svGmsMax:
		svGmsMax = row[33]
	if row[33] < svGmsMin:
		svGmsMin = row[33]
	if row[34] == 'x':
		continue
	hold2.append(row[34]) #lose bpSaved
	if row[34] > bpSavedMax:
		bpSavedMax = row[34]
	if row[34] < bpSavedMin:
		bpSavedMin = row[34]
	if row[35] == 'x':
		continue
	hold2.append(row[35]) #lose bpFaced
	if row[35] > bpFacedMax:
		bpFacedMax = row[35]
	if row[35] < bpFacedMin:
		bpFacedMin = row[35]
	
	x = random.randrange(0,2)
	if x == 1: #winner first
		hold1.extend(hold2)
		hold1.append(1)
		playerStats.append(hold1)
	else: #loser first
		hold2.extend(hold1)
		hold2.append(0)
		playerStats.append(hold2)
#normalize
for players in playerStats:
	players[1] = (players[1] - heightMin) / (heightMax - heightMin)
	players[15] = (players[15] - heightMin) / (heightMax - heightMin)
	players[2] = (players[2] - ageMin) / (ageMax - ageMin)
	players[16] = (players[16] - ageMin) / (ageMax - ageMin)
	players[3] = (players[3] - rankMin) / (rankMax - rankMin)
	players[17] = (players[17] - rankMin) / (rankMax - rankMin)
	players[4] = (players[4] - rankPtsMin) / (rankPtsMax - rankPtsMin)
	players[18] = (players[18] - rankPtsMin) / (rankPtsMax - rankPtsMin)
	players[5] = (players[5] - aceMin) / (aceMax - aceMin)
	players[19] = (players[19] - aceMin) / (aceMax - aceMin)
	players[6] = (players[6] - dfMin) / (dfMax - dfMin)
	players[20] = (players[20] - dfMin) / (dfMax - dfMin)
	players[7] = (players[7] - svptMin) / (svptMax - svptMin)
	players[21] = (players[21] - svptMin) / (svptMax - svptMin)
	players[8] = (players[8] - in1Min) / (in1Max - in1Min)
	players[22] = (players[22] - in1Min) / (in1Max - in1Min)
	players[9] = (players[9] - won1Min) / (won1Max - won1Min)
	players[23] = (players[23] - won1Min) / (won1Max - won1Min)
	players[10] = (players[10] - won2Min) / (won2Max - won2Min)
	players[24] = (players[24] - won2Min) / (won2Max - won2Min)
	players[11] = (players[11] - svGmsMin) / (svGmsMax - svGmsMin)
	players[25] = (players[25] - svGmsMin) / (svGmsMax - svGmsMin)
	players[12] = (players[12] - bpSavedMin) / (bpSavedMax - bpSavedMin)
	players[26] = (players[26] - bpSavedMin) / (bpSavedMax - bpSavedMin)
	players[13] = (players[13] - bpFacedMin) / (bpFacedMax - bpFacedMin)
	players[27] = (players[27] - bpFacedMin) / (bpFacedMax - bpFacedMin)


#p(class 0) = 1 / (1 + e^-output)
#old ex of players = [0, 190, 29.67556468, 0, 185, 29.35797399, 1] #winner then loser

#b is in order:
#kind of add, first hand, first height, first age, first rank, first rank pts, first ace,first df,first svpt,first 1stIn, first 1stWon,first 2ndWon,first SvGms,first bpSaved,first bpFaced,2 hand,2 height,2 age,2 rank,2 rank pts,2 ace,2 df,2 svpt,2 1stIn,2 1stWon,2 2ndWon,2 SvGms,2 bpSaved,2 bpFaced

b = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
prediction = 0
countRight=0
accuracy = []

coef=.1
for i in range(20):
	coef += .01
	countRight = 0
	for players in playerStats:
		power = -(b[0] + b[1]*players[0] + b[2]*players[1] + b[3]*players[2] + b[4]*players[3] + b[5]*players[4] + b[6]*players[5]+b[7]*players[6] + b[8]*players[7] + b[9]*players[8] + b[10]*players[9] + b[11]*players[10] + b[12]*players[11]+ b[13]*players[12] + b[14]*players[13] + b[15]*players[14] + b[16]*players[15] + b[17]*players[16] + b[18]*players[17] + b[19]*players[18] + b[20]*players[19] + b[21]*players[20] + b[22]*players[21] + b[23]*players[22] + b[24]*players[23] + b[25]*players[24] + b[26]*players[25] + b[27]*players[26] + b[28]*players[27])
		if prediction > .5:
			if players[28] == 1:
				countRight = countRight+1
		if prediction < .5:
			if players[28] ==0:
				countRight = countRight+1
		if power > 100:
			prediction = 1
		else:
			prediction = 1/(1+ math.pow(math.e, power))
		b[0] = b[0] + coef*(players[28]-prediction)*prediction*(1-prediction)*1.0 #b0 doesn't have input value
		for i in range(1,29):
			b[i] = b[i] + coef*(players[28]-prediction)*prediction*(1-prediction)*players[i-1]
	accuracy.append((coef, countRight/len(playerStats)))

print(b)
print(min(accuracy, key=lambda x: x[1]))
print(max(accuracy, key=lambda x: x[1]))


#testing
#
#
#
#
#
test_data = pandas.read_csv('test_data.csv')
test_data.fillna('x', inplace = True)

#the list of data
playerStats = []
hold1 = []
hold2 = []
#to normalize, hold max & min I FREAKING HAXXORED IT WHY EVEN USE PANDAS I AM *ASHAMED* OF MYSELF OMG
#BUT THERE ISN'T EVEN TIME TO FIX IT SHOOT ME IN THE EAR I DON'T DESERVE TO HEAR
heightMax =0
heightMin = 100000
ageMax=0
ageMin=1000000
rankMax=0
rankMin=1000000
rankPtsMax=0
rankPtsMin=10000
aceMax=0
aceMin=100000
dfMax=0
dfMin=1000000
svptMax=0
svptMin=100000
in1Max=0
in1Min=1000000
won1Max=0
won1Min=1000000
won2Max=0
won2Min=1000000
svGmsMax=0
svGmsMin=1000000
bpSavedMax=0
bpSavedMin=1000000
bpFacedMax=0
bpFacedMin=100000

#hand r=0, l=1, height, age, win/loss (1/0)
for index, row in atp_data.iterrows():
	hold1 = []
	hold2 = []
	#win hand
	if row[2] == 'x':
		continue
	if row[2] == 'R':
		hold1.append(0)
	elif row[2] == 'L':
		hold1.append(1)
	#sometimes there isn't a value for height
	if row[3] == 'x':
		continue
	row3 = float(row[3])
	hold1.append(row3) #win height
	if row3 > heightMax:
		heightMax = row3
	if row3 < heightMin:
		heightMin = row3
	if row[5] == 'x':
		continue
	hold1.append(row[5]) #win age
	if row[5] > ageMax:
		ageMax = row[5]
	if row[5] < ageMin:
		ageMin = row[5]
	if row[6] == 'x':
		continue
	hold1.append(row[6]) #win rank
	if row[6] > rankMax:
		rankMax = row[6]
	if row[6] < rankMin:
		rankMin = row[6]
	if row[7] == 'x':
		continue
	hold1.append(row[7]) #win rank pts
	if row[7] > rankPtsMax:
		rankPtsMax = row[7]
	if row[7] < rankPtsMin:
		rankPtsMin = row[7]
	if row[18] == 'x':
		continue
	hold1.append(row[18]) #win ace
	if row[18] > aceMax:
		aceMax = row[18]
	if row[18] < aceMin:
		aceMin = row[18]
	if row[19] == 'x':
		continue
	hold1.append(row[19]) #win df
	if row[19] > dfMax:
		dfMax = row[19]
	if row[19] < dfMin:
		dfMin = row[19]
	if row[20] == 'x':
		continue
	hold1.append(row[20]) #win svpt
	if row[20] > svptMax:
		svptMax = row[20]
	if row[20] < svptMin:
		svptMin = row[20]
	if row[21] == 'x':
		continue
	hold1.append(row[21]) #win 1stIn
	if row[21] > in1Max:
		in1Max = row[21]
	if row[21] < in1Min:
		in1Min = row[21]
	if row[22] == 'x':
		continue
	hold1.append(row[22]) #win 1stWon
	if row[22] > won1Max:
		won1Max = row[22]
	if row[22] < won1Min:
		won1Min = row[22]
	if row[23] == 'x':
		continue
	hold1.append(row[23]) #win 2ndWon
	if row[23] > won2Max:
		won2Max = row[23]
	if row[23] < won2Min:
		won2Min = row[23]
	if row[24] == 'x':
		continue
	hold1.append(row[24]) #win SvGms
	if row[24] > svGmsMax:
		svGmsMax = row[24]
	if row[24] < svGmsMin:
		svGmsMin = row[24]
	if row[25] == 'x':
		continue
	hold1.append(row[25]) #win bpSaved
	if row[25] > bpSavedMax:
		bpSavedMax = row[25]
	if row[25] < bpSavedMin:
		bpSavedMin = row[25]
	if row[26] == 'x':
		continue
	hold1.append(row[26]) #win bpFaced
	if row[26] > bpFacedMax:
		bpFacedMax = row[26]
	if row[26] < bpFacedMin:
		bpFacedMin = row[26]
	#lose hand
	if row[9] == 'x':
		continue
	if row[9] == 'R':
		hold2.append(0)
	elif row[9] == 'L':
		hold2.append(1)
	#sometimes there isn't a value for height
	if row[10] == 'x':
		continue
	hold2.append(row[10]) #lose height
	if row[10] > heightMax:
		heightMax = row[10]
	if row[10] < heightMin:
		heightMin = row[10]
	if row[12] == 'x':
		continue
	hold2.append(row[12]) #lose age
	if row[12] > ageMax:
		ageMax = row[12]
	if row[12] < ageMin:
		ageMin = row[12]
	if row[13] == 'x':
		continue
	hold2.append(row[13]) #lose rank
	if row[13] > rankMax:
		rankMax = row[13]
	if row[13] < rankMin:
		rankMin = row[13]
	if row[14] == 'x':
		continue
	hold2.append(row[14]) #lose rank pts
	if row[14] > rankPtsMax:
		rankPtsMax = row[14]
	if row[14] < rankPtsMin:
		rankPtsMin = row[14]
	if row[27] == 'x':
		continue
	hold2.append(row[27]) #lose ace
	if row[27] > aceMax:
		aceMax = row[27]
	if row[27] < aceMin:
		aceMin = row[27]
	if row[28] == 'x':
		continue
	hold2.append(row[28]) #lose df
	if row[28] > dfMax:
		dfMax = row[28]
	if row[28] < dfMin:
		dfMin = row[28]
	if row[29] == 'x':
		continue
	hold2.append(row[29]) #lose svpt
	if row[29] > svptMax:
		svptMax = row[29]
	if row[29] < svptMin:
		svptMin = row[29]
	if row[30] == 'x':
		continue
	hold2.append(row[30]) #lose 1stIn
	if row[30] > in1Max:
		in1Max = row[30]
	if row[30] < in1Min:
		in1Min = row[30]
	if row[31] == 'x':
		continue
	hold2.append(row[31]) #lose 1stWon
	if row[31] > won1Max:
		won1Max = row[31]
	if row[31] < won1Min:
		won1Min = row[31]
	if row[32] == 'x':
		continue
	hold2.append(row[32]) #lose 2ndWon
	if row[32] > won2Max:
		won2Max = row[32]
	if row[32] < won2Min:
		won2Min = row[32]
	if row[33] == 'x':
		continue
	hold2.append(row[33]) #lose SvGms
	if row[33] > svGmsMax:
		svGmsMax = row[33]
	if row[33] < svGmsMin:
		svGmsMin = row[33]
	if row[34] == 'x':
		continue
	hold2.append(row[34]) #lose bpSaved
	if row[34] > bpSavedMax:
		bpSavedMax = row[34]
	if row[34] < bpSavedMin:
		bpSavedMin = row[34]
	if row[35] == 'x':
		continue
	hold2.append(row[35]) #lose bpFaced
	if row[35] > bpFacedMax:
		bpFacedMax = row[35]
	if row[35] < bpFacedMin:
		bpFacedMin = row[35]
	
	x = random.randrange(0,2)
	if x == 1: #winner first
		hold1.extend(hold2)
		hold1.append(1)
		playerStats.append(hold1)
	else: #loser first
		hold2.extend(hold1)
		hold2.append(0)
		playerStats.append(hold2)
#normalize
for players in playerStats:
	players[1] = (players[1] - heightMin) / (heightMax - heightMin)
	players[15] = (players[15] - heightMin) / (heightMax - heightMin)
	players[2] = (players[2] - ageMin) / (ageMax - ageMin)
	players[16] = (players[16] - ageMin) / (ageMax - ageMin)
	players[3] = (players[3] - rankMin) / (rankMax - rankMin)
	players[17] = (players[17] - rankMin) / (rankMax - rankMin)
	players[4] = (players[4] - rankPtsMin) / (rankPtsMax - rankPtsMin)
	players[18] = (players[18] - rankPtsMin) / (rankPtsMax - rankPtsMin)
	players[5] = (players[5] - aceMin) / (aceMax - aceMin)
	players[19] = (players[19] - aceMin) / (aceMax - aceMin)
	players[6] = (players[6] - dfMin) / (dfMax - dfMin)
	players[20] = (players[20] - dfMin) / (dfMax - dfMin)
	players[7] = (players[7] - svptMin) / (svptMax - svptMin)
	players[21] = (players[21] - svptMin) / (svptMax - svptMin)
	players[8] = (players[8] - in1Min) / (in1Max - in1Min)
	players[22] = (players[22] - in1Min) / (in1Max - in1Min)
	players[9] = (players[9] - won1Min) / (won1Max - won1Min)
	players[23] = (players[23] - won1Min) / (won1Max - won1Min)
	players[10] = (players[10] - won2Min) / (won2Max - won2Min)
	players[24] = (players[24] - won2Min) / (won2Max - won2Min)
	players[11] = (players[11] - svGmsMin) / (svGmsMax - svGmsMin)
	players[25] = (players[25] - svGmsMin) / (svGmsMax - svGmsMin)
	players[12] = (players[12] - bpSavedMin) / (bpSavedMax - bpSavedMin)
	players[26] = (players[26] - bpSavedMin) / (bpSavedMax - bpSavedMin)
	players[13] = (players[13] - bpFacedMin) / (bpFacedMax - bpFacedMin)
	players[27] = (players[27] - bpFacedMin) / (bpFacedMax - bpFacedMin)


countRight = 0

for players in playerStats:
	power = -(b[0] + b[1]*players[0] + b[2]*players[1] + b[3]*players[2] + b[4]*players[3] + b[5]*players[4] + b[6]*players[5]+b[7]*players[6] + b[8]*players[7] + b[9]*players[8] + b[10]*players[9] + b[11]*players[10] + b[12]*players[11]+ b[13]*players[12] + b[14]*players[13] + b[15]*players[14] + b[16]*players[15] + b[17]*players[16] + b[18]*players[17] + b[19]*players[18] + b[20]*players[19] + b[21]*players[20] + b[22]*players[21] + b[23]*players[22] + b[24]*players[23] + b[25]*players[24] + b[26]*players[25] + b[27]*players[26] + b[28]*players[27])
	if (players[28] - prediction) > .5:
		countRight = countRight+1
	elif (prediction - players[28]) > .5:
		countRight = countRight+1
	if power > 100:
		prediction = 1
	else:
		prediction = 1/(1+ math.pow(math.e, power))
	b[0] = b[0] + .11*(players[28]-prediction)*prediction*(1-prediction)*1.0 #b0 doesn't have input value
	for i in range(1,29):
		b[i] = b[i] + .11*(players[28]-prediction)*prediction*(1-prediction)*players[i-1]

print(countRight/len(playerStats))










