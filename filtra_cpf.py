import pandas as pd


dados = pd.read_csv('C:\\Users\\wesle\\Documents\\dados\\socios_csv.csv', sep= ',', encoding= 'utf-8')

print ('----------------Tabela de Sócios---------------: \n')

print(dados)

cpf = input('Entre com o CPF ou CNPJ: ')

cpf_filtrados = dados['cpf_cnpj_socio'] == cpf

print('----------------Dados Filtrados------------------: \n')

print(dados[cpf_filtrados])

