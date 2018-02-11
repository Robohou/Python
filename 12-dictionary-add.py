people = {'Name':'xiaohou', 'Tel':891971134, 'Height':180}

people['Age']= int(input('Please input your age: '))

print(people)

people['QQ'] = int(input('Please input your tecent ID: '))
print(people)
chose = input('Do you want to change your Tel? Y/N ')
if chose=='Y':
    people['Tel']=int(input("PLease input your new Tel: "))
print(people)
