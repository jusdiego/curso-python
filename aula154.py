'''
    Classes decoradoras (Decorator classes)
'''

class Multiplicar:
    def __init__(self, multiplicador):
        self.multiplicador = multiplicador 

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.multiplicador
        return interna


@Multiplicar(10)
def soma(x,y):
    return x+y


soma1 = soma(1,2)
print(soma1) 