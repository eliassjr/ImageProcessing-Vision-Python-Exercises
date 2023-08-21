
## PEÇAS INICIAIS PARA DESPACHO
pecas = ['Celular', 'Computador', 'Impressora', 'TV', 'Notebook']

## TECNICA INICIAL DE PROCESSAMENTO
tecnica = 'F'

## LOOP INFINITO
while True:

    print('''
        Operações
    
        [ T ] Selecionar Técnica de Processamento
        [ E ] Entrada de Dados
        [ P ] Processar Peça
        [ S ] Sair do Programa
        ''')

## ENTRADA PARA ESCOLHER A OPÇÃO.
## CONDICIONAL PARA PODER DIGITAR APENAS AS OPÇÃOS EXIBIDAS APLICADA
    opcao = input('Qual você deseja? ')
    while (opcao.isalpha() == False) or opcao not in 'TEPSteps':
        opcao = input('Entrada Incorreta. Digite a opção novamente: ')


## SELEÇÃO DA TÉCNICA DE PROCESSAMENTO
    if opcao in 'Tt':

        print('''
        Tecnicas de Processamento:
    
        [ F ] FIFO
        [ L ] LIFO
        ''')

        tecnica = input('Qual você deseja? ')

        while (tecnica.isalpha() == False) or tecnica not in 'FfLl':
            tecnica = input('Entrada Incorreta. Digite a opção novamente: ')

        if tecnica in 'Ff':
            print('Tecnica FIFO selecionada!')

        if tecnica in 'Ll':
            print('Tecnica LIFO selecionada!')


## CÓDIGO PARA ADIÇAO DE DADOS. DEPENDENDO DA TECNICA SELECIONADA O ITEM É INSERIDO NO INICIO DA LISTA OU NO FINAL.
    if opcao in 'Ee':
        if tecnica in 'Ff':
            item = input('Qual item deseja incluir?: ')
            pecas.insert(0, item)
            print('FIFO: Item adicionado na primeira posição com sucesso!')

        if tecnica in 'Ll':
            item = input('Qual item deseja incluir?: ')
            pecas.append(item)
            print('LIFO: Item adicionado na ultima posição com sucesso!')

## CÓDIGO PARA PROCESSAMENTO DA PEÇA. A PEÇA FINAL OU INICIAL É REMOVIDA DA LISTA COM O COMANDO POP
    if opcao in 'Pp':

        if len(pecas) != 0:

            if tecnica in 'Ff':
                print(f'Processando {pecas[0]} ... ')
                pecas.pop(0)
                print('Item Despachado Através do Método FIFO!')

            if tecnica in 'Ll':
                print(f'Processando {pecas[len(pecas)-1]} ... ')
                pecas.pop(len(pecas) - 1)
                print('Item Despachado Através do Método LIFO!')
        else:
            print('Nenhuma peça disponível para despacho')


## CÓDIGO PARA FINALIZAÇÃO DO PROGRAMA E EXIBIÇÃO DOS ITENS RESTANTES
    if opcao in 'Ss':
        print('\nFinalizando Programa...')

        print('\nItens restantes para despache: ')

        for i in range(0, len(pecas), 1):
            print(f'{pecas[i]}')


        print('\nPrograma Finalizado!')
        break

