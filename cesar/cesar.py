from string import ascii_letters


def encripta(frase, rotacao=13):
    """
    Função que encripta uma frase com o alfabeto cifrado de César.
    :param frase: string
    :param n: int
    :return: string
    """
    frase_encriptada = ''
    for caracter in frase:
        if caracter in ascii_letters:
            frase_encriptada += ascii_letters[
                (ascii_letters.index(caracter) + rotacao) % len(ascii_letters)
            ]
        else:
            frase_encriptada += caracter
    return frase_encriptada


def decripta(frase, rotacao=13):
    """
    Função que decripta uma frase com o alfabeto cifrado de César.
    :param frase: string
    :param n: int
    :return: string
    """
    frase_decriptada = ''
    for caracter in frase:
        if caracter in ascii_letters:
            frase_decriptada += ascii_letters[
                (ascii_letters.index(caracter) - rotacao) % len(ascii_letters)
            ]
        else:
            frase_decriptada += caracter
    return frase_decriptada


if __name__ == '__main__':
    encripted = encripta('mikaela')

    print(encripted)
