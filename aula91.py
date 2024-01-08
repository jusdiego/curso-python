'''
    Introdução às Generator functions em Python 
'''

def generator(n=0, maximum=10):
    while True:
        yield n # Pausa
        n += 1 
    
        if n >= maximum:
            return 

gen = generator(maximum=100)
for i in gen:
    print(i)