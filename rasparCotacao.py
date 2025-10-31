# Algortimo para raspar dados da cotação de moedas
# Autor: Profº Gabriel Novais
# Data: 30/10/2025

import requests# Biblioteca para entrar nos sites
from bs4 import BeautifulSoup# Bib. para raspar as info

def rasparMoeda(moeda):
    link = f"https://wise.com/br/currency-converter/{moeda}-to-brl-rate?amount=1"
    requisicao = requests.get(link)

    codigoFonte = BeautifulSoup(requisicao.text, "html.parser")
    #print(codigoFonte)

    # Comando para separar a tag 'input' do meu código fonte:
    inputs = codigoFonte.find_all('input')
    cotacao = inputs[1]['value']
    return str(cotacao)


# valor = input("Digite a moeda para converter: ")
# rasparMoeda(valor)

conteudoHTML = f'''
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Cotação Salva</title>
    </head>
    <body>
        <h1>Cotação Dólar:</h1>
        <h3>{rasparMoeda('usd')}</h3>
        <h1>Cotação Libra:</h1>
        <h3>{rasparMoeda('gbp')}</h3>
        <h1>Cotação Euro:</h1>
        <h3>{rasparMoeda('eur')}</h3>
    </body>
</html>
'''

with open("cotacao.html", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudoHTML)