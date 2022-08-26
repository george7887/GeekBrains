A = [9,1,2,0.3,4,5]
N = len(A)
iMax = 0
iMin = 0
i = 0
while i<N :
	if A[i] > A[iMax]:
		iMax = i
	elif  A[i] < A[iMin]:
		iMin = i
	i = i+1

print (iMax,iMin)
