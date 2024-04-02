## @file parse_tests.py
## @brief Testy pre matematickú knižnicu
## @author Jaroslav Podmajerský

import pytest
import parse as parse
import math

#-----------------------------------------------------------------------------------------------------------------------------------

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
#    result = parse.evaluate("-3^5.5")
#    assert result == -3**5
    
    result = parse.evaluate("3√8-2*3^2")
    assert result == -16

def test_Evaluate_Basic_Arithmetic_FAILURE():
    with pytest.raises(ZeroDivisionError):       
        parse.evaluate("1/0")
    with pytest.raises(ZeroDivisionError):       
        parse.evaluate("1/-0")
    # with pytest.raises(ZeroDivisionError):       
    #     parse.evaluate("0^0")

    with pytest.raises(ValueError):
        parse.evaluate("0√2")
    with pytest.raises(ValueError):
        parse.evaluate("-2√2")
    
    with pytest.raises(ValueError):
        parse.evaluate("2^1.5")

#-----------------------------------------------------------------------------------------------------------------------------------

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

    with pytest.raises(ValueError):
        parse.evaluate("log(-1,5)")
    with pytest.raises(ValueError):
        parse.evaluate("log(1,5)")
    with pytest.raises(ValueError):
        parse.evaluate("log(2,0)")
    with pytest.raises(ValueError):
        parse.evaluate("log(2,0)")
    with pytest.raises(ValueError):       
        parse.evaluate("log(0.8,2)")
    
    with pytest.raises(ValueError):
        parse.evaluate("ln(0)")
    with pytest.raises(ValueError):
        parse.evaluate("ln(-1)")

    with pytest.raises(ValueError):
        parse.evaluate("-2!")
    with pytest.raises(ValueError):
        parse.evaluate("0.5!")

#-----------------------------------------------------------------------------------------------------------------------------------

def test_Evaluate_Order_of_Operations():

    result = parse.evaluate("(1-2)*3")
    assert result == -3
    result = parse.evaluate("(1-2)/3")
    assert result == pytest.approx(-1/3)
    result = parse.evaluate("5*-(4.2/(3+1.2))")
    assert result == -5
    
    result = parse.evaluate("3^(3-1)")
    assert result == 3**2
    # result = parse.evaluate("(2*2+4)//(2^(3-2))")
    # assert result == pytest.approx(2)
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
    result = parse.evaluate("log((log((2+3),125)),(3!+(5-2))) * (5-3^2)-(4//2+ln(e^2))")
    assert result == pytest.approx(-12)

#-----------------------------------------------------------------------------------------------------------------------------------

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
    result = parse.evaluate("log(2-(-(3)),--((125)))")
    assert result == pytest.approx(3)
    result = parse.evaluate("ln((((e^2))))")
    assert result == pytest.approx(2)

def test_Evaluate_SYNTAX_Const():
    result = parse.evaluate("e")
    assert result == pytest.approx(math.e)
    result = parse.evaluate("pi")
    assert result == pytest.approx(math.pi)

#-----------------------------------------------------------------------------------------------------------------------------------

def test_Evaluate_SYNTAX_FAILURE():
    with pytest.raises(SyntaxError):
        parse.evaluate("")
    with pytest.raises(SyntaxError):
        parse.evaluate("()")
    with pytest.raises(SyntaxError):
        parse.evaluate("(5())")
    with pytest.raises(SyntaxError):
        parse.evaluate("(5(-)2)")
    with pytest.raises(SyntaxError):
        parse.evaluate("(5(-2)")
    with pytest.raises(SyntaxError):
        parse.evaluate("(5(-2))")
    with pytest.raises(SyntaxError):
        parse.evaluate("(5-2))")
    with pytest.raises(SyntaxError):
        parse.evaluate("(5-2(*3)")

def test_Evaluate_SYNTAX_FAILURE_Unknown_Characters():
    with pytest.raises(SyntaxError):
        parse.evaluate("e+x")
    with pytest.raises(SyntaxError):
        parse.evaluate("eabx")
    with pytest.raises(SyntaxError):
        parse.evaluate("☺☻♥♦♣š?É")
    with pytest.raises(SyntaxError):
        parse.evaluate("1+ 2")
    with pytest.raises(SyntaxError):
        parse.evaluate("2///3")
    with pytest.raises(SyntaxError):
        parse.evaluate("2**3")
    with pytest.raises(SyntaxError):   
        parse.evaluate("56,2")
    
def test_Evaluate_SYNTAX_FAILURE_Argument_Error_Basic_Arithmetic(): 
    with pytest.raises(SyntaxError):
        parse.evaluate("+")
    with pytest.raises(SyntaxError):
        parse.evaluate("5-")
    with pytest.raises(SyntaxError):
        parse.evaluate("5*")
    with pytest.raises(SyntaxError):
        parse.evaluate("/0")
    with pytest.raises(SyntaxError):
        parse.evaluate("5-/0")
    with pytest.raises(SyntaxError):
        parse.evaluate("6//")
    with pytest.raises(SyntaxError):
        parse.evaluate("-5+*+6")
    with pytest.raises(SyntaxError):
        parse.evaluate("3*/4")

def test_Evaluate_SYNTAX_FAILURE_Argument_Error_Factorial():
    with pytest.raises(SyntaxError):
        parse.evaluate("!")
    with pytest.raises(SyntaxError):
        parse.evaluate("!5")
    with pytest.raises(SyntaxError):
        parse.evaluate("5!5")
    with pytest.raises(SyntaxError):
        parse.evaluate("5!!5")
    with pytest.raises(SyntaxError):
        parse.evaluate("5(!)")
    with pytest.raises(SyntaxError):
        parse.evaluate("5(!!)")
    with pytest.raises(SyntaxError):
        parse.evaluate("(5(!))")

def test_Evaluate_SYNTAX_FAILURE_Argument_Error_Logarithms():
    with pytest.raises(SyntaxError):
        parse.evaluate("log()")
    with pytest.raises(SyntaxError):
        parse.evaluate("log(1)")
    with pytest.raises(SyntaxError):
        parse.evaluate("log(1,2")
    with pytest.raises(SyntaxError):
        parse.evaluate("log(1,2))")
    with pytest.raises(SyntaxError):
        parse.evaluate("log(1(2,)5)")
    with pytest.raises(SyntaxError):
        parse.evaluate("log(log(5,3,3)")

    with pytest.raises(SyntaxError):
        parse.evaluate("ln()")
    with pytest.raises(SyntaxError):
        parse.evaluate("ln(5")
    with pytest.raises(SyntaxError):
        parse.evaluate("ln(5))")
    with pytest.raises(SyntaxError):
        parse.evaluate("ln(5,2)")
    