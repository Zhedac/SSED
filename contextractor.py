import requests
import os
import re
import urllib.parse
from bs4 import BeautifulSoup
import pprint

l = open("lang_name.txt", "r")
languages = l.read().splitlines()

ignored=["import", "include", "main", "echo"]
dict = {}

for lang in languages:
	localdict = {}
	URL = "https://esolangs.org/wiki/"+str(lang)
	page = requests.get(URL)
	bs = BeautifulSoup(page.content, 'html.parser')

	codeno = 1
	data = []

	for sample in bs.findAll(["code", "pre"]):
		x=str(urllib.parse.unquote(sample.text)).replace("\n","")
		if len(x) > 20 and all(ele not in x for ele in ignored):
			data.append(x)
	
	if len(data)>=1:
		for m in data:
			print()
			print("Probable code", codeno)
			print("    ")
			print(m[:120])
			print("    ")
			codeno += 1
		print()
		print("language is: ", str(lang))

		codenoi = input("which probable code no. to be saved: ")
		m=1
		for i in codenoi:
			localdict["code"+str(m)]=data[int(i)-1]
			m += 1
		dict[str(lang)] = localdict
		os.system('cls' if os.name ==  'nt' else 'clear')	

pprint.pprint(dict)
