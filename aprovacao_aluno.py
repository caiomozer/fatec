#atributos recebem informação do usuário como float
p1 = float(input("Digite a primeira nota: "))
p2 = float(input("Digite a segunda nota: "))
falta = int(input("Digite a quantidade de faltas: "))

#calcula média e faltas
qtd_aulas = 20
media = (p1+p2)/2
percent_falta = float(falta/qtd_aulas)

#executa condições
#Deve ter menos de 30% de faltas
if percent_falta > 0.3:
	print("Aluno reprovado por faltas!")
#Calcula média, tem que ser pelo menos 6
elif media >= 6:
	print("Aluno Aprovado!")
#Se não tiver média, pega nota da p3 e recalcula média.
else:
	p3 = float(input("Digite a terceira nota: "))
	media = (p1+p2+p3)/3
	
	if media >= 6:
		print("Aluno aprovado no exame!")
	else:
		print("Aluno reprovado por nota!")





