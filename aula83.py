'''
    Empacotamento e desempacotamento de dicionarios
'''        


'''
print(pessoa.keys()) ---> (['nome', 'sobrenome'])
print(pessoa.values()) --> (['Aline', 'Souza']) 
print(pessoa.items()) --v
([('nome', 'Aline'), ('sobrenome', 'Souza')])
'''

'''
for chave, valor in pessoa.items():
    print(chave, falor)
'''

a, b = 1, 2
a, b = b, a 

#print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}

#print(pessoa_completa)

def mostra_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

#mostra_argumentos_nomeados(nome='Joana', qlq=123)
mostra_argumentos_nomeados(**pessoa_completa)

