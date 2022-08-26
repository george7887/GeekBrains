a = [8,2,1,3,6,4,5,0]
N = len(a)
iMax = 0
max = a[iMax]
iMin = 0
min = a[iMin]
i = 0
while i<N :
	if a[i] > max:
		iMax = i
		max =a[i]
	elif a[i] < min:
		iMin = i
		min = a[i]
	i = i + 1
if iMax > iMin:
	k1 = iMin
	k2 = iMax
else:
	k2 = iMin
	k1 = iMax
sum = 0
i = k1 + 1
while i < k2:
	sum = sum + a[i]
	i = i + 1

print (sum)
