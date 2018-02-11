print("-"*50)
print("*"*50)
currentstr = input("PLease input a sentence, the program will cal the word num:")

currentstr=currentstr.replace(' ','')## Delete the 'Space' value
newstr=''  #a new string to store the result
for i in currentstr:
	if(currentstr.count(i)<=1):# if  there is only one word in currentstr
		newstr=newstr+i
		newstr=newstr+':'
		newstr=newstr+str(1)+' '
	else:#the word has 2 or more numbers
		if(newstr.count(i)<1): # has not register in the new string
			newstr= newstr+i
			newstr=newstr+':'
			newstr= newstr+str(currentstr.count(i))+' '

print("-"*50)
print("The word number in this sentence is : %s"%newstr)
print("-"*50)
