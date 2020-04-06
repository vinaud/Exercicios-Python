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
    Calcula a Razão Hapax Legomana que é o número de palavras
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
    Calcula o tamanho médio de sentença que é a soma dos números de caracteres em 
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

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e devolve a assinatura do texto.'''
    wal = calcula_wal(texto)
    ttr = calcula_ttr(texto)
    hlr = calcula_hlr(texto)
    sal = calcula_sal(texto)
    sac = 1
    pal = 1

    assinatura = [wal, ttr, hlr, sal, sac, pal]

    return assinatura

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver
     o grau de similaridade nas assinaturas.'''
    pass


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos
     e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade
      de ter sido infectado por COH-PIAH.'''
    pass

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

    media = calcula_wal(texto)
    print ("Media das palavras:",media)

    print("Valor de ttr:", calcula_ttr(texto))
    print("Valor de hlr:", calcula_hlr(texto))
    print("Valor de sal:", calcula_sal(texto))
    return 0

test_run_assinatura()

