import requests
import json
import re
import urllib.parse
from bs4 import BeautifulSoup


URL = 'https://esolangs.org/wiki/Language_list'
page = requests.get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

eso=open("eso_list.txt", "w")

for name in bs.findAll('a', attrs={'href': re.compile('(?:^/wiki/)')})[1:-22]:
	output=urllib.parse.unquote(name.get("href")[6:])
	eso.write(output + "\n")

eso.close()