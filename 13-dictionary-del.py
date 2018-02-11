people = {'Name':'xiaohou', 'Tel':891971134, 'Height':180}

people['Age']= int(input('Please input your age: '))

print(people)

people['QQ'] = int(input('Please input your tecent ID: '))
print(people)
chose = input('Do you want to change your Tel? Y/N ')
if chose=='Y':
    people['Tel']=int(input("PLease input your new Tel: "))
print(people)

chose1=input('Do you want to del your QQ for safe? Y/N: ')
if chose1=='Y':
    del people['QQ']
    print('After deleting ID, the people is %s :'%people)

# delete
# chose2 = input('Do you want to delete the whole dictionary Y/N ')
# if chose2 == 'Y':
#     del people
# print('After deleting, the people is %s :'%people)
# ctrl +/
chose2 = input('Do you want to delete the whole dictionary Y/N ')
if chose2 == 'Y':
    people.clear()
print('After deleting, the people is %s :'%people)
