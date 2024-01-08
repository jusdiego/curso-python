'''
    Generator expression, Iterables e Iterators em Python
    Iteravel --> responsabilidade de deter os valores sequencialmente
    Iterator - entregar um valor por vez, saber somente próximo
    Generator --> funções que sabem pausar 
    Todo generator é um iterator, mas um iterator não é um generator
    sys.getsizeof --> mostra o tamanho em bytes na memória
'''



import sys

iterable = ['Eu', 'Tenho', '__inter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(1000000)]  
generator = (n for n in range(1000000))
print(sys.getsizeof(lista)) 
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
