print('-'*50)
print('*'*50)
print('-'*50)
print('Welcome to the system, have a good day, you must enter name and code')
while True:
	name = input('Please enter your name here:')
	if name == 'houchaozhong':
		print('Welcome, Mr Hou\n')
		code = int(input('Mr %s, please input your code:'%name))
		if code == 123:
			print('Have a good day!')
			break
	else:
		print("You don't have the permission, the database is not registered!\n")
		chose=input('Continue to enter the right name Y, or exit the program N Y/N?:')
		if chose =='Y':
			continue
		elif chose =='N':
			break
		else:
			print('You do not understand the rule, program exit NOW!!!')
			break

print('-'*50)
print('*'*50)
print('-'*50)

