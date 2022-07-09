import requests
from bs4 import BeautifulSoup

url = 'https://lista.mercadolivre.com.br/'
produto = input('Digite o nome do produto: ')
response = requests.get(url + produto)


## andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default"

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core ui-search-result--advertisement andes-card--padding-default'})
## ui-search-item__group ui-search-item__group--title


## ui-search-item__group__element ui-search-link


## price-tag-fraction


## price-tag-cents

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link'})
    real =  produto.find('span', attrs={'class': 'price-tag-fraction'})
    centavos =  produto.find('span', attrs={'class': 'price-tag-cents'})
    print('Titulo do produto: ', titulo.text)
    print('Link do produto: ', link['href'])
    print('Preço do produto R$: ', real.text+','+centavos.text, 'reais')
    print('\n\n')
    
