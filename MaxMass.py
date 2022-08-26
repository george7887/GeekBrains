a=[1,8,3,9,10,6,2]
iMax=0
i=0
N=len(a)
while i<N:
	if a[i] > a[iMax]:
		iMax=i
	i=i+1
print(iMax,a[iMax])

