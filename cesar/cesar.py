from string import ascii_letters


def encripta(frase, n=13):
    """
    Função que encripta uma frase com o alfabeto cifrado de César.
    :param frase: string
    :param n: int
    :return: string
    """
    frase_encriptada = ''
    for letra in frase:
        if letra in ascii_letters:
            frase_encriptada += ascii_letters[(ascii_letters.index(letra) + n) % len(ascii_letters)]
        else:
            frase_encriptada += letra
    return frase_encriptada

def decripta(frase, n=13):
    """
    Função que decripta uma frase com o alfabeto cifrado de César.
    :param frase: string
    :param n: int
    :return: string
    """
    frase_decriptada = ''
    for letra in frase:
        if letra in ascii_letters:
            frase_decriptada += ascii_letters[(ascii_letters.index(letra) - n) % len(ascii_letters)]
        else:
            frase_decriptada += letra
    return frase_decriptada

if __name__ == '__main__':
    encripted = encripta('mikaela')
    
    print(encripted)