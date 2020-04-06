"""
o programa COH-PIAH faz a analise de textos inseridos pelo usuário, calcula a assinatura dos textos
e verifica se são prováveis cópias

"""
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo 
    e devolve uma assinatura a ser comparada com os textos fornecidos'''
    
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    #recebe os textos e os armazena em uma lista
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto,
    detectando ponto final, exxclamação ou nterrogação e fazendo split da string'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca,
    detectando virgula, dois pontos e ponto-virgula, fazendo split da string'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_wal(texto):
    #calcula media de caracteres das palavras de um texto
    soma = 0
    media = 0
    frases = []
    palavras = []

    sentencas = separa_sentencas(texto)

    for sentenca in sentencas:
        frases = frases + separa_frases(sentenca)
    
    for frase in frases:
        palavras = palavras + separa_palavras(frase)
    
    for palavra in palavras:
        soma = soma + len(palavra)
    
    media = soma / len(palavras)

    return media

def calcula_ttr(texto):
    """
    calcula a Relação Type-Token: Número de palavras diferentes utilizadas
     em um texto divididas pelo total de palavras.

    """
    frases = []
    palavras = []
    palavras_diferentes = 0
    ttr = 0

    sentencas = separa_sentencas(texto)

    for sentenca in sentencas:
        frases = frases + separa_frases(sentenca)
    
    for frase in frases:
        palavras = palavras + separa_palavras(frase)
    
    palavras_diferentes = n_palavras_diferentes(palavras)

    ttr = palavras_diferentes / len(palavras)
    return ttr

def calcula_hlr(texto):
    """
    Calcula a Razão Hapax Legomana, que é o número de palavras
     que aparecem uma única vez dividido pelo total de palavras.
    """
    
    frases = []
    palavras = []
    palavras_unicas = 0
    hlr = 0

    sentencas = separa_sentencas(texto)

    for sentenca in sentencas:
        frases = frases + separa_frases(sentenca)
    
    for frase in frases:
        palavras = palavras + separa_palavras(frase)
    
    palavras_unicas = n_palavras_unicas(palavras)

    hlr = palavras_unicas / len(palavras)
    return hlr

def calcula_sal(texto):
    """
    Calcula o tamanho médio de sentença, que é a soma dos números de caracteres em 
    todas as sentenças dividida pelo número de sentenças 
    (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
    """
    sal = 0
    soma_caracteres = 0
    sentencas = separa_sentencas(texto)

    for sentenca in sentencas:
        soma_caracteres = soma_caracteres + len(sentenca)
    
    sal = soma_caracteres / len(sentencas)

    return sal

def calcula_sac(texto):
    """
    Calcula a complexidade de sentença, que é o número total de frases divido pelo número de sentenças.
    """
    sac = 0
    frases = []
    sentencas = separa_sentencas(texto)

    for sentenca in sentencas:
        frases = frases + separa_frases(sentenca)

    sac = len(frases) / len(sentencas)

    return sac

def calcula_pal(texto):
    """
    Calcula o Tamanho médio de frase, que é a soma do número de caracteres em
    cada frase dividida pelo número de frases no texto(os caracteres que separam
     uma frase da outra não devem ser contabilizados como parte da frase).
    """
    pal = 0
    soma_caracteres = 0

    frases = []
    sentencas = separa_sentencas(texto)

    for sentenca in sentencas:
        frases = frases + separa_frases(sentenca)
    
    for frase in frases:
        soma_caracteres = soma_caracteres + len(frase)

    pal = soma_caracteres / len(frases)

    return pal

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e devolve a assinatura do texto.
       cada item da assinatura é calculado em um método próprio
    '''
    wal = calcula_wal(texto)
    ttr = calcula_ttr(texto)
    hlr = calcula_hlr(texto)
    sal = calcula_sal(texto)
    sac = calcula_sac(texto)
    pal = calcula_pal(texto)

    assinatura = [wal, ttr, hlr, sal, sac, pal]

    return assinatura

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver
     o grau de similaridade nas assinaturas. A função de comparação é:
     S(ab) = (Somatório(i=1 -> 6) |F i,a - F i,b|) / 6, onde:
     S(ab) - grau de similardade entre duas assinatura;
     F i,a é o valor de cada traço linguístico i no texto a; e
     F i,b é o valor de cada traço linguístico i no texto b.
     '''
     
    somatorio = 0
    grau_similaridade = 0

    for i in range(6):
         somatorio = somatorio + abs(as_a[i] - as_b[i])
    grau_similaridade = somatorio / 6

    return grau_similaridade

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos
     e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade
      de ter sido infectado por COH-PIAH.'''

    numero_maior = 0
    for i in range(len(textos)):
        assinatura = calcula_assinatura(textos[i])
        if compara_assinatura(assinatura,ass_cp) > numero_maior:
            numero_maior = i
    return numero_maior

def main():
    #recebe a assinatura ja conhecida de uma pessoa específica
    #para servir de base de comparação
    assinatura_portador = le_assinatura()
    print(assinatura_portador)

    #recebe os textos a sserem analisados e os armazena em uma lista
    textos = le_textos()
    print(textos)
     

def test_run_assinatura():
    texto = input("insira um texto")
    assinatura = calcula_assinatura(texto)

    print(assinatura)
    
    return 0

def test_run_compara_assinatura():
    valor = compara_assinatura([4.34, 0.05, 0.02, 12.81, 2.16, 0.0],[3.96, 0.05, 0.02, 22.22, 3.41, 0.0])
    print("valor da comparação:", valor)

def test_run_avalia():
    Textos = ['Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.', 'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.', 'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.']
    assinatura = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]

    valor= avalia_textos(Textos, assinatura)
    print('valor:',valor)

#test_run_assinatura()
#test_run_compara_assinatura()
test_run_avalia()

