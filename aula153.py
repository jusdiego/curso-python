'''
    Método especial __call__
    callable é algo que pode ser executado com parênteses
    Em classes normais, __call__ faz a instâncias de um 
    classe 'callable'.
'''

class CallMe:
    def __init__(self, phone):
        self.phone = phone 


    def __call__(self, nome):
        print(nome, 'esta chamando', self.phone)
        return 123

call1 = CallMe('1231231')
retorno = call1('Diego')
print(retorno)