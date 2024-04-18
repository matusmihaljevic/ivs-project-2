## 
# @file parse_tests.py
# @brief Testy pre parser
# @author Jaroslav Podmajerský

import pytest
import parse as parse
import math

#------------------------------------------------------BASIC-ARITHMETIC---------------------------------------------------

def test_Evaluate_Basic_Arithmetic():
    result = parse.evaluate("5+4-3")
    assert result == 6
    result = parse.evaluate("2*4+3")
    assert result == 11
    result = parse.evaluate("2/4-1")
    assert result == -0.5

    result = parse.evaluate("2√4-2")
    assert result == 0
    result = parse.evaluate("4√2")
    assert result == pytest.approx(2**(1/4))

    result = parse.evaluate("3^1")
    assert result == 3
    result = parse.evaluate("5^0")
    assert result == 1
    result = parse.evaluate("0^0")
    assert result == 1
    result = parse.evaluate("3√8-2*3^2")
    assert result == -16

    result = parse.evaluate("3//2")
    assert result == 1
    result = parse.evaluate("100//100")
    assert result == 1
    result = parse.evaluate("73//-17")
    assert result == -5
    result = parse.evaluate("-60//7")
    assert result == -9
    result = parse.evaluate("18.78//4")
    assert result == 4
    result = parse.evaluate("1886.45678//46.8789")
    assert result == 40
    result = parse.evaluate("16//3+8")
    assert result == 13
    result = parse.evaluate("20//21")
    assert result == 0

def test_Evaluate_Basic_Arithmetic_FAILURE():
    result = parse.evaluate("1/0")
    assert result == "Delenie nulou"
    result = parse.evaluate("5/-0")
    assert result == "Delenie nulou"
    result = parse.evaluate("0√2")
    assert result == "Index musí byť prirodzené číslo"
    result = parse.evaluate("-2√2")
    assert result == "Index musí byť prirodzené číslo"
    result = parse.evaluate("2^1.5")
    assert result == "Exponent musí byť prirodzené číslo"
    result = parse.evaluate("2004//0")
    assert result == "Delenie nulou"

#-----------------------------------------------------ADVANCED-ARITHMETIC------------------------------------------------------

def test_Evaluate_Advanced_Math_Functions():

    result = parse.evaluate("log(8,2)")
    assert result == pytest.approx(math.log(2) / math.log(8))
    result = parse.evaluate("log((8-3),2)")
    assert result == pytest.approx(math.log(2) / math.log(5))
    result = parse.evaluate("ln(5-3)")
    assert result == pytest.approx(math.log(2))
    result = parse.evaluate("ln(5-3)*ln(2√4)")
    assert result == pytest.approx(math.log(2)*math.log(math.sqrt(4)))

    result = parse.evaluate("0!")
    assert result == 1
    result = parse.evaluate("3!")
    assert result == 6

    result = parse.evaluate("ln(e^2)+4*2-0*1-log(2,8)")
    assert result == pytest.approx(7)

def test_Evaluate_Advanced_Math_Functions_FAILURE():
    
    result = parse.evaluate("log(-1,5)")
    assert result == "log(x) nie je definovaný pre x <= 0"
    result = parse.evaluate("log(1,5)")
    assert result == "základ musí byť > 1"
    result = parse.evaluate("log(2,0)")
    assert result == "log(x) nie je definovaný pre x <= 0"
    result = parse.evaluate("log(0.8,2)")
    assert result == "Číslo musí byť prirodzené"
    
    result = parse.evaluate("ln(0)")
    assert result == "ln(x) nie je definovaný pre x <= 0"
    result = parse.evaluate("ln(-1)")
    assert result == "ln(x) nie je definovaný pre x <= 0"
   
    result = parse.evaluate("-2!")
    assert result == "Číslo nesmie byť záporné"
    result = parse.evaluate("0.5!")
    assert result == "Číslo musí byť prirodzené"

#-----------------------------------------------------ORDER-OF-OPERATIONS--------------------------------------------------------

def test_Evaluate_Order_of_Operations():

    result = parse.evaluate("(1-2)*3")
    assert result == -3
    result = parse.evaluate("(1-2)/3")
    assert result == pytest.approx(-1/3)
    result = parse.evaluate("5*-(4.2/(3+1.2))")
    assert result == -5
    
    result = parse.evaluate("3^(3-1)")
    assert result == 3**2
    result = parse.evaluate("((3+2.5)-0.5)^(3-ln(1))")
    assert result == pytest.approx(5**3)

    result = parse.evaluate("(7-3)!")
    assert result == math.factorial(4)
    result = parse.evaluate("(7-3)!/(2√9)!")
    assert result == pytest.approx(4)

    result = parse.evaluate("log(2,8)!")
    assert result == pytest.approx(math.factorial(3))
    result = parse.evaluate("log((log((2+3),125)),(3!+(5-2)))")
    assert result == pytest.approx(2)
    result = parse.evaluate("log((log((2+3),125)),(3!+(5-2))) * (5-3^2)-(2√4+ln(e^2))")
    assert result == pytest.approx(-12)

#------------------------------------------------------------SYNTAX---------------------------------------------------------------

def test_Evaluate_SYNTAX():
    result = parse.evaluate("(((3)))")
    assert result == 3
    result = parse.evaluate("--(--(3))")
    assert result == 3
    result = parse.evaluate("+--++-+--5-+--+--++1")
    assert result == -6
    result = parse.evaluate("--(-3)")
    assert result == -3
    result = parse.evaluate("--(-3)")
    assert result == -3

