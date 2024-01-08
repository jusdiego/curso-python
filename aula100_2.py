import copy
from dados import produtos
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False)



p(produtos)
print('-'*10)

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = [
    {**p, 'preco': round(p['preco']*1.1)}
    for p in copy.deepcopy(produtos)
]

p(novos_produtos)
print('-'*10)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome  = sorted(
    copy.deepcopy(produtos), 
    key= lambda x: x['nome'],
    reverse=True
)

p(produtos_ordenados_por_nome)
print('-'*10)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), 
    key= lambda x: x['preco'],
)

p(produtos_ordenados_por_preco)
print('-'*10)
