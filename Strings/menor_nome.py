# recebe uma lista de nomes e retorna o menor deles.
#  Este nome deve ser devolvido com a primeira letra maiúscula e seus demais caracteres minúsculos

def menor_nome(nomes):
    menor = nomes[0].strip()
    
    for nome in nomes:
        if len(nome.strip()) < len(menor) :
            menor = nome.strip()
 
    return menor.capitalize()
    

print('menor:',menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))
print('menor:',menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))
print('menor:',menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))