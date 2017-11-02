#ride regression from Machine Learning in Action
#actually just copying the Listing 8.3

#calculates weights
#implements ridge regression for any given value of lambda (default .2, var actually lam bc 'lambda' is a python keyword)
#construct matrix xTx
def ridgeRegres(xMat, yMat, lam=.2):
	xTx = xMat.T*xMat
	denom = xTx + eye(shape(xMat)[1])*lam
	if linalg.det(denom) == 0.0:
		print("This matrix is singular, cannot do inverse")
		return
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




