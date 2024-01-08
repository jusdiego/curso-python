'''
    Funções decoradoras e decoradores
    Decorar = Adicionar / Remover / Restringir / Alterar
    Funções decoradoras são funções que decoram outras funções
    Decoradores são usados para fazer o Python
    usar as funções decoradas em outras funções 
    Decoradores são "Syntax Sugar" (Açúcar sintático)
'''

def decoradora(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'Seu resultado é {resultado}')
        print('Você foi decorado')
        return resultado
    return interna

@decoradora
def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('123')
print(invertida)