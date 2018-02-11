row = 1
while row <= 9:
	col = 1
	while col<=row:
		if col<row:
			print("%dx%d=%-2d "%(row, col, row*col), end=' ')
		else:
			print("%dx%d=%-2d "%(row, col, row*col))## In order to delete the line between two row
		col+=1
##	print('\n')
	row+=1
