import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import csv
import os


caminho = "C://temp/temperatura.csv"
arq_existe = os.path.isfile(caminho) # Para validar existencia do arquivo, retorna True ou False

data = []
t_min = []
t_max = []
amplitude = []
media = []

# Alterando o dialeto do csv, recebendo delimitador ";" ao invés de ","
csv.register_dialect('csv_ponto_virgula', delimiter=';')

if (arq_existe):
    # Pegando Arquivo, se existir...
    file = open(caminho, 'r', newline = '')
    c = csv.DictReader(file, dialect='csv_ponto_virgula')

    # Criando lista de temperaturas e data
    for row in c:
        t_min.append(float(row['Temperatura Mínima']))
        t_max.append(float(row['Temperatura Máxima']))
        data.append(row['Data'])

    # Criando lista de media e amplitude
    amplitude = [t2 - t1 for t1, t2 in zip(t_min, t_max)]
    media = [(t1 + t2)/2 for t1, t2 in zip(t_min, t_max)]

    # Definindo labels e sizes para o gráfico de pizza
    legenda = '0 a 16', '16 a 20', '20 a 26', '26 a 30', '30 a 36', '36 a 41', '>41'
    sizes = [0,0,0,0,0,0,0]

    # Os tamanhos dos pedaços da pizza são definidos na iteração abaixo
    for row in media:
        if row >= 41:
            sizes[6] += 1
        elif row >= 36:
            sizes[5] += 1
        elif row >= 30:
            sizes[4] += 1
        elif row >= 26:
            sizes[3] += 1
        elif row >= 20:
            sizes[2] += 1
        elif row >= 16:
            sizes[1] += 1
        elif row >= 0:
            sizes[0] += 1

    # Criando uma tela para os gráficos
    fig = plt.figure(constrained_layout=True)

    # cria a geometria de distribuição da tela, 2 graficos de um lado, 1 de outro
    gs0 = gridspec.GridSpec(1,2, figure= fig)
    gs1 = gridspec.GridSpecFromSubplotSpec(2,1, subplot_spec=gs0[0])
    gs2 = gridspec.GridSpecFromSubplotSpec(1,1, subplot_spec=gs0[1])
    
    # Criando gráfico de amplitude
    ax = fig.add_subplot(gs1[0])
    ax.plot(data, amplitude)
    ax.set_title('Amplitude Térmica')

    # Criando gráfico de temperaturas
    ax = fig.add_subplot(gs1[1])
    ax.plot(data, t_min)
    ax.plot(data, t_max)
    ax.set_title('Temperatura Máxima e Mínima')

    # Criando gráfico de pizza
    ax = fig.add_subplot(gs2[0])
    ax.pie(sizes, labels = legenda, radius=0.7)
    ax.set_title('Média de temperaturas')

    plt.show()

else:
    print("Execute primeiro o programa coleta_temperatura_p2.py")

