from cesar import decripta


def test_decripta_vazio():
    assert decripta('') == ''


def test_decripta_mikaela_com_letra_maiuscula():
    assert decripta('Zvxnryn') == 'Mikaela'


def test_decripta_mikaela_com_letra_minuscula():
    assert decripta('zvxnryn') == 'mikaela'


def test_decripta_mikaela_com_letra_maiuscula_e_minuscula():
    assert decripta('ZvxnryN') == 'MikaelA'
