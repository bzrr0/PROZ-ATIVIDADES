# A: Veículos com duas ou três rodas;
# if qtdRodas = 2 or qtdRodas = 3
# B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
# if qtdRodas = 4 and qtdPessoas <=8 and kgPeso <=3500
# C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
# if qtdRodas >= 4 and 3500 <= kgPeso <= 6000
# D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; 
# if qtdRodas >= 4 and qtdPessoas > 8
# E: Veículos com quatro rodas ou mais e com mais de 6000 kg.
# if qtdRodas >=4 and kgPeso > 6000
#  
qtdPessoas = int(input('- Capacidade Total de Pessoas no Veículo: '))
qtdRodas = int(input('- Quantidade de rodas: '))
kgPeso = int(input('- Peso bruto em quilogramas: '))
valor = str
if qtdRodas==2 or qtdRodas==3:
    valor = 'A'
if qtdRodas==4 and qtdPessoas<=8 and kgPeso<=3500:
    valor = 'B'
if qtdRodas>=4 and 3500<kgPeso<=6000:
    valor = 'C'
if qtdRodas>=4 and qtdPessoas>8:
    valor = 'D'
if qtdRodas >=4 and kgPeso > 6000:
    valor = 'E'
match valor: # utilizei switch case pra treinar
    case 'A':
        print('A melhor categoria de habilitação para o veículo informado a partir das condições propostas é: ', valor)
    case 'B':
        print('A melhor categoria de habilitação para o veículo informado a partir das condições propostas é: ', valor)
    case 'C':
        print('A melhor categoria de habilitação para o veículo informado a partir das condições propostas é: ', valor)
    case 'D':
        print('A melhor categoria de habilitação para o veículo informado a partir das condições propostas é: ', valor)
    case 'E':
        print('A melhor categoria de habilitação para o veículo informado a partir das condições propostas é: ', valor)
