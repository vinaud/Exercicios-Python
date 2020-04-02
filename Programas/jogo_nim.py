def computador_escolhe_jogada(n, m):
    return 0

def usuario_escolhe_jogada(n, m):
    pecasRetiradas = m + 1
    while pecasRetiradas > m:

       pecasRetiradas = int(input("Quantas peças você vai retirar?"))
       if pecasRetiradas > m:
           print("Oops! Jogada inválida! Tente de novo.")
           print()
       else:
           if pecasRetiradas == 1:
               print("Você retirou uma peça.")
               print()
           else:
               print("Você retirou",pecasRetiradas,"peças.")
               print()
           return pecasRetiradas
    

def partida():
    #input n e m
    #decidir se jogador ou pc começa
    totalPecas = int(input("Quantas pecas?"))
    pecasJogada = int(input("Limite de peças por jogada?"))

    if totalPecas % (pecasJogada + 1) == 0:
        print()
        print("Você começa")
        usuario_escolhe_jogada(totalPecas, pecasJogada)
    else:
        print()
        print("Computador começa")

    return 0

def campeonato():
    #realiza três partidas
    vitoriasJogador = 0
    vitoriasComputador = 0
    
print("Bem-vindo ao jogo NIM, Escolha: ")
print()
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato 2")

opcao = int(input())

if opcao == 1:
    partida()
elif opcao == 2:
    campeonato()
else:
    print("Opção inválida!")
