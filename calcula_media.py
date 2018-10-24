
#Este programa calcula média de n fatores inseridos pelo usuário.

def media(*args):
  media = float(sum(args)/len(args))
  return media

#checa se foram inseridos números inteiros e cria uma tupla
while True:
  try:
    argumentos = tuple(int(x.strip()) for x in input("Informe os valores para calcular a média, separados por ',': ").split(","))
    break
  except ValueError:
    print("Não é um número inteiro!")

#quebra a tupla e joga na função media()
print(media(*argumentos))