# Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado; 
# Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado; 
# Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado. 
# if media<7    or  if falta>3      print(reprovado)
# if media>=7   and if falta<=3     print(aprovado)
nome = str(input('Informe o nome do aluno: '))
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(nome, 'teve a média igual a: ', media)
falta = float(input('Informe a quantidade de faltas desse aluno: '))

if media>=7 and falta<=3:
    print('O aluno está aprovado.')
elif media<7 or falta>3:
    print('O aluno está reprovado')