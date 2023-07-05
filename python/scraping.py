print('We gaan scrapen')

import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://coinmarketcap.com')

heeldehtml = BeautifulSoup(pagina.content, 'html.parser')
body = heeldehtml.find('tbody')

#print(body.prettify())

prijs = heeldehtml.find('.sc-bc83b59-0')
print(prijs)