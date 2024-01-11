'''
    Context Manager com função - Criando e Usando gerenciadores de contexto
'''

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('ABRINDO ARQUIVO')
        file = open(caminho_arquivo, modo, encoding='utf8')
        yield file
    except Exception as e:
        print('Ocorreu erro', e)
    finally:
        print('Fechando arquivo'.upper)
        file.close()


with my_open('aula150.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n', 123)
    print('WITH', file)