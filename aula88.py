'''
    Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
    Mutáveis [], {}, set() --> lista, dicionario, conjunto
    Imutáveis (), '', 0, 0.0, None, False, range(0, 10 ) 
    -->       tupla, string, int, float, None, booleano, intervalo
'''

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
booleano = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{booleano=}', falsy(booleano))
print(f'{intervalo=}', falsy(intervalo))