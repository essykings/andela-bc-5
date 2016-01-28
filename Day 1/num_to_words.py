def num_to_words(n):
	nw= {"zero":0, "one":1, "two":2,"three":3 }
	
	words= []
	for i in n:
		words.append (nw[i])
		return " ".join([words])
num_to_words(200)




