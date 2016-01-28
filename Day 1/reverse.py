#a ="hello"
#print (a [::-1])
  s= list(word)
    for i in range(len(word)//2):
        temp= s[i]
        s[i]= s[len(word)-i-1]
        s[len(word)-i-1] = temp
    return "".join(s)
    
print reverse2("hello")