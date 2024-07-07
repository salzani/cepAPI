import requests
import re
import json
import pandas

apiURL = 'https://viacep.com.br/ws'

def dataFormat(jsonData):
    cityInfo = jsonData.get('localidade')
    ufInfo = jsonData.get('uf')
    ibgeInfo = jsonData.get('ibge')
    dddInfo = jsonData.get('ddd')

    print('')
    print('||||||||||||||||||||||||')
    print(f'cidade: {cityInfo}')
    print(f'UF: {ufInfo}')
    print(f'IBGE: {ibgeInfo}')
    print(f'dddInfo: 0{dddInfo}')
    print('||||||||||||||||||||||||')

    return {
        'Cidade': cityInfo,
        'UF': ufInfo,
        'IBGE': ibgeInfo,
        'DDD': f'0{dddInfo}'
    }


def returnCep(apiReceive):
    apiResponse = requests.get(apiReceive)

    if apiResponse.status_code == 200:
        data = apiResponse.json()
        return dataFormat(data)
    else:
        print(f'Error to request | STATUS: {apiResponse.status_code}')
        return None


cepInput = input('Entre com o CEP: ')

cep = re.sub(r'[^a-zA-Z0-9]', '', cepInput)

cepTreatment = f'{apiURL}/{cep}/json/'

returnCep(cepTreatment)

print('')
print('Preencher planilha?')
print('(S) | (N)')
print('')

fillSheet = input().strip().upper()
