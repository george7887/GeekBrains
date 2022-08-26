a = [-2,-1,0,1,2]
i = 0
while i < len(a):
	if a[i] < 0:
		a[i] = 0
	i = i + 1
print (a)
