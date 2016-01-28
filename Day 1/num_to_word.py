def num_to_word(n):
	nw= {"0":"zero", "1":"one", "2":"two","3":"three" }
	n= str(n)
	
	words= []
	for i in n:
		words.append(nw[i])
	return " ".join(words)
num_to_word(200)
