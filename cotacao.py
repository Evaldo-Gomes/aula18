# Cotação de Moedas
import requests

def getCotacao(codMoeda):
    try:
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/last/{codMoeda}-BRL')

        # Dicionário
        requisicao_dic = requisicao.json()

        cotacao = requisicao_dic[f'{codMoeda}BRL']['bid']
        return cotacao
    except:
        print('Código da Moeda Inválido')
        return None

# Teste - Cotação do Dólar
print(f'{getCotacao("USD")}')