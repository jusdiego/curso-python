'''
    Funções decoradoras e decoradores
    Decorar = Adicionar / Remover / Restringir / Alterar
    Funções decoradoras são funções que decoram outras funções
    Decoradores são usados para fazer o Python
    usar as funções decoradas em outras funções 
'''

def decoradora(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = decoradora(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)