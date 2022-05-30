from cesar import encripta


def test_encripta_vazio():
    assert encripta('') == ''
    
def test_encripta_um_caractere():
    assert encripta('a') == 'n'

def test_encripta_dois_caracteres():
    assert encripta('ab') == 'no'

def test_encripta_tres_caracteres():
    assert encripta('abc') == 'nop'

def test_encripta_nome():
    assert encripta('mikaela') == 'zvxnryn'