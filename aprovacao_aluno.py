#atributos recebem informa��o do usu�rio como float
p1 = float(input("Digite a primeira nota: "))
p2 = float(input("Digite a segunda nota: "))
falta = int(input("Digite a quantidade de faltas: "))

#calcula m�dia e faltas
qtd_aulas = 20
media = (p1+p2)/2
percent_falta = float(falta/qtd_aulas)

#executa condi��es
#Deve ter menos de 30% de faltas
if percent_falta > 0.3:
	print("Aluno reprovado por faltas!")
#Calcula m�dia, tem que ser pelo menos 6
elif media >= 6:
	print("Aluno Aprovado!")
#Se n�o tiver m�dia, pega nota da p3 e recalcula m�dia.
else:
	p3 = float(input("Digite a terceira nota: "))
	media = (p1+p2+p3)/3
	
	if media >= 6:
		print("Aluno aprovado no exame!")
	else:
		print("Aluno reprovado por nota!")





