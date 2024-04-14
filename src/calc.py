## 
# @file calc.py
# @brief Matematická knižnica pre kalkulačku
# @author Matúš Mihaljevič


##
# @brief Súčet dvoch čísiel
# @return Súčet a + b
def add(a: float, b: float) -> float:
    return a + b


##
# @brief Rozdiel dvoch čísiel
# @return Rozdiel a - b
def sub(a: float, b: float) -> float:
    return a - b


##
# @brief Súčin dvoch čísiel
# @return Súčin a * b
def mult(a: float, b: float) -> float:
    return a * b


##
# @brief Podiel dvoch čísiel
# @return Podiel a / b
# @exception ZeroDivisionError Ak je deliteľ rovný 0
def div(a: float, b: float) -> float:
    if(b == 0):
        raise ZeroDivisionError("Delenie nulou")

    return a / b   


##
# @brief Celočíselný podiel dvoch čísiel
# @return a // b
# @exception ZeroDivisionError Ak je deliteľ rovný 0
def int_div(a : float, b: float) -> int:
    if(b == 0):
        raise ZeroDivisionError("Delenie nulou")

    return int(a // b)    


##
# @brief Faktoriál prirodzeného čísla
# @return Faktoriál n!
# @exception ValueError Ak je číslo záporné    
def fact(n: int) -> int:
    if not isinstance(n, (int, float)):
        raise TypeError("Číslo musí byť prirodzené")

    if isinstance(n, float) and n.is_integer():
        n = int(n)
    elif not isinstance(n, int):
        raise TypeError("Číslo musí byť prirodzené")
    
    if n < 0:
        raise ValueError("Číslo nesmie byť záporné")

    result = 1
    while n != 0:
        result *= n
        n -= 1

    return result    


##
# @brief Mocnica čísla s prirodzeným exponentom
# @return x^n
# @param base Základ
# @param exponent Exponent
# @exception ValueError Ak je základ rovný 0 a exponent záporné číslo    
def pow(base : float, exponent: int) -> float:
    if not isinstance(exponent,  int):
        raise ValueError("Exponent musí byť prirodzené číslo")
    
    if (base == 0) and (exponent < 0):
        raise ValueError("Delenie nulou")

    return base ** exponent


##
# @brief Odmocnina čísla s prirodzeným indexom
# @return x^{1/n}
# @param base Základ
# @param index Index
# @exception ValueError Ak je index menší alebo rovný 0
# @exception ValueError Ak je základ záporný a index kladný    
def root(base: float, index: int) -> float:
    if not isinstance(index, (int, float)):
        raise ValueError("Číslo musí byť prirodzené")

    if isinstance(index, float) and index.is_integer():
        index = int(index)
    elif not isinstance(index, int):
        raise ValueError("Číslo musí byť prirodzené")
    if index <= 0:
        raise ValueError("Index musí byť prirodzené číslo")

    if (base < 0) and (index % 2 == 0):
        raise ValueError("Párna odmocnina nie je definovaná pre záporné čísla")

    return base**(1/index)


##
# @brief Prirodzený logaritmus
# @return ln(n)
# @exception ValueError ak je hodnota menšia alebo rovná 0
def ln(n: float) -> float:
    if n <= 0:
        raise ValueError("ln(x) nie je definovaný pre x <= 0")

    if n == 1:
        return 0
    
    iterations = 100000000
    result = iterations * ((n ** (1/iterations)) - 1)
    return result


##
# @brief Logaritmus čísla argument o základe base
# @return log(argument)
# @param base Základ
# @param argument Argument
# @exception ValueError ak je argument záporné číslo
# @exception ValueError ak je základ <= 1
def log(base: int, argument: float) -> float:
    if not isinstance(base, (int, float)):
        raise ValueError("Číslo musí byť prirodzené")

    if isinstance(base, float) and round(base, 6).is_integer():
        base = int(base)
    elif not isinstance(base, int):
        raise ValueError("Číslo musí byť prirodzené")
    
    if argument <= 0:
        raise ValueError("log(x) nie je definovaný pre x <= 0")
    
    if base <= 1:
        raise ValueError("základ musí byť > 1")
       
    iterations = 100000000
    result = (iterations * ((argument ** (1/iterations)) - 1)) / (iterations * ((base ** (1/iterations)) - 1))

    return result