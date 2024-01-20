"""Este é um módulo de exemplo

    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante
"""

variavel = 1 

def soma(x: int | float, y: int | float) -> int | float:
    """
    Soma x e y

    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante

    :param x: Numero 1
    :type x: int or float
    :param y: Numero 2
    :type: int or float
    
    :return: A soma entre x e y
    :rtype: int or float
    """

    return x + y

def multiplica(
        x: int | float,
        y: int | float,
        z: int | float | None = None
) -> int | float:
    """Multiplica x, y e/ou z

    Multiplica x e y. Se z for enviado, multiplica x,y e z.
    """    

    if z is None:
        return x*y
    return x * y * z


variavel_2 = 2 
variavel_3 = 3 
variavel_4 = 4 
