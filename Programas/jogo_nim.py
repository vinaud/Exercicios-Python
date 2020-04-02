def computador_escolhe_jogada(n, m):
    if n < m:
        print("O computador tirou",n,"peças.")
        print()
        return n

    else:
        pecasRetiradas = n%(m+1)

        if pecasRetiradas > 0:
            print("O computador tirou",pecasRetiradas,"peças.")
            print()
            return pecasRetiradas

        else:
            print("O computador tirou",pecasRetiradas,"peças.")
            print()
            return m

def usuario_escolhe_jogada(n, m):
    pecasRetiradas = m + 1
    while pecasRetiradas > m :

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
    totalPecas = 0
    limiteJogada = 3

    while limiteJogada > totalPecas:

        totalPecas = int(input("Quantas pecas?"))
        limiteJogada = int(input("Limite de peças por jogada?"))
        if(limiteJogada> totalPecas):
            print("Valor inválidos")

    pecas = totalPecas
    if totalPecas % (limiteJogada + 1) == 0:
        print()
        print("Você começa")

        while pecas > 0:
           pecas = pecas - usuario_escolhe_jogada(pecas, limiteJogada)
           if pecas <= 0:
               print("Fim de jogo! você ganhou")
               return "jogador"
           else:
               print("Agora restam",pecas,"peças no tabuleiro")
               print()
               pecas = pecas - computador_escolhe_jogada(pecas, limiteJogada)
               if pecas <= 0:
                   print("Fim de jogo! o computador ganhou")
                   return "computador"
               else:
                   print("Agora restam",pecas,"peças no tabuleiro")
                   print()
            
    else:
        print()
        print("Computador começa")
        
        while pecas > 0:
               pecas = pecas - computador_escolhe_jogada(pecas,limiteJogada)
               if pecas <= 0:
                   print("Fim de jogo! o computador ganhou")
                   return "computador"
               else:
                   print("Agora restam",pecas,"peças no tabuleiro")
                   print()
                   pecas = pecas - usuario_escolhe_jogada(pecas, limiteJogada)
                   if pecas <= 0:
                       print("Fim de jogo! você ganhou")
                       return "jogador"
                   else:
                       print("Agora restam",pecas,"peças no tabuleiro")
                       print()
    

def campeonato():
    #realiza três partidas
    vitoriasJogador = 0
    vitoriasComputador = 0
    counter = 1

    while counter <= 3:
        print()
        print("**** Rodada",counter,"****")
        print()
        resultado = partida()
        if resultado == "jogador":
            vitoriasJogador = vitoriasJogador + 1
        else:
            vitoriasComputador = vitoriasComputador + 1
        
        counter = counter + 1
    print()
    print("**** Final do campeonato ****")
    print("Placar: você",vitoriasJogador,"X",vitoriasComputador,"Computador")
    print()
    
def main():
    opcao = 0
    while opcao !=1 and opcao !=2:
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
 

main()