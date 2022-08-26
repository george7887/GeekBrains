a = [5,1,2,1,3,9,0,8,4,6,8,7]
N = len(a)
i=0
while i<N:
	j = 0
	while j<N-1:
		if a[j] > a[j+1]:
			touch = a[j]
			a[j] = a[j+1]
			a[j+1] = touch
		j = j + 1
	i = i + 1
print (a)
