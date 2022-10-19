url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
import re
from bs4 import BeautifulSoup
import requests
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
pattern = r"/title/tt*"
with open('names.txt', 'w') as fp:
	for i in soup.find_all('a'):
		if type(i.get('href')) is str:
			if re.match(pattern, i.get('href')) is not None:
				if i.string is not None:
					fp.write(i.string + '\n')



