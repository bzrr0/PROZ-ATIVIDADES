
print("Informe seu nome completo: ")
nome = str(input())
print(nome)

ano_correto = False
while(ano_correto == False):
    print("Informe seu ano de nascimento: ")
    try:
        ano = int(input())
        if (1922<=ano<=2021):
            ano_correto = True
            idade = 2022 - ano
            print("Nome: "+ nome)
            print("Idade: ", idade)
        else :
            print("Você digitou um ano inválido, ou seja, fora do intervalo entre 1922 e 2021. Por favor digitar um ano válido.")
    except:
        print("Caracter inválido, por favor digite um ano válido")

