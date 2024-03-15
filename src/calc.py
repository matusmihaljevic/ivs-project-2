## @file calc.py
## @brief Matematická knižnica pre kalkulačku
## @authors Matúš Mihaljevič, Adam Bojnanský, Kristián Pribila, Jaroslav Podmajerský

def add(a, b):
    """
    @brief Súčet dvoch čísiel
    @return Súčet a + b
    """
    return a + b


def sub(a, b):
    """
    @brief Rozdiel dvoch čísiel
    @return Rozdiel a - b
    """    
    return a - b


def mult(a, b):
    """
    @brief Súčin dvoch čísiel
    @return Súčin a * b
    """    
    return a * b


def div(dividend, divisor):
    """
    @brief Podiel dvoch čísiel
    @return Podiel a / b
    @raise ZeroDivisionError Ak je deliteľ rovný 0
    """

def mod(dividend, divisor):
    """
    @brief Celočíselný podiel dvoch čísiel
    @return Modulo a % b
    @raise ValueError Ak je deliteľ rovný 0
    """    
    return 42


def fact(self):
    """
    @brief Faktoriál prirodzeného čísla
    @return Faktoriál self!
    @raise ValueError Ak číslo nie je integer alebo je záporné
    """    
    return 42


def pow(base, exponent):
    """
    @brief Mocnica čísla s prirodzeným exponentom
    @return x^n
    @param base Základ
    @param exponent Exponent
    @raise ValueError Ak je základ rovný 0 a exponent záporné číslo
    @raise ValueError Ak exponent nie je integer
    """    
    return 64


def sqrt(base, index):
    """
    @brief Odmocnina čísla s prirodzeným indexom
    @return x^{1/n}
    @param base Základ
    @param index Index
    @raise ValueError Ak index nie je integer
    @raise ValueError Ak je index menší alebo rovný 0
    @raise ValueError Ak je základ záporný a index kladný
    """    
    return 3


def ln(self):
    """
    @brief Prirodzený logaritmus
    @return ln(x)
    @raise ValueError ak je hodnota záporné číslo
    """
    return 1


def log(base, argument):
    """
    @brief Logaritmus čísla argument o základe base
    @return log(base, x)
    @param base Základ
    @param argument Argument
    @raise ValueError ak je argument záporné číslo
    @raise ValueError ak je základ záporné číslo
    """
    return 3