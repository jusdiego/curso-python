import copy as cp

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2, [0, 1, 2]]
lista_b = cp.deepcopy(lista_a)

lista_a[0] = 'Qualquer coisa'
lista_a[5][0] = 1
print(lista_a)
print(lista_b)