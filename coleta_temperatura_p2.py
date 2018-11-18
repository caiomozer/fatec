import csv
import os

caminho = "C://temp/temperatura.csv"

# Criando a data
dia = input("Digite o dia da coleta: ")
mes = input("Digite o mês da coleta: ")
ano = input("Digite o ano da coleta: ")

# não deixando a formatação na mão do usuário
data = dia + "/" + mes + "/" + ano

# coletando as temperaturas
temp_min = float(input("Digite a temperatura mínima do dia: "))
temp_max = float(input("Digite a temperatura máxima do dia: "))

# guarda informação se o arquivo já foi criado
arq_existe = os.path.isfile(caminho)

if arq_existe:
    # se arquivo criado, então adiciona as variáveis no final do documento
    file = open(caminho, 'a', newline = '')
    c = csv.writer(file, delimiter = ';')
    
    c.writerow([data, temp_min, temp_max])
    
    file.close()
    
    print("Arquivo atualizado com sucesso.")
else:
    # se arquivo não foi criado, cria o arquivo, 
    # adiciona cabeçalho e primeiros dados
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    file = open(caminho, 'w', newline = '')
    c = csv.writer(file, delimiter = ';')
    
    c.writerow(['Data', 'Temperatura Mínima', 'Temperatura Máxima'])
    c.writerow([data, temp_min, temp_max])
   
    file.close()
    
    print("Arquivo criado com sucesso.")




