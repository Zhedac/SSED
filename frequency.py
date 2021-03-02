from collections import Counter 
    

stri ='The quick brown fox jumps over the lazy dog . | } ; , ( ) '

#character count
def char(stri):
	res = Counter(stri) 
  
	print ("Count of all characters is :\n "+  str(res)) 

#word count
def word(stri):
	str_list = stri.split() 
  
	unique_words = set(str_list) 
      
	for words in unique_words : 
		print('Frequency of ', words , 'is :', str_list.count(words))

char(stri)
word(stri)

