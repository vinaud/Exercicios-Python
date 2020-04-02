def computador_escolhe_jogada(n, m):
    
    pecasRetiradas = m-1
    while (n - pecasRetiradas) % (m + 1) != 0 and pecasRetiradas -1 > 0:
        pecasRetiradas = pecasRetiradas - 1
    
    if pecasRetiradas == 1:
        print("O computador tirou uma peça.")
        print()
    else:
        print("O computador tirou",pecasRetiradas,"peças.")
        print()

    return pecasRetiradas

def usuario_escolhe_jogada(n, m):
    pecasRetiradas = m + 1
    while pecasRetiradas > m:

       pecasRetiradas = int(input("Quantas peças você vai retirar?"))
       if pecasRetiradas > m:
           print("Oops! Jogada inválida! Tente de novo.")
           print()
       else:
           if pecasRetiradas == 1:
               print("Você tirou uma peça.")
               print()
           else:
               print("Você tirou",pecasRetiradas,"peças.")
               print()
           return pecasRetiradas
    

def partida():
    #input n e m
    #decidir se jogador ou pc começa
    totalPecas = int(input("Quantas pecas?"))
    limiteJogada = int(input("Limite de peças por jogada?"))
    pecas = totalPecas

    if totalPecas % (limiteJogada + 1) == 0:
        print()
        print("Você começa")

        while pecas > 0:
           pecas = pecas - usuario_escolhe_jogada(totalPecas, limiteJogada)
           if pecas <= 0:
               print("Fim de jogo! você ganhou")
               return "jogador"
           else:
               print("Agora restam",pecas,"peças no tabuleiro")
               pecas = pecas - computador_escolhe_jogada(pecas, limiteJogada)
               if pecas <= 0:
                   print("Fim de jogo! o computador ganhou")
                   return "computador"
               else:
                   print("Agora restam",pecas,"peças no tabuleiro")
            
    else:
        print()
        print("Computador começa")
        computador_escolhe_jogada(totalPecas,limiteJogada)

    return ""

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