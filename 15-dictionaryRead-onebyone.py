people = {'Name': 'xiaohou', 'Tel': 891971134, 'Height': 180}
for i in people.keys():
    print(i)
print('-'*30)
for j in people.values():
    print(j)
print('-'*30)
for item in people.items():
    print(item)
print('-'*30)

for a,b in people.items():
    print("a=%s, b=%s"%(a, b))

