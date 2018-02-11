
old_name = input("Pleas input the file you want to copy")
f = open(old_name,'r')
f_b =open('[copy]'+old_name,'w') 
f_b.write(f.read())
f.close()
f_b.close()
