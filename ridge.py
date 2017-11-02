from numpy import *
def loadDataSet(fileName):
	numFeat = len(open(fileName).readline().split(','))-1
	dataMat = []; labelMat = []
	fr = open(fileName)
	for line in fr.readlines():
		lineArr =[]
		curLine = line.strip().split(',')
		for i in range(numFeat):
			lineArr.append(float(curLine[i]))
			dataMat.append(lineArr)
			labelMat.append(float(curLine[-1]))
			return dataMat,labelMat

def standRegres(xArr,yArr):
	xMat = mat(xArr); yMat = mat(yArr).T
	xTx = xMat.T*xMat
	if linalg.det(xTx) == 0.0:
		print("This matrix is singular, cannot do inverse")
		return
	ws = xTx.I * (xMat.T*yMat)
	return ws


#ridge regression from Machine Learning in Action
#actually just copying the Listing 8.3
#ridge regression uses identity matrix multiplied by some constant lambda, add to matrix xTx so it's non-singular & can take inverse of the matrix sum
#formula for coefficients now = w^ = ((xTx + lambda*I)^-1)xTy
#weights = (xTranspose x + lamda*identity)(<- inverse of) * xTranspose*y vector
#ridge regression for having more features than data points
#-if above, can't compute xTx's inverse. X won't be full rank
#lambda = max value on sum of ws, so can decrease unimportant params(below)
#ridge regression is a shrinkage method--can throw out unimportant parameters and gives better prediction value than linear regression
#lambda is chosen to minimize prediction error; choose different lambdas until you find the one with smallest prediction error lol

#calculates weights
#implements ridge regression for any given value of lambda (default .2, var actually lam bc 'lambda' is a python keyword)
def ridgeRegres(xMat, yMat, lam=.2):
	#construct matrix xTx
	xTx = xMat.T*xMat
	#add ridge term times scalar lam. numpy's eye() creates identity matrix
	denom = xTx + eye(shape(xMat)[1])*lam
	#check if lam = 0, which means matrix=singular, so no inverse
	if linalg.det(denom) == 0.0:
		print("This matrix is singular, cannot do inverse")
		return
	#if not singular, calculate weights & return
	ws = denom.I * (xMat.T*yMat)
	return ws

#tests weights over a number of lambda values
#ex how to normalize data: subtract mean from each feature & divide by variance
def ridgeTest(xArr, yArr):
	xMat= mat(xArr); yMat = mat(yArr).T
	yMean = mean(yMat,0)
	yMat = yMat - yMean
	xMeans = mean(xMat,0)
	xVar = var(xMat,0)
	xMat = (xMat - xMeans)/xVar
	numTestPts = 30
	wMat = zeros((numTestPts,shape(xMat)[1]))
	#call ridgeRegres() with 30 different lambda values
	#lambda values vary exponentially so can see how v small/large values of lamda affect results
	#pack weights into a matrix & return matrix
	for i in range(numTestPts):
		ws = ridgeRegres(xMat,yMat,exp(i-10))
		wMat[i,:]=ws.T
	return wMat

'''in shell
reload(regression)
abX,abY=regression.loadDataSet('datastuff.txt')
ridgeWeights = regression.ridgeTest(abX,abY)
#to plot out the weights for 30 diff lambda values
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(ridgeWeights)
plt.show()
'''

#in plot, regression coefficients plotted vs log(lambda). magnitude of coefficients shows which variables=most descriptive in predicting output
#where lambda=smallest at left, full values of coefficients, same as linear regression
#on right where lambda=huge, coefficients=0. Then in middle, good coefficients with better prediction results
#need cross-validation testing now

#for quick testing, func(lambda) returns accuracy
