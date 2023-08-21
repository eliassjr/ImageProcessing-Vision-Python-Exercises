from random import randint
import matplotlib.pyplot as plt
from matplotlib import animation

## LISTA COM OS VALORES DE MEDIÇÃO SORTEADOS

valores = []

## POSIÇÃO DAS MEDIÇÕES

posicao = []
i = 0

## ENTRADA DO VALOR DA TEMPERATURA NOMINAL
## EXISTE O LOOP QUE RETORNA A PERGUNTA CASO AS CONDIÇÕES NÃO SEJAM CUMPRIDAS

setup = input('Qual valor nominal:  ')
while (setup.isnumeric() == False) or (int(setup) < 400) or (int(setup) > 900):
    setup = input('ENTRADA INCORRETA: DIGITE NOVAMENTE O VALOR NOMINAL  ')

## DEFINIÇÃO DA FIGURA E ADIÇÃO DELA A VARIÁVEL PARA PLOTAGEM
setup = int(setup)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)


## FUNÇÃO NECESSÁRIA PARA USAR A FUÇÃO DE ANIMAÇÃO
## NA FUNÇÃO É UTILIZADO O COMANDO RANDINT PARA SORTEIO
## EXISTEM AS CONDICIONAIS PARA SEREM EXIBIDAS DEPENDENDO DA TEMPERATURA
def Monitoramento(i):

    x = randint(400, 900)
    if x > (setup*1.3):
        print('ALARME CRITICO: DESLIGAR O SISTEMA')
    elif x <= (setup*1.3) and x > (setup*1.1):
        print('TEMPERATURA ELEVADA')
    elif x <= (setup*1.1) and x > (setup*0.9):
        print('TEMPERATURA OK')
    elif x <= (setup*0.9) and x > (setup*0.7):
        print('TEMPERATURA BAIXA')
    elif x < (setup*0.7):
        print('TEMPERATURA NEGATIVA CRÍTICA')

## COMANDOS PARA PLOTAGEM DO GRÁFICO
    posicao.append(i)
    valores.append(x)
    ax.clear()
    ax.plot(posicao, valores, "--o", label="Medição")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Valor")
    plt.legend()
    plt.grid(True)
    plt.title("Monitoramento")


## FUNÇÃO DE ANIMAÇÃO PARA DEIXAR O GRÁFICO EM TEMPO REAL
a = animation.FuncAnimation(fig, Monitoramento, interval=1000)
i += 1
plt.show()



