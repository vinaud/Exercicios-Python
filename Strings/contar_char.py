# recebe uma string e, de acordo com o segundo parâmetro, conta suas vogais ou suas consoantes
def is_vogal(letra):
    if letra =='a' or  letra == 'A' or letra == 'e' or letra =='E' or  letra == 'i' or letra == 'I' or letra =='o' or  letra == 'O' or letra == 'u' or letra =='U':
        return True
    return False

def conta_letras(frase, contar="vogais"):
    count = 0
    frase_clean = frase.strip()
    
    if contar =='vogais':
        for char in frase_clean:
            if is_vogal(char):
                count += 1

    elif contar == 'consoantes':
        for char in frase_clean:
            if not char == ' ' and not is_vogal(char):
                count += 1

    return count



