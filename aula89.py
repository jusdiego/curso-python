'''
    dir, hasattr e getattr em Python
    dir --> todos os nomes definidos dentro do objeto 
    hasattr --> checa se um objeto tem um nome determinado
    getattr --> definir um nome dinamicamente
'''

string = 'Diego'
metodo = 'upper'


if hasattr(string, 'upper'):
    print('Exites upper')
    print(string.upper())

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)