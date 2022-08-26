A = [1,2,3,4,5,6,7]
N = len(A)
i = 0
while i < N/2:
	temp = A[i]
	A[i] = A[N-i-1]
	A[N-i-1] = temp
	i += 1
print (A,)
