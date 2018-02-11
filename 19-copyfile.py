
old_name = input("Pleas input the file you want to copy")
position = old_name.rfind(".")
new_name = old_name[0:position]+'[copy]'+'.py'

f = open(old_name,'r')
f_b =open(new_name,'w') 
f_b.write(f.read())
f.close()
f_b.close()
