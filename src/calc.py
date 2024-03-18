## @file calc.py
## @brief Matematická knižnica pre kalkulačku
## @authors Matúš Mihaljevič, Adam Bojnanský, Kristián Pribila, Jaroslav Podmajerský

def add(a, b):
    """
    @brief Súčet dvoch čísiel
    @return Súčet a + b
    """
    return round(a + b, 7)


def sub(a, b):
    """
    @brief Rozdiel dvoch čísiel
    @return Rozdiel a - b
    """    
    return round(a - b, 7)


def mult(a, b):
    """
    @brief Súčin dvoch čísiel
    @return Súčin a * b
    """    
    return round(a * b, 7)


def div(dividend, divisor):
    """
    @brief Podiel dvoch čísiel
    @return Podiel a / b
    @raise ZeroDivisionError Ak je deliteľ rovný 0
    """
    if(divisor == 0):
        raise ZeroDivisionError("Delenie nulou")

    return round(dividend / divisor, 7)    


def mod(dividend, divisor):
    """
    @brief Celočíselný podiel dvoch čísiel
    @return Modulo a % b
    @raise ZeroDivisionError Ak je deliteľ rovný 0
    """    
    if(divisor == 0):
        raise ZeroDivisionError("Delenie nulou")

    return dividend % divisor    


def fact(self):
    """
    @brief Faktoriál prirodzeného čísla
    @return Faktoriál self!
    @raise ValueError Ak číslo nie je integer alebo je záporné
    """    
    if self < 0:
        raise ValueError("Číslo nesmie byť záporné")

    if not isinstance(self, int):
        raise TypeError("Číslo musí byť prirodzené")

    result = 1
    while self != 0:
        result *= self
        self -= 1

    return result    


def pow(base, exponent):
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

    return round(base ** exponent, 7)


def root(base, index):
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
        raise ValueError("Číslo nie je možné odmocniť")

    guess = initialGuess
    while True:
        nextGuess = ((index - 1) * guess + base / (guess ** (index - 1))) / index
        if abs(nextGuess - guess) < tolerance:
            return round(nextGuess, 7)
        guess = nextGuess    


def ln(self):
    """
    @brief Prirodzený logaritmus
    @return ln(x)
    @raise ValueError ak je hodnota menšia alebo rovná 0
    """
    if self <= 0:
        raise ValueError("ln(x) nie je definovaný pre x <= 0")

    if self == 1:
        return 0
    
    n = 100000000
    result = n * ((self ** (1/n)) - 1)
    return round(result, 7)


def log(base, argument):
    """
    @brief Logaritmus čísla argument o základe base
    @return log(base, x)
    @param base Základ
    @param argument Argument
    @raise ValueError ak je argument záporné číslo
    @raise ValueError ak je základ <= 1
    """
    if argument <= 0:
        raise ValueError("log(x) nie je definovaný pre x <= 0")
    
    if base <= 1:
        raise ValueError("základ musí byť > 1")
       
    n = 100000000
    result = (n * ((argument ** (1/n)) - 1)) / (n * ((base ** (1/n)) - 1))

    return round(result, 7)