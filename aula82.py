def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica
 
#Usando a função lambda
print(executa(lambda x, y: x+y, 2, 3))

print(soma(5, 5))

print(executa(soma, 10, 20))

duplica = executa( lambda m: lambda n: n*m, 2)
print(duplica(50))