matriz1 = []
matriz2 = []
matriz3 = []
linha = []
conta0 = 0
conta1 = 0
bloco1 = 0
bloco2 = 0
bloco3 = 0

############ CRIAÇÃO DAS MATRIZES ############


print('''
PROGRAMA DE INDICAÇÃO DE DIREÇÃO DO ROBÔ
        ''')


while True:    #UTILIZADO PARA TRATAMENTO DE ERRO
    try:
        opcao = input('DIGITE O NOME DO ARQUIVO QUE VOCÊ DESEJA UTILIZAR: ')
        caminho = f"ex4_testes/{opcao}.txt"
        with open(caminho, 'r') as f:
            for valor in f:
                colunas = int((len(valor) - 1) / 3)   ## VAI DIVIDIR AS COLUNAS POR 3 E PEGAR A PRIMEIRA PARTE
                x = valor[0:colunas]
                linha = []
                for j in x:
                    linha.append(j)
                matriz1.append(linha)
        break
    except:
        print('NOME INVÁLIDO! ')


with open(caminho, 'r') as g:

    # Separação do segundo bloco
    for valor in g:
        colunas = int((len(valor) - 1) / 3)  ## VAI DIVIDIR AS COLUNAS POR 3 E PEGAR A SEGUNDA PARTE
        x = valor[colunas:colunas*2]
        linha = []
        for j in x:
            linha.append(j)
        matriz2.append(linha)
with open(caminho, 'r') as h:

    # Separação do terceiro bloco
    for valor in h:
        colunas = int((len(valor) - 1) / 3)  ## VAI DIVIDIR AS COLUNAS POR 3 E PEGAR A TERCEIRA PARTE
        x = valor[colunas*2:colunas*3]
        linha = []
        for j in x:
            linha.append(j)
        matriz3.append(linha)
############ INTERPRETAÇÃO DAS MATRIZES ############

#### SENSOR 1 - BLOCO 1 ####

print(f'\nREALIZANDO O TESTE DO ARQUIVO {opcao}...\n')

for linha in matriz1:
    for x in linha:
        if x == '0':
            conta0+=1   # PONTOS PRETOS
        if x == '1':
            conta1+=1   # PONTOS BRANCOS

if conta0 > conta1:

    if (conta1/(colunas*6)) < 0.3:    #DIVIDE O NUMERO DE PONTOS BRANCOS PELO NÚMERO TOTAL DO BLOCO
        print('NÍVEL LÓGICO BLOCO 1: 0')
        bloco1 = 0
    else:                              #SE O VALOR DE SUJEIRA NO BLOCO FOR MAIOR OU IGUAL A 30%
        print('NÍVEL LÓGICO BLOCO 1: ERRO NA CONVERSÃO. AJUSTE A IMAGEM ')
        bloco1 = 2

if conta1 > conta0:
    if (conta0/(colunas*6)) < 0.3:     #DIVIDE O NUMERO DE PONTOS PRETOS PELO NÚMERO TOTAL DO BLOCO
        print('NÍVEL LÓGICO BLOCO 1: 1')
        bloco1 = 1
    else:
        print('NÍVEL LÓGICO BLOCO 1: ERRO NA CONVERSÃO. AJUSTE A IMAGEM ')
        bloco1 = 2

if conta1 == conta0:
    print('NÍVEL LÓGICO BLOCO 1: ERRO NA CONVERSÃO. AJUSTE A IMAGEM ')
    bloco1 = 2

conta0 = conta1 = 0

#### SENSOR 2 - BLOCO 2 ####

for linha in matriz2:
    for x in linha:
        if x == '0':
            conta0+=1   # PONTOS PRETOS
        if x == '1':
            conta1+=1   # PONTOS BRANCOS

if conta0 > conta1:
    if (conta1/(colunas*6)) < 0.3:
        print('NÍVEL LÓGICO BLOCO 2: 0')
        bloco2 = 0
    else:
        print('NÍVEL LÓGICO BLOCO 2: ERRO NA CONVERSÃO. AJUSTE A IMAGEM ')
        bloco2 = 2

if conta1 > conta0:
    if (conta0/(colunas*6)) < 0.3:
        print('NÍVEL LÓGICO BLOCO 2: 1')
        bloco2 = 1
    else:
        print('NÍVEL LÓGICO BLOCO 2: ERRO NA CONVERSÃO. AJUSTE A IMAGEM ')
        bloco2 = 2

if conta1 == conta0:
    print('NÍVEL LÓGICO BLOCO 2: ERRO NA CONVERSÃO. AJUSTE A IMAGEM ')
    bloco2 = 2

conta0 = conta1 = 0

#### SENSOR 3 - BLOCO 3 ####

for linha in matriz3:
    for x in linha:
        if x == '0':
            conta0+=1   # PONTOS PRETOS
        if x == '1':
            conta1+=1   # PONTOS BRANCOS

if conta0 > conta1:
    if (conta1/(colunas*6)) < 0.3:
        print('NÍVEL LÓGICO BLOCO 3: 0')
        bloco3 = 0
    else:
        print('NÍVEL LÓGICO BLOCO 3: ERRO NA CONVERSÃO. AJUSTE A IMAGEM ')
        bloco3 = 2

if conta1 > conta0:
    if (conta0/(colunas*6)) < 0.3:
        print('NÍVEL LÓGICO BLOCO 3: 1')
        bloco3 = 1
    else:
        print('NÍVEL LÓGICO BLOCO 3: ERRO NA CONVERSÃO. AJUSTE A IMAGEM ')
        bloco3 = 2

if conta1 == conta0:
    print('NÍVEL LÓGICO BLOCO 3: ERRO NA CONVERSÃO. AJUSTE A IMAGEM ')
    bloco3 = 2

##### RESULTADO DA DIREÇÃO #####

print("")

if bloco1 == 2 or bloco2 == 2 or bloco3 == 2:
    print('COMANDO: ERRO')

if bloco1 == 0 and bloco2 == 0 and bloco3 == 0:
    print('COMANDO: PARE')

if bloco1 == 0 and bloco2 == 0 and bloco3 == 1:
    print('COMANDO: DIREITA')

if bloco1 == 0 and bloco2 == 1 and bloco3 == 0:
    print('COMANDO: FRENTE')

if bloco1 == 0 and bloco2 == 1 and bloco3 == 1:
    print('COMANDO: FRENTE')

if bloco1 == 1 and bloco2 == 0 and bloco3 == 0:
    print('COMANDO: ESQUERDA')

if bloco1 == 1 and bloco2 == 0 and bloco3 == 1:
    print('COMANDO: FRENTE')

if bloco1 == 1 and bloco2 == 1 and bloco3 == 0:
    print('COMANDO: FRENTE')

if bloco1 == 1 and bloco2 == 1 and bloco3 == 1:
    print('COMANDO: PARE')