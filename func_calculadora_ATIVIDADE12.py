print("###################################### INICIANDO CALCULADORA ######################################")
def calculadora(n1,operador,n2):
  if operador == '+':
    return n1+n2
  elif operador == '-':
    return n1-n2
  elif operador == '*':
    return n1*n2
  elif operador == '/':
    return n1/n2
while True:
  n1 = int(input('Primeiro valor: '))
  n2 = int(input('Segundo valor: '))
  operador = str(input('Operação desejada: '))
  print('Resultado:',calculadora(n1,operador,n2))