
def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quadriplicar(numero):
    return numero * 4

print(duplicar(10))
print(triplicar(10))
print(quadriplicar(10))

print(10*'-')
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(10)
triplicar = criar_multiplicador(10)
quadruplicar = criar_multiplicador(10)

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))