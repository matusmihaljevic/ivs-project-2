## @file calc.py
## @brief Matematická knižnica pre kalkulačku
## @author Matúš Mihaljevič

def add(a: float, b: float) -> float:
    """
    @brief Súčet dvoch čísiel
    @return Súčet a + b
    """
    return a + b


def sub(a: float, b: float) -> float:
    """
    @brief Rozdiel dvoch čísiel
    @return Rozdiel a - b
    """    
    return a - b


def mult(a: float, b: float) -> float:
    """
    @brief Súčin dvoch čísiel
    @return Súčin a * b
    """    
    return a * b


def div(a: float, b: float) -> float:
    """
    @brief Podiel dvoch čísiel
    @return Podiel a / b
    @raise ZeroDivisionError Ak je deliteľ rovný 0
    """
    if(b == 0):
        raise ZeroDivisionError("Delenie nulou")

    return a / b   


def int_div(a : float, b: float) -> int:
    """
    @brief Celočíselný podiel dvoch čísiel
    @return a // b
    @raise ZeroDivisionError Ak je deliteľ rovný 0
    """    
    if(b == 0):
        raise ZeroDivisionError("Delenie nulou")

    return int(a // b)    


def fact(n: int) -> int:
    """
    @brief Faktoriál prirodzeného čísla
    @return Faktoriál n!
    @raise ValueError Ak číslo nie je integer alebo je záporné
    """    
    if not isinstance(n, int):
        raise TypeError("Číslo musí byť prirodzené")
    
    if n < 0:
        raise ValueError("Číslo nesmie byť záporné")

    result = 1
    while n != 0:
        result *= n
        n -= 1

    return result    


def pow(base : float, exponent: int) -> float:
    """
    @brief Mocnica čísla s prirodzeným exponentom
    @return x^n
    @param base Základ
    @param exponent Exponent
    @raise ValueError Ak je základ rovný 0 a exponent záporné číslo
    @raise ValueError Ak exponent nie je integer
    """    
    if (base == 0) and (exponent < 0):
        raise ValueError("Delenie nulou")

    if not isinstance(exponent, int):
        raise ValueError("Exponent musí byť celé číslo")

    return base ** exponent


def root(base: float, index: int) -> float:
    """
    @brief Odmocnina čísla s prirodzeným indexom
    @return x^{1/n}
    @param base Základ
    @param index Index
    @raise ValueError Ak index nie je integer
    @raise ValueError Ak je index menší alebo rovný 0
    @raise ValueError Ak je základ záporný a index kladný
    """    
    initialGuess = 1
    tolerance = 1e-16

    if (not isinstance(index, int)) or (index <= 0):
        raise ValueError("Index musí byť prirodzené číslo")

    if (base < 0) and (index % 2 == 0):
        raise ValueError("Párna odmocnina nie je definovaná pre záporné čísla")

    guess = initialGuess
    while True:
        nextGuess = ((index - 1) * guess + base / (guess ** (index - 1))) / index
        if abs(nextGuess - guess) < tolerance:
            return round(nextGuess, 7)
        guess = nextGuess    


def ln(n: float) -> float:
    """
    @brief Prirodzený logaritmus
    @return ln(n)
    @raise ValueError ak je hodnota menšia alebo rovná 0
    """
    if n <= 0:
        raise ValueError("ln(x) nie je definovaný pre x <= 0")

    if n == 1:
        return 0
    
    iterations = 100000000
    result = iterations * ((n ** (1/iterations)) - 1)
    return round(result, 7)


def log(base: float, argument: float) -> float:
    """
    @brief Logaritmus čísla argument o základe base
    @return log(argument)
    @param base Základ
    @param argument Argument
    @raise ValueError ak je argument záporné číslo
    @raise ValueError ak je základ <= 1
    """
    if argument <= 0:
        raise ValueError("log(x) nie je definovaný pre x <= 0")
    
    if base <= 1:
        raise ValueError("základ musí byť > 1")
       
    iterations = 100000000
    result = (iterations * ((argument ** (1/iterations)) - 1)) / (iterations * ((base ** (1/iterations)) - 1))

    return round(result, 7)