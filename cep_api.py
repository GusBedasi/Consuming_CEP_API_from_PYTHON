import requests
import re

#Valida por meio de expressão regular se o CEP contém 8 digitos, caso não tenha o if else statement entra em loop, executando o método de novo, até que seja atingido as condições propostas.
def valida_cep():
    cep = input('Digite um CEP: ')

    if re.match('[0-9]{8}', cep):
        return cep
    else: 
        valida_cep()

# Executa o método e recupera o valor retornado do CEP válidado
def cep_info():
    cep = valida_cep()

    #Manda um GET para a API do site, enviando o CEP digitado pelo usuário.
    req =  requests.get('https://cep.awesomeapi.com.br/json/{}' .format(cep))
    #Armazena as informações em JSON.
    address_data = req.json()
    # Valida se o corpo do JSON têm 3 campos, que é caracteristico de quando há erro.
    if len(address_data) == 3:
        #Se tiver só 3 itens em seu corpo informa o usuário e o envia para o começo do método, entrando em loop até que digite o código correto.
        print("CEP inválido, digite um correto, por gentileza.")
        cep_info()
    # Uma vez válidado o CEP informa de forma organizada as informações referente o mesmo.
    else: 
        print()
        print("CEP: {}" .format(address_data['cep']))
        print("Endereço: {}" .format(address_data['address']))
        print("Bairro: {}" .format(address_data['district']))
        print("Cidade: {}" .format(address_data['city']))
        print("UF: {}" .format(address_data['state']))
        print("Latitude: {}" .format(address_data['lat']))
        print("Longitude: {}" .format(address_data['lng']))
        print("DDD: ({})" .format(address_data['ddd']))

cep_info()