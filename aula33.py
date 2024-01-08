"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool


O método .zfill() em Python é utilizado para preencher uma string 
numérica à esquerda com zeros, ajustando o comprimento total da string. 
Isso é útil, por exemplo, quando você deseja garantir que um número 
tenha um determinado número de dígitos, preenchendo com zeros à esquerda se necessário.

"""
string = '1000'
# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# print(string)
# print(outra_variavel)
print(string.zfill(10))