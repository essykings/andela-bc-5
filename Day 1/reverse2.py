def reverse2(s):
	new_string = " "
	i= len(s)-1
	while i>0:
    	new_string +=s[i]
    	i-=1
    return new_string
print reverse2("esther")
