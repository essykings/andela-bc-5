def num_to_word4(n):
    words = ["zero","one","two","three","four","five","six",]
    if n<=9:
        return words[n]
    else:
        return num_to_word4(n//10) + " "+ words [n%10] 
num_to_word4(20)
