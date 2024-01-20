"""Este é um módulo de exemplo

    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante
"""

variavel = 1 

class FOO:
    """Este é um módulo de exemplo

    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante
    """
    def soma(self, x: int | float, y: int | float) -> int | float:
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
            self,
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

    def bar(self):
        """O que ele faz

        :raises NotImplementedError: Se o método não for definido
        :raises ValueError: Se o valor não for int ou float
        """
        raise NotImplementedError('Teste')


    variavel_2 = 2 
    variavel_3 = 3 
    variavel_4 = 4 