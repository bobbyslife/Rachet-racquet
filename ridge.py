#ride regression from Machine Learning in Action
#actually just copying the Listing 8.3
#ridge regression is a shrinkage method--can throw out unimportant parameters and gives better prediction value than linear regression
#lambda

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
def ridgeTest(xArr, yArr):
	xMat= mat(xArr); yMat = mat(yArr).T
	yMean = mean(yMat,0)
	yMat = yMat - yMean
	xMeans = mean(xMat,0)
	xVar = var(xMat,0)
	xMat = (xMat - xMeans)/xVar
	numTestPts = 30
	wMat = zeros((numTestPts,shape(xMat)[1]))
	for i in range(numTestPts):
		ws = ridgeRegres(xMat,yMat,exp(i-10))
		wMat[i,:]=ws.T
	return wMat




