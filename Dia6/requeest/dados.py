from bs4 import BeautifulSoup
import requests 
import matplotlib.pyplot as plt


url = 'https://site-ds.netlify.app/'
pagina = requests.get(url)
html = pagina.text

# print(html)

soup =  BeautifulSoup(html, 'html.parser')

produtos = []
valores  = []
lista_valores_reais = []

for item in soup.find_all('div', class_= 'produto'):
    preco = item.find('span', class_ = 'preco').text
    valores.append(preco)
    # print(valores)
    lista_valores  =  [valor.replace('R$','').strip() for valor in valores]
    l = [v.replace(',','').strip() for v in lista_valores]
    dados_reais = [v.replace('.','').strip() for v in l]
    lista_valores_reais = [float(i) for i in dados_reais]

print(lista_valores_reais)

for item2 in soup.find_all('div', class_= 'produto'):
    nome = item2.find('h2', class_ = 'nome').text
    produtos.append(nome)
print(produtos)    


plt.bar(produtos, lista_valores_reais)
plt.show()

