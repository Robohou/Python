import random

offices = [[],[],[]]

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


for name in names:
	index = random.randint(0,2)
	offices[index].append(name)
offices_num=0
for tempNames in offices:
	print('Office Num %d has %d People'%(offices_num, len(tempNames)))
	for iname in tempNames:
		print("%s"%iname, end=' ')
	print("\n")
	print("-"*30)
	offices_num+=1

