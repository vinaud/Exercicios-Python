# recebe uma frase e retorna todas as letras maiúsculas contidas nela

def maiusculas(frase):
    lista_maiusculas = ''
    for letra in frase:
        if 65 <= ord(letra) <= 90:
            lista_maiusculas += letra
            
    return lista_maiusculas

print(maiusculas('PrOgRaMaMoS em python!'))
