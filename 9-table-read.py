i = 0
table = ['hou', 'hu', 'wang', 12, 34, 56]
while i< len(table):
	print(table[i])
	i+=1
temp = input('Please input your name:')

table.append(temp)
bble =table## you cant write like this: bble=table.append(temp), this will be wrong, bble is NoneType.
print('Now the table is:\n')
j = 0
while j< len(bble):
	print(bble[j])
	j+=1
