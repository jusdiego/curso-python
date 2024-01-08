'''
    List Comprehension --> É uma forma rápida de criar listas 
'''

import pprint   

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = [i*2 
         for i in range(10)
        ]

#print(lista)


#Mapeamento de dados em list comprehension 
# If ternário antes do For 
#

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

novos_produtos = [
    {**produto, 'preco': produto['preco']*1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(*novos_produtos, sep='\n')
# p(novos_produtos)


# Filtrando com list comprehension 
# If depois do For (não possui else), só adiciona o item caso
# a condição do if seja verdadeira

L = [i for i in range(10) if i <= 5]
#print(L)

novos_produtos = [
    {**produto, 'preco': produto['preco']*1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10 
]

p(novos_produtos)





