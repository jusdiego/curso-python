'''
    Dictionary Comprehension e Set Comprehension
'''

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dc = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor 
    in produto.items()
    if chave == 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b')
]

# df = {
#     chave: valor
#     for chave, valor in lista
# }

#p(dict(lista))


s1 = {2**i for i in range(10)}

print(s1)
print(set(range(10)))