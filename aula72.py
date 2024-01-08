 
def multiplicacao(*args):
    multi = 1
    for i in args:
        multi *= i
    return multi 

mult = multiplicacao(1, 2, 3, 4, 5)
mult_2 = multiplicacao(6, 7, 8, 9, 10)

print(mult)
print(1*2*3*4*5)

print(mult_2)
print(6*7*8*9*10)

''' 
def par(i):
    if i % 2 == 0:
        return print('é par')
    return print('é impar')

par(1)
par(2)
par(3)
par(4)  
par(5)
par(6)
par(7)
par(8)
par(9)
par(10)
'''