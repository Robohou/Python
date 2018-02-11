i = 1
j = 1
while j <10:

	while i<=100:
		i+=1
		if i>10:
			break
		if i%2==0:
			if i == 4:
				continue
			print('i is-- %d'%i)
	j+=1
	if (j==2)or(j==4):
		continue

	print('j is----------- %d'%j)