def test_Evaluate_SYNTAX_Factorial():
    result = parse.evaluate("3!!")
    assert result == 720
    result = parse.evaluate("(3!)!")
    assert result == 720

def test_Evaluate_SYNTAX_Logarithms():
    result = parse.evaluate("log((2-(-(3))),--((125)))")
    assert result == pytest.approx(3)
    result = parse.evaluate("ln((((e^2))))")
    assert result == pytest.approx(2)
    

def test_Evaluate_SYNTAX_Const():
    result = parse.evaluate("e")
    assert result == pytest.approx(math.e)
    result = parse.evaluate("pi")
    assert result == pytest.approx(math.pi)

#------------------------------------------------------------SYNTAX-FAILURE-------------------------------------------------------------

def test_Evaluate_SYNTAX_FAILURE():

   
    with pytest.raises(SyntaxError) as err_info:
        parse.evaluate("")
    assert str(err_info.value) == "Nepovolený znak"
    
    with pytest.raises(SyntaxError) as err_info:
        parse.evaluate("()")
    assert str(err_info.value) == "Nepovolený znak"

    with pytest.raises(SyntaxError) as err_info:
        parse.evaluate("+")
    assert str(err_info.value) == "Nedostatok operandov pre operáciu '+'"

    with pytest.raises(SyntaxError) as err_info:
        parse.evaluate("(5())")
    assert str(err_info.value) == "Nepovolený znak"
    with pytest.raises(SyntaxError) as err_info:
        parse.evaluate("(5(-)2)")
    assert str(err_info.value) == "Nedostatok operandov pre operáciu '-'"
    with pytest.raises(SyntaxError) as err_info:
        parse.evaluate("(5-2))")
    assert str(err_info.value) == "Nedostatok operandov pre operáciu '*'"

    #Test-Neuzavrete zatvorky
    with pytest.raises(SyntaxError) as err_info:
        parse.evaluate("(5(-2)")
    assert str(err_info.value) == "Syntaktická chyba"
    with pytest.raises(SyntaxError) as err_info:
        parse.evaluate("(5(-2))")
    assert str(err_info.value) == "Syntaktická chyba"
    with pytest.raises(SyntaxError) as err_info:
        parse.evaluate("(5-2))")
    assert str(err_info.value) == "Syntaktická chyba"
    

def test_Evaluate_SYNTAX_FAILURE_Unknown_Characters():

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("e+x")
    assert str(err_inf.value) == "Nepovolený znak"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("eabx")
    assert str(err_inf.value) == "Nepovolený znak"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("☺☻♥♦♣š?É")
    assert str(err_inf.value) == "Nepovolený znak"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("2///3")
    assert str(err_inf.value) == "Syntaktická chyba"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("2**3")
    assert str(err_inf.value) == "Syntaktická chyba"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("56,4")
    assert str(err_inf.value) == "Syntaktická chyba"

    
def test_Evaluate_SYNTAX_FAILURE_Argument_Error_Basic_Arithmetic():

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("3*/4")
    assert str(err_inf.value) == "Syntaktická chyba"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("/0")
    assert str(err_inf.value) == "Nedostatok operandov pre operáciu '/'"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("5-")
    assert str(err_inf.value) == "Nedostatok operandov pre operáciu '-'"
    
    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("5*")
    assert str(err_inf.value) == "Nedostatok operandov pre operáciu '*'"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("5-/0")
    assert str(err_inf.value) == "Syntaktická chyba"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("5√")
    assert str(err_inf.value) == "Nedostatok operandov pre operáciu '√'"
    
    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("-5+*+6")
    assert str(err_inf.value) == "Syntaktická chyba"
     

def test_Evaluate_SYNTAX_FAILURE_Argument_Error_Factorial():

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("!")
    assert str(err_inf.value) == "Nedostatok operandov pre funkciu '!'"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("!5")
    assert str(err_inf.value) == "Nedostatok operandov pre funkciu '!'"
    
    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("5(!)")
    assert str(err_inf.value) == "Nedostatok operandov pre funkciu '!'"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("5(!!)")
    assert str(err_inf.value) == "Nedostatok operandov pre funkciu '!'"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("(5(!))")
    assert str(err_inf.value) == "Nedostatok operandov pre funkciu '!'"


def test_Evaluate_SYNTAX_FAILURE_Argument_Error_Logarithm():

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("log()")
    assert str(err_inf.value) == "Nedostatok operandov pre operáciu 'log'"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("log(1)")
    assert str(err_inf.value) == "Nedostatok operandov pre operáciu 'log'"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("log(1,2")
    assert str(err_inf.value) == "Syntaktická chyba pre operáciu 'log'"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("log(1,2))")
    assert str(err_inf.value) == "Syntaktická chyba pre operáciu 'log'"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("log(1(2,)5)")
    assert str(err_inf.value) == "Syntaktická chyba pre operáciu 'log'"
    
    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("log(log(5,3,3)")
    assert str(err_inf.value) == "Syntaktická chyba pre operáciu 'log'"

def test_Evaluate_SYNTAX_FAILURE_Argument_Error_Natural_Logarithm():
    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("ln()")
    assert str(err_inf.value) == "Nedostatok operandov pre funkciu 'ln'"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("ln(5")
    assert str(err_inf.value) == "Syntaktická chyba pre operáciu 'ln'"
    
    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("ln(5))")
    assert str(err_inf.value) == "Syntaktická chyba pre operáciu 'ln'"

    with pytest.raises(SyntaxError) as err_inf:
        parse.evaluate("ln(5,2)")
    assert str(err_inf.value) == "Syntaktická chyba pre operáciu 'ln'"
    