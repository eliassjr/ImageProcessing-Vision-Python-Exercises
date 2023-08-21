import matplotlib.pyplot as plt

## LISTA INICIAL QUE ATRAVÉS DELA SERÁ GERADA ListaA e ListaB
lista = [50, 20, 30, 20, 50, 60, 30, 80, 10, 100]
listaA = []
listaB = []
posicao = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0
pos = 0
maior = 0
menor = 0
cont = 0
contlista = 10


## LOOP DO PROGRAMA INFINITO
while True:

    print('''
    Operações

    [ 1 ] Visualizar Gráfico
    [ 2 ] Acrescentar Dados
    [ 3 ] Finalizar o programa
    ''')

    opção = int(input('Qual você deseja? '))

    ## SE O USUÁRIO APERTAR 1 ELE VIZUALIZA O GRÁFICO NO ESTADO INICIAL
    ## O VALOR DA Lista A É ELEVADO AO QUADRADO E ADICIONADO AO FINAL DA ListaA
    ## A ListaB É ORGANIZADA EM ORDEM ATRAVÉS DO COMANDO SORTED

    if opção == 1:
        while x < contlista:
            a = lista[x]
            listaA.append(a**2)
            x += 1
        listaB = lista.copy()
        listaB = sorted(listaB)

    ## COMANDOS DE PLOT DO GRÁFICO
        plt.subplot(2, 2, 1)
        plt.plot(posicao, lista, label='Lista Principal')
        plt.legend()
        plt.grid(True)

        plt.subplot(2, 2, 2)
        plt.plot(posicao, listaA, label='ListaA')
        plt.legend()
        plt.grid(True)

        plt.subplot(2, 2, 3)
        plt.plot(posicao, listaB, label='ListaB')
        plt.legend()
        plt.grid(True)
        plt.show()

    ## SE O USUÁRIO APERTAR 2 ELE PODE ACRESCENTAR DADOS
    ## SÃO UTILIZADAS CONDICIONAIS PARA ELE RETORNAR A PERGUNTA CASO PREENCHA COM ALGO FORA DA CONDIÇÃO

    if opção == 2:
        perg = int(input('Quantos numeros deseja adicionar? '))
        while cont < perg:
            n = int(input(f'Digite o {cont+1}° numero:  '))
            while n > 100 or n < 0:
                n = int(input(f'Número Inválido. Digite o {cont + 1}° numero:  '))
            lista.append(n)
            posicao.append(contlista)
            contlista+=1
            cont+=1
        print('Números Adicionados!')


    if opção == 3:
        print('\n Programa Finalizado!')
        break


