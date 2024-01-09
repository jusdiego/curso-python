'''
    Context Manager com classes
    Você pode implementar seus própios protocolos
    apenas implementando os dunder methods que o
    Python vai usar.
    Isso é chamado de Duck typing. Um conceito
    relacionado com tipagem dinâmica onde o Python não
    está interessado com a tipagem dinâmica, mas se alguns métodos
    existem no seu objeto para que ele funcione de forma adequeda.
    
    Duck Typing:
    Quando vejo um pássaro que caminha como um pato, nada como 
    um pato e grasna como um pato, eu chamo aquele pássro de pato.

     Para criar um context manager, os métodos __enter__ e __exit__
     devem ser implementados.

     O método __exit__ receberá a classe de exceção, a exceção e o 
     traceback. Se ele retornar True, exceção no with será suprimida.
'''

# Ex:
# with open('aula149.txt', 'w') as file:
    # ...

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo 
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()


with MyOpen('aula149.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    print('WITH', file)